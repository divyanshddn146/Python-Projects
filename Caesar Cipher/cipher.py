from art import logo
print(logo)

while(True):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26


    def caesar(text,shift,direction):
        cipher=""
        if(direction=="decode"):
            shift *=-1
        for letter in text:
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position=position+shift
                new_letter=alphabet[new_position]
                cipher=cipher+new_letter
            else:
                cipher=cipher+letter
        print(f"Here's the {direction}d text {cipher}")
        
    
    caesar(text,shift,direction)
    x=input("Type 'yes' if you want to go again.Otherwise type 'no':")
    if(x=="yes"):
        continue
    else:
        print("Goodbye")
        break

