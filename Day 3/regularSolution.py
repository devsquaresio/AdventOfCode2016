with open("day3.txt", "r") as f:
    regular_nums = [k.strip() for k in f.readlines()]

possible_triangles = 0
possible_triangles2 = 0

for i in (regular_nums):
    vertices1 = sorted([int(k.strip()) for k in i.split(" ") if k != ''])
    if (int(vertices1[0]) + int(vertices1[1])) > int(vertices1[2]): possible_triangles += 1

for i, v in enumerate(regular_nums):
    if v != '':
        vertices1 = [int(k.strip()) for k in regular_nums[i].split(" ") if k != '']
        vertices2 = [int(k.strip()) for k in regular_nums[i + 1].split(" ") if k != '']
        vertices3 = [int(k.strip()) for k in regular_nums[i + 2].split(" ") if k != '']
        group1 = sorted([int(vertices1[0]), int(vertices2[0]), int(vertices3[0])])
        group2 = sorted([int(vertices1[1]), int(vertices2[1]), int(vertices3[1])])
        group3 = sorted([int(vertices1[2]), int(vertices2[2]), int(vertices3[2])])
        if (int(group1[0]) + int(group1[1])) > int(group1[2]): possible_triangles2 += 1
        if (int(group2[0]) + int(group2[1])) > int(group2[2]): possible_triangles2 += 1
        if (int(group3[0]) + int(group3[1])) > int(group3[2]): possible_triangles2 += 1
        regular_nums[i + 1] = ""
        regular_nums[i + 2] = ""

print(f"The first part of the solution to the problem is {possible_triangles}")
print(f"The second part of the solution to the problem is {possible_triangles2}")
