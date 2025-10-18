# SystemFit — Real‑Time Team Fit Recommender

*Players • Coaches • Coaching Staff — using current game data*

**Status:** In progress (starting Winter Break 2025)
**Demo:** Streamlit MVP planned
**Plan:** If it works well after testing, I’ll deploy it as a simple **cloud app** so the public can try it.

---

## Backstory (why this exists)

I’m a **Liverpool** fan. Our biggest rivals are **Manchester United**. Over the last decade, United haven’t looked like the powerhouse they used to be. They’ve spent huge fees on players and hired famous coaches, but the results haven’t matched the investment. My take: it’s often a **fit** problem, not a talent problem.

So I’m building **SystemFit**—a simple recommendation tool (powered by a small ML model) that picks people who actually **fit the team’s style right now**. I’ll start with **Manchester United** as the first case study, then make it easy to add other clubs later.

---

## What is this?

SystemFit is a personal project that helps a soccer club pick the **right people** for how they play **right now**. It starts with **players** and later can include **coaches** and **coaching staff**. The goal is to use **current match data (that's  integrating API instead of a static dataset which won't reflect real time scenarios or data)** to build a clear, up‑to‑date shortlist.

**Simple idea:** big names aren’t always the best fit. This tool looks for **fit + form** and explains *why* a pick makes sense.

---

## What it will do (MVP)

* **Input:** Team + role (e.g., pressing forward, ball‑progressing CM) and basic constraints (budget, age, league).
* **Output:** **Top‑10 list** with a simple **FitScore**, percentiles vs role peers, a small **recent‑form** trend, and a **“review”** zone for borderline cases.

**Later:**

* **Coach Fit:** build a basic style card for coaches and match that to a club profile.
* **Staff Fit:** early signals from role speciality and tenure (exploratory only).

---

## How it works

1. **Get fresh stats** from public football data sites (APIs).
2. **Measure recent form** (last 6–10 games), adjusted for minutes and league strength.
3. **Compare** each candidate to what the team needs (style + role).
4. **Rank** them and show short, readable reasons.
5. **Flag** uncertain cases to a **review zone** for a human to decide.

---

## Why it’s useful

* **Up‑to‑date:** updates after matches, so shortlists don’t go stale.
* **Clear:** simple scores and small explanations anyone can read.
* **Practical:** helps avoid “name over fit” signings.

---

## Plan / To‑Do (winter break)

* [ ] Write the data pull script (rate‑limit safe).
* [ ] Build basic features and a first **FitScore**.
* [ ] Make a simple **Streamlit** page (inputs, Top‑10, reasons, last‑updated).
* [ ] Back‑test on a few past months and note where it worked/failed.
* [ ] If results look good → **deploy a cloud demo** and share the link.

---

**.env.example**

```
API_FOOTBALL_KEY=your_key_here
FDATA_KEY=optional
UNDERSTAT_OK=use_at_own_risk
DATABASE_URL=postgresql://user:pass@localhost:5432/systemfit
```

---

## Cloud plan

If tests look good: **Streamlit on Vercel**, small API (optional), and a lightweight database (Neon/Supabase Postgres or DuckDB). Nightly or post‑match refresh.

---

## Notes on data & license

* I won’t redistribute third‑party match data. Users bring their own API keys and accept the provider’s terms.
* **Code license:** Apache‑2.0.

---

## One‑liner Summary

**SystemFit:** a personal, real‑time tool that ranks **players (and later coaches/staff)** for team fit using **current match data**, with a simple score and reasons anyone can understand.
