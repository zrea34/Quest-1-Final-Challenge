import csv


# class used to create instances of pairs
class Department:
    id: str
    expenses: int

    def __init__(self, dep, expenses):
        self.dep = dep               # key
        self.expenses = expenses   # value


# opening file, deleting header and then storing only necessary entries into a list called department_list
with open("city-of-seattle-2012-expenditures-dollars.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    row_num = 1
    department_list = []
    for line in reader:
        if row_num != 1:
            pair = Department(line[0], int(line[3]))
            department_list.append(pair)
            row_num += 1
        else:
            row_num += 1

# creating dictionary of {department:expenses} pairs
myDict = {}
for item in department_list:
    myDict[item.dep] = item.expenses

# creating lists of expenses (values) for each department (keys)
value_list = []
for key in myDict.keys():
    for item in department_list:
        # if the department name matches the current key, add the expense to value_list
        if item.dep == key:
            value_list.append(item.expenses)
            myDict[key] = value_list
        else:
            # once item.dep is no longer equal to the current key, wipe list and restart with new key
            value_list = []

# once each department (key) has a list of expenses (value),
# sum up each departments expenses and replace the list (value) with the sum
for key in myDict.keys():
    total = 0
    for item in myDict.get(key):
        total += item
    myDict.update({key: total})

# printing out the entries neatly
for j, k in myDict.items():
    print("{0} --> ${1:,}.00".format(j, k))


# total amount spent by city  of Seattle
total_spent = 0
for key in myDict.keys():
    total_spent = myDict.get(key) + total_spent

print("\nTotal spent by the city of Seattle in 2012: " + '${:,}.00'.format(total_spent))
