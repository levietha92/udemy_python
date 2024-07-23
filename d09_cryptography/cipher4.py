#IMPROVE UX

import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
# added logo
print(art.logo)


# def encode(text, shift):
#     shifted_concat = ""
#     for index in range(0,len(text)):
#       if text[index] not in alphabet:
#         shifted = text[index] # return identical char
#         # print(shifted)
#       else:
#         index_original = alphabet.index(text[index])
#         # print(index_original)
        
#         if index_original + shift >= 26:
#           index_shifted = index_original + (shift - 26)
#         else:
#           index_shifted = index_original + shift
        
#         shifted = alphabet[index_shifted]
        
#       shifted_concat += shifted
    
#     print("The encoded message is " + shifted_concat)


# def decode(text, shift):
#     shifted_concat = ""
#     for index in range(0,len(text)):
#       if text[index] not in alphabet:
#         shifted = text[index] # return identical char
#         # print(shifted)
#       else:
#         index_original = alphabet.index(text[index])
#         # print(index_original)
  
#         if index_original - shift < 0:
#           index_shifted = index_original - (shift - 26)
#         else:
#           index_shifted = index_original - shift
  
#         shifted = alphabet[index_shifted]
  
#       shifted_concat += shifted
  
#     print("The decoded message is " + shifted_concat)


def caesar(text, shift, direction):
    if direction == 'decode':
      shift *= -1
    
    shifted_concat = ""
      
    for index in range(0,len(text)):
      if text[index] not in alphabet:
        shifted = text[index] # return identical char
      else:
        index_original = alphabet.index(text[index])

        if index_original - shift < 0 or index_original + shift >= 26: #this could be replaced with module check shift = shift % 26
          index_shifted = index_original + (shift - 26)
        else:
          index_shifted = index_original + shift

        shifted = alphabet[index_shifted]

      shifted_concat += shifted

    print(f"The {direction}d message is | {shifted_concat}")


ask = 'yes'
while ask == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    ask = input("Do you want to continue? ")

if ask == 'no':
    print("Goodbye %^&&*(")
