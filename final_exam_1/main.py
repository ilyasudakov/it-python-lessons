import pandas as pd
import matplotlib.pyplot as plt
import json

data = pd.read_csv("medical_examination.csv")

data = data.drop_duplicates()
data = data.dropna()

data_list = []

for _, row in data.iterrows():
    data_list.append(
        {
            "model": "patients.Patient",
            "pk": int(row["id"]),
            "fields": {
                # "age": pd.to_datetime(row["age"], unit="d").strftime("%Y-%m-%d"),
                "age": int(row["age"]),
                "gender": int(row["gender"]),
                "height": int(row["height"]),
                "weight": row["weight"],
                "ap_hi": int(row["ap_hi"]),
                "ap_lo": int(row["ap_lo"]),
                "cholesterol": int(row["cholesterol"]),
                "gluc": int(row["gluc"]),
                "smoke": int(row["smoke"]),
                "alco": int(row["alco"]),
                "active": int(row["active"]),
                "cardio": int(row["cardio"]),
            },
        }
    )

json_object = json.dumps(data_list, indent=4)

# Writing to sample.json
with open("patients/fixtures/patients.json", "w") as outfile:
    outfile.write(json_object)
