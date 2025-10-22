class Employee:
    def __init__(self, name, idNumber, department, title):
        self.__name = name
        self.__idNumber = idNumber
        self.__department = department
        self.__title = title

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_idNum(self, idNumber):
        self.__idNumber = idNumber

    def get_idNum(self):
        return self.__idNumber

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.__department

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def __str__(self):
        return 'Name: ' + self.__name + '\nID number: ' + str(self.__idNumber) +\
               '\nDepartment: ' + self.__department + '\nTitle: ' + self.__title
    
    
        
