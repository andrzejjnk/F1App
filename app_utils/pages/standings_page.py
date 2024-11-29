import streamlit as st
from utils.lib import *

def ShowStandingsPage() -> None:
    st.title("Standings")

    options = ["Standings", "Compare drivers per year"]
    years = [2022, 2023, 2024]
    
    st.session_state.select_option = st.selectbox("Select option:", options, key="standings_plot_option")
    st.session_state.year = st.selectbox("Select year:", years, key="select_year_standings")

    drivers_to_compare = get_drivers_per_year_from_races(st.session_state.year)['Driver'].tolist()
    drivers_to_compare.insert(0, "All")
    if st.session_state.select_option == options[1]:
        st.session_state.selected_drivers = st.multiselect("Select drivers:", drivers_to_compare, default="All", key="select_drivers_standings")
        if not st.session_state.selected_drivers:
            st.session_state.selected_drivers = ["All"]

    if st.session_state.select_option == options[0]:
        races_df = get_driver_points_per_season_with_race_results(st.session_state.year)
        sprints_df = get_driver_points_per_season_with_sprint_results(st.session_state.year)
        standings_df = merge_race_and_sprint_data(races_df, sprints_df)
        st.dataframe(standings_df, hide_index=True, use_container_width=True)

    elif st.session_state.select_option == options[1]:
        if "All" in st.session_state.selected_drivers:
            fig = plot_drivers_points_specified_year_standings(st.session_state.year)
        else:
            fig = plot_drivers_points_specified_year_standings(st.session_state.year, st.session_state.selected_drivers)
        st.plotly_chart(fig)