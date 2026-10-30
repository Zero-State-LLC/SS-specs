# Elite and Boss Contract

Status: CANONICAL  
Contract version: `bosses-001`

## Improper Search Daemon

The elite activates in Z-05 after M-C cleanup.

| Property | Value |
|---|---:|
| HP | 450 (D-090) |
| Radius | 26 |
| Base speed | 108 units/second |
| Contact damage | 14 DPS |
| Spawn delay after M-C | 90 ticks |

State sequence repeats until defeated:

1. `PURSUIT` for 120 ticks.
2. `QUERY_TELEGRAPH` for 45 ticks: display three 56-unit circles at Player position and ±96 units perpendicular to facing.
3. `QUERY_RESOLVE`: each circle still containing the Player deals 14 damage; circles do not overlap.
4. `REDACTION_DASH_TELEGRAPH` for 36 ticks: show one 72-unit-wide lane to the sampled Player position.
5. `REDACTION_DASH` for 30 ticks at 288 units/second; normal solid collision; contact remains active.
6. `RECOVER` stationary for 60 ticks.

The Daemon has no invulnerability, summons, random attack choice, Camera control, or Exposure effect. At zero HP, emit `EliteDefeated(improperSearchDaemon,tick)` once and open the route to Z-06 after 60 ticks.

## Algorithmic Moderate

The single boss activates when the living Player enters Z-06 after the elite is defeated.

| Property | Value |
|---|---:|
| HP | 1600 (D-090) |
| Radius | 30 |
| Base speed | 120 units/second |
| Base contact damage | 10 DPS (D-096) |
| Initial attack delay | 90 ticks |
| Phase transition recovery | 45 ticks, movement only; not damage-immune |

### Canonical policy phases

Health bands use HP after the tick's ordered damage batch:

| Phase | HP after batch | Observation | Speed | Contact | Orbit |
|---|---:|---:|---:|---:|---:|
| Public Safety | 1200–1600 | 105/100 | 100/100 | 100/100 | 0/100 |
| Civil Liberties | 800–1199 | 108/100 | 90/100 | 104/100 | 72/100 |
| Temporary Safeguard | 400–799 | 112/100 | 118/100 | 110/100 | 18/100 |
| Independent Review | 1–399 | 116/100 | 104/100 | 116/100 | −55/100 |

These ratios adapt verified legacy San Francisco policy values. A damage batch may cross multiple thresholds, but only the final resulting phase is entered and one transition event is emitted. Phase cannot move backward.

Orbit modifies normalized pursuit by adding the perpendicular direction × orbit ratio before normalization. Even entity parity chooses the initial perpendicular orientation; negative ratio reverses it.

**Captain path search (D-118, superseding D-116).** The Captain finds its way round solids with a shortest-path search. Geometry is in whole units (positions truncated), with exact integer arithmetic. "Solids" means the live solids it collides with, taken in ascending ID order (UTF-8).

1. **Clear leg.** A leg from a to b is clear when, for every solid, its distance to the box is at least the smallest of these:
   - the Captain's radius;
   - a's distance to that box;
   - b's distance to that box.

   So a body touching a wall may leave along it, and a Player pressed into a wall may be reached, but a leg through a box (distance 0) never is.
2. **Direct.** If the leg Captain → Player is clear, the Captain pursues the Player directly, orbit included, as before D-116.
3. **Nodes.** Each solid has four corner nodes: its box corners moved out by the radius + 4 on both axes, in the order (min X, min Y), (max X, min Y), (min X, max Y), (max X, max Y). A node is dropped if it is:
   - within the radius of any box;
   - or outside the arena bounds shrunk by the radius.
4. **Path.** Otherwise it takes the shortest path Captain → nodes → Player over clear legs.
   - Leg costs are `isqrt` lengths.
   - The search is Dijkstra, with ties going to the lower node index (solid order, then corner order).
   - A node within 2 units of the Captain counts as reached and is not used as the first step.
   - The Captain steers for the first node on the path, with no orbit.
5. **No path.** If no path exists, it pursues the Player directly.

