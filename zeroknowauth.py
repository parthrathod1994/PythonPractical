import random
import hashlib

#Client Side Registration Code
plain_pass = str(input("Register Password:"))

hash_pass = hashlib.md5(plain_pass.encode()) #MD5 hash generate
int_pass = int(hash_pass.hexdigest(),16)      #Convert Hex to Int
finalvalue = pow(5,int_pass,97)    #(5^int_pass)mod 97  Stored on Server Side Database
print(finalvalue)

#Authentication Code
usr_pass = str(input("Enter Password:"))

hash_usrpass = hashlib.md5(usr_pass.encode()) #MD5 hash generate
int_usrpass = int(hash_usrpass.hexdigest(),16)      #Convert Hex to Int

finalvalue_usr = pow(5,int_usrpass,97)    #(5^int_pass)mod 97  Stored on Server Side Database
print(finalvalue_usr)

rx = 92
a = random.randrange(1,1000)
print("rx=",rx)
print("a=",a)

t1 = pow(5,rx,97)
print("t1:",t1)

concatstr = str(finalvalue_usr) + str(t1) + str(a)
print("Concat =",concatstr)

cx = hashlib.md5(concatstr.encode())

int_cx = int(cx.hexdigest(),16)%97

zx = (rx - (int_cx*int_usrpass))%97

if zx < 0:
    zx = zx + 97

print(int_cx,",",zx)

t2 = (pow(finalvalue,int_cx,97) * pow(5,zx,97))%97

concatstr2 = str(finalvalue) + str(t2) + str(a)

cx2 = hashlib.md5(concatstr2.encode())

int_cx2 = int(cx2.hexdigest(),16)%97

print(int_cx2)

