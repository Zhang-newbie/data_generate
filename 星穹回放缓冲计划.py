
from utils import *

from generater import BaseGenerate
import os
from std_ans import get_ans

class Grenrate(BaseGenerate):
    def generate_one(self):
       
        a ,c= random_int(2,100000),random_int(1,100000)
        b = random_int(1,a-1)
        print(a,b,c)




if __name__ == "__main__":
    # 获取文件名
    file_name = os.path.basename(__file__).replace(".py", "")

    g = Grenrate(f".\data\{file_name}",1,30)
    g.do_generate()

    get_ans(f".\data\{file_name}",f".\\testcpp\{file_name}.cpp")

    