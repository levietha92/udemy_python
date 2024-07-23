#solved all the parted setions in this sript

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode(text,shift):
    shifted = "" # [] # this could be string, simpler
    for letter in text:
        index_original = alphabet.index(letter)
        index_shifted = index_original + shift # will run into index error if letter at the end of alphabet
        shifted += alphabet[index_shifted]
    print("The encode message is " + shifted)
        


def decode(text,shift):
    shifted = ""
    for letter in text:
        index_original = alphabet.index(letter)
        index_shifted = index_original - shift
        shifted += alphabet[index_shifted]
    print("The decoded message is " + shifted)

def caesar(text, shift, direction):
    if direction == 'encode':
        encode(text, shift)
    else:
        decode(text, shift)

caesar(text, shift, direction)