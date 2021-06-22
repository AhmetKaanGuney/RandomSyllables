# todo define letters
# todo define syllable , algorithm for v=vowel c=consonant so: "vc", "vcv", "vcc", "cv", "cvc"
# forbidden syllable combos : 'bk' , 'bf' , 'tk' , 'mn' , 'pc' , 'bz'
# todo random syllable generation
# todo random word generation from syllables (max 4 syllables)
# todo max 3 words printed
# todo input for; reshuffle syllables , generate new word
import random
import os
# ### LETTERS AND SYLLABLE RULES ###
vowels = "aeiou"  # 5 letters
consonants = "bcdfghjklmnpqrstvwxyz"  # 20 letters
alphabet = "abcdefghijklmnopqrstuvwxyz"  # 26 letters
rule0 = "vc"
rule1 = "vcv"
rule2 = "vcc"
rule3 = "cv"
rule4 = "cvc"
syllable_rules = [rule0, rule1, rule2, rule3, rule4]  # 5 items (0-4)
# ### LETTER DICTIONARY
dict_syll = {}
# ### RANDOM VALUES
ran_cons = random.randrange(0, 20)
ran_vow = random.randrange(0, 4)


# ### Syllable Generator
def random_syll(syll_rules):
    x = 0
    output = []
    random_syll_rule = random.choice(syll_rules)
    syll_range = range(len(random_syll_rule))
    # print("random rule is ", random_syllable_rule)
    for letter in syll_range:
        if random_syll_rule[letter] == "v":
            output.append(random.choice(vowels))
        else:
            output.append(random.choice(consonants))
        x += 1
    return output


# ### USER INPUT
user_input = int(input("How many syllables do you want? : "))
# ### Word Generator
while user_input != 0:
    for i in range(0, 3):
        word_list = []
        for n in range(0, user_input):
            syll_i = random_syll(syllable_rules)
            word_list.append("".join(syll_i))
        word = "".join(word_list)
        print(word.capitalize())
    input("---Next---")
    os.system("cls")
else:
    print("ENDED")
