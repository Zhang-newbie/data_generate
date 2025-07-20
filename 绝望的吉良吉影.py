
from utils import *

from generater import BaseGenerate
import os
from std_ans import get_ans

class Grenrate(BaseGenerate):
    def generate_one(self):
        n ,m,k,p = random_int(1,1000000),random_int(1,10000),random_int(1,1000000),random_int(1,1000000)
        print(n,m,k,p,end="\n")
        print_line(random_int_list(m,1,1000))
        print_line(random_int_list(n,1,1000))



if __name__ == "__main__":
    # 获取文件名
    file_name = os.path.basename(__file__).replace(".py", "")

    g = Grenrate(f"./data/{file_name}",1,30)
    g.do_generate()

    get_ans(f".\\data\{file_name}",f".\\testcpp\{file_name}.cpp")

    