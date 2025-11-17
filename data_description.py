import pandas as pd
import numpy as np

df = pd.read_csv('fetal_health.csv')

col_keeping = ['baseline value', 'accelerations', 'fetal_movement', 'uterine_contractions', 'light_decelerations', 'severe_decelerations',
       'prolongued_decelerations', 'abnormal_short_term_variability', 'mean_value_of_short_term_variability',
       'percentage_of_time_with_abnormal_long_term_variability', 'mean_value_of_long_term_variability', 'fetal_health']

stats= df[col_keeping].agg(['mean','std']).T

stats.columns = ["Mean", "Standard Deviation"]

print(stats)
