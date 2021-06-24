from gui import *
from app import syl

while True:
    event, values = window.read()

    if event is None:
        break

    print(event, values)

    if event == "-GENERATE-":
        selected_number = None
        radio_buttons = {1: window["-RADIO1-"], 2: window["-RADIO2-"], 3: window["-RADIO3-"]}

        # Detect radio button
        for button in radio_buttons:
            button_value = radio_buttons[button].get()
            if button_value is True:
                selected_number = button

        print(selected_number)

window.close()
