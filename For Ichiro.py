user_input = input()

root = user_input.lower()

n1 = ord(root[0:1]) - 96  # 'n' is the number value of first 4 letters of input
n2 = ord(root[1:2]) - 96
n3 = ord(root[2:3]) - 96
n4 = ord(root[3:4]) - 96

c1 = ord(root[-1]) - 96
c2 = ord(root[-2]) - 96

C = round((c1 + c2) / 2)  # Cipher value

r1 = (n1 + 1 + C) % 26  # 'r' is 'n' put through cipher
r2 = (n2 + 2 + C) % 26
r3 = (n3 + 3 + C) % 26
r4 = (n4 + 4 + C) % 26

if r1 == r2:                # Duplicate Test START
    r1 = (r1 + 1) % 26
    if r1 == r3:
        r1 = (r1 + 1) % 26
    elif r1 == r4:
        r1 = (r1 + 1) % 26

if r1 == r3:
    r1 = (r1 + 1) % 26
    if r1 == r2:
        r1 = (r1 + 1) % 26
    elif r1 == r4:
        r1 = (r1 + 1) % 26

if r1 == r4:
    r1 = (r1 + 1) % 26
    if r1 == r2:
        r1 = (r1 + 1) % 26
    elif r1 == r3:
        r1 = (r1 + 1) % 26

if r2 == r3:
    r2 = (r2 + 1) % 26
    if r2 == r1:
        r2 = (r2 + 1) % 26
    elif r2 == r4:
        r2 = (r2 + 1) % 26

if r2 == r4:
    r2 = (r2 + 1) % 26
    if r2 == r1:
        r2 = (r2 + 1) % 26
    elif r2 == r3:
        r2 = (r2 + 1) % 26

if r3 == r4:
    r3 = (r3 + 1) % 26
    if r3 == r1:
        r3 = (r3 + 1) % 26
    elif r3 == r2:
        r3 = (r3 + 1) % 26  # Duplicate Test END

pas = {} # Fill in words corresponding to numbers from 0 - 25
         # Remember index 0 corresponds to Z.

f1 = pas[r1]
f2 = pas[r2]
f3 = pas[r3]
f4 = pas[r4]

print("Input: " + root)
print("Cipher: " + str(C))
print("First: " + f1 + " " + str(r1))
print("Second: " + f2 + " " + str(r2))
print("Third: " + f3 + " " + str(r3))
print("Fourth: " + f4 + " " + str(r4))
print("Pass: " + f1 + f2 + f3 + f4)
print("Pass+: " + f1.capitalize() + f2 + f3 + f4 + str(n1))
