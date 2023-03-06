import os
import xlwings as xw

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

def readtxt_select_to_df(txt_file):
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

    max_bytes = set_max_bytes()
    print(f"Select only the the files which are larger than: {max_bytes} bytes")
    df_rfa_selected_files = df_rfa_files_datasize[df_rfa_files_datasize["filesize"]>max_bytes]
    return df_rfa_selected_files







