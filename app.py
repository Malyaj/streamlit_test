import streamlit as st
import datetime

# Initialize state
if "run" not in st.session_state:
    st.session_state.run = False


st.header('Hold off')
st.markdown("---")

st.set_page_config(page_title="Examples", layout="wide")

col1, col2 = st.columns([1, 4])  # narrow left col, wider right col
with col1:
    # Multi-select dropdown for metrics
    metrics_options = ['spend', 'units', 'visits', 'spend_card', 'units_card', 'visits_card']
    metrics_selected = st.multiselect("Select Metrics:"
                                      , metrics_options
                                      )

    include_refund = ['Include Refunds', 'Exclude Refunds']
    include_refund_choice = st.radio("Choose an option:", include_refund)

    min_date = datetime.date(2024, 1, 1)
    max_date = datetime.date(2025, 12, 31)
    min_date_str = min_date.strftime('%Y-%m-%d')
    max_date_str = max_date.strftime('%Y-%m-%d')

    start_date = st.date_input(f"From date (earliest {min_date_str}):"
                               , value=min_date
                               , min_value=min_date
                               , max_value=max_date
                               )
    
    end_date = st.date_input(f"To date (latest {max_date_str}):"
                             , value=max_date
                             , min_value=min_date
                             , max_value=max_date
                            )
    

    all_stores = [f"store_{str(idx).rjust(2, '0')}" for idx in range(1, 101, 3)]
    stores_selections = st.multiselect("Choose store:", all_stores)    
    
with col2:
    # Action button
    if st.button("Submit"):
        st.session_state.run = True  # Set flag to trigger processing

    # Output only runs after button is pressed
    if st.session_state.run:
        st.write(f"start_date : {start_date}")
        st.write(f"end_date : {end_date}")
        st.write(f"Selected stores : {stores_selections}")
        st.write(f"Selected Metrics : {metrics_selected}")
