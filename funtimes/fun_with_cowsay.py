import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Good morning " + sys.argv[2])