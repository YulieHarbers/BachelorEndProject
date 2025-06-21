import pandas as pd
import numpy as np
import os

rawData = pd.read_csv(r"C:\Users\20223868\OneDrive - TU Eindhoven\Documents\School\year 3\BEP\code\results-survey911887final.csv")

rawData.set_index("What is your participant ID?", inplace=True)
dataS = rawData[[
       'Please enter your age',
       'What study year are you currently in? [1st Year]',
       'What study year are you currently in? [2nd Year]',
       'What study year are you currently in? [3rd Year]',
       'What study year are you currently in? [4th Year]',
       'What study year are you currently in? [5th Year]',
       'What study year are you currently in? [6th Year or higher]',
       'What is your gender? [Male]', 'What is your gender? [Female]',
       'What is your gender? [Other]',
       'What is your gender? [I prefer not to say]',
       'What is your current education?',
       'What is your ethnic background?',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 0][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 1][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 2][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 3][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 4][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 5][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 6][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 7][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 8][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 9][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 10][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 11][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 12][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 13][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 14][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 15][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 16][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 17][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 18][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 19][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 20][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 21][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 22][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 23][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 24][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 25][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 26][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 27][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 28][Scale 2]',
       'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 29][Scale 2]'
       ]].copy()

def getStudyYear(row):
    if row["What study year are you currently in? [1st Year]"] == "Yes":
        return 1
    elif row["What study year are you currently in? [2nd Year]"] == "Yes":
        return 2
    elif row["What study year are you currently in? [3rd Year]"] == "Yes":
        return 3
    elif row["What study year are you currently in? [4th Year]"] == "Yes":
        return 4
    elif row["What study year are you currently in? [5th Year]"] == "Yes":
        return 5
    elif row["What study year are you currently in? [6th Year or higher]"] == "Yes":
        return 6
    else:
        return None
dataS.loc[:, "studyYear"] = dataS.apply(getStudyYear, axis=1)
dataS = dataS.drop(["What study year are you currently in? [1st Year]", "What study year are you currently in? [2nd Year]", "What study year are you currently in? [3rd Year]", "What study year are you currently in? [4th Year]", "What study year are you currently in? [5th Year]", "What study year are you currently in? [6th Year or higher]"], axis=1)

participant_folders =['pp02', 'pp03', 'pp04', 'pp06', 'pp22', 'pp30', 'pp31', 'pp24', 'pp25', 'pp45', 'pp53', 'pp47', 'pp49', 'pp56', 'pp66', 'pp75', 'pp70', 'pp85', 'pp93', 'pp102', 'pp96', 'pp104', 'pp103', 'pp91', 'pp115', 'pp107', 'pp110', 'pp112', "pp95", "pp97"]
base_directory = r"C:\Users\20223868\OneDrive - TU Eindhoven\Documents\School\year 3\BEP\code\OpenFace_DATA"
selected_columns = [
    "AU01_r", "AU02_r", "AU04_r", "AU05_r", "AU06_r", "AU07_r", "AU09_r", "AU10_r", "AU12_r", "AU14_r",
    "AU15_r", "AU17_r", "AU20_r", "AU23_r", "AU25_r", "AU26_r", "AU45_r",
    "AU01_c", "AU02_c", "AU04_c", "AU05_c", "AU06_c", "AU07_c", "AU09_c", "AU10_c", "AU12_c", "AU14_c",
    "AU15_c", "AU17_c", "AU20_c", "AU23_c", "AU25_c", "AU26_c", "AU28_c", "AU45_c"
]

summary_data = []

