from pathlib import Path
import pandas as pd

def create_dataframe(csv_file):
    """ Creates, prints and returns a pandas dataframe containing data from a csv file

    Args:
        csv_file: The raw data in csv format

    Returns:
        df: A pandas dataframe with the data """
    
    df = pd.read_csv('CW1Trial/EMPLOYMENT.csv')

    print(df)
    return




