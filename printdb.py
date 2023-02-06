from persistence import *


def main():
    # TODO: implement
    print("Activities")
    activities = repo.get_activities()
    for activity in activities:
        activity = list(activity)
        activity = [x.decode() if isinstance(x, bytes) else x for x in activity]
        activity = tuple(activity)
        print(activity)
    print("Branches")
    branches = repo.get_branches()
    for branch in branches:
        branch = list(branch)
        branch = [x.decode() if isinstance(x, bytes) else x for x in branch]
        branch = tuple(branch)
        print(branch)
    print("Employees")
    employees = repo.get_employees()
    for employee in employees:
        employee = list(employee)
        employee = [x.decode() if isinstance(x, bytes) else x for x in employee]
        employee = tuple(employee)
        print(employee)
    print("Products")
    products = repo.get_products()
    for product in products:
        product = list(product)
        product = [x.decode() if isinstance(x, bytes) else x for x in product]
        product = tuple(product)
        print(product)
    print("Suppliers")
    suppliers = repo.get_suppliers()
    for supplier in suppliers:
        supplier = list(supplier)
        supplier = [x.decode() if isinstance(x, bytes) else x for x in supplier]
        supplier = tuple(supplier)
        print(supplier)
    print("\nEmployees report")
    employees_report = repo.get_employees_report()
    for employee in employees_report:
        employee = list(employee)
        employee = [x.decode() if isinstance(x, bytes) else x for x in employee]
        employee = tuple(employee)
        print(" ".join(str(x) for x in employee))
    print("\nActivities report")
    activity_report = repo.get_activity_report()
    for activity in activity_report:
        activity = list(activity)
        activity = [x.decode() if isinstance(x, bytes) else x for x in activity]
        activity = tuple(activity)
        print(activity)


if __name__ == '__main__':
    main()
