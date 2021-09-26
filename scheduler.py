from csv import reader
from sys import argv
from copy import deepcopy

# describe how many header rows/columns in the CSV
header = (1, 1)
content = []

availability, time_prefs = {}, {}
input_filename = argv[1]
with open(input_filename, newline='') as file:
    buffer = reader(file, delimiter=',')
    for (i, row) in enumerate(buffer):
        content.append(row)
        if i == 0:
            continue

        for (j, val) in enumerate(row):
            if j == 0:
                continue

            for p in val.split("|"):
                p = p.strip()
                if p == "":
                    continue

                if p not in availability:
                    availability[p] = set()

                availability[p].add((j - 1, i - 1))

# sort by least available first
people_sorting = lambda p: (len(availability[p]), float("inf")
                            if p not in required else -required[p])

# centres-of-gravity
from example import get_preferences, get_required

centre = ((len(content[0]) - header[0]), (len(content) - header[1]) // 2)
time_prefs = get_preferences(centre)
required = get_required(availability)

for time in range(header[1], header[1] + i):
    for day in range(header[0], header[0] + j):
        content[time][day] = ""


def assign(assigned, required):
    if len(required) == 0:
        return assigned

    for p in sorted(list(availability), key=people_sorting):
        if p not in required:
            continue

        assigned_copy, required_copy = deepcopy(assigned), deepcopy(required)
        pref_key = "" if p not in time_prefs else p
        viable = False

        for (day, time) in sorted(availability[p], key=time_prefs[pref_key]):
            if assigned_copy[time + header[1]][day + header[0]] == "":
                assigned_copy[time + header[1]][day + header[0]] = p
                viable = True
                break

        if not viable:
            return None

        if required_copy[p] <= 1:
            del required_copy[p]
        else:
            required_copy[p] -= 1

        result = assign(deepcopy(assigned_copy), deepcopy(required_copy))
        if result is not None:
            return result


result = assign(deepcopy(content), deepcopy(required))

content = []
for row in result:
    output = f"|{'|'.join(row)}|"
    content.append(output)

content.insert(1, "|-" * len(result[1]) + "|")

output_filename = argv[2]
f = open(output_filename, "w")
f.write("\n".join(content) + "\n")
f.close()
