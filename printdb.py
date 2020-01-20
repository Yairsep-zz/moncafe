import sqlite3
import sys
from Repository import repo


def main(argv):
    print_table(repo.activity.findall(), "Activities")
    print_table(repo.coffee_stand.findall(), "Coffee_Stands")
    print_table(repo.employee.findall(), "Employees")
    print_table(repo.product.findall(), "Products")
    print_table(repo.supplier.findall(), "Suppliers")
    print()
    print_EmployeeReport(repo.employeeReport.findall())
    print()
    print_table(repo.activityReport.findall(), "Activities")


def print_table(list_of_tuples, name):
    print(name)
    for item in list_of_tuples:
        print(item)


def print_EmployeeReport(list):
    print("Employee Report")
    output = ""
    for item in list:
        output=""
        output =  str(item[0]) + ' ' +str(item[1]) + ' ' + str(item[2]) + ' '
        # print(item[1], end=' ')
        # print(item[2], end=' ')
        if item[3] == None:
            output =str (output) + '0'
        else:
            output = str(output) + str(item[3])
        print(output)


if __name__ == '__main__':
    main(sys.argv)
