def read_values(filename):
    list_values = []
    fo = open(filename, 'r')
    line = fo.readline()
    while line != "":
        list_values.append(int(line))
        line = fo.readline()
    fo.close()
    return list_values


def get_sums(listValues):
    newList = []
    i = 0
    index = 0
    sum = 0
    while i < len(listValues):
        if index < 3:
            index += 1
            sum += listValues[i]
        if index == 3:
            newList.append(sum)
            i -= 2
            index = 0
            sum = 0
        i += 1
    return newList


def get_number_of_increased_values(listValues):
    prevValue = listValues[0]
    count = 0
    for value in listValues[1:]:
        if value > prevValue:
            count += 1
        prevValue = value
    return count


listValues = read_values("day01/values.txt")
print(get_number_of_increased_values(get_sums(listValues)))
