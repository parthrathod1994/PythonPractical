from random import randint
from operator import xor
rand = []
char_Cipher = []
bin_cipher = []
bin_newcipher = []
char_newplaintext = []
bin_newplaintext = []
newkey = []
def generatekey(key,keylength):
    #print("key = ",end="")
    for i in range(0,key):
        rand.append(randint(0,1))
        print(rand[i],end="")

    file2 = open("key.txt", "wt")

    print("\nNew Generated Key = ",end="")
    if keylength < key:
        for i in range(0,keylength*10):
            newkey.append(rand[i])
            #print(newkey[i], end="")
            file2.write(str(newkey[i]))
    else:
        for i in range(0, keylength*10):
            newkey.append(rand[i%key])
            #print(newkey[i], end="")
            file2.write(str(newkey[i]))

    print("Key is Generated and Save Into key.txt file")
    file2.close()


def encrypt(keydata):

    file3 = open("bin_plaintext.txt", "wt")

    for i in range(0,len(keydata)):
        char_Cipher.append(format(ord(keydata[i]),'010b'))
        file3.write(char_Cipher[i])
    file3.close()

    file4 = open("key.txt","r")
    file3 = open("bin_plaintext.txt", "r")
    bin_key = file4.read()
    bin_plain = file3.read()

    file5 = open("bin_ciphertext.txt","wt")

    bin_cipher = int(bin_key,2) ^ int(bin_plain,2)

    file5.write(bin(bin_cipher))
    file5.close()
    file3.close()
    print("Ciphertext Generated in bin_ciphertext.txt")

def decrypt():
    file4 = open("key.txt", "r")
    file5 = open("bin_ciphertext.txt", "r")

    bin_key = file4.read()
    bin_cipher = file5.read()
    bin_cipher = bin_cipher[2:]

    bin_newcipher = bin_cipher

    if len(bin_cipher) < len(bin_key):
        dif = len(bin_key) - len(bin_cipher)
        for i in range(0,dif):
            bin_newcipher = '0' + bin_newcipher

    char_newplaintext = int(bin_key,2) ^ int(bin_newcipher,2)

    file6 = open("bin_newplaintext.txt", "wt")
    file6.write(bin(char_newplaintext))
    file6.close()
    file5.close()
    file4.close()

    char_newplaintext = bin(char_newplaintext)
    char_newplaintext = char_newplaintext[2:]

    bin_newplaintext = char_newplaintext

    if len(char_newplaintext) < len(bin_key):
        dif = len(bin_key) - len(char_newplaintext)
        for i in range(0,dif):
            bin_newplaintext = '0' + bin_newplaintext

    data_convert = []
    data_newplaintext = []

    file3 = open("newplaintext.txt", "wt")

    k=0
    print("Data=",end="")
    for i in range(0,len(bin_key),10):
        data_convert = bin_newplaintext[i:i+10]
        data_convert = '0b' + data_convert
        data_newplaintext.append(chr(int(data_convert, 2)))
        file3.write(data_newplaintext[k])
        print(data_newplaintext[k],end="")
        k=k+1
    file3.close()


flag=1
while flag==1:
    file1 = open("plaintext.txt", "r")
    plaintext = file1.read()
    file1.close()
    print("Data=" , plaintext)
    keylen = len(plaintext)
    print("Keylen=",keylen)
    print("1. Generate Key")
    print("2. encryption")
    print("3. decryption")
    print("Select Option:",end="")
    option = int(input())
    if option == 1:
        #if len(rand) == 0:
        print("Enter Key=",end="")
        key = int(input())
        generatekey(key,keylen)
        #else:
         #   print("Key Is Already Generated")
    elif option == 2:
        #if len(rand) != 0:
            encrypt(plaintext)
        #else:
         #   print("Generate Key First")
    elif option == 3:
        #if len(rand) != 0 and len(char_Cipher):
            decrypt()
        #else:
         #   print("Generate Key First")
    else:
        print("Invalid Input")
    print("\nContinue enter 1:",end="")
    flag=int(input())
