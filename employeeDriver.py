#****************************************************************************************************
#
# Name: Spencer Verharst
# Course: COSC 2110 Computer Languages: Python
# Assignment: grapevines.py
# Due Date: 01/07/2025
# Description:
# This program does variuos things such as adding, deleteing, and loading to a binary file using classes.
#
#****************************************************************************************************

import pickle
import employee
import os

#****************************************************************************************************

FILENAME = 'employees.dat'
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


#****************************************************************************************************

def load_employees():
    endFile = False
    in_file = open(FILENAME, 'rb')
    employee_dict = {}
    try:
        while not endFile:
            try:
                employee_dict = pickle.load(in_file)
            except EOFError:
                endFile = True
    except IOError:
        employee_dict = {}

    in_file.close()

    return employee_dict

#****************************************************************************************************
        
def get_user_choice():
    print('Menu')
    print('-' * 20)
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an existing employee')
    print('4. Delete an employee')
    print('5. Quit', '\n')
    choice = int(input('Enter your choice: '))
    try:
        if choice < LOOK_UP or choice > QUIT:
            choice = int(input('Enter your choice again: '))
    except ValueError:
        print('must be a number')
             
    return choice

#****************************************************************************************************        

def add(employee_dict):
    name = input('Enter employee name: ')
    idNumber = int(input('Enter employee ID number: '))
    department = input('Enter employee department: ')
    title = input('Enter employee title: ')
    entry = employee.Employee(name=name, idNumber=idNumber, department=department, title=title)

    if idNumber not in employee_dict:
        employee_dict[idNumber] = entry
        print('New employee was added.')
    else:
        print('This employee already exist.')
                   

#****************************************************************************************************

def look_up(employee_dict):
    lookUp = int(input('Enter an employee ID number: '))

    if lookUp in employee_dict:
        print(employee_dict[lookUp])
    else:
        print('The specified ID number was not found.')
                

#****************************************************************************************************

def change(employee_dict):
    idNumber = int(input('Enter an employee ID number: '))

    if idNumber in employee_dict:
        name = input('Enter a new employee name: ')
        department = input('Enter a new employee department: ')
        title = input('Enter a new employee title: ')
        entry = employee.Employee(name=name, idNumber=idNumber, department=department, title=title)
        employee_dict[idNumber] = entry
        print('New Employee added.')
    else:
        print('The specified ID number was not found.')
                

#****************************************************************************************************

def delete(employee_dict):
    idNum = int(input('Enter employee ID number: '))

    if idNum in employee_dict:
        del employee_dict[idNum]
    else:
        print('The specifed ID number was not found')

#****************************************************************************************************

def save_employees(employee_dict):
    out_file = open(FILENAME, 'wb')

    pickle.dump(employee_dict, out_file)

    out_file.close()

#****************************************************************************************************

def main():
    emp1 = employee.Employee(name='Susan Meyer', idNumber=47899, department='Accounting', title='Vice President')
    emp2 = employee.Employee(name='Mark Jones', idNumber=39119, department='IT', title='Programmer')
    emp3 = employee.Employee(name='Joy Rodgers', idNumber=81774, department='Manufacturing', title='Engineer')
    employee_dict = {47899: emp1, 39119: emp2, 81774: emp3}

    save_employees(employee_dict)
    
    employees = load_employees()
    
    choice = 1
    
    while choice != QUIT:
        choice = get_user_choice()
        if choice == LOOK_UP:
            look_up(employee_dict)
        elif choice == ADD:
            add(employee_dict)
        elif choice == CHANGE:
            change(employee_dict)
        elif choice == DELETE:
            delete(employee_dict)
        elif choice == QUIT:
            save_employees(employee_dict)
        
    
    
#****************************************************************************************************

if __name__=='__main__':
    main()

#****************************************************************************************************

'''Menu
--------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit 

Enter your choice: 1
Enter an employee ID number: 47899
Name: Susan Meyer
ID number: 47899
Department: Accounting
Title: Vice President
Menu
--------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit 

Enter your choice: 2
Enter employee name: John Doe
Enter employee ID number: 1234
Enter employee department: IT
Enter employee title: Programmer
New employee was added.
Menu
--------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit 

Enter your choice: 1
Enter an employee ID number: 1234
Name: John Doe
ID number: 1234
Department: IT
Title: Programmer
Menu
--------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit 

Enter your choice: 4
Enter employee ID number: 1234
Menu
--------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit 

Enter your choice: 1
Enter an employee ID number: 1234
The specified ID number was not found.
Menu
--------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit 

Enter your choice: 3
Enter an employee ID number: 39119
Enter a new employee name: James Doe
Enter a new employee department: IT
Enter a new employee title: Programmer
New Employee added.
Menu
--------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit 

Enter your choice: 1
Enter an employee ID number: 39119
Name: James Doe
ID number: 39119
Department: IT
Title: Programmer
Menu
--------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit 

Enter your choice: 5'''

#****************************************************************************************************
