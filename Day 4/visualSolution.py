import turtle
import string

wn = turtle.Screen()
wn.bgcolor("dark grey")
wn.title("Day 4 Solution! Both Parts! (2016)")

main_writer = turtle.Turtle()
main_writer.hideturtle()
main_writer.penup()

sequence_turtle = turtle.Turtle()
sequence_turtle.penup()
sequence_turtle.hideturtle()
sequence_turtle.color('blue')

decode_turtle = turtle.Turtle()
decode_turtle.penup()
decode_turtle.hideturtle()
decode_turtle.color('black')
decode_turtle.goto(0, -60)

storage = turtle.Turtle()
storage.penup()
storage.hideturtle()
storage.color('brown')
storage.goto(-175, 375)

countert = turtle.Turtle()
countert.hideturtle()
countert.penup()
countert.color("purple")
countert.goto(200, 350)

room = turtle.Turtle()
room.hideturtle()
room.penup()
room.color('red')
room.goto(0, -375)

sequence_turtle.goto(0,50)

main_writer.goto(-200, 100)
main_writer.color('red')
main_writer.write('Main Rooms: ', align='center', font=('Courier', 24, 'normal'))
main_writer.color('dark green')
main_writer.goto(-175, -10)
main_writer.write('Decoded String: ', align='center', font=('Courier', 24, 'normal'))

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
    sequence_turtle.clear()
    sequence_turtle.write(sequence, align='center', font=("Courier", 21, 'normal'))
    room.clear()
    room.write(f'Room #{rooms.index(sequence) + 1}', align='center', font=("Courier", 11, 'normal'))
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

        decode_turtle.clear()
        decode_turtle.write(base_string, align='center', font=("Courier", 21, 'normal'))

        if base_string == 'northpole object storage': 
            north_pole_object_location = id

    storage.goto(-200,350)
    storage.clear()
    storage.write(f'''North Storage ID: {north_pole_object_location}''', align='center', font=("Courier", 18, 'normal'))
    countert.goto(200, 350)
    countert.clear()
    countert.write(f'''Valid ID Sum: {id_sum}''', align='center', font=("Courier", 18, 'normal'))

wn.exitonclick()
