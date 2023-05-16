# BGU Mart Supermarket Chain Management Software

BGU Mart is a software application built to manage supermarket chains. It provides functionality for managing employees, buying and selling products, managing inventory, and logging activities for tax purposes. This project aims to implement a tool using Python and SQLite to build the BGU Mart software.

## Method and Technical Description

The software consists of three Python modules and a SQLite database. The modules are as follows:

1. `initiate.py`: This module is responsible for creating the SQLite database and inserting the initial data from a configuration file. It takes the configuration file as an argument and builds the database with the specified tables and data.

2. `action.py`: This module handles supermarket activities such as sales and deliveries. It reads an actions file as an argument and performs each action sequentially. It checks the quantity of the sold product before processing the action.

3. `printdb.py`: This module prints the contents of the database. It provides reports on various tables, including detailed employee reports and activity reports.

## Database Structure

The `bgumart.db` database consists of the following tables:

1. `employees`: Holds information about the employees, including their ID, name, salary, and the branch they work in.

2. `suppliers`: Stores information about the suppliers, including their ID, name, and contact information.

3. `products`: Contains information about the products, including their ID, description, price, and quantity.

4. `branches`: Stores information about the branches, including their ID, location, and the number of employees.

5. `activities`: Stores information about all activities in the supermarket chain, including sales and deliveries. It includes the product ID, quantity, activator ID (employee or supplier), and date.

## Usage

To use the BGU Mart software, follow these steps:

1. Run the `initiate.py` module with a configuration file as an argument to create the initial database:
   ```
   python3 initiate.py config.txt
   ```

2. Run the `action.py` module with an actions file as an argument to perform supermarket activities:
   ```
   python3 action.py action.txt
   ```

3. Run the `printdb.py` module to print the contents of the database:
   ```
   python3 printdb.py
   ```

   The module will print the tables in the following order: Activities, Branches, Employees, Products, and Suppliers. It will also provide a detailed employees report and activity report as described in the project requirements.

Note: Make sure to replace `config.txt` and `action.txt` with the actual file names for your configuration and actions files.

## Configuration and Action Files

### Configuration File

The configuration file is a text file that contains information about employees, suppliers, products, and branches. Each line in the file represents a record of a specific type (E for employees, S for suppliers, P for products, and B for branches). Here's an example:

```
B,3,Chicago,40
E,106,Sue Davis,75000,3
P,5,Mango,2,7
S,6,Jkl Enterprises,(678) 901-2345
```

### Action File

The action file is a text file that contains supermarket activities such as sales and deliveries. Each line represents an activity and consists of four values: product ID, quantity, activator ID (employee or supplier), and date. A positive quantity represents a supply arrival, while a negative quantity represents a sale. Here's an example:

```
3, 500, 56, 20230110
100, -500, 1234, 20230110
```

## Development Environment

The BGU Mart software is developed using the Python programming language and utilizes the SQLite database for data storage. Here are the software's development requirements:

Python: Ensure that Python is installed on your system. You can download Python from the official Python website (https://www.python.org) and follow the installation instructions for your operating system.

SQLite: The SQLite database engine is included with Python by default, so there is no need for a separate installation.

Text Editor or Integrated Development Environment (IDE): Choose a text editor or IDE of your preference to write and run the Python code. Popular options include Visual Studio Code, PyCharm, Sublime Text, and Atom.

BGU Mart Source Code: Download the source code files for the BGU Mart software, including initiate.py, action.py, printdb.py, and the database file bgumart.db.

Once you have the development environment set up and the source code files ready, you can start using the BGU Mart software by following the instructions mentioned earlier.

Remember to adjust the command line arguments in the instructions according to your configuration and action files. Also, ensure that the configuration and action files are correctly formatted to match the expected input structure.

With the software set up and running, you can manage supermarket chain activities, such as sales, deliveries, and employee reports. The SQLite database provides a reliable and efficient storage solution, while the Python modules handle the logic and data manipulation.
