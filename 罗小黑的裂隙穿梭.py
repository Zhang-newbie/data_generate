
from utils import *

from generater import BaseGenerate
import os
from std_ans import get_ans

class Grenrate(BaseGenerate):
    def generate_one(self):
        n = random_int(3,30000)
        t = random_int(2,n)
        print(n,t)

        for i in range(1,n):
            print(random_int(1,n-i),end=" " if i < n-1 else "\n")




if __name__ == "__main__":
    # 获取文件名
    file_name = os.path.basename(__file__).replace(".py", "")

    g = Grenrate(f".\\data\\{file_name}",1,30)
    g.do_generate()

    get_ans(f".\\data\{file_name}",f".\\testcpp\{file_name}.cpp")

    