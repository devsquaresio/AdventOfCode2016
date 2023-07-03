import hashlib, string

passcode, counter, txt = '', 0, '[Your input goes here...]'
passcode2, passcode2real = ['_' for i in range(0, 8)], ''

while (len(passcode) < 8) or ('_' in passcode2):
    testval = hashlib.md5(txt.encode(encoding='utf-8') + str(counter).encode(encoding='utf-8'))
    if testval.hexdigest().startswith('00000'):
        if len(passcode) < 8:
            passcode += (testval.hexdigest()[5])
        if testval.hexdigest()[5] in string.digits and int(testval.hexdigest()[5]) <= 7 and passcode2[int(testval.hexdigest()[5])] == '_':
            passcode2[int(testval.hexdigest()[5])] = testval.hexdigest()[6]      
    counter += 1

for i in passcode2:
    passcode2real += str(i)

print("The first part of the solution to the problem is {}".format(passcode))
print("The second part of the solution to the problem is {}".format(passcode2real))

