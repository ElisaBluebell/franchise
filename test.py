error = 0

f = open("jeju_school_list.csv", "r", encoding="utf-8")

while True:
    line = f.readline()

    if not line:
        break

    if line.count(",") > 6:
        print(line)
        error += 1

f.close()
print(f"count_error: {error}")
