from persistence import *

import sys


def main(args: list[str]):
    inputfilename: str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline: list[str] = line.strip().split(", ")
            # TODO: apply the action (and insert to the table) if possible
            product_id = int(splittedline[0])
            quantity = int(splittedline[1])
            activator_id = int(splittedline[2])
            date = splittedline[3]
            if quantity > 0:
                repo.add_activity(product_id, quantity, activator_id, date)
                repo.update_product_quantity(product_id, quantity)
            elif quantity < 0:
                if repo.get_product_quantity(product_id) + quantity >= 0:
                    repo.add_activity(product_id, quantity, activator_id, date)
                    repo.update_product_quantity(product_id, quantity)
                pass
            else:
                # if quantity = 0 or not enough products do nothing
                pass


if __name__ == '__main__':
    main(sys.argv)
