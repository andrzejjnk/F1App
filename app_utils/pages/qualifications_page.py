import streamlit as st
from utils.lib import *

def ShowQualificationsPage() -> None:
    st.title("Qualifications")

    options = ["Qualifying Results per race", "Qualifying Results per driver", "Gaps to the leader"]
    years = [2022, 2023, 2024]
    st.session_state.select_option = st.selectbox("Select option:", options, key="qualifications_results_plot_option")
    st.session_state.year = st.selectbox("Select year:", years, key="select_year_qualifications_results")
    drivers_to_compare = get_drivers_per_year_from_qualifications(st.session_state.year)['Driver'].tolist()
    drivers_to_compare.insert(0, "All")
    
    if st.session_state.select_option == options[0] or st.session_state.select_option[2]:
        st.session_state.country = st.selectbox("Select qualifications:", list(race_orders[int(st.session_state.year)].values()), key="select_countries_qualifications_results")

    if st.session_state.select_option == options[2]:
        st.session_state.quali_session = st.selectbox("Select session:", ['Q1', 'Q2', 'Q3'], key="select_session_qualifications_results")

    if not st.session_state.select_option == options[0] and not st.session_state.select_option == options[1] and not st.session_state.select_option == options[2]:
        st.session_state.selected_drivers = st.multiselect("Select drivers:", drivers_to_compare, default="All", key="select_drivers_qualifications_results")
        if not st.session_state.selected_drivers:
            st.session_state.selected_drivers = ["All"]
    elif st.session_state.select_option == options[1] and not st.session_state.select_option == options[2]:
        st.session_state.selected_drivers = st.selectbox("Select drivers:", drivers_to_compare[1: ], key="select_drivers_qualifications_results")
        if not st.session_state.selected_drivers:
            st.session_state.selected_drivers = ["All"]

    if st.session_state.select_option == options[0]:
        qualifications_result_year_country_df = get_qualifications_data_race_year(st.session_state.country, st.session_state.year)
        qualifications_result_year_country_df['Year'] = qualifications_result_year_country_df['Year'].astype(str)
        st.dataframe(qualifications_result_year_country_df, hide_index=True, use_container_width=True)

    if st.session_state.select_option == options[1]:
        qualifications_result_year_driver_df = get_driver_results_per_year_qualifications(st.session_state.year, st.session_state.selected_drivers)
        qualifications_result_year_driver_df['Year'] = qualifications_result_year_driver_df['Year'].astype(str)
        st.dataframe(qualifications_result_year_driver_df, hide_index=True, use_container_width=True)

    if st.session_state.select_option == options[2]:
        quali_df = get_qualifications_data_race_year(st.session_state.country, st.session_state.year)
        time_deltas_df = calculate_time_delta(quali_df)
        fig = plot_time_gap_per_session(time_deltas_df, st.session_state.quali_session)
        st.plotly_chart(fig)
    first_call = False