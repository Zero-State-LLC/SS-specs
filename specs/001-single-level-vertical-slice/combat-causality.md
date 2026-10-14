# Combat causality clarification

Status: CANONICAL (D-103 implementation candidate)
Contributor workflows: AGENTS.md. Scope: accepted phases 1–3; art and device acceptance deferred.

## Collision and identity
Ruleset ss-rules-008 replaces ss-rules-007; older replays fail closed before tick 1. Content, arena and envelope schema identities remain unchanged. Preserve the existing world-wall convention: projectile center segment versus solid rectangles; projectile radius expands circular actor targets only. Wall entry time uses the same Q8 interval [0,256] and half-away rounding as actor sweep time. Earliest entry wins, walls win equal quantized times. Starting inside/on an actor hit circle is entry at zero, not exit time. Stationary overlap hits at zero. Other LOS and ordering conventions remain unchanged. Tests must exercise simulation intersection generation, not only sorting supplied times.

## Damage evidence
Every ruleset-008 playerDamaged retains amount, remainingIntegrity and sourceEntityId, and adds damageKind (projectile/mine/contact/attack), ownerEntityId (decimal ID or null), impactXQ8/impactYQ8 (Player anchor, raw fixed-point integers), sourceXQ8/sourceYQ8 (incoming hazard point or null), and contributors (decimal source IDs). Projectile direction uses its previous point on the incoming sweep, retained before retirement. A mine uses its own ID/center, with Vendor ID stored separately as owner. Direct attacks/contact use the actor. Contact lists up to three current contributors in descending DPS then stable-ID order; this does not claim exact attribution of carried fractional damage. Multiple contributors, absent source or coincident source draw a non-directional ring, never an invented upward direction. Distinct hazards may not be coalesced into a false single directional claim. Reduced presentation preserves this meaning.

projectileHit adds impactXQ8/impactYQ8 at target anchor and projectileKind (civicPulse/ricochet). A trace requires one civicPulse and one ricochet hit sharing original projectile ID and distinct targets. Independent shots never form a chain. Separate chains stay separate; incomplete evidence draws no invented path. Event evidence is immutable and cannot drive gameplay.

## Weapon presentation (phase 3)
Civic Pulse remains the only automatic weapon. Its logical weapon anchor equals the Player simulation anchor; a visible hand/device muzzle offset is cosmetic and cannot move projectile authority. Aim follows the firing target independently of locomotion facing. A discharge cue requires weaponFired; no target means no cue. Warm-white round pulse, trail and impact remain distinct from hostile fire. Physical emitter design requires a later model-sheet review; this does not approve a fantasy staff or firearm.

## Upgrade clarity
Retain the required protected SwiftUI overlay, equal ordered cards, no default or timeout. Cards communicate role, practical effect, numerical summary and exclusions; spoken and visual meaning match. Non-color icons, VoiceOver activation and 200% Dynamic Type reflow/scroll are required.

- Signal Jammer: camera contact minus 1/tick (minimum 1); Fog/Observation minus 25%; no Tamper or damage reduction. Phase 3 renders a cyan segmented interference contour only while modification occurs, static under reduced motion.
- Ricochet Pulse: one additional target within 160 units, full damage, clear LOS, no third hit. Trace only the real pair.
- Ghost Step: dodge 540 units/s for 0.2 s; cooldown 1.5 s; camera concealment 0.5 s including dodge. Start through start+29 inclusive is 30 ticks. No damage immunity; Fog/Observation and Tamper still apply. Baseline Dodge may share the existing afterimage recipe, but must not display Ghost Step's separate non-color concealment boundary. Phase 3 adds that boundary for the actual immunity window.

Ambush tutorial says TRIPLE DAMAGE, correcting stale D-090 copy without changing damage.

## Bounded history
Retain positions for current and one previous presented snapshot only. Immutable hit/chain positions come from events. Expired IDs must not accumulate for the whole run. Restart clears position/coalescing history.

## Acceptance
- CC-001: real simulation target-before-wall, wall-before-target and exact tie; start-inside, stationary and missing intersections.
- CC-002: mine with distant/dead owner records hazard and owner separately; retired bolt retains incoming point.
- CC-003: multiple-contact, absent/coincident direction uses a ring; distinct hazards remain truthful.
- CC-004: unrelated same-tick hits produce no trace; two chains yield two separate traces; incomplete pairs produce none.
- CC-005: position history bounded by current plus previous snapshot; restart clears it.
- CC-006: ruleset-007 rejected; old/new golden canonical states reviewed before new hashes adopted.
- CC-007: visual/spoken copy matches triple ambush, 30-tick concealment, no damage immunity.
- CC-008 (phase 3): aim/fire, Jammer and concealment effects and accessible overlay verified on device.
