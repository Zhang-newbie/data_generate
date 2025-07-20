import os
import sys
from abc import abstractmethod

class BaseGenerate:
    def __init__(self,path,begin,end):
        self.path = path
        self.begin = begin
        self.end = end
        os.makedirs(path,exist_ok=True)
    
    def do_generate(self):
        for i in range(self.begin,self.end+1):
            sys.stdout.write(f"generate {i}/{self.end}\r")
            with open(os.path.join(self.path,f"{i}.in"),"w",encoding="utf-8") as f:
                sys.stdout = f
                self.generate_one()
            sys.stdout = sys.__stdout__

    @abstractmethod
    def generate_one(self):
        pass