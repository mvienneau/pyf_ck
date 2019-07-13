import numpy as np 

class Tape():
    def __init__(self):
        self.tape = [0]
        self.pointer = 0
    def incr(self):
        self.tape[self.pointer] += 1
    def decr(self):
        self.tape[self.pointer] += -1
    def movef(self):
        if self.pointer == len(self.tape) - 1: self.tape.append(0)
        self.pointer += 1
    def moveb(self):
        self.pointer += -1
    def output(self):
        print (chr(int(self.tape[self.pointer])))
    def inp(self, inp):
        self.tape[self.pointer] = inp
    def check_loop(self):
        if self.tape[self.pointer] == 0:
            return 0
        else:
            return 1


def evaluate(str):
    tape = Tape()
    parens = find_matching_paren(str)
    # instruction pointer
    i = 0
    while i < len(str):
        char = str[i]
        if char == "+": tape.incr()
        if char == "-": tape.decr()
        if char == ">": tape.movef()
        if char == "<": tape.moveb()
        if char == ".": tape.output()
        if char == "[":
            if not(tape.check_loop()):
                i = parens[i][1]
        if char == "]":
            if tape.check_loop():
                i = parens[i][0]
        i = i + 1



def find_matching_paren(str):
    se = {}
    starts = []
    for i, char in enumerate(str):
        if char == "[":
            starts.append(i)
        if char == "]":
            start = starts.pop()
            se[start] = (start, i)
            se[i] = (start, i)
    return se

    
    
s = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>"
# [2,1,2,1]
evaluate(s)


