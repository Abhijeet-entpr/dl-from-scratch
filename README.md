# Deep Learning From Scratch

## Goal

Build deep-learning understanding from first principles over 20 weeks: implement core concepts in NumPy, progressively move to PyTorch, reproduce a real paper/model, and finish with a defensible public portfolio.

## 20-Week Roadmap

| Week | Focus | Planned Tasks | Target | Milestone |
|---|---|---:|---:|---|
| W1 | Build the workshop · Play the whole game | 12 | 20 | **M0** |
| W2 | Readable, typed code · Debugging as a method | 12 | 22 | |
| W3 | Arrays and dtypes · The axis mental model | 18 | 25 | **M1 HARD GATE** |
| W4 | Supervised framing · Splits and leakage | 18 | 26 | |
| W5 | Linear regression from scratch · Gradient descent behaviour | 18 | 23 | **M2** |
| W6 | Single-neuron gradient · Two-layer derivation | 18 | 23 | |
| W7 | Graph design · Value: add and mul | 18 | 23 | **M3 HARD GATE** |
| W8 | PyTorch as your engine · nn.Module, Dataset, DataLoader | 18 | 24 | |
| W9 | What convolution actually is · Naive conv2d in NumPy | 18 | 26 | |
| W10 | CNNs in PyTorch · ResNet and skip connections | 18 | 24 | **M4** |
| W11 | HOLIDAY — zero scheduled tasks | 0 | 0 | Holiday |
| W12 | Return + tokenisation · Embeddings | 18 | 26 | |
| W13 | The transformer block · Mini-GPT assembly | 18 | 23 | **M5 HARD GATE** |
| W14 | The alignment problem · Contrastive learning intuition | 18 | 24 | |
| W15 | Assemble the model · First real training run | 19 | 24 | |
| W16 | Evaluation harness · Zero-shot classification | 19 | 24 | **M6 HARD GATE** |
| W17 | Reading a paper for implementation · Scope the reproduction | 16 | 22 | |
| W18 | Evaluate and iterate · Final reproduction run | 18 | 23 | **M7** |
| W19 | Extend the ablation · Statistical honesty | 19 | 23 | |
| W20 | Portfolio assembly · Build the defence | 19 | 23 | **M8** |

## Milestones

| Milestone | Week | Description |
|---|---|---|
| **M0** | W1 | Workshop ready: development environment, repository, workflow, and public logging are operational. |
| **M1** | W3 | NumPy foundations: arrays, dtypes, shapes, and axes are understood well enough to reason about numerical code. |
| **M2** | W5 | Gradient descent: linear regression and optimisation are implemented from scratch and behaviour is understood. |
| **M3** | W7 | Autodiff foundations: computational graphs and backpropagation are implemented and understood. |
| **M4** | W10 | CNN foundations: convolution and modern CNN architectures are understood and implemented in PyTorch. |
| **M5** | W13 | Transformer foundations: tokenisation, embeddings, attention, transformer blocks, and a Mini-GPT are assembled. |
| **M6** | W16 | Evaluation: the model can be evaluated with a reproducible harness, including zero-shot classification. |
| **M7** | W18 | Reproduction: a paper implementation is scoped, trained, evaluated, and iterated on. |
| **M8** | W20 | Portfolio complete: results, ablations, analysis, documentation, and defence material are assembled into the final public portfolio. |

## Log

### Day 001 · 2026-09-01 · Environment

- Set up VS Code + Remote-WSL and confirmed development happens inside the WSL Linux environment.
- Created the public `dl-from-scratch` repository, scaffolded the project, created the Python virtual environment, and configured the initial Git workflow.
- Configured GitHub SSH authentication and established the public daily-log protocol for the 20-week project.

### Day 002 · YYYY-MM-DD · Title

- What I built:
- What I learned:
- Evidence / result:

### Day 003 · YYYY-MM-DD · Title

- What I built:
- What I learned:
- Evidence / result:

## Progress

- [x] Day 001 — Environment
- [ ] Day 002
- [ ] Day 003
- [ ] Day 004
- [ ] Day 005
- [ ] Day 006
- [ ] Day 007
- [ ] Day 008
- [ ] Day 009
- [ ] Day 010

## Repository Structure

```text
dl-from-scratch/
├── README.md
├── .gitignore
├── .venv/
├── notebooks/
├── src/
├── tests/
├── data/
└── projects/
