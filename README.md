# Right Fit Finder (Live)
*Players • Coaches • Coaching Staff — using current game data*

> **Status:** Work-in-progress (see roadmap).  
> **Goal (in simple words):** Help a club pick the **right people**—on and off the pitch—using **fresh, real-time data**, not last year’s tables.

## Why this exists (the story)
I’m a Liverpool fan. Rivalry aside, my view is that **Manchester United’s** struggles over the past decade are partly a **scouting/fit** problem: big-name signings that don’t align with the team’s **role, system, or pressing style**. This project focuses on the **scouting layer** — finding **right-fit** players (and later coaches and staff), so decisions are based on **fit and form**, not hype.

### For people new to football (soccer)
Think of it like hiring for a company: the “best” résumé isn’t always the **best fit** for *your* team and *today’s* needs. This tool finds candidates who match **how your team actually plays** right now, and explains **why** they fit.

---

## Why live APIs (not a static dataset)?
**Static CSVs** are common (and a bit cliché). They go stale, miss injuries and form, and can leak future info into training.  
**Hypothesis:** If we pull **current match data via APIs**, compute **rolling form** (last 6–10 matches), and use a simple **learning-to-rank** model, we can generate **better “fit” shortlists** than any static snapshot—especially for clubs that need to move quickly and buy for **fit**, not fame.

**What live data unlocks**
- **Timeliness** — rankings update after each match.  
- **Context** — minutes, injuries, opponent strength, and role usage are baked in.  
- **Fair testing** — generate a shortlist “as of” a date, then check what happened *after* (minutes, xG/xA, transfers).

---

## What this app will do
1) **Right Player Finder (MVP)**  
   - **Input:** Team & role (e.g., “pressing forward”, “ball-progressing midfielder”).  
   - **Output:** **Top-10 shortlist** with a **FitScore**, percentiles vs role peers, recent-form trend, and a **“review” gray zone** for borderline cases.  
   - **Why it helps:** Fewer name-over-fit mistakes, faster shortlists, clearer reasons.

2) **Coach Fit (Phase 3)**  
   - **Idea:** Build a **coach style profile** from their teams’ historic patterns (pressing intensity, possession %, directness, etc.).  
   - **Output:** Match a coach’s style to a club’s desired style & constraints.

3) **Coaching Staff Fit (Phase 4, exploratory)**  
   - **Idea:** Early signals from tenure, role specialism (set-pieces, analysis), and known networks.  
   - **Note:** Data is sparse; we’ll document limits and treat this as research.

---

## How it works (no jargon)
- We fetch **fresh stats** from public football APIs.  
- We calculate **rolling performance** (last 6–10 games), adjusted for playing time and league strength.  
- We compare candidates to **what the team needs** (your system & roles).  
- We score and rank candidates, then explain **why** each one fits.  
- If the model isn’t sure, it flags the candidate for **human review** (the gray zone).

### For tech folks (a peek)
- **Data:** API-FOOTBALL / football-data.org (live backbone), optional Understat xG (community libs), StatsBomb Open (static baseline).  
- **Store:** Postgres or DuckDB with `as_of` timestamps.  
- **Features:** per-90 stats, rolling windows, league-translation coefficients, availability.  
- **Models:** k-NN similarity + **learning-to-rank** (e.g., XGBoost) → **FitScore**.  
- **Risk controls:** sample-size penalty, league-translation penalty, **gray-zone** review band.  
- **UI:** Streamlit (MVP), then FastAPI backend + Streamlit/Vercel frontend.

---

## Public app (plan)
I plan to **deploy a public demo** so anyone—**with or without football knowledge**—can try it:
- **Streamlit** MVP (fastest): dropdowns for team & role, Top-10 table, explanations.  
- **Then**: split to **FastAPI** backend + hosted frontend (Render/Railway/Vercel).  
- **Updates**: nightly or post-match refresh; “Last updated” shown in the app.

---

## Roadmap
**Phase 1 (MVP — Players, 2–3 roles, one club)**  
- Live ingest, rolling features, FitScore, Top-10 shortlist, gray-zone flag, Streamlit UI, backtest on past windows.

**Phase 2 (Multi-team Europe)**  
- Team “profiles” in JSON/YAML (style weights, role needs, constraints).  
- League translation and caching to manage API quotas.  
- Team dropdown in the app.

**Phase 3 (Coach Fit)**  
- Coach style embeddings; match coach → club profile.  
- Validate on post-hire style continuity (temporal holds).

**Phase 4 (Coaching Staff Fit, exploratory)**  
- Early signals & limits; publish findings and next steps.

---

## Getting started (dev)
```bash
# 1) setup
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2) config
cp .env.example .env   # add your API keys

# 3) build + run (MVP)
python scripts/ingest.py
python scripts/features.py
python scripts/rank.py
streamlit run app.py
```

`.env.example`
```
API_FOOTBALL_KEY=your_key_here
FDATA_KEY=optional
UNDERSTAT_OK=use_at_own_risk
DATABASE_URL=postgresql://user:pass@localhost:5432/right_fit_finder
```

---

## Licensing & data use
- **Code:** Apache-2.0 (permissive).  
- **Docs/diagrams:** (optional) CC BY 4.0 if you want to allow reuse with attribution.  
- **Data:** We **do not** redistribute third-party match/player data. Users fetch their own via API keys and accept provider terms. See `DATA_LICENSE.md` and `NOTICE`.

---

## Contributing
Issues and PRs welcome—especially team profiles (JSON), league coefficients, and UI improvements. See `CONTRIBUTING.md` for the workflow.

---

## FAQ (for everyone)
- **Is this “AI”?** It uses machine-learning to rank candidates and explain fit. We keep it **simple and transparent** on purpose.  
- **Will it replace scouts?** No. It **augments** scouting—surfacing good options faster and explaining why. Humans still decide.  
- **Can it be wrong?** Yes. That’s why we flag a **gray zone** for review and monitor results over time.

---

### Portfolio blurb (copy/paste)
**Right Fit Finder (Live):** a tool that picks **players, coaches, and staff** who fit a team’s style using **current game data**. It updates after every match, explains **why** each pick fits, and flags risky choices for review—so clubs avoid name-over-fit signings and fans (even newcomers) can follow the logic.
