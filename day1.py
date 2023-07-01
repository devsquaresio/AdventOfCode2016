with open("day1.txt", "r") as f:
    directions = [k.strip() for k in f.readline().split(",")]

coords = [0, 0]
last_direction = ''
coord_list = []
second_answer = []
direction_map = {"N": [-1, 1], "S": [1, -1], "W": [-1, 1], "E": [1, -1]}

def parse_directions(directions):
    return [directions[:1], directions[1:]]

for i, d in enumerate(directions):
    step = 0
    take = 0
    di = parse_directions(d)
    distance = 0
    if i % 2 == 0:
        if last_direction == '':
            distance = ((1 if di[0] == 'R' else -1) * int(di[1]))
            if distance < 0:
                step = -1
            else:
                step = 1
            take = coords[0]
            comp_value = coords[0]
            if step == -1:
                while take > (distance + comp_value):
                    if not second_answer:
                        if coords in coord_list:
                            second_answer = coords.copy()
                            print(coords.copy())
                    coord_list.append(coords.copy())
                    coords[0] += step
                    take -= 1
            else:
                while take < (distance + comp_value):
                    if not second_answer:
                        if coords in coord_list:
                            second_answer = coords.copy()
                            print(coords.copy())
                    coord_list.append(coords.copy())
                    coords[0] += step
                    take += 1
            if di[0] == 'R':
                last_direction = 'E'
            else:
                last_direction = 'W'
        else:
            pair = direction_map[last_direction]
            val = 1 if di[0] == 'R' else 0
            distance = (pair[val] * int(di[1]))
            comp_value = coords[0]
            if distance < 0:
                step = -1
            else:
                step = 1
            take = coords[0]
            if step == -1:
                while take > (distance + comp_value):
                    if not second_answer:
                        if coords in coord_list:
                            second_answer = coords.copy()
                            print(coords.copy())
                    coord_list.append(coords.copy())
                    coords[0] += step
                    take -= 1

            else:
                while take < (distance + comp_value):
                    if not second_answer:
                        if coords in coord_list:
                            second_answer = coords.copy()
                            print(coords.copy())
                    coord_list.append(coords.copy())
                    coords[0] += step
                    take += 1
            if last_direction == 'N':
                if di[0] == 'R':
                    last_direction = 'E'
                else:
                    last_direction = 'W'
            else:
                if di[0] == 'R':
                    last_direction = 'W'
                else:
                    last_direction = 'E'

    else:
        pair = direction_map[last_direction]
        val = 1 if di[0] == 'R' else 0
        distance = (pair[val] * int(di[1]))
        if distance < 0:
            step = -1
        else:
            step = 1
        take = coords[1]
        comp_value = coords[1]
        if step == -1:
            while take > (distance + comp_value):
                if not second_answer:
                        if coords in coord_list:
                            second_answer = coords.copy()
                            print(coords.copy())
                coord_list.append(coords.copy())
                coords[1] += step
                take -= 1
        else:
            while take < (distance + comp_value):
                if not second_answer:
                        if coords in coord_list:
                            second_answer = coords.copy()
                            print(coords.copy())
                coord_list.append(coords.copy())
                coords[1] += step
                take += 1
        if last_direction == 'W':
            if di[0] == 'R':
                last_direction = 'N'
            else:
                last_direction = 'S'
        else:
            if di[0] == 'R':
                last_direction = 'S'
            else:
                last_direction = 'N'

print(f"The answer to the first part is: {sum(abs(k) for k in coords)}")
print(f"The answer to the second part is: {sum(abs(k) for k in second_answer)}")