from classes import *

cls = globals()["ClassA"]
instance = cls("A1", "B1")
instance.print()

cls = globals()['ClassB']
instance = cls("A2", "B2")
instance.print()