
from utils import *

from generater import BaseGenerate



class Grenrate(BaseGenerate):
    def generate_one(self):
        # print(random_en(random_int(100,1000)))
        # print(random_en(random_int(1,100)))
        len1 = random_int(100,1000)
        len2 = random_int(1,len1)
        str1 = random_en(len1)
        print(str1)
        print(str1[:len2])




if __name__ == "__main__":
    g = Grenrate("./data/完美的再创世",11,12)
    g.do_generate()