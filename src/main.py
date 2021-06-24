from gui import *
from generators import run_generators


def main():
    while True:
        event, values = window.read()

        if event is None:
            break

        # -------------------------------------------------- #
        #      When GENERATE button is pressed generate      #
        #      a word for 'x' amount of syllables            #
        #      'x' = whichever radio button is selected      #
        # -------------------------------------------------- #
        if event == "-GENERATE-":
            selected_number = None
            radio_buttons = {1: window["-RADIO1-"], 2: window["-RADIO2-"], 3: window["-RADIO3-"]}

            # Detect radio button
            for button in radio_buttons:
                button_value = radio_buttons[button].get()
                if button_value is True:
                    selected_number = button

            # Return Output from generator
            output = run_generators(selected_number)
            window["-RESULT-"].update(output)
            window.refresh()

    window.close()


# ---------------------- #
#      ENTRY POINT       #
# ---------------------- #
if __name__ == "__main__":
    main()
