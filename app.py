import streamlit as st
from st_on_hover_tabs import on_hover_tabs
from utils.lib import *
from app_utils.pages.overview_page import ShowOverviewPage
from app_utils.pages.highlights_page import ShowHighlightsPage
from app_utils.pages.standings_page import ShowStandingsPage
from app_utils.pages.race_page import ShowRacePage
from app_utils.pages.sprint_page import ShowSprintPage
from app_utils.pages.qualifications_page import ShowQualificationsPage
from app_utils.pages.sprint_qualifications_page import ShowSprintQualificationsPage
from app_utils.pages.FP1 import ShowFP1_Page
from app_utils.pages.FP2 import ShowFP2_Page
from app_utils.pages.FP3 import ShowFP3_Page


st.set_page_config(page_title="F1App", page_icon=":racing_car:", layout="wide")
st.markdown('<style>' + open('app_utils/css/style.css').read() + '</style>', unsafe_allow_html=True)

# Set the background image
# background_image = """
# <style>
# [data-testid="stAppViewContainer"] > .main {
#     background-image: url("");
#     background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
#     background-position: center;  
#     background-repeat: no-repeat;
# }
# </style>
# """

AppTabs = ['Overview', 'Highlights','Standings', 'Race', 'Sprint', 'Qualifications', 'Sprint Qualifications', 'FP1', 'FP2', 'FP3']
icons = ['dashboard', 'dashboard', 'dashboard', 'dashboard', 'dashboard', 'dashboard', 'dashboard', 'dashboard', 'dashboard', 'dashboard']

with st.sidebar:
    tabs = on_hover_tabs(tabName=AppTabs, iconName=icons, default_choice=0)
    

if tabs == 'Overview':
    ShowOverviewPage()

elif tabs == 'Highlights':
    ShowHighlightsPage()

elif tabs == 'Standings':
    ShowStandingsPage()

elif tabs == 'Race':
    ShowRacePage()

elif tabs == 'Sprint':
    ShowSprintPage()

elif tabs == 'Qualifications':
    ShowQualificationsPage()

elif tabs == 'Sprint Qualifications':
    ShowSprintQualificationsPage()

elif tabs == 'FP1':
    ShowFP1_Page()

elif tabs == 'FP2':
    ShowFP2_Page()

elif tabs == 'FP3':
    ShowFP3_Page()