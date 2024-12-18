
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):

    output_text = ""
    not_in_alphabet =""
    new_original_text =""
    for letter in original_text:
        if letter not in alphabet:
            not_in_alphabet += letter
            original_text.replace(letter,'')
        else:
            new_original_text += letter

    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in new_original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}{not_in_alphabet}")





play_again = False
while not play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    yes_no = input("would you like to play again? yes/no?\n")
    if yes_no == "no":
        print("thank you for playing")
        play_again = True




