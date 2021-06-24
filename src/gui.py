import PySimpleGUI as sg

white = "#f2f0e5"
sweet_green = "#567b79"
sweet_brown = "#80493a"
text_bg_color = "#4e584a"
sg.theme_background_color(sweet_green)
sg.theme_element_background_color(sweet_green)
sg.theme_text_element_background_color(sweet_green)
sg.theme_text_color(white)
sg.theme_button_color(sweet_brown)

question_row = [sg.Text("How many syllables do you want in your word? : ", font=("SegoeUI", 15)),
                sg.Radio(text="1", group_id="-RADIO-", default=True, key="-RADIO1-", font=("SegoeUI", 14)),
                sg.Radio(text="2", group_id="-RADIO-", key="-RADIO2-", font=("SegoeUI", 14)),
                sg.Radio(text="3", group_id="-RADIO-", key="-RADIO3-", font=("SegoeUI", 14))]

generate_button = [sg.Button("GENERATE", font=("SegoeUI", 18), key="-GENERATE-", )]

result_text = [sg.Text(text="", key="-RESULT-", font=("SegoeUI", 18), size=(30, 5), justification="center",
                       background_color=text_bg_color)]

# LAYOUT
layout = [[sg.Column([question_row, generate_button, result_text],
                     element_justification="center", justification="center")]]

window = sg.Window("Random Syllables", layout, size=(650, 200))


