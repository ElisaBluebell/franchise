item = 0
file_name = "스타벅스 제주외도DT점"

f = open(f"{file_name}.csv", "r", encoding="euc-kr")
total = {}
for line in f.readlines():
    line = line.split(", ")
    if total.keys() == "":
        if line[1] != "아파트":
            total[line[1]] = 1
        else:
            if line[3] != "None":
                total[line[1]] += int(line[3])

    else:
        if line[1] in total.keys():
            if line[1] != "아파트":
                total[line[1]] += 1
            else:
                if line[3] != "None":
                    total[line[1]] += int(line[3])
        else:
            total[line[1]] = 1
    if "스타벅스" in line[0]:
        item += 1

print(total)
print(item)
