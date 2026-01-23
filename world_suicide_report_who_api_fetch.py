import requests
import pandas as pd
import pprint
from pathlib import Path

def get_data():
    data_url = "https://ghoapi.azureedge.net/api/MH_12?$orderby=NumericValue desc&$select=SpatialDim,TimeDim,NumericValue&$top=1000"

    data_res = requests.get(data_url)
    if data_res.status_code == 200:
        data = data_res.json()
        record = data["value"]
        print(f"{len(record)} entries aquired.")

        df = pd.DataFrame(record)
        df["NumericValue"] = pd.to_numeric(df["NumericValue"], errors='coerce')

        df = df.sort_values(by=["TimeDim"], ascending=False)

        df = df.rename(columns={
            "SpatialDim": "Country",
            "TimeDim": "Year",
            "NumericValue": "SuicideRate"
        })
        df["SuicideRate"] = pd.to_numeric(df["SuicideRate"], errors='coerce').round(2)
        df["SuicideRate"] = df["SuicideRate"].apply(lambda x: f"{x:.2f}" if pd.notnull(x) else "")
        return df
    else:
        raise Exception(f"Failed to fetch from {data_res}, status:{data_res.raise_for_status()}")


def get_credentials():
    country_url = "https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues"

    country_res = requests.get(country_url)
    if country_res.status_code == 200:
        country = country_res.json()
        country = country["value"]

        cf = pd.DataFrame(country)
        return cf
    else:
        raise Exception(f"Failed to fetch from {country_res}, status:{country_res.raise_for_status()}")


def merge(df, cf):
    df_merged = df.merge(
        cf,
        left_on="Country",
        right_on="Code",
        how="left"
    )

    df_merged = df_merged.drop(columns=["Dimension", "Country", "Code", "ParentDimension", "ParentCode"])

    df_final = df_merged.rename(columns={
        "Title": "Country",
        "ParentTitle": "Region"
    })
    return df_final

def sort(df_final):
    df_final = df_final.sort_values(by=["Year", "Country"], ascending=[False, True,])
    print(df_final.head(20))
    return df_final


def export(df_final):
    path = Path(r"C:\Users\IVY\Documents\World_suicide_report.csv")

    df_final.to_csv(path, index=False, float_format='%.2f')


d = get_data()
c = get_credentials()
m = merge(d, c)
s = sort(m)
e = export(s)