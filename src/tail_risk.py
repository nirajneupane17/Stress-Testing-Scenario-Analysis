"""
tail_risk.py
============
Tail risk estimation — VaR, ES, rolling measures.
Author : Niraj Neupane | github.com/nirajneupane17
"""
import numpy as np
import pandas as pd


def compute_var_es(returns, confidence_levels=[0.90,0.95,0.975,0.99,0.995]):
    rows = []
    for cl in confidence_levels:
        var_val = abs(np.percentile(returns, (1-cl)*100))
        tail    = returns[returns <= -var_val]
        es_val  = abs(tail.mean()) if len(tail) > 0 else var_val
        rows.append({'confidence': f'{int(cl*100)}%',
                     'VaR': round(var_val,4), 'ES': round(es_val,4),
                     'ES/VaR': round(es_val/var_val,3)})
    return pd.DataFrame(rows).set_index('confidence')


def rolling_tail_risk(returns, window=252, cl=0.99):
    var_series = returns.rolling(window).quantile(1-cl)*(-1)
    es_series  = returns.rolling(window).apply(
        lambda x: abs(x[x<=np.percentile(x,(1-cl)*100)].mean()) if len(x[x<=np.percentile(x,(1-cl)*100)])>0 else np.nan
    )
    return pd.DataFrame({f'VaR_{int(cl*100)}': var_series,
                          f'ES_{int(cl*100)}': es_series})


def stress_var(returns, stress_period_mask, cl=0.99):
    normal_var = abs(np.percentile(returns, (1-cl)*100))
    stress_var = abs(np.percentile(returns[stress_period_mask], (1-cl)*100))
    multiplier = stress_var / normal_var if normal_var > 0 else 1
    return {'normal_var': round(normal_var,4), 'stress_var': round(stress_var,4),
            'stress_multiplier': round(multiplier,2)}
