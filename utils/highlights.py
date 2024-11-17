import pandas as pd
from typing import List


def get_highlights_player(year: int, race: str, session: str) -> str | None:
    videos = pd.read_csv('data/videos/videos.csv')
    selected_row = videos[(videos['Year'] == year) & 
                        (videos['Race'] == race) & 
                        (videos['Session'] == session)]
    
    if selected_row.empty:
        print("Not found any row compliant with input parameters!")

    ACCOUNT_ID = selected_row.iloc[0, 0]
    PLAYER_ID = selected_row.iloc[0, 1]
    VIDEO_ID = selected_row.iloc[0, 2]
    # Video player URL syntax:
    #f"https://players.brightcove.net/{ACCOUNT_ID}/{PLAYER_ID}_default/index.html?videoId={VIDEO_ID}"
    video_player = f"https://players.brightcove.net/{ACCOUNT_ID}/{PLAYER_ID}_default/index.html?videoId={VIDEO_ID}"
    return video_player


def get_highlights_name(year: int, race: str, session: str) -> str:
    highlights_name = f"{race} {year} Grand Prix {session}"
    return highlights_name

def get_sessions_per_year_and_race(year: int, race: str) -> List[str] | None:
    videos = pd.read_csv('data/videos/videos.csv')
    selected_rows = videos[(videos['Year'] == year) & 
                        (videos['Race'] == race) ]

    if selected_rows.empty:
        print("Not found any row compliant with input parameters!")

    return list(selected_rows['Session'])


def get_highlights_for_specified_year_race_and_session(year: int, race: str, session: str) -> str | None:
    video_player = get_highlights_player(year, race, session)
    highlights_name = get_highlights_name(year, race, session)
    return (video_player, highlights_name)
