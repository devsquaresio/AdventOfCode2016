import string

with open("day4.txt", "r") as f:
    rooms = [k.strip('\n') for k in f.readlines()]

id_sum, north_pole_object_location = 0, 0
alphabet_key = {}

for i, v in enumerate(string.ascii_lowercase): alphabet_key[i] = v

def decode(letter, num):
    return alphabet_key[(((string.ascii_letters).index(letter)) + (num % 26)) % 26]

for sequence in rooms:
    letter_counter, counter = {}, 0
    letter = sequence[counter]
    while letter not in string.digits:
        if letter != '-':
            if letter in letter_counter: letter_counter[letter] += 1
            else: letter_counter[letter] = 1
        counter += 1
        letter = sequence[counter]
    id, topfive = int(sequence[-10:-7]), sequence[-6:-1]
    vals = sorted(letter_counter.values(), reverse=True)[:5]
    t_count = 0
    for i in topfive:
        if i in letter_counter.keys():
            if letter_counter[i] in vals:
                t_count += 1
                vals.remove(letter_counter[i])
    
    if t_count == 5:
        id_sum += id
        base_string = ''
        for i in sequence[:-11]:
            if i == '-': base_string += ' '
            else: base_string += decode(i, id)

        if base_string == 'northpole object storage': north_pole_object_location = id

print(f"The first part of the solution to the problem is {id_sum}")
print(f"The second part of the solution to the problem is {north_pole_object_location}")
            
