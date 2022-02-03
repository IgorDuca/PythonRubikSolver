import random
from pprint import pprint

# from whiteCross import checkWhiteCross
from generator import generateRubik
from recognize import Recognize

def RubikSolver():
    rubik = generateRubik() # Generates the Rubik's Cube

    availableMethods = Recognize.whitecross(rubik) # Uses the recognizer class to see if the Rubik has a good whitecross

RubikSolver()