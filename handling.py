# Python script to handle missing values in data
import pandas as pd
def handle_missing_values(data_frame):
    filled_data = data_frame.fillna(method='ffill')
    return filled_data