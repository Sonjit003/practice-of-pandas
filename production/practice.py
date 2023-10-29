import pandas as pd
from pathlib import Path
import os




input_path = Path("data").joinpath("input")
output_path = Path("data").joinpath("output")

def reading_input_data(filename:str)-> pd.DataFrame:
    file_path = input_path.joinpath(filename)
    df = pd.read_csv(file_path)
    return df 

# df = reading_input_data("inputdata.csv")
def delete_tours_from_collumnB(df: pd.DataFrame):
    df = df[df["Tour ID"].isnull()]
    return df



def lentg_of_Lane(text:str)->bool:
    p = len(text.split("->"))
    if p == 2:
        return True
    return p
    

def delete_milk_run(df:pd.DataFrame):
   
    df["Lane_count"] = df["Lane"].apply(lambda x: lentg_of_Lane(x))
    return df
 


def drop_Lane_count_column(df:pd.DataFrame)-> pd.DataFrame:
    df = df[df["Lane_count"] == True]
    df.drop(["Lane_count"], axis= "columns", inplace=True)
    return df

columnss = [ "Scheduled Truck Arrival - 1 date", "Scheduled Truck Arrival - 2 date"]


def change_date_formate(df: pd.DataFrame, columns: list, date_formate)->pd.DataFrame:
    
    for column in columns:
        df[column] = pd.to_datetime(df[column], format= "mixed").dt.strftime(date_formate)
    df["Corresponding CPT"] = pd.to_datetime(df["Corresponding CPT"], format="mixed").dt.strftime("%m/%d/%y  %H:%M")
    return df



def main():
    df = reading_input_data("inputdata.csv")
    df = delete_tours_from_collumnB(df)
    df = delete_milk_run(df)
    df = drop_Lane_count_column(df)
    df = change_date_formate(df,columnss,"%m/%d/%y")
    df.to_csv("myoutput.csv", index=False)


if __name__ == "__main__":
    main()