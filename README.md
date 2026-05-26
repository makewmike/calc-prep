# calc-prep 📐

A self-managed Calculus 1 readiness tracker powered by AI study sessions.

Each study session is coached by Claude using the skill in `skills/calc-coach.md`.
Session logs are committed to this repo after every session, keeping progress visible
in the GitHub contribution graph and giving me a readable study history.

---

## Current Status

- **Readiness score:** 5/12 (May 25, 2026)
- **Target:** Calc 1 ready at Coastline Community College
- **Overall goal:** Physics B.S. pathway → CSUSM / ASU transfer

---

## Topic Mastery

| Topic | Mastery (0–10) | Last Studied | Priority |
|---|---|---|---|
| Algebra (equations, exponents, radicals) | 4 | — | 🔴 High |
| Functions & graphs (domain, range, transforms) | 4 | — | 🔴 High |
| Composition & inverses | 4 | — | 🔴 High |
| Trigonometry (unit circle, identities) | 4 | — | 🔴 High |
| Exponentials & logarithms | 4 | — | 🔴 High |
| Limits intuition & behavior | 3 | — | 🔴 High |

> Mastery is updated each session in `progress/mastery.json`.

---

## 6–8 Week Plan

| Week | Focus |
|---|---|
| 1–2 | Algebra bootcamp |
| 3–4 | Functions, graphs, inverses |
| 5–6 | Trig + exponentials/logs |
| 7–8 | Limits intuition + mixed review |

---

## Repo Structure

```
calc-prep/
├── README.md               ← This file; goals and current mastery
├── skills/
│   └── calc-coach.md       ← AI study coach instruction file (load this into Claude)
├── logs/
│   └── YYYY-MM-DD-NN.md    ← One session log per study block
├── progress/
│   ├── mastery.json        ← Numeric topic mastery scores (0–10)
│   └── streak.json         ← Session count, streak, total minutes
├── quizzes/
│   └── YYYY-MM-DD-quiz.md  ← Saved quiz questions and reviewed answers
└── notes/
    └── <topic>.md          ← Concept reference notes built during sessions
```

---

## How to Start a Session

Open Claude (desktop app, Claude.ai, or Claude Code with GitHub MCP) and paste:

```
Load skills/calc-coach.md and start a study session.
```

Or use one of the starter prompts in `skills/calc-coach.md`.

---

## Contribution Graph

Every completed session produces a commit to `main` attributed to your GitHub email.
The commit message format is:

```
study: <topic> (<duration>m) — session <N>
```

Example: `study: trig unit circle + inverse functions (45m) — session 3`
