txt = '[Enter input here...]'

codes = [k for k in txt]

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def unpack(self):
        return [self.x, self.y]

    def __add__(self, vec2):
        return Vector2D(vec2.x + self.x, vec2.y + self.y)

cardinals = {"D": Vector2D(0, 1), "U": Vector2D(0, -1), "L": Vector2D(-1, 0), "R": Vector2D(1, 0)}

base_coords = Vector2D(1, 1)

passcode = ''
passcode2 = ''

num_grid = [[1,2,3],
            [4,5,6],
            [7,8,9]]

num_grid2 = [["","",1,"",""],
            ["", 2, 3, 4, ""],
            [5, 6, 7, 8, 9],
            ["", "A", "B", "C", ""],
            ["","","D","",""]]

for i in codes:
    if i != '\n':
        if (base_coords + cardinals[i]).x <= (len(num_grid[0]) - 1) and (base_coords + cardinals[i]).x >= 0 and (base_coords + cardinals[i]).y >= 0 and  (base_coords + cardinals[i]).y <= (len(num_grid[0]) - 1):
            base_coords = base_coords + cardinals[i]

    else:
        vals = base_coords.unpack()
        passcode += str(num_grid[vals[1]][vals[0]])

for i in codes:
    if i != '\n':
        if (((base_coords + cardinals[i]).x >= 0 and (base_coords + cardinals[i]).x <= (len(num_grid2[0]) - 1) and (base_coords + cardinals[i]).y >= 0 and (base_coords + cardinals[i]).y <= (len(num_grid2[0]) - 1)) and num_grid2[(base_coords + cardinals[i]).y][(base_coords + cardinals[i]).x] != ''):
            base_coords = base_coords + cardinals[i]
    else:
        vals = base_coords.unpack()
        passcode2 += str(num_grid2[vals[1]][vals[0]])

print(f"The first part of the solution to the problem is {passcode}")
print(f"The second part of the solution to the problem is {passcode2}")
