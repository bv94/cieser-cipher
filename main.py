from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# init
user_exit = False
user_choice = ""
user_input = ""
shift_num = 0


def recode(text, shift, direction):
    shift %= len(alphabet)+1
    if(direction == "1" or direction == "decode" or direction == "decrypt"):
        shift *= -1

    recoded_text = ""
    for word in text:
        recoded_text += alphabet[alphabet.index(word)+shift]
        # print(recoded_text)
    return recoded_text


print(logo)
while(user_input != "q"):

    user_choice = input(
        "whould you like to encode a message or decode a message?\n>")
    user_input = input("what is the message \n>")
    shift_num = int(input("what should be the shift num\n>"))
    print(recode(user_input, shift_num, user_choice))

    user_input = input("\n\n would you like to go again?, q for quit\n>")
