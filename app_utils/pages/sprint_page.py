import streamlit as st
from utils.lib import *

def ShowSprintPage() -> None:
    st.title("Sprint")

    options = ["Sprint Results per sprint", "Sprint Results per driver", "Compare points from sprints in a specified year", "Compare positions in a specified year", "Compare positions in a specified sprint"]
    years = [2022, 2023, 2024]
    st.session_state.select_option = st.selectbox("Select option:", options, key="sprint_results_plot_option")
    if not st.session_state.select_option == options[4]:
        st.session_state.year = st.selectbox("Select year:", years, key="select_year_sprint_results")
    drivers_to_compare = get_drivers_per_year_from_sprints(st.session_state.year)['Driver'].tolist()
    drivers_to_compare.insert(0, "All")
    
    if st.session_state.select_option == options[0]:
        st.session_state.country = st.selectbox("Select sprint:", list(sprint_orders[int(st.session_state.year)].values()), key="select_countries_sprint_results")
    elif st.session_state.select_option == options[4]:
        st.session_state.country = st.selectbox("Select sprint:", unique_sprints, key="select_countries_sprint_results")

    if not st.session_state.select_option == options[0] and not st.session_state.select_option == options[1]:
        st.session_state.selected_drivers = st.multiselect("Select drivers:", drivers_to_compare, default="All", key="select_drivers_sprint_results")
        if not st.session_state.selected_drivers:
            st.session_state.selected_drivers = ["All"]
    elif st.session_state.select_option == options[1]:
        st.session_state.selected_drivers = st.selectbox("Select drivers:", drivers_to_compare[1: ], key="select_drivers_sprint_results")
        if not st.session_state.selected_drivers:
            st.session_state.selected_drivers = ["All"]

    if st.session_state.select_option == options[0]:
        sprint_result_year_country_df = get_sprint_result_data_sprint_year(st.session_state.country, st.session_state.year)
        sprint_result_year_country_df['Year'] = sprint_result_year_country_df['Year'].astype(str)
        st.dataframe(sprint_result_year_country_df, hide_index=True, use_container_width=True)

    if st.session_state.select_option == options[1]:
        sprint_result_year_driver_df = get_driver_results_per_year_sprints(st.session_state.year, st.session_state.selected_drivers)
        sprint_result_year_driver_df['Year'] = sprint_result_year_driver_df['Year'].astype(str)
        st.dataframe(sprint_result_year_driver_df, hide_index=True, use_container_width=True)

    elif st.session_state.select_option == options[2]:
        if "All" in st.session_state.selected_drivers:
            fig = plot_drivers_points_specified_year_sprints(st.session_state.year)
        else:
            fig = plot_drivers_points_specified_year_sprints(st.session_state.year, st.session_state.selected_drivers)
        st.plotly_chart(fig)

    elif st.session_state.select_option == options[3]:
        if "All" in st.session_state.selected_drivers:
            fig = plot_comparision_between_drivers_specified_year_sprints(st.session_state.year)
        else:
            fig = plot_comparision_between_drivers_specified_year_sprints(st.session_state.year, st.session_state.selected_drivers)
        st.plotly_chart(fig)

    elif st.session_state.select_option == options[4]:
        if "All" in st.session_state.selected_drivers:
            fig = plot_comparision_between_drivers_specified_country_sprints(st.session_state.country, drivers_to_compare[1: ])
        else:
            fig = plot_comparision_between_drivers_specified_country_sprints(st.session_state.country, st.session_state.selected_drivers)
        st.plotly_chart(fig)