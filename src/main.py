from gui import *
import random
import os
# TODO allow user to craft their own rules
# -------------------------------- #
#    LETTERS AND SYLLABLE RULES    #
# -------------------------------- #
# alphabet = "abcdefghijklmnopqrstuvwxyz"  # 26 letters
consonants = "bcdfghklmnprstvyz"  # 17 letters,  carefully chosen
vowels = "aeiou"  # 5 letters

# These are specifically chosen rules to have better results
rule0 = "vc"
rule1 = "vcv"
rule2 = "cv"
rule3 = "cvc"
syllable_rules = [rule0, rule1, rule3]  # 5 items (0-4)

# ------------------------ #
#      RANDOM VALUES       #
# ------------------------ #
ran_cons = random.randrange(0, 20)
ran_vow = random.randrange(0, 4)


# ------------------------ #
#    SYLLABLE GENERATOR    #
# ------------------------ #
def generate_random_syllable():
    syllable = []
    random_syll_rule = random.choice(syllable_rules)
    syll_range = range(len(random_syll_rule))
    # print("random rule is ", random_syllable_rule)
    for letter in syll_range:
        if random_syll_rule[letter] == "v":
            syllable.append(random.choice(vowels))
        else:
            syllable.append(random.choice(consonants))

    return syllable


# ------------------------------------  #
#      ASK THE AMOUNT OF SYLLABLES      #
# ------------------------------------  #
user_input = -1  # this is just a placeholder for the loop to run at least once
while user_input <= 0:
    user_input = int(input("How many syllables do you want? : "))


# ------------------------ #
#      WORD GENERATOR      #
# ------------------------ #
def generate_word():
    word_list = []
    for n in range(0, user_input):
        syllable = generate_random_syllable()
        word_list.append("".join(syllable))
    word = "".join(word_list)
    capitalized_word = word.capitalize()
    return capitalized_word


# ------------------------ #
#      OUTPUT RESULTS      #
# ------------------------ #
while user_input != 0:
    for i in range(0, 3):
        output = generate_word()
        print(output)

    # Go to the next iteration
    input("---Next---")
    os.system("cls")
else:
    print("ENDED")
