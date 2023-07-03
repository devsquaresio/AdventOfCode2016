with open("day6.txt", "r") as f:
    txt = [k.strip() for k in f.readlines()]

columns = []
for i in range(0, 8):
    columns.append([])
for i in range(0,len(txt)):
    for j in range(0, 8):
        columns[j].append(txt[i][j])

counting_dict = {}
most_common_letters = []
least_common_letters = []

for i in columns:
    answer_found1, answer_found2 = False, False
    counting_dict = {}
    for j in i:
        if j in counting_dict.keys(): counting_dict[j] += 1
        else: counting_dict[j] = 1
    vals = sorted(counting_dict.values(), reverse=True)
    vals2 = sorted(counting_dict.values())
    for j in sorted(i):
        if counting_dict[j] == vals[0] and not answer_found1:
            most_common_letters.append(j)
            answer_found1 = True
        if counting_dict[j] == vals2[0] and not answer_found2:
            least_common_letters.append(j)
            answer_found2 = True

part1answer, part2answer = '', ''
for i in most_common_letters:
    part1answer += i
for i in least_common_letters:
    part2answer += i

print(f"The first part of the solution to the problem is {part1answer}")
print(f"The second part of the solution to the problem is {part2answer}")
    
