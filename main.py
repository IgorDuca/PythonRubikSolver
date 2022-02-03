import random
from pprint import pprint

from whiteCross import checkWhiteCross

class Solver():
    def __init__(self):
        self.blocks = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9']
        self.parsed_blocks = []
    def shuffle(self):
        blocks = self.blocks
        parsed_blocks = self.parsed_blocks

        for i in range(0, 4):
            face_list = []
            for ii in range(0, 9):
                rand = random.choice(blocks)
                print("Choice: {} - Index: {} | Length: {} | New length: {}".format(rand, blocks.index(rand), len(blocks), len(blocks) - 1))
                face_list.append(rand)
                blocks.remove(rand)
            
            parsed_blocks.append(face_list)
        
        for block in parsed_blocks:
            blocks.append(block)

        print("")
        pprint(blocks)
        print("")
    def recognize_methods(self):
        blocks = self.blocks

        checkWhiteCross(blocks)

solver = Solver()
solver.shuffle()
solver.recognize_methods()