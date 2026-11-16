# Runtime #237: missing live playback pose

Observed November 16, 2026. Diagnosis only. No runtime, test assertion, fixture, CI configuration or production behavior changed.

## Finding

The failed CI capture really did omit **zero-based movement frame 11**, in exactly one of six views: **1.25x magnification, camera tracking off, Reduced Motion on**. Its 49 movement observations contain 15 distinct authored poses. The other five CI views contain all 16, as do all six views in the unchanged focused local retry.

This is not missing texture evidence: every movement observation in the failing view has both sprite and texture present, with selected clip `player_move|w`. The native summary reports one failure only, the 15-versus-16 census assertion. No world-trace or digest assertion failure was reported.

## Measured timing

Failing attachment: `ci-records/73A85006-8911-444B-8594-BC44958333E0.json`.

| Observed ticks | Observed frames | SpriteKit callback-time delta | Post-action uptime delta |
| --- | --- | --- | --- |
| 21 to 26 | 10 to 12 | 66.918 ms | 74.338 ms |
| 30 to 36 | 14 to 2 | 109.076 ms | 114.147 ms |
| 38 to 53 | 3 to 12 | 281.601 ms | 311.916 ms |

The first two possible visits to pose 11 fall inside the 10-to-12 and 3-to-12 observation gaps. The remaining movement observations end at frame 8 on tick 75. Frame 11 therefore never enters the observed-frame set.

The update after the largest gap takes 36.010 ms in total, of which 34.366 ms is simulation stepping and 0.352 ms is renderer work. Its preceding update takes 7.480 ms. These measurements do **not** identify the cause of the approximately 282 ms callback gap. Scheduling, other main-thread work, rendering outside these measured sections and host conditions require further evidence before attribution.

The authored clip has 16 poses at 32 timing units per second, one unit per pose, so its nominal pose duration is 31.25 ms. The live observer records the texture after actions evaluate, not every theoretical pose traversed between callbacks. The simulation accumulator independently clamps each callback contribution to 0.25 s, accounting for the 15-tick jump across the largest gap. This preserves the distinction between authoritative stepping and observed display coverage.

## Source references

Runtime `AppTests/DisplayedPlaybackTests.swift`, unchanged between failed head `01e9317a8bbc0ee02d5d583beaaeb9966542fd6b` and trial head `c1f9fb5106759ec19da9d8d82fc542de9846b394`:

- Lines 973-976: authored movement timing.
- Lines 522-559: clock sampling, clamped accumulator and authoritative stepping.
- Lines 647-709: actual post-action texture lookup, record creation and `seen` set insertion.
- Lines 1145-1147: live SKView completion path.
- Lines 1169-1170: authoritative trace/digest checks.
- Line 1184: unchanged requirement for all 16 observed poses.

Source SHA-256: `dd3bd113bcba2a1341781902303d47aafe0912dd9fd2e0df7795800bf3510e74`.

## Provenance and limits

- Failed GitHub Actions run: `43779430334`, artifact `app-tests-Debug`, artifact ID `14187829828`. Original archive size: 606,898,760 bytes.
- `ci-summary.json` is directly exported from the preserved `SSRuntime.xcresult`. It reports 165 passed logical tests, one failed, no skips. Device aggregation includes parameterized executions and reports a different passed count. These counts are not interchangeable.
- Failed environment: iPhone SE (3rd generation) simulator, iOS 26.2, macOS 15.8.2.
- `ci-records/` contains all six original JSON attachments and their xcresult export manifest, unchanged.
- `local-records/` contains all six original attachments from the unchanged focused local retry on iPhone 17 Pro simulator, iOS 26.5. That test passed on November 16 at 01:00 UTC in 19.814 seconds. Different device/OS and focused execution mean this is comparison evidence, not equivalent host-load reproduction.
- Native `ci-summary.json` and original records are authoritative. This analysis does not claim that a sampled texture necessarily reached physical scanout.

## Reproduce the census and largest gap

From this directory:

```python
import json
from pathlib import Path
for directory in ['ci-records', 'local-records']:
    for path in sorted(Path(directory).glob('*.json')):
        if path.name == 'manifest.json':
            continue
        rows = json.loads(path.read_text())
        seen = {r['frame'] for r in rows if r['frame'] >= 0}
        moving = [r for r in rows if r['requestedClip'] == 'player_move']
        gaps = [(b['clockSample']['spriteKitTime'] - a['clockSample']['spriteKitTime'],
                 a['tick'], b['tick'], a['frame'], b['frame'])
                for a, b in zip(rows, rows[1:])
                if a['requestedClip'] == 'player_move' or b['requestedClip'] == 'player_move']
        print(directory, path.name, rows[0]['magnification'], rows[0]['tracksPlayer'],
              rows[0]['reducedMotion'], len(moving), sorted(set(range(16)) - seen), max(gaps))
```

## Disposition

Keep runtime #237 open. The omission mechanism is now supported by actual records, while the source of the callback stall and an acceptable remedy remain unresolved. The 16-pose assertion is honest and must not be lowered, converted to deterministic export, or hidden with automatic retries. Before any remedy, define whether it addresses live scheduling or diagnostic classification, preserve independent authoritative checks, and reproduce on the failing environment. No change to Player settle timing, source art or projection selection follows from this diagnosis.
