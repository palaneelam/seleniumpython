

# hello - > mjqqt
# shift = 5
# *******************************************************

# TODO: create a function called 'encrypt' that takes the 'text' and 'shift' as inputs
# TODO: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet
# by the shift amount and print the encrypted text.
# For eg.: plain_text = "hello"
#          shift = 5
#          cipher_text = "mjqqt"
#          print output = "The encoded text is mjqqt"
# TODO: Call the encrypt function and pass in the user inputs. You should be able to test the code
# and encrypt a message

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
            'w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z']
print('''
         _...._
       .`      `.
      / ***      **         The Crystal Ball
     : **         :         says.........
     :            :        You don't really
      *          **       believe in fortunes,
       `-.,,,,.-'              do you?
        _(    )_
       )        (
      (          )
       `-......-`lc
''')
direction = input("Type 'encrypt' to Encrypt, or type 'decrypt' to Decrypt: ")
inp_text = input("Type your word:").lower()
inp_shift = int(input("Enter the shift value:"))

def encrypt(text,shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]  #m
        cipher_text += new_letter    #cipher_text = mjqqt
    print(f"The encoded text is {cipher_text}")

# encrypt(inp_text,inp_shift)

# TODO create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs
# TODO Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet
# by the shift amount and print the decrypted text
# e.g - cipher_text = "mjqqt"
#       shift = 5
#       plain_text = "hello"
#       print output: "The decoded text is hello"
# TODO - Check if the user wanted to encrypt or decrypt the message by checking the 'direction'
# variable. Then call te correct function based on that 'direction' variable. You should be able to
# test the code to encrypt *AND* decrypt a message

def decrypt(text, shift):
    pass



if direction == "encrypt":
    encrypt(inp_text,inp_shift)
elif direction == "decrypt":
    decrypt(inp_text,inp_shift)
else:
    print("Incorrect choice!")










