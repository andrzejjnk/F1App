import streamlit as st
from utils.lib import *

def ShowFP3_Page():
    st.title("Practice 3")

    options = ["Practice 3 Results per race", "Practice 3 Results per driver", "Gaps to the leader"]
    years = [2022, 2023, 2024]
    st.session_state.select_option = st.selectbox("Select option:", options, key="practice3_results_plot_option")
    st.session_state.year = st.selectbox("Select year:", years, key="select_year_practice3_results")
    drivers_to_compare = get_drivers_per_year_from_practice3_data(st.session_state.year)['Driver'].tolist()
    drivers_to_compare.insert(0, "All")
    
    if st.session_state.select_option == options[0] or st.session_state.select_option == options[2]:
        st.session_state.country = st.selectbox("Select practice 3:", list(practice3_orders[int(st.session_state.year)].values()), key="select_countries_practice3_results")

    if not st.session_state.select_option == options[0] and not st.session_state.select_option == options[1] and not st.session_state.select_option == options[2]:
        st.session_state.selected_drivers = st.multiselect("Select drivers:", drivers_to_compare, default="All", key="select_drivers_practice3_results")
        if not st.session_state.selected_drivers:
            st.session_state.selected_drivers = ["All"]
    elif st.session_state.select_option == options[1] and not st.session_state.select_option == options[2]:
        st.session_state.selected_drivers = st.selectbox("Select drivers:", drivers_to_compare[1: ], key="select_drivers_practice3_results")
        if not st.session_state.selected_drivers:
            st.session_state.selected_drivers = ["All"]

    if st.session_state.select_option == options[0]:
        practice3_result_year_country_df = get_practice3_data_data_race_year(st.session_state.country, st.session_state.year)
        practice3_result_year_country_df['Year'] = practice3_result_year_country_df['Year'].astype(str)
        st.dataframe(practice3_result_year_country_df, hide_index=True, use_container_width=True)

    if st.session_state.select_option == options[1]:
        practice3_result_year_driver_df = get_driver_results_per_year_practice3_data(st.session_state.year, st.session_state.selected_drivers)
        practice3_result_year_driver_df['Year'] = practice3_result_year_driver_df['Year'].astype(str)
        st.dataframe(practice3_result_year_driver_df, hide_index=True, use_container_width=True)

    if st.session_state.select_option == options[2]:
        practice3_result_year_country_df = get_practice3_data_data_race_year(st.session_state.country, st.session_state.year)
        fig = plot_time_gap_practice_session(practice3_result_year_country_df, 'FP3')
        st.plotly_chart(fig)