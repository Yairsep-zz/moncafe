import os
import sys

from Repository import repo
from DTO import Employee, Supplier, Product, Coffee_stand


def main(argv):

    repo.deleteifExist()
    repo.create_tables()
    load_configuration()


def load_configuration():
    config = sys.argv[1]
    # file_action = open(sys.argv[2])
    file = open(config, 'r')
    content = file.read()
    lines = content.split("\n")

    for line in lines:
        p = line.split(", ")
        if p[0] == "E":
            repo.employee.insert(Employee(p[1], p[2], p[3], p[4]))
        if p[0] == "S":
            repo.supplier.insert(Supplier(p[1], p[2], p[3]))
        if p[0] == "P":
            repo.product.insert(Product(p[1], p[2], p[3], 0))
        if p[0] == "C":
            repo.coffee_stand.insert(Coffee_stand(p[1], p[2], p[3]))


if __name__ == '__main__':
    main(sys.argv)
