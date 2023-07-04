with open("day7.txt", "r") as f:
    addresses = [k.strip() for k in f.readlines()]

valid_addresses_tls, valid_addresses_ssl = 0, 0

for address in addresses:
    has_validity_tls = 'False'
    in_brackets = ''
    for index, letter in enumerate(address):
        if letter == '[': in_brackets = 'True'
        elif letter == ']': in_brackets = 'False'
        else:
            try:
                if '{}{}{}{}'.format(letter, address[index+1], address[index+2], address[index+3]) == (letter + address[index+1] + address[index+1] + letter) and letter != address[index + 1]:
                    if in_brackets == 'True':
                        has_validity_tls = 'False'
                        break
                    else: has_validity_tls = 'True'

            except IndexError: pass
            
    if has_validity_tls == 'True':
        valid_addresses_tls += 1

for address in addresses:
    has_validity_ssl, in_brackets = False, False
    hypernet = list(filter(lambda x: address.replace("[", "]").split("]").index(x) % 2 == 1, address.replace("[", "]").split("]")))
    for v, i in enumerate(address):
        if i == '[': in_brackets = True
        elif i == ']': in_brackets = False
        else:
            try:
                if (i + address[v+1] + address[v+2]) == (i + address[v+1] + i) and i != address[v+1] and not in_brackets:
                    for j in hypernet: 
                        if (address[v+1] + i + address[v+1]) in j: has_validity_ssl = True

            except IndexError: pass
     
    if has_validity_ssl == True:
        valid_addresses_ssl += 1

print(f'The first part of the solution to the problem is {valid_addresses_tls}')
print(f'The second part of the solution to the problem is {valid_addresses_ssl}')
