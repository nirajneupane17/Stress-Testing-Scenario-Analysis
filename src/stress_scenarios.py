"""
stress_scenarios.py
===================
Stress testing scenarios — historical and hypothetical.
Author : Niraj Neupane | github.com/nirajneupane17
"""
import numpy as np
import pandas as pd

HYPOTHETICAL_SCENARIOS = {
    'Severe Recession':   {'SPY':-0.35,'QQQ':-0.40,'TLT':+0.15,'GLD':+0.05,'EFA':-0.30},
    'Stagflation':        {'SPY':-0.20,'QQQ':-0.25,'TLT':-0.15,'GLD':+0.20,'EFA':-0.18},
    'Rate Shock +300bps': {'SPY':-0.12,'QQQ':-0.15,'TLT':-0.22,'GLD':-0.05,'EFA':-0.10},
    'Credit Crisis':      {'SPY':-0.25,'QQQ':-0.28,'TLT':+0.10,'GLD':+0.08,'EFA':-0.22},
    'Equity Crash -40%':  {'SPY':-0.40,'QQQ':-0.45,'TLT':+0.18,'GLD':+0.10,'EFA':-0.35},
    'Russia-Ukraine':     {'SPY':-0.08,'QQQ':-0.12,'TLT':-0.08,'GLD':+0.12,'EFA':-0.15},
}

HISTORICAL_PERIODS = {
    'GFC 2008':         ('2008-09-01','2009-03-31'),
    'Euro Crisis 2011': ('2011-07-01','2011-11-30'),
    'COVID-19 2020':    ('2020-02-15','2020-05-31'),
    'Rate Shock 2022':  ('2022-01-01','2022-12-31'),
}


def compute_drawdown(returns_series):
    cum = (1 + returns_series).cumprod()
    roll_max = cum.expanding().max()
    return (cum - roll_max) / roll_max * 100


def compute_scenario_pnl(scenarios, weights, assets):
    results = {}
    for sc, shocks in scenarios.items():
        shock_vec = np.array([shocks[a] for a in assets])
        results[sc] = round(np.dot(weights, shock_vec) * 100, 2)
    return results


def historical_crisis_stats(port_returns):
    rows = []
    for name, (s, e) in HISTORICAL_PERIODS.items():
        mask = (port_returns.index >= s) & (port_returns.index <= e)
        period = port_returns[mask]
        if len(period) > 0:
            cum_ret = (1 + period).prod() - 1
            max_dd  = compute_drawdown(period).min()
            rows.append({'Period': name, 'Total Return': round(cum_ret*100,2),
                         'Max Drawdown': round(max_dd,2),
                         'Ann. Vol': round(period.std()*np.sqrt(252)*100,2),
                         'Days': len(period)})
    return pd.DataFrame(rows).set_index('Period')
