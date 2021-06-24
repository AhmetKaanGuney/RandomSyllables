import PySimpleGUI as sg

question_row = [sg.Text("How many syllables do you want in your word? : ", font="SeguiUI"),
                sg.Radio(text="1", group_id="-RADIO-", default=True, key="-RADIO1-"),
                sg.Radio(text="2", group_id="-RADIO-", key="-RADIO2-"),
                sg.Radio(text="3", group_id="-RADIO-", key="-RADIO3-")]

generate_button = [sg.Button("GENERATE", font="SeguiUI", key="-GENERATE-")]

layout = [question_row, generate_button]

window = sg.Window("Random Syllables", layout)

while True:
    event, values = window.read()
    print(event, values)

    if event is None:
        break

    if event == "-GENERATE-":
        selected_number = None
        buttons_dict = {1: window["-RADIO1-"], 2: window["-RADIO2-"], 3: window["-RADIO3-"]}

        # Detect radio button
        for key in buttons_dict:
            if buttons_dict[key].get() is True:
                selected_number = key

        print(selected_number)

window.close()