The search runs every tick from the current position. The corner graph depends only on the radius, the arena bounds and the live solids, so a runtime may memoise it. Telegraphs, attacks, phases, speed and damage are unchanged. There is no leash: the Captain may follow the Player out of the Court. Standard enemies keep § Corner pursuit (D-114), and the Daemon is unchanged.

### Attack vocabulary

The boss has exactly four attacks.

#### Safety Rationale

- Telegraph: 45 ticks, 70-degree cone, range 260.
- Lock cone heading on the final telegraph tick.
- Resolve: 18 damage once inside cone with solid-geometry occlusion.
- Cooldown contribution: 90 ticks.

#### Narrow Tailoring

- Telegraph: 30 ticks.
- Fire three projectiles at sampled Player heading −12°, 0°, +12°.
- Projectile: speed 420, radius 7, lifetime 72 ticks, 9 damage.
- Solids consume projectiles.
- Cooldown contribution: 75 ticks.

#### Temporary Order

- Telegraph: 48 ticks at one authored Captain Camera emitter.
- Activate its fixed field for 180 ticks.
- The Captain Camera is not a standard Camera, cannot be targeted or destroyed, and does not count toward Network Blackout.
- While Player is in its unobstructed field, apply an Observation pulse of base +10 Exposure every 30 ticks, multiplied by the current phase Observation ratio and then upgrade modifiers; round half away from zero.
- Only one Temporary Order field may be active.
- Cooldown contribution: 120 ticks.

#### Independent Review

- Telegraph: 60 ticks with six radial lanes.
- Resolve six projectiles at equal 60-degree spacing, speed 360, radius 7, lifetime 90 ticks, 8 damage.
- A deterministic safe gap is created by omitting the lane nearest the current vector from boss to Player; therefore five projectiles spawn.
- Exact angular ties omit the lower numbered lane.
- Cooldown contribution: 105 ticks.

### Court Lockdown (D-109)

After the Court release (exposure.md § Court release), Exposure is live in the Court. If it reaches 1000 there, Lockdown latches for the rest of the run, and while it holds the Captain presses harder:
- The attack **cooldown** counts down by 2 per tick instead of 1. The contributions above are effectively halved: 45, 38, 60 and 53 ticks, rounding up.
- Telegraph durations, transition recovery, damage, projectiles, fields and phase rules are unchanged, so every attack stays exactly as readable and avoidable.
- Before the Court release, Lockdown cannot coincide with an active Captain, so this applies only to Lockdown entered in the Court.

