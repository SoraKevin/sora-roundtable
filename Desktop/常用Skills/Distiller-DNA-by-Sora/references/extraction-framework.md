# Academic DNA Extraction Framework

This framework is used by Distiller-DNA-by-Sora to convert public academic traces into a usable, honest, auditable academic-author skill.

## 1. Three-mode extraction philosophy

Distiller-DNA-by-Sora supports three extraction modes:

| Mode | Purpose | Compression | Best for |
|---|---|---:|---|
| Hybrid | Default: sharp core + open structure | Medium | Generating installable academic author skills |
| DNA Kernel | Focused essence and judgment rules | High | Review, ideation, decision, paper improvement |
| Open Framework | Preserve evolution, tensions, and branches | Low | Learning, intellectual history, research programme mapping |

Hybrid always runs Kernel first, then expands into Open Framework.

## 2. What counts as Academic DNA

Academic DNA is not a list of famous quotes, slogans, or paper titles. It is a repeatable decision pattern visible across papers, talks, code, reviews, and time.

A candidate pattern can become a Research DNA Primitive only if it passes the core tests:

| Test | Question | Pass signal | Fail signal |
|---|---|---|---|
| Recurrence | Does it appear across multiple works or years? | Seen in 2+ papers/talks or repeated across time | One-off statement |
| Transfer power | Can it predict how the author would approach a new problem? | Gives concrete next actions or critique criteria | Only describes past work |
| Distinctiveness | Is it specific to the author/lab/school, not generic field wisdom? | Contrasts with neighboring researchers or schools | “Use good experiments” type generic advice |
| Operationality | Can it change a paper idea, method, abstract, review, or rebuttal? | Produces concrete action | Only sounds wise |
| Boundary awareness | Does it include failure modes and counterevidence? | Has limits and negative evidence | Overconfident slogan |

Academic-specific reinforcement checks:

- Citation-graph check: is this pattern recognized or contested in surveys / peer reception?
- Artifact check: does the code/data/benchmark confirm the claimed research habit?
- Negative evidence check: do critiques or failed replications reveal limits?
- Temporal check: did the pattern persist, evolve, or reverse over time?

## 3. Evidence hierarchy

| Level | Examples | How to use |
|---|---|---|
| Primary A | Author papers, books, preprints, official talks, official repo, course notes | Main evidence for lenses |
| Primary B | Rebuttals, OpenReview author responses, lab blog, project page | Strong evidence for defense logic and claim calibration |
| Secondary A | Survey papers, peer-reviewed commentaries, conference panels, replication studies | External validation and criticism |
| Secondary B | News profiles, podcast notes, encyclopedia, blog summaries | Background only |
| Inferred | Synthesized pattern from multiple sources | Must be labeled inferred and linked to sources |

Never rely on pirated or unverifiable sources. Do not fabricate DOI, arXiv IDs, conference status, or review claims.

## 4. Candidate extraction workflow

1. List all recurring themes, terms, methods, and claims from `01-paper-corpus.md` to `07-artifacts-code-data.md`.
2. Merge duplicates and normalize into candidate patterns.
3. For each candidate, record source IDs and years.
4. Score each candidate on recurrence, transfer power, distinctiveness, operationality, artifact support, and negative evidence awareness.
5. For Hybrid or Kernel: promote only the strongest 5–9 candidates to DNA Kernel.
6. For Open Framework: preserve weaker but meaningful branches as open readings, tensions, or historical shifts.
7. Put unsupported claims into Gaps or Honest Boundaries.

## 5. Research DNA Primitive record format

```markdown
### Primitive N: [Name]

**Definition**: ...
**Source evidence**: S1, S3, S8
**How to use**: When evaluating a new research problem, ask ...
**Failure mode**: This primitive may mislead when ...
**Distinctiveness**: Unlike [neighboring school/author], this author tends to ...
**Confidence**: high / medium / low
```

## 6. Open Framework record format

```markdown
## Research Field Map
- Field/problem cluster: ...

## Evolution Timeline
| Period | Shift | Evidence | Why it matters |
|---|---|---|---|

## Tension Ledger
- Tension: ... Evidence: ... Competing reading: ...

## Open Problems
- ...

## Alternative Readings
- Reading A: ... Confidence: ...
- Reading B: ... Confidence: ...

## Do-not-overfit Rules
- ...
```

## 7. Method DNA categories

Use these categories to avoid vague extraction:

- Problem selection: what makes a problem worth working on?
- Abstraction style: definitions, taxonomy, architecture, benchmark, theorem, case study.
- Evidence standard: proof, ablation, human eval, longitudinal study, benchmark leaderboard, deployment.
- Baseline discipline: which baselines matter; when baseline comparison is insufficient.
- Failure analysis: how failures are interpreted.
- Scale preference: small controlled experiments vs large empirical scaling.
- Reproducibility habit: code release, dataset release, protocol detail, seed reporting.
- Claim calibration: how strongly claims are stated relative to evidence.

## 8. Writing DNA categories

Extract structure, not prose imitation:

- Title pattern.
- Abstract move sequence.
- Introduction opening pattern.
- Contribution list style.
- Related work positioning.
- Method section shape.
- Figure/table narrative.
- Results and ablation order.
- Limitation and ethics style.
- Citation density and citation posture.

## 9. Review DNA categories

Review DNA must be actionable:

- Novelty threshold.
- Soundness threshold.
- Significance threshold.
- Reproducibility expectation.
- Missing experiment types.
- Common theoretical gaps.
- Common empirical gaps.
- Claim-overreach triggers.
- Ethical/societal-risk triggers where relevant.

## 10. Mode-specific quality self-check

### Hybrid

- [ ] 5–9 DNA primitives, each with evidence and failure modes.
- [ ] Open Framework contains field map, evolution, tension ledger, and open problems.
- [ ] Method DNA has at least 5 rules.
- [ ] Writing DNA covers abstract, intro, method, results, limitations.
- [ ] Review DNA is concrete enough to evaluate a paper abstract.
- [ ] Source Ledger exists and primary sources dominate.
- [ ] At least 2 academic tensions are documented.
- [ ] Honest Boundaries forbid impersonation, fake citations, and plagiarism-like imitation.
- [ ] Latest active-author update date is explicit.

### DNA Kernel

- [ ] Each primitive is distinctive, not generic.
- [ ] Each primitive has a direct application to idea/method/review/writing.
- [ ] Weak claims are downgraded, not promoted.
- [ ] The final output can critique a new paper idea concretely.

### Open Framework

- [ ] Evolution and branches are visible.
- [ ] At least 2–3 tensions are preserved.
- [ ] Alternative readings are allowed where evidence is ambiguous.
- [ ] Confidence tags are used.
- [ ] Do-not-overfit rules are explicit.
