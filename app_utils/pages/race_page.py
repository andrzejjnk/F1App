import streamlit as st
from utils.lib import *

def ShowRacePage() -> None:
    st.title("Race")
    
    options = ["Race Results per race", "Race Results per driver", "Compare points from races in a specified year", "Compare positions in a specified year", "Compare positions in a specified race"]
    years = [2022, 2023, 2024]
    st.session_state.select_option = st.selectbox("Select option:", options, key="race_results_plot_option")
    if not st.session_state.select_option == options[4]:
        st.session_state.year = st.selectbox("Select year:", years, key="select_year_race_results")
    drivers_to_compare = get_drivers_per_year_from_races(st.session_state.year)['Driver'].tolist()
    drivers_to_compare.insert(0, "All")

    if st.session_state.select_option == options[0]:
        st.session_state.country = st.selectbox("Select race:", list(race_orders[int(st.session_state.year)].values()), key="select_countries_race_results")
    elif st.session_state.select_option == options[4]:
        st.session_state.country = st.selectbox("Select race:", unique_races, key="select_countries_race_results")
    
    if not st.session_state.select_option == options[0] and not st.session_state.select_option == options[1]:
        st.session_state.selected_drivers = st.multiselect("Select drivers:", drivers_to_compare, default="All", key="select_drivers_race_results")
        if not st.session_state.selected_drivers:
            st.session_state.selected_drivers = ["All"]
    elif st.session_state.select_option == options[1]:
        st.session_state.selected_drivers = st.selectbox("Select drivers:", drivers_to_compare[1: ], key="select_drivers_race_results")
        if not st.session_state.selected_drivers:
            st.session_state.selected_drivers = ["All"]

    if st.session_state.select_option == options[0]:
        race_result_year_country_df = get_race_result_data_race_year(st.session_state.country, st.session_state.year)
        race_result_year_country_df['Year'] = race_result_year_country_df['Year'].astype(str)
        st.dataframe(race_result_year_country_df, hide_index=True, use_container_width=True)

    if st.session_state.select_option == options[1]:
        race_result_year_driver_df = get_driver_results_per_year(st.session_state.year, st.session_state.selected_drivers)
        race_result_year_driver_df['Year'] = race_result_year_driver_df['Year'].astype(str)
        st.dataframe(race_result_year_driver_df, hide_index=True, use_container_width=True)

    elif st.session_state.select_option == options[2]:
        if "All" in st.session_state.selected_drivers:
            fig = plot_drivers_points_specified_year(st.session_state.year)
        else:
            fig = plot_drivers_points_specified_year(st.session_state.year, st.session_state.selected_drivers)
        st.plotly_chart(fig)

    elif st.session_state.select_option == options[3]:
        if "All" in st.session_state.selected_drivers:
            fig = plot_comparision_between_drivers_specified_year(st.session_state.year)
        else:
            fig = plot_comparision_between_drivers_specified_year(st.session_state.year, st.session_state.selected_drivers)
        st.plotly_chart(fig)

    elif st.session_state.select_option == options[4]:
        if "All" in st.session_state.selected_drivers:
            fig = plot_comparision_between_drivers_specified_country(st.session_state.country, drivers_to_compare[1: ])
        else:
            fig = plot_comparision_between_drivers_specified_country(st.session_state.country, st.session_state.selected_drivers)
        st.plotly_chart(fig)