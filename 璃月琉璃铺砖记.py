
from utils import *

from generater import BaseGenerate
import os
from std_ans import get_ans

class Grenrate(BaseGenerate):
    def generate_one(self):
        m = random_int(1,16)
        n = random_int(m,16)
        print(m,n,end="\n")



if __name__ == "__main__":
    file_name = os.path.basename(__file__).replace(".py", "")

    g = Grenrate(f".\\data\\{file_name}",1,30)
    g.do_generate()

    get_ans(f".\\data\\{file_name}",f".\\testcpp\\{file_name}.cpp")

    