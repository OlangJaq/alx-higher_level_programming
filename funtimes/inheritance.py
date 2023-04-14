#!/usr/bin/python3
'''A Python program to demonstrate inheritance'''


class person(object):     
    #Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    #check if the person is an employ
    def display(self):
        print(self.name, self.id)

#drive code
emp = person("Jack", 102)
emp.display()
