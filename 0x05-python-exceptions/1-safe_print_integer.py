#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(avlue))
        return True
    except IndexError:
        pass
    finally:
        print()
        return False