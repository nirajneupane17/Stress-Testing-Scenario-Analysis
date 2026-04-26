# Stress Testing & Scenario Analysis

Python-based stress testing framework covering historical 
crisis scenarios, hypothetical macroeconomic shocks, interest 
rate and credit spread stress, reverse stress testing, and 
tail risk estimation across multi-asset portfolios.

---

## Overview

Stress testing is a regulatory and risk management requirement 
under Basel III, CCAR, and DFAST frameworks. This project 
builds a comprehensive stress testing engine that goes beyond 
simple shock application — covering scenario design, portfolio 
sensitivity analysis, and reverse stress testing to identify 
what scenarios break a portfolio.

---

## Scenarios Implemented

**Historical Crisis Scenarios**
- Black Monday 1987 — single-day equity crash
- dot-com crash 2000 to 2002 — prolonged drawdown
- Global Financial Crisis 2008 to 2009
- COVID-19 crash March 2020
- Russia-Ukraine 2022 — commodity and rate shock

**Hypothetical Macroeconomic Scenarios**
- Severe recession — GDP -4%, unemployment +5%
- Stagflation — high inflation with low growth
- Interest rate shock — parallel shift +300bps
- Credit crisis — spreads widen 500bps
- Equity crash — -40% with vol spike to 60%

**Sensitivity Analysis**
- Factor sensitivity across equity, rates, credit, FX
- Marginal contribution to stress loss
- Concentration risk under stress

**Reverse Stress Testing**
- Identify scenarios that cause portfolio loss > threshold
- Break-even scenario construction
- Regulatory capital implications

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-%233670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54) ![NumPy](https://img.shields.io/badge/NumPy-%230288D1.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-%234527A0.svg?style=for-the-badge&logo=pandas&logoColor=white) ![SciPy](https://img.shields.io/badge/SciPy-%231565C0.svg?style=for-the-badge&logo=scipy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23C62828.svg?style=for-the-badge&logo=Matplotlib&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-%2300C853.svg?style=for-the-badge&logo=plotly&logoColor=white)

---

## Project Structure

```
Stress-Testing-Scenario-Analysis/
│
├── data/
│   ├── returns.csv
│   └── prices.csv
│
├── notebooks/
│   ├── 01_historical_scenarios.ipynb
│   ├── 02_hypothetical_scenarios.ipynb
│   ├── 03_sensitivity_analysis.ipynb
│   ├── 04_reverse_stress_testing.ipynb
│   └── 05_tail_risk_estimation.ipynb
│
├── src/
│   ├── stress_scenarios.py
│   ├── sensitivity.py
│   └── tail_risk.py
│
├── results/
│   ├── 01_historical_crisis_drawdowns.png
│   ├── 02_scenario_pnl_impact.png
│   ├── 03_sensitivity_heatmap.png
│   ├── 04_reverse_stress_test.png
│   ├── 05_tail_risk_distribution.png
│   ├── 06_stress_var_comparison.png
│   ├── 07_factor_contribution.png
│   └── stress_test_summary.csv
│
└── README.md
```

---

## Key Results

- COVID-19 scenario produced worst single-month loss of 
  23.4% for equal-weight portfolio — exceeding 99% VaR
- Interest rate +300bps shock reduced fixed income 
  allocation value by 18.2% — DV01 driven loss
- Reverse stress test identified equity crash of -32% 
  combined with credit spread widening of 400bps as the 
  portfolio break-even scenario
- Stagflation scenario produced the most persistent 
  drawdown — 14 months to recovery vs 6 months for 
  the COVID crash

---

## Regulatory Context

- Basel III — FRTB stress testing requirements
- CCAR and DFAST — Federal Reserve stress test frameworks
- SR 11-7 — model validation for stress testing models
- ICAAP — Internal Capital Adequacy Assessment Process

---

## References

- Basel Committee — Supervisory Framework for Stress Testing
- Federal Reserve — CCAR Scenarios and Methodology
- McNeil, Frey and Embrechts — Quantitative Risk Management
