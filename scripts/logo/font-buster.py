import os
import sys

class FontBuster(object):

    def __init__(self):
        fin = open('haffa-font-A.svg','r');
        self.lines = fin.readlines()
    
    def parse(self):
        for l in self.lines:
            l = l.strip()
            if l.startswith('transform'):
                print(l)
                self.transform = l
                tx = float(self.transform[21:29])
                ty = float(self.transform[31:-2])
                print(tx,ty)
            if l.startswith('d='):
                self.path = l.split()
                for c in self.path:
                    print(c)

if __name__ == '__main__':
    fb = FontBuster()
    fb.parse()
