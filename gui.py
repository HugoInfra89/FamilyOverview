import PySimpleGUI as psg

def generate_gui(guiname="DefaultName", max_family_size=0):

    #Generate all the labels for the window
    label1 = psg.Text("This is example text:")
    label2 = psg.Text(max_family_size)
    label3 = psg.Text("Maximum family size:")
    input_box = psg.InputText("Please enter the data size of the family")
    select_button = psg.Button("Select Family")

    # Make the layout of the window
    layout_gui = [[label1, label2],
                  [label3, input_box],
                  [select_button]
                  ]

    #Make the window
    window = psg.Window(title=f"Overview of families of {guiname}", layout=layout_gui)
    window.read()
    window.close()




generate_gui()