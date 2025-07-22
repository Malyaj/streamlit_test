import streamlit as st
import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

from utils import generate_dummy_retail_transactions

df = generate_dummy_retail_transactions(num_transactions=500)
df.to_csv("dummy_retail_transactions.csv", index=False)

data = pd.read_csv("dummy_retail_transactions.csv")
data['date'] = pd.to_datetime(data['date'])
st.header('Query Tool')
st.dataframe(data.head(4))
st.markdown("---")

st.set_page_config(page_title="Query Tool", layout="wide")

col1, col2 = st.columns([1, 4])  # narrow left col, wider right col
with col1:
    query_dict = dict()
    
    # Multi-select dropdown for metrics
    metrics_options = ['spend', 'units', 'visits', 'spend_card', 'units_card', 'visits_card']
    metrics_selected = st.multiselect("Select Metrics:"
                                      , metrics_options
                                      )
    query_dict['metrics_list'] = metrics_selected
    
    include_refund = ['Include Refunds', 'Purchase Only']
    include_refund_choice = st.radio("Choose an option:", include_refund)

    
    query_dict['purchase_only'] = False
    if include_refund_choice == include_refund_choice[-1]:
        query_dict['purchase_only'] = True

    min_date = data['date'].min()
    max_date = data['date'].max()
    min_date_str = min_date.strftime('%Y-%m-%d')
    max_date_str = max_date.strftime('%Y-%m-%d')

    start_date = st.date_input(f"From date (earliest {min_date_str}):"
                               , value=min_date
                               , min_value=min_date
                               , max_value=max_date
                               )
    query_dict['to_date'] = start_date
    start_date = pd.to_datetime(start_date)
    
    end_date = st.date_input(f"To date (latest {max_date_str}):"
                             , value=max_date
                             , min_value=min_date
                             , max_value=max_date
                            )
    query_dict['from_date'] = end_date
    end_date = pd.to_datetime(end_date)
    
    # data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

    all_stores = data['store_id'].unique().tolist()
    stores_selections = st.multiselect("Choose store:", all_stores)
    query_dict['filters'] = dict()
    if stores_selections:
        query_dict['filters']['store'] = stores_selections
    
with col2:
    # Execute each aggregation and store the result
    # result = {alias: func(data[col]) for alias, col, func in aggregations}
    # Convert result to a single-row DataFrame
    # agg_df = pd.DataFrame([result])
    # Show DataFrame
    st.subheader("Data Table:")
    st.write(query_dict)  # Interactive table
