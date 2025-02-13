import os
import pandas as pd
import matplotlib.pyplot as plt

# Current directory of nps.py
current_directory = os.path.dirname(os.path.abspath(__file__))

# Filepath to survery responses
file_path = os.path.join(current_directory, "Survey_responses.csv")

# Check if file exists
if os.path.isfile(file_path):
    survey_data = pd.read_csv(file_path)
    print(survey_data.head())
    print(survey_data.columns)
else:
    print(f"File {file_path} was not found.")


# Define the column name for Question 7
question_7_column = '7.  How likely are you to recommend this app to other F1 fans? '

# Extract responses for Question 7
responses_q7 = survey_data[question_7_column]

# Categorize responses into Promoters, Passives, and Detractors
promoters = responses_q7[responses_q7 >= 9].count()  # Scores 9 or 10
passives = responses_q7[(responses_q7 >= 7) & (responses_q7 <= 8)].count()  # Scores 7 or 8
detractors = responses_q7[responses_q7 <= 6].count()  # Scores 0 through 6

# Calculate total number of responses
total_responses = len(responses_q7)

# Calculate NPS
nps = ((promoters - detractors) / total_responses) * 100

print("NPS Stats:")
print(f"promoters: {promoters}")
print(f"passives: {passives}")
print(f"detractors: {detractors}")
print(f"total responses: {total_responses}")
print(f"Net Promoter Score: {nps:.1f} %")

file_path_nps_png = os.path.join(current_directory, "nps_score.png")

# Data for the pie chart
labels = ['Promoters 😊', 'Passives 😐', 'Detractors 😠']
sizes = [23, 4, 9]
colors = ['#4CAF50', '#FFC107', '#F44336']  # Green, Yellow, Red
explode = (0.1, 0, 0)  # Explode the Promoters slice for emphasis

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12})
plt.title('Net Promoter Score Breakdown', fontsize=16)

plt.savefig(file_path_nps_png)
plt.tight_layout()
plt.show()


