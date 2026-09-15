# M4 Design and Build Text-Only Prototype Rubric — 12 points

Use whole points only. Performance levels: Mastery / Proficient / Developing / No Evidence.

| Criterion | Mastery — 3 | Proficient — 2 | Developing — 1 | No Evidence — 0 |
|---|---|---|---|---|
| **Three-Layer Responsibility** — MLO 4.2 | Text interface, business logic, and stubbed data responsibilities are clearly separable; core rules can operate independently of the interface and the boundaries support later reuse. | Three layers are distinguishable and generally separated, with minor responsibility leakage or coupling. | Layers are named but responsibilities are substantially mixed, duplicated, or difficult to inspect independently. | No usable three-layer separation is demonstrated. |
| **Executable Behavior + Traceability** — MLO 4.2 | A complete selected product-slice path runs; behavior materially reflects the design investigation and demonstrates at least one traced requirement/acceptance criterion. | A meaningful path runs and is connected to product work, with minor gaps in behavior or traceability. | Prototype runs only partially or traceability is asserted rather than demonstrated. | No meaningful executable product-slice evidence or traceability is shown. |
| **State / Data Design** — MLO 4.2 | Required state is represented deliberately; the stubbed data boundary is replaceable and preserves the information needed by the selected behavior without spreading persistence assumptions through the interface. | State and stubbed data are generally appropriate, with minor coupling, missing detail, or unnecessary hard-coding. | State/data choices are incomplete, fragile, or embedded across layers in ways that obscure responsibility. | No usable state/data design is demonstrated. |
| **Evaluation, Revision + Handoff** — MLO 4.3 support | Uses prototype behavior as evidence: identifies what the build confirmed or exposed, makes a defensible revision or explicitly justifies no revision, names unresolved/stubbed work, and makes the next implementation question clear. | Evaluates prototype behavior and identifies relevant remaining work, with minor gaps in revision rationale or handoff clarity. | Reflection is mostly descriptive; consequences, revision, or unresolved work are vague. | No meaningful evaluation, revision evidence, or handoff is shown. |

## Alignment note
- Criteria 1–3 directly assess MLO 4.2.
- Criterion 4 supplies implementation-based evidence for MLO 4.3 and the M4 → M5 handoff.
- The rubric evaluates responsibility, behavior, evidence, and revision — not a required file naming convention or identical implementation.
