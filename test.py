import PySimpleGUI as sg

# Define the layout
layout = [
    [sg.Text('Select multiple items:')],
    [sg.Listbox(values=['Item 1', 'Item 2', 'Item 3'], size=(20, 4), key='-LIST-', select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],
    [sg.Button('OK'), sg.Button('Cancel')]
]

# Create the window
window = sg.Window('Listbox Example', layout)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break
    if event == 'OK':
        selected_items = values['-LIST-']
        print(f'Selected items: {selected_items}')

# Close the window
window.close()