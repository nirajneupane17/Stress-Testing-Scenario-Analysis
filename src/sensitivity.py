"""
sensitivity.py
==============
Portfolio sensitivity analysis across asset shocks.
Author : Niraj Neupane | github.com/nirajneupane17
"""
import numpy as np
import pandas as pd


def compute_sensitivity_matrix(weights, assets, shock_range=(-0.40, 0.40, 0.05)):
    shocks = np.arange(*shock_range)
    rows = []
    for shock in shocks:
        row = {'Shock (%)': round(shock*100, 0)}
        for i, asset in enumerate(assets):
            row[asset] = round(weights[i]*shock*100, 3)
        row['Portfolio'] = round(sum(weights[i]*shock for i in range(len(assets)))*100, 3)
        rows.append(row)
    return pd.DataFrame(rows).set_index('Shock (%)')


def marginal_contribution(weights, returns, scenario_shocks, assets):
    rows = []
    for asset, w in zip(assets, weights):
        shock = scenario_shocks.get(asset, 0)
        rows.append({'Asset': asset, 'Weight': round(w*100,1),
                     'Shock (%)': round(shock*100,1),
                     'Contribution (%)': round(w*shock*100,2)})
    return pd.DataFrame(rows).set_index('Asset')


def concentration_risk(weights, assets):
    hhi = sum(w**2 for w in weights)
    return {'HHI': round(hhi, 4), 'Effective_N': round(1/hhi, 2),
            'Max_weight': round(max(weights)*100, 1),
            'Top_asset': assets[np.argmax(weights)]}
