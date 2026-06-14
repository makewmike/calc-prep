# calc-prep 📐

A self-managed Calculus 1 readiness tracker powered by AI study sessions.

Each study session is coached by Claude using the skill in `skills/calc-coach.md`.
Session logs are committed to this repo after every session, keeping progress visible
in the GitHub contribution graph and giving me a readable study history.

---

## Current Status

- **Readiness score:** 5/12 (May 25, 2026 diagnostic)
- **Average mastery:** 4.2/10
- **Sessions completed:** 2
- **Total study time:** 53 minutes
- **Current streak:** 1 day(s)
- **Last session:** 2026-06-14
- **Target:** Calc 1 ready at Coastline Community College
- **Overall goal:** Physics B.S. pathway → CSUSM / ASU transfer

---

## Topic Mastery

| Topic | Mastery (0–10) | Last Studied | Priority |
|---|---|---|---|
| Algebra (equations, exponents, radicals) | 5 | 2026-06-14 | 🟡 Medium |
| Functions & graphs (domain, range, transforms) | 4 | — | 🔴 High |
| Composition & inverses | 4 | — | 🔴 High |
| Trigonometry (unit circle, identities) | 4 | — | 🔴 High |
| Exponentials & logarithms | 4 | — | 🔴 High |
| Limits intuition & behavior | 4 | 2026-05-26 | 🔴 High |

> Mastery scores and the table above are regenerated automatically by `generate_readme.py`.
> Run `python generate_readme.py` after any manual edits to `progress/mastery.json`.

---

## 6–8 Week Plan

| Week | Focus |
|---|---|
| 1–2 | Algebra bootcamp |
| 3–4 | Functions, graphs, inverses |
| 5–6 | Trig + exponentials/logs |
| 7–8 | Limits intuition + mixed review |

---

## Branching Strategy

| Branch | Purpose |
|---|---|
| `main` | Stable. All real study sessions commit here. |
| `dev` | Experimental changes to `skills/calc-coach.md`, new topic structures, or script edits. Merge to `main` once verified. |

To start an experimental change:
```bash
git checkout dev
# make edits
git push origin dev
# open a PR or merge to main when ready
```

---

## Repo Structure

```
calc-prep/
├── README.md                    ← This file; auto-updated by generate_readme.py
├── generate_readme.py           ← Regenerates mastery table from mastery.json
├── validate.py                  ← Validates progress JSON files against schemas
├── setup.sh                     ← One-time repo initialization script (see below)
├── skills/
│   └── calc-coach.md            ← AI study coach instruction file
├── logs/
│   └── YYYY-MM-DD-NN.md         ← One session log per study block
├── progress/
│   ├── mastery.json             ← Numeric topic mastery scores (0–10)
│   ├── mastery.schema.json      ← JSON Schema for mastery.json
│   ├── streak.json              ← Session count, streak, total minutes
│   └── streak.schema.json       ← JSON Schema for streak.json
├── quizzes/
│   └── YYYY-MM-DD-quiz.md       ← Saved quiz questions and reviewed answers
└── notes/
    └── <topic>.md               ← Concept reference notes built during sessions
```

---

## Setup (First Time Only)

`setup.sh` is a one-time initialization script. Run it once after cloning the repo on a new machine:

```bash
bash setup.sh
```

It sets your Git `user.email` and `user.name`, makes an initial commit, and prints the commands to push to GitHub. You only need this when setting up on a new machine — it is not part of the normal study workflow.

---

## Scripts

| Script | When to run | What it does |
|---|---|---|
| `python validate.py` | Before any commit | Validates `mastery.json` and `streak.json` against their schemas. Exits with error if malformed. |
| `python generate_readme.py` | After any session | Regenerates the mastery table and status block in this README from live JSON data. |

The AI coach runs both scripts automatically during Phase 4 of each session.

---

## How to Start a Session

One-liner (no copy-paste required):

```
Start a new calc prep session using makewmike/calc-prep
```

The coach reads all progress files automatically. See `skills/calc-coach.md` for topic override, drill-only, and catch-up review starters.

---

## Contribution Graph

Every completed session produces a commit to `main` attributed to your GitHub email.
The commit message format is:

```
study: <topic> (<duration>m) — session <N>
```

Example: `study: trig unit circle + inverse functions (45m) — session 3`
