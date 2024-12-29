import streamlit as st
from utils.lib import *
 
def ShowHighlightsPage() -> None:
    st.title("F1 Highlights Viewer")

    years = [2022, 2023, 2024]
    st.session_state.year = st.selectbox("Select year:", years, key="highlights_years", index=years.index(years[-1]))
    races = list(race_orders[st.session_state.year].values())
    default_index = len(races) - 1
    st.session_state.country = st.selectbox("Select GP:", races, key="highlights_countries", index=default_index)    
    sessions = get_sessions_per_year_and_race(st.session_state.year, st.session_state.country)
    st.session_state.session_name = st.selectbox("Select session:", sessions, key="highlights_session", index=sessions.index('Race'))
    video_player, highlights_name = get_highlights_for_specified_year_race_and_session(st.session_state.year, st.session_state.country, st.session_state.session_name)
    st.write(highlights_name)

    embed_url = video_player

    st.markdown(f"""
        <iframe width="100%" height="700" src="{embed_url}" frameborder="0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)