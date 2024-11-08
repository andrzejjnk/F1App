import pandas as pd
import bs4 as bs
import urllib.request
from urllib.error import HTTPError
import os
from typing import List

years = [2022, 2023, 2024]

pages_normal = [
    "race-result", "fastest-laps", "pit-stop-summary", "starting-grid", "qualifying", 
    "practice-3", "practice-2", "practice-1"
]
pages_sprint22 = [
    "race-result", "fastest-laps", "pit-stop-summary", "starting-grid", "qualifying", 
    "sprint-results", "sprint-grid", "practice-2", "practice-1"
]
pages_sprint = [
    "race-result", "fastest-laps", "pit-stop-summary", "starting-grid", "qualifying", 
    "sprint-results", "sprint-grid", "sprint-qualifying", "practice-1"
]

pages_normal_after_1238 = [
    "race-result", "fastest-laps", "pit-stop-summary", "starting-grid", "qualifying", 
    "practice/3", "practice/2", "practice/1"
]
pages_sprint_after_1238 = [
    "race-result", "fastest-laps", "pit-stop-summary", "starting-grid", "qualifying", 
    "sprint-results", "sprint-grid", "sprint-qualifying", "practice/1"
]

sprints = [
    "2022/races/1109/emilia-romagna", "2022/races/1115/austria", "2022/races/1137/brazil",
    "2023/races/1207/azerbaijan", "2023/races/1213/austria", "2023/races/1216/belgium",
    "2023/races/1221/qatar", "2023/races/1222/united-states", "2023/races/1224/brazil",
    "2024/races/1233/china", "2024/races/1234/miami", "2024/races/1239/austria", 
    "2024/races/1247/united-states"
]

def replace_page_in_urls(urls: List[str]) -> List[str]:
    updated_urls = []
    
    for url in urls:
        try:
            race_number = int(url.split("/")[7])
        except (IndexError, ValueError):
            print(f"Nieprawidłowy format URL: {url}")
            continue

        if race_number <= 1237:
            pages_normal_list = pages_normal
            pages_sprint_list = pages_sprint22 if "2022" in url else pages_sprint
        else:
            pages_normal_list = pages_normal_after_1238
            pages_sprint_list = pages_sprint_after_1238

        is_sprint = any(sprint in url for sprint in sprints)
        selected_pages = pages_sprint_list if is_sprint else pages_normal_list

        for page in selected_pages:
            updated_url = url.replace("race-result", page)
            updated_urls.append(updated_url)

    return updated_urls


urls = []
with open('urls/races_url.txt', 'r') as file:
    urls = [line.strip() for line in file]


updated_urls = replace_page_in_urls(urls)
with open("urls/updated_urls.txt", "w") as file:
    for url in updated_urls:
        file.write(url + "\n")


def read_urls_from_file(file_path: str) -> list:
    """Funkcja do odczytu URL-i z pliku tekstowego."""
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

def download_tables(urls: list) -> None:
    """Funkcja do pobierania tabel z podanych URL-i i zapisywania ich jako CSV."""
    error_log_path = "error_log.txt"

    for url in urls:
        try:
            source = urllib.request.urlopen(url).read()
            soup = bs.BeautifulSoup(source, 'lxml')

            tables = soup.find_all('table')
            if not tables:
                raise ValueError(f"No table found in {url}")

            data_table = tables[0]
            data = pd.read_html(str(data_table), flavor='bs4', header=[0])[0]
            data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

            parts = url.split("/")
            year = parts[5]
            race_number = parts[7]
            country = parts[8].replace("-", " ").title()

            session_name = url.split("/")[-1].replace(".html", "")

            if '-' in session_name:
                session_name = session_name.replace('-', '_')

            if int(race_number) >= 1238:
                if session_name == "1":
                    session_name = "practice_1"
                elif session_name == "2":
                    session_name = "practice_2"
                elif session_name == "3":
                    session_name = "practice_3"

            directory = f"data/{year}/{session_name}"
            os.makedirs(directory, exist_ok=True)

            data.to_csv(f"{directory}/{country}.csv", index=False)

            print(f"{country} {year} written to {directory}/{country}.csv")

        except Exception as e:
            with open(error_log_path, "a") as log_file:
                log_file.write(f"Error processing {url}: {e}\n")
            print(f"Error processing {url}: {e}")


def add_mising_column_to_data(files: List[str]) -> None:
    for file in files:
        df = pd.read_csv(file)
        df['Time'] = ','
        df.to_csv(file, index=False)

    
# delete 3 unnecessary files which were downloaded, because f1 web page has problems with urls
def delete_incorrect_data(files: List[str]) -> None:
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"The file {file} has been deleted.")
        else:
            print(f"The file {file} does not exist.")


paths_files_to_add_missing_column = ['data/2022/starting_grid/Emilia Romagna.csv', 'data/2022/starting_grid/Austria.csv', 'data/2022/starting_grid/Brazil.csv']
paths_to_delete = ['data/2022/practice_3/Emilia Romagna.csv', 'data/2022/practice_3/Austria.csv', 'data/2022/practice_3/Brazil.csv']


def remove_unwanted_rows_from_csv(directory: str) -> None:
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(subdir, file)
                
                try:
                    df = pd.read_csv(file_path)

                    unwanted_rows = df[df.apply(lambda row: row.astype(str).str.contains("Q1 107% time|^Note|Russell and Piastri|Magnussen received", na=False).any(), axis=1)]

                    if not unwanted_rows.empty:
                        print(f"Removing unwanted rows from {file_path}")
                        df = df[~df.index.isin(unwanted_rows.index)]

                    df.to_csv(file_path, index=False)

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")


def preprocess_data() -> None:
    try:
        data_directory = 'data'
        urlsss = read_urls_from_file(r'urls/updated_urls.txt')
        download_tables(urlsss)
        add_mising_column_to_data(paths_files_to_add_missing_column)
        delete_incorrect_data(paths_to_delete)
        remove_unwanted_rows_from_csv(data_directory)
        print("Data was processed successfully")

    except Exception as e:
        print(f"An error occurred while processing data! {e}")


if __name__=="__main__":
    preprocess_data()