import os
import pandas as pd
import numpy as np

class FraudTrackerEngine:
    def __init__(self, random_state=42):
        self.random_state = random_state

    def load_and_clean_data(self, filepath):
        df = pd.read_csv(filepath)
        return df

    def calculate_channel_summary(self, df):
        return df.groupby('channel')[['is_fraud', 'anomaly_score', 'amount_usd']].agg({'is_fraud': 'sum', 'anomaly_score': 'mean', 'amount_usd': 'sum'}).round(2)
