import os
import xlwings as xw
import csv
import pandas as pd
import os as os

pd.options.display.max_columns = 5
pd.options.display.max_rows = 20
pd.options.display.width = 200



def set_max_bytes():
    max_bytes = int(input("What is the max amount of allowable bytes: "))
    return max_bytes

def rfa_selection(filepath, extension=".rfa"):
    all_files_list = os.listdir(path=filepath)
    rfa_list = []
    for file_name in all_files_list:
        if extension in file_name:
            rfa_list.append(file_name)
    return rfa_list

def makelist_in_txt(txt_file, list):
    with open(file=txt_file, mode="w") as file:
        new_rfa_txtdoc_list = ["%s\n" % file_name for file_name in list]
        file.writelines(new_rfa_txtdoc_list)

def readtxt_select_to_df(txt_file, max_bytes):
    with open(txt_file, mode="r") as file:
        readed_list = file.readlines()

        dict = {}
        for i, file in enumerate(readed_list):
            file = file.strip()
            file_path = f"families\{file}"
            file_size = os.stat(file_path).st_size
            dict[i] = [file, file_path , file_size]

    import pandas as pd
    df_rfa_files_datasize = pd.DataFrame(dict).T
    df_rfa_files_datasize.rename(columns={0:"filename",1:"filepath",2:"filesize"}, inplace=True)

    print(f"Select only the the files which are larger than: {max_bytes} bytes")
    df_rfa_selected_files = df_rfa_files_datasize[df_rfa_files_datasize["filesize"]>max_bytes]
    return df_rfa_selected_files

def get_families_from_csv():
    df_csv_data = pd.read_csv("families.csv")
    df_csv_data["filename"] = df_csv_data["filename"].apply(str)
    df_csv_data["filesize"] = df_csv_data["filesize"].apply(str)
    df_csv_data["filename and filesize"] = df_csv_data["filename"] + ", " "bytes=" + df_csv_data["filesize"]

    xw.view( df_csv_data)
    df_csv_data.to_csv("families.csv")
    return df_csv_data["filename and filesize"]

def check_file_paths():
    df_csv_data = pd.read_csv("families.csv")
    print(df_csv_data)
    for i, row in df_csv_data.iterrows():
        filepath=row["filepath"]
        # filepath = filepath.replace(" ","_")

        import os
        absolute_path = os.path.abspath(filepath)
        print(absolute_path)

        normalized_path = os.path.normpath(filepath)
        print(normalized_path)

        if os.path.isfile(normalized_path):
            print("File exists.")
            os.system(normalized_path)
        else:
            print("File does not exist.")


def open_selected_families(dict_of_selected_families):
    print(dict_of_selected_families)

    breakpoint()

    selected_family = dict_of_selected_families['family_selection'][0]

    df_csv_data = pd.read_csv("families.csv")
    boolmask = df_csv_data['filename and filesize']==selected_family

    selected_filepath = df_csv_data["filepath"][boolmask].values[0]
    absolute_path = os.path.abspath(selected_filepath)
    print(absolute_path)

    normalized_path = os.path.normpath(selected_filepath)
    print(normalized_path)

    if os.path.isfile(normalized_path):
        print("File exists.")
        os.system(normalized_path)
    else:
        print("File does not exist.")

