'''
Caesar cipher - Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either use frequency analysis to guess the key, or just try all 25 keys.
'''

class Ceasar:

    alphabet = ['a','b','c','d','e',
                'f','g','h','i','j',
                'k','l','m','n','o',
                'p','q','r','s','t',
                'u','v','w','x','y',
                'z']

    # the cipher must be stored in the individual files of the encodign
    def __init__(self, cipher):
        self.cipher = cipher


    def start(self):
        pass

    # controls user actions
    # 1 =  encode message - > save or unsave
    # 2 =  decode message - > decodes a list of messages
    def prompt(self):
        print("This is the ceasar_cipher challange \n")
        print("Enter ... 1 for encoding .txt file")
        print("Enter ... 2 for decoding .txt file")
        print("Enter ... 3 to quit")
        control = int(input("Insert your command."))
        return control

    #@staticmethod
    def create_cipher_file(self, message):
        file = open(str(self.cipher) + ".log", "w")
        file.write(str(message))
        file.close()
        return self

    # enable encode depeneding on the hard coding
    def encode_message(self, cipher, message):
        # take individual string alphabets and increment the list with cipher number
        encode_message = list(message)
        for foo in range(len(encode_message)):
            # print(encode_message[foo])
            for bar in range(len(Ceasar.alphabet)):
                if Ceasar.alphabet[bar]  == encode_message[foo]:
                    Ceasar.alphabet[bar] = encode_message[foo]
                    baz = bar + cipher
                    # maybe appending the sequence into a static list would be better?
                    if baz > 25:
                        baz = baz - 26
                        print(Ceasar.alphabet[baz])
                        Ceasar.create_cipher_file(self, Ceasar.alphabet[baz])
                    else:
                        print(Ceasar.alphabet[baz])
                        Ceasar.create_cipher_file(self, Ceasar.alphabet[baz])
        return("exit 0")

    # enable decode depending on the hard coding
    def decode_message(self, cipher, message):
        pass

# -------------------------------------------------------------------------------------
# code execution
# -------------------------------------------------------------------------------------

encryption_token = int(input("Please input your encryption token number ... : "))
message = str(input("Please input your message ... : "))
c = Ceasar(encryption_token)
c.encode_message(encryption_token, message)
# c.prompt()
print("return 0")
