from functions import rfa_selection, makelist_in_txt, readtxt_select_to_df
import os as os
import pandas as pd
import xlwings as xw

pd.options.display.max_columns = 3
pd.options.display.max_rows = 20
pd.options.display.width = 100

cwd = os.getcwd()                                               #Get the current working directory
txt_file = "txt_file.txt"

filepath = f"{cwd}\\families"

rfa_list = rfa_selection(filepath=filepath, extension=".rfa")   #Makes a list of all files in the directory with a .rfa extension
makelist_in_txt(txt_file="txt_file.txt", list=rfa_list)         #Generate a text file within all the names of the families
df = readtxt_select_to_df(txt_file="txt_file.txt")              #Makes a dataframe with only the families which are larger than ... bytes
df.to_csv("families.csv", index=False, sep=",")                 #Write the data to a csv file

xw.view(df)

