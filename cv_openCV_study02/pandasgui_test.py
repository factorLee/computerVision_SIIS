import pandas as pd
from pandasgui import show
# from pandasgui.datasets import pokemon, titanic, all_datasets

df_dataset = pd.read_csv("train.csv")
show(df_dataset)