for participant in participant_folders:
    participant_path = os.path.join(base_directory, participant)
    for i in range(30):
        filename = f'cropped_video{i:02d}.csv'
        filepath = os.path.join(participant_path, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
        df = pd.read_csv(filepath)
        df.columns = df.columns.str.strip()
        missing_cols = [col for col in selected_columns if col not in df.columns]
        if missing_cols:
            print(f"Skipping {filename}: missing columns {missing_cols}")
            continue

        # Create interaction columns
        for col in selected_columns:
            if col.endswith('_r'):
                base = col[:-2]
                presence_col = f"{base}_c"
                if presence_col in df.columns:
                    interaction_col = f"{base}_interaction"
                    df[interaction_col] = df[col] * df[presence_col]
        interaction_columns = [f"{col[:-2]}_interaction" for col in selected_columns if col.endswith('_r') and f"{col[:-2]}_c" in df.columns]
        all_columns_to_summarize = selected_columns + interaction_columns
        means = df[all_columns_to_summarize].mean()
        stds = df[all_columns_to_summarize].std()
        row = {'participant': participant, 'file': filename}
        for col in all_columns_to_summarize:
            row[f'{col}_mean'] = means[col]
            row[f'{col}_std'] = stds[col]
        summary_data.append(row)
        print(row)

#summary DataFrame
summary_df = pd.DataFrame(summary_data)

def getGender(row):
    if row["What is your gender? [Male]"] == "Yes":
        return True
    else:
        return False
dataS["isMale"] = dataS.apply(getGender, axis=1)
dataS = dataS.drop(["What is your gender? [Male]", "What is your gender? [Female]", "What is your gender? [Other]", "What is your gender? [I prefer not to say]"], axis=1)

dataS.rename(columns={"Please enter your age": "age", "What is your current education?":"educationLevel", "What is your ethnic background?":"ethnicity"}, inplace=True)

dataS.rename(columns={
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 0][Scale 2]': "affEng0",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 1][Scale 2]': "affEng1",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 2][Scale 2]': "affEng2",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 3][Scale 2]': "affEng3",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 4][Scale 2]': "affEng4",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 5][Scale 2]': "affEng5",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 6][Scale 2]': "affEng6",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 7][Scale 2]': "affEng7",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 8][Scale 2]': "affEng8",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 9][Scale 2]': "affEng9",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 10][Scale 2]': "affEng10",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 11][Scale 2]': "affEng11",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 12][Scale 2]': "affEng12",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 13][Scale 2]': "affEng13",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 14][Scale 2]': "affEng14",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 15][Scale 2]': "affEng15",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 16][Scale 2]': "affEng16",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 17][Scale 2]': "affEng17",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 18][Scale 2]': "affEng18",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 19][Scale 2]': "affEng19",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 20][Scale 2]': "affEng20",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 21][Scale 2]': "affEng21",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 22][Scale 2]': "affEng22",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 23][Scale 2]': "affEng23",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 24][Scale 2]': "affEng24",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 25][Scale 2]': "affEng25",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 26][Scale 2]': "affEng26",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 27][Scale 2]': "affEng27",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 28][Scale 2]': "affEng28",
    'For cognitive engagement, answer this question: Were you prepared to exert the required effort to learn the material in this section?  \xa0  For affective engagement answer this question: Did you like this section or feel interested or enjoyment while watching this section?  [Video 29][Scale 2]': "affEng29"
}, inplace=True)

for i in range(30):
    dataS[f"affEng{i}"] = dataS[f"affEng{i}"].map({"Yes": True, "No": False})

affEngVars = []
for i in range(30):
    affEngVars.append(f"affEng{i}")


summary_df["participant"] = pd.to_numeric(summary_df["participant"].str[2:])

labels = np.array([])

rows = summary_df.shape[0]

pd.to_numeric(summary_df.iloc[0]["file"][-6:-4])

for i in range(rows):
    videonr = pd.to_numeric(summary_df.iloc[i]["file"][-6:-4])
    partnr = pd.to_numeric(summary_df.iloc[i]["participant"])
    try:
        labels = np.append(labels, dataS.loc[partnr][f"affEng{videonr}"])
    except KeyError as e:
        labels = np.append(labels, np.NaN)
        print(f"Can't find video number {videonr} for participant {e}")

summary_df["labels"] = labels
summary_df["labels"] = summary_df["labels"].astype('Int64')
summary_df.to_csv(r'C:\Users\20223868\OneDrive - TU Eindhoven\Documents\School\year 3\BEP\code\fau_with_labels.csv', index=False)
