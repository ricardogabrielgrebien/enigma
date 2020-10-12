import sys
import json

string = "asdf"


def setAlphabetWired():
    with open('alphabetWired.json') as json_file:
        data = json.load(json_file)
        alphabetWired = data['letters']
        return alphabetWired



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetWired = setAlphabetWired()


circle1 = 1
circle2 = 2
circle3 = 3

def rotate(circle, rotations):
    for rotation in range(rotations):
        temp = alphabetWired[0]
        for i in range(25):
            alphabetWired[i] = alphabetWired[i+circle]
        alphabetWired[25] = temp

def getLetterEncrypt(letter):
    letterpos = alphabet.index(letter)
    return alphabetWired[letterpos]

def getLetterDecrypt2(letter):
    letterposInWired = alphabetWired.index(letter)
    return alphabet[letterposInWired]
    

# encode
def encode(string):
    #reset alphabetWired
    alphabetWired = setAlphabetWired()

    stringEncoded = ""
    print("Encode string: ", string)
    for letter in string:
        stringEncoded += getLetterEncrypt(letter)
        rotate(circle1, 1)
        #print(letter, end='') 
    print("string ecoded: ", stringEncoded)
        

# decode
def decode(stringEncoded):
    decodedString = ""
    #reset alphabetWired
    alphabetWired = setAlphabetWired()

    print("string to encode: ", stringEncoded)
    for letter in stringEncoded:
        decodedString += getLetterDecrypt2(letter)
        rotate(circle1, 1)
    print("decoded string: ", decodedString)
    

def printAlphabet():
    for letter in alphabetWired:
        print('\"'+letter+'\"', end=',')


if sys.argv[1] == "encode":
    encode(sys.argv[2])
elif sys.argv[1] == "decode":
    decode(sys.argv[2])
else:
    print("command not found: ", sys.argv[1])