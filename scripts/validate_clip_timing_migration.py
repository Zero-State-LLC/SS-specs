#!/usr/bin/env python3
"""BP-003 mechanical v1→v2 evidence; never writes/adopts a new delivery."""
from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
MAX_INT = (1 << 63) - 1


def validate_timing(document, validator):
    validator.validate(document)
    for clip in document['clips']:
        timing = clip['timing']
        units = timing['frameUnits']
        if len(units) != len(clip['frameIds']):
            raise ValueError('frame/duration count mismatch')
        if sum(units) > MAX_INT:
            raise ValueError('duration sum overflow')
        for direction in clip['directions'] or [None]:
            selected = [u for frame, u in zip(clip['frameIds'], units)
                        if direction is None or f'_{direction}_' in frame]
            if not selected:
                raise ValueError('empty facing')
            if sum(selected) * 60 > MAX_INT:
                raise ValueError('tick numerator overflow')


def main():
    before = json.loads((ROOT / 'contracts/clip-metadata-001.json').read_text())
    schema = json.loads((ROOT / 'contracts/clip-metadata-002.schema.json').read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    after = deepcopy(before)
    after['schemaVersion'] = 'clip-metadata-002'
    for clip in after['clips']:
        clip['timing'] = {'unitsPerSecond': clip.pop('framesPerSecond'),
                          'frameUnits': [1] * len(clip['frameIds'])}
    validate_timing(after, validator)
    facings = 0
    for old, new in zip(before['clips'], after['clips']):
        restored = deepcopy(new)
        restored['framesPerSecond'] = restored.pop('timing')['unitsPerSecond']
        assert restored == old, old['clipId']
        for direction in old['directions'] or [None]:
            indices = [i for i, frame in enumerate(old['frameIds'])
                       if direction is None or f'_{direction}_' in frame]
            previous = Fraction(len(indices), old['framesPerSecond'])
            current = Fraction(sum(new['timing']['frameUnits'][i] for i in indices),
                               new['timing']['unitsPerSecond'])
            assert previous == current, (old['clipId'], direction)
            assert (previous * 60).__ceil__() == (current * 60).__ceil__()
            facings += 1
    # Each malformed case is rejected by structural or explicit arithmetic checks.
    rejected = 0
    for field, value in [('unitsPerSecond', 0), ('unitsPerSecond', True),
                         ('unitsPerSecond', 1.5), ('unitsPerSecond', MAX_INT + 1),
                         ('frameUnits', []), ('frameUnits', [1]),
                         ('frameUnits', [-1]), ('frameUnits', [False]),
                         ('frameUnits', [1.5]), ('extra', 1)]:
        bad = deepcopy(after); bad['clips'][0]['timing'][field] = value
        try:
            validate_timing(bad, validator)
        except (ValueError, ValidationError):
            rejected += 1
        else:
            raise AssertionError(f'accepted malformed {field}: {value}')
    for mode in ['mixed', 'missing', 'sum-overflow', 'tick-overflow']:
        bad = deepcopy(after); clip = bad['clips'][0]
        if mode == 'mixed': clip['framesPerSecond'] = 12
        elif mode == 'missing': del clip['timing']
        else:
            count = len(clip['frameIds'])
            unit = MAX_INT if mode == 'sum-overflow' else MAX_INT // count
            clip['timing']['frameUnits'] = [unit] * count
        try:
            validate_timing(bad, validator)
        except (ValueError, ValidationError):
            rejected += 1
        else:
            raise AssertionError(f'accepted malformed {mode}')
    vectors = [(12, [1]*6, Fraction(1,2), 30), (32, [1]*16, Fraction(1,2), 30),
               (14, [1]*6, Fraction(3,7), 26), (112, [3]*16, Fraction(3,7), 26),
               (24, [1,2,1,2], Fraction(1,4), 15)]
    for timebase, holds, duration, ticks in vectors:
        actual = Fraction(sum(holds), timebase)
        assert actual == duration and (actual*60).__ceil__() == ticks
    print(f'clip timing migration: OK — {len(after["clips"])} clips, {facings} facing selections, '
          f'{rejected} malformed cases, {len(vectors)} exact vectors; active v1 unchanged')


if __name__ == '__main__':
    main()
