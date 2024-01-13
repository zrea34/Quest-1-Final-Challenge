import csv
'''
# write to the file
with open("users.txt", "a") as file:
    file.write("\nZach Hope")


# read the file
with open("users.txt", "r") as file:

    for line in file:
        print(line)
'''


'''
class User:
    name: str
    email: str

    def __init__(self, name, email):
        self.name = name
        self.email = email


with open("users.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    user_list = []
    row_number = 1
    for list in reader:
        if row_number != 1:
            user = User(list[0] + " " + list[1], list[2])
            user_list.append(user)
            row_number += 1
        else:
            row_number += 1

print(user_list)
for item in user_list:
    print(item.email + " is the email of " + item.name)
'''


class Customer:
    name: str
    email: str
    balance: int

    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance


with open("customers.csv", "r") as cust:
    reader = csv.reader(cust, delimiter=",")
    cust_list = []
    row_num = 1
    for list in reader:
        if row_num != 1:
            customer = Customer(list[0] + " " + list[1], list[2], list[3])
            cust_list.append(customer)
            row_num += 1
        else:
            row_num += 1

for i in range(len(cust_list)):
    print(cust_list[i].balance)
