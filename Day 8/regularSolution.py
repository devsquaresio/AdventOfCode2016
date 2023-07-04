with open("day8.txt", "r") as f:
    actions = [k.strip() for k in f.readlines()]

screen, dimensions, pixel_count = [], [50, 6], 0

def print_screen(screen):
    for i in screen:
        for v, j in enumerate(i):# Some stuff for better visibility
            if [screen[i][v] for i in range(0, len(screen))] == ['.' for i in range(6)]: print(' ' * 5, end='')
            elif j == '.': print(' ', end='')
            else: print(j, end='')
        print('', end='\n')

for j in range(dimensions[1]):
    temp = []
    for i in range(dimensions[0]):
        temp.append('.')
    screen.append(temp)

for action in actions:
    if action.startswith("rect"):
        width, height = map(int, action.split(" ")[1].split('x'))
        for j in range(height):
            for i in range(width):
                screen[j][i] = '#'

    else:
        direction, line, amount = action.split(" ")[1], int(action.split(" ")[2].split('=')[1]), int(action.split(" ")[4])
        if direction == 'row':
            temp = screen[line].copy()
            for i in range(len(temp)):
                screen[line][(i + amount) % dimensions[0]] = temp[i]
        else:
            temp = [screen[i][line] for i in range(0, len(screen))].copy()
            for i in range(len(temp)):
                screen[(i + amount) % dimensions[1]][line] = temp[i]

for j in screen:
    for i in j:
        if '#' in i: pixel_count += 1

print(f'The first part of the solution to the problem is {pixel_count}')
print("Unfortunately, I can't read the second code. However, I can give it to you! Here it is: ", end='\n\n')
print_screen(screen)



