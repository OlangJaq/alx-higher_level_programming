#!/usr/bin/python3



class employee():
    """a sample employ class"""

    raise_amnt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@email.com.format(sefl.first, self.last)"
    
    @property
    def fullname(self):
        return "{} {}.format(self.first, self.las)"
    
    def pay(self):
        self.pay = int(self.pay * self.raise_amnt)