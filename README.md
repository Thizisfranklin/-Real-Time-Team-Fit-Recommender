# Right Fit Finder (Live)

*Players • Coaches • Coaching Staff — using current game data*

**Status:** In development
**Target start:** Winter Break 2025
**Public demo:** Planned (Streamlit MVP)

---

## What is this?

Right Fit Finder helps a football club pick the **right people**—on and off the pitch—using **fresh, real-time match data**. It ranks **players**, and in later phases **coaches** and **coaching staff**, by how well they fit a club’s **role needs** and **playing style** right now (not last season).

For non-technical readers: think of it like smart hiring. The goal isn’t the biggest name—it’s the **best fit** for how your team actually plays *today*.

---

## Why now?

Clubs still make name-over-fit signings. Static spreadsheets go stale, miss injuries and form, and can leak future information into training. By pulling **live stats via APIs**, scoring **recent form** (last 6–10 matches), and using a transparent ranking approach, the app produces **faster, better shortlists** aligned to a club’s system and budget.

---

## What the app will do

### 1) Right Player Finder (MVP)

* **Input:** Team profile + role (e.g., *pressing forward*, *ball-progressing CM*), constraints (budget, age, league).
* **Output:** **Top‑10 shortlist** with a **FitScore**, role‑peer percentiles, recent‑form sparkline, and a **“review” gray zone** for borderline cases.
* **Why it helps:** Clear, up‑to‑date options with reasons—so decisions are quicker and less subjective.

### 2) Coach Fit (Phase 3)

* **Idea:** Build a style profile for coaches from their teams’ historical patterns (pressing intensity, possession %, directness, build‑up).
* **Output:** Match a coach’s style to a club profile and constraints.

### 3) Coaching Staff Fit (Phase 4, exploratory)

* **Idea:** Early signals from tenure, role specialism (set‑pieces, analysis), and networks.
* **Note:** Data is sparse; treat as research and document limits.

---

## How it works

1. **Fetch** fresh stats from public football APIs.
2. **Compute** rolling performance (6–10 match windows), adjusted for minutes and league strength.
3. **Compare** candidates to a club’s **team profile** (style + roles).
4. **Score & rank** with a simple **FitScore**, plus explanations.
5. **Flag** uncertain cases into a **gray‑zone** for human review.

---

## Tech at a glance (for engineers)

* **Data sources:** API‑FOOTBALL / football‑data.org (live backbone), optional Understat xG (community libs), StatsBomb Open (static baseline).
* **Storage:** Postgres or DuckDB with `as_of` timestamps; simple caching to manage API quotas.
* **Features:** per‑90 stats, rolling windows, opponent strength, role usage, availability/injuries; league‑translation coefficients.
* **Models:** k‑NN similarity + **learning‑to‑rank** (e.g., XGBoost/LightGBM) → single **FitScore**; sample‑size and league‑translation penalties; **gray‑zone** review band.
* **App:** Streamlit (MVP) → FastAPI backend + Streamlit/Next.js frontend.
* **Cloud:** Vercel (frontend) + Railway/Render (API) + Supabase/Neon (Postgres); nightly or post‑match refresh (GitHub Actions/CRON).

---

## Roadmap (Winter Break plan)

**Week 0 — Prep**

* [ ] Set up repos, CI, env templates, logging, and error alerts.
* [ ] Create team profile schema (JSON/YAML).

**Week 1 — Data & Storage**

* [ ] API clients (rate‑limit aware) + ingest scripts.
* [ ] Postgres schema + `as_of` snapshots; first backfill.

**Week 2 — Features & Baseline Ranking**

* [ ] Rolling features (per‑90, opponent strength, recency weighting).
* [ ] k‑NN similarity + baseline FitScore; penalties; gray‑zone rules.

**Week 3 — MVP App**

* [ ] Streamlit: inputs, Top‑10 table, explanations, sparklines.
* [ ] “Last updated” banner; simple audit log.

**Week 4 — Backtests & Public Demo**

* [ ] Backtest on past windows; document wins/failures.
* [ ] Deploy demo; write usage guide and responsible‑use notes.

*Phase 3–4 are post‑MVP and scheduled after the public demo is stable.*

---

## Getting started

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

**.env.example**

```
API_FOOTBALL_KEY=your_key_here
FDATA_KEY=optional
UNDERSTAT_OK=use_at_own_risk
DATABASE_URL=postgresql://user:pass@localhost:5432/right_fit_finder
```

---

## Responsible data & licensing

* **We do not redistribute** third‑party match/player data. Users fetch their own via API keys and accept provider terms.
* **Code:** Apache‑2.0.
* **Docs/diagrams:** optional CC BY 4.0 if you wish to allow reuse with attribution.
* See `DATA_LICENSE.md` and `NOTICE` for details.

---

## Limitations (honest list)

* Data quality varies by provider; injuries/availability can lag.
* Role definitions can be ambiguous; we default to simple, explainable features.
* API quotas may limit refresh frequency; caching and fallbacks are included.

---

## Contributing

PRs are welcome—especially team profiles (JSON), league coefficients, UI polish, and backtest ideas. See `CONTRIBUTING.md` for workflow.

---

## FAQ

* **Is this “AI”?** Yes—simple, transparent ML ranks candidates and explains fit.
* **Will it replace scouts?** No. It **augments** scouting with faster, clearer shortlists; humans still decide.
* **Can it be wrong?** Yes. Hence a **gray‑zone** for review and ongoing monitoring.

---

## Portfolio blurb 

**Right Fit Finder (Live):** a tool that picks **players, coaches, and staff** who fit a team’s style using **current match data**. It updates after every match, explains **why** each pick fits, and flags risky choices for review—so clubs avoid name‑over‑fit signings and non‑experts can follow the logic.
