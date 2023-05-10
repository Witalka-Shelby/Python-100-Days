from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceaser(text, shift, cipher_direction):
        result = []
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)

                if cipher_direction == "encode":
                    new_index = position + (shift % 26)

                if cipher_direction == "decode":
                    new_index = position - (shift % 26)

                result.append(alphabet[new_index])
            else:
                result.append(letter)
        
        print(f"Here's the {cipher_direction}d result: {''.join(result)}")
        
    ceaser(text=text, shift=shift, cipher_direction=direction)
    do_again = input("Type 'yes' if you want to go again.Otherwise type 'no'.").lower()
    if do_again == "no":
        break