from persistence import *

import sys
import os


def add_branche(splittedline: list[str]):
    # TODO: add the branch into the repo
    branch_id = splittedline[0]
    branch_location = splittedline[1]
    branch_number_of_employees = splittedline[2]
    branch = Branche(branch_id, branch_location, branch_number_of_employees)
    repo.add_branch(branch)


def add_supplier(splittedline: list[str]):
    # TODO: insert the supplier into the repo
    supplier_id = splittedline[0]
    supplier_name = splittedline[1]
    supplier_contact_information = splittedline[2]
    supplier = Supplier(supplier_id, supplier_name, supplier_contact_information)
    repo.add_supplier(supplier)


def add_product(splittedline: list[str]):
    # TODO: insert product
    product_id = splittedline[0]
    product_description = splittedline[1]
    product_price = splittedline[2]
    product_quantity = splittedline[3]
    product = Product(product_id, product_description, product_price, product_quantity)
    repo.add_product(product)


def add_employee(splittedline: list[str]):
    # TODO: insert employee
    employee_id = splittedline[0]
    name = splittedline[1]
    salary = splittedline[2]
    branch_id = splittedline[3]
    employee = Employee(employee_id, name, salary, branch_id)
    repo.add_employee(employee)


adders = {"B": add_branche,
          "S": add_supplier,
          "P": add_product,
          "E": add_employee}


def main(args: list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline: list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])


if __name__ == '__main__':
    main(sys.argv)
    # main("config.txt")
