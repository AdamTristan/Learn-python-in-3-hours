
employee_file = open("readme.txt", "r")

print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readlines())
for employee in employee_file.readlines():
    print(employee)
employee_file.close()