import sys

from Repository import repo
from DTO import Activity, Product


def main(argv):
    # repo.remove_Activities_if_exist()
    load_actions()


def load_actions():
    action = sys.argv[1]
    file = open(action, 'r')
    content = file.read()
    lines = content.split("\n")

    for line in lines:
        p = line.split(", ")
        current_product_id = int(p[0])
        current_product = repo.product.find(current_product_id)
        # Case Supply activity
        if int(p[1]) > 0:
            repo.activity.insert(Activity(p[0], p[1], p[2], p[3]))
            repo.product.update(current_product, int(current_product.quantity) + int(p[1]))
        # Sale Activity
        if int(p[1]) < 0:
            current_quantity = int(current_product.quantity)
            if current_quantity + int(p[1]) >= 0:
                repo.activity.insert(Activity(p[0], p[1], p[2], p[3]))
                repo.product.update(
                    current_product, current_quantity + int(p[1]))
        if int(p[1]) == 0:
            break


if __name__ == '__main__':
    main(sys.argv)
