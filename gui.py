import PySimpleGUI as psg
from functions import get_families_from_csv
import pandas as pd


def generate_gui(guiname="DefaultName", max_family_size=0):


    #Generate all the labels for the window
    label1 = psg.Text("List of families larger than: ")
    label2 = psg.Text(f"{max_family_size} bytes")
    list_box = psg.Listbox(values=get_families_from_csv(),
                           key="family_selection",
                           enable_events=True,
                           select_mode=psg.LISTBOX_SELECT_MODE_EXTENDED,
                           size=[50,20])
    select_button = psg.Button("select")

    # Make the layout of the window
    layout_gui = [[label1, label2],
                  [list_box],
                  [select_button]]

    #Make the window
    window = psg.Window(title=f"Overview of families of {guiname}",
                        layout=layout_gui,
                        font=("Helvitica", 12))


    while True:
        event, selected_family_dictionary = window.read()
        print(event)
        families_dict = selected_family_dictionary
        print(families_dict)
        match event:
            case "select":
                return selected_family_dictionary
                break

    window.close()