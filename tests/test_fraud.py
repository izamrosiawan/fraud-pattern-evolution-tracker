import os
import pytest
import pandas as pd
from src.fraud_engine import FraudTrackerEngine

def test_fraud_engine():
    engine = FraudTrackerEngine()
    df = engine.load_and_clean_data("data/kaggle_fraud_dataset.csv")
    assert not df.empty
    assert 'is_fraud' in df.columns
    summary = engine.calculate_channel_summary(df)
    assert 'anomaly_score' in summary.columns