Measured (scratch probe, 270 legal runs, runtime `5b36566` plus the rule; SS-specs #69):
- Runs that re-entered Lockdown in the Court won 41% (stealth) and 50% (competent), against 61% for those that did not.
- Overall win rate was 52.6%, against 57.0% unchanged.

### Captain Court threshold (D-096)

On the tick the boss activates (`bossActivated`), the Player's Integrity is
raised to at least `player.courtThresholdRestorePercent` (50%) of
`player.integrity` (75 of 150). It is never lowered. The boss fight is judged
on its own: the attrition of the run so far does not decide it before the
first telegraph. The change is authoritative, ordered after the boss
activation in phase 16, and appears in the receipt as a restore, not as damage.

**Quiet approach (D-101).** If `quietApproach` (exposure.md) is still `true`
when the boss activates, the floor is `player.courtQuietRestorePercent` (60%)
instead, that is 90 of 150. This is the stealth reward: a Player who reached
M-C without ever being `tracked` enters the Captain fight measurably
stronger. It uses the same restore, so it is never lowered and never damage.

### Phase presentation (D-096)

Presentation only. Each phase lights the Authority Court differently, on the
world layer (never the HUD), crossfading over 1 s at the phase change:

| Phase | Light |
|---|---|
| Public Safety | cool civic white-blue |
| Civil Liberties | amber |
| Temporary Safeguard | deep red |
| Independent Review | stark white with blue edges |

Every boss telegraph draws a **countdown ring** that closes over the
telegraph's duration, so the moment of resolution is readable without
counting. Reduced Motion keeps the ring and drops any pulse. Reduced Flash
lowers each palette to 60% saturation, and no light ever brightens the scene by
more than the Lockdown tint (animation.md § 8b).

### Phase schedules

Each phase begins its sequence at index 0. After an attack resolves, wait its cooldown contribution, then advance cyclically.

| Phase | Sequence |
|---|---|
| Public Safety | Safety Rationale → Narrow Tailoring |
| Civil Liberties | Narrow Tailoring → Safety Rationale → Temporary Order |
| Temporary Safeguard | Temporary Order → Narrow Tailoring → Safety Rationale |
| Independent Review | Independent Review → Narrow Tailoring → Temporary Order |

Phase transition cancels an unresolved telegraph and hostile projectiles owned by the prior attack, retires the active Captain Camera field, enters 45 ticks of transition recovery, and begins the new sequence. It does not clear standard enemies, standard Camera state, Exposure, mines, or Player projectiles.

## Defeat and Extraction

Boss defeat retires all boss projectiles and Captain Camera fields immediately. It emits `BossDefeated(algorithmicModerate,tick)` once. Extraction arms only under `encounter-objectives.md`. Player death on the same tick remains terminal failure even if boss HP reaches zero.

## Golden vectors

| ID | Scenario | Expected |
|---|---|---|
| BO-001 | Daemon uninterrupted cycle | exact 120/45/instant/36/30/60 timing |
| BO-002 | boss HP 1600/1200/1199/800/799/400/399/1 | phases match table |
| BO-003 | one batch 1220→780 | one transition to Temporary Safeguard |
| BO-020 | boss activates with the Player at 40 Integrity | Player raised to 75 |
| BO-021 | boss activates with the Player at 120 Integrity | unchanged at 120 |
| BO-022 | boss activates at 40 Integrity with `quietApproach` true | Player raised to 90 |
| BO-023 | boss activates at 40 Integrity with `quietApproach` false | Player raised to 75 |
| BO-024 | boss activates at 100 Integrity with `quietApproach` true | unchanged at 100 |
| BO-004 | phase transition during telegraph | prior attack canceled; 45-tick recovery |
| BO-005 | Temporary Order pulse in Public Safety | +11 Exposure before upgrade |
| BO-006 | same pulse with Signal Jammer | +8 after 25% reduction |
| BO-007 | Independent Review lane tie | lower numbered lane omitted |
| BO-008 | boss defeat with active field/projectiles | all retire immediately |
| BO-009 | boss and Player die same tick | terminal failure; boss death recorded |
| BO-010 | Lockdown holds in the Court and the Captain has 90 cooldown ticks left | the cooldown elapses in 45 ticks and the next telegraph starts on the tick after (46th), not the 91st |
| BO-011 | Lockdown entered in the Court during a telegraph | telegraph length unchanged; only later cooldowns count down by 2 |
| BO-012 | Court released and Exposure never reaches 1000 | cooldowns count down by 1, as before (120 cooldown ticks, telegraph on the 121st) |
| BO-010 | zero Cameras destroyed | boss remains defeatable and Extraction can arm |
| BO-025 | the Captain at (1278, 1284) east of a lone 192 × 320 block centred (1152, 1248), the Player held at (980, 1300) west of it | comes within 90 units within 900 ticks (before D-116 it stopped at the face) |
| BO-026 | in the arena, the Captain at (1278, 1284) / (1336, 828) / (2156, 427), the Player held at (1036, 1435) / (1290, 1415) / (2214, 32) | comes within 90 units within 1 800 ticks: the narrow gap under `solid-06`, and the two freezes found under D-117 (`solid-08`, the top edge) |
| BO-027 | the debug `boss` scenario, the Player standing still at the far spawn | the run ends in failure within 6 000 ticks (under D-116 the Captain froze under `solid-11-court-column-a`) |
| BO-028 | a 64 × 144 column centred (1920, 704); radius 30 | the leg (1966, 802)→(1502, 802) is not clear (26 units below the column); (1966, 810)→(1502, 810) is; (1982, 704)→(1982, 900), starting in contact, is |
