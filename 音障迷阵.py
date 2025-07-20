
from traceback import print_list
from utils import *

from generater import BaseGenerate
import os
from std_ans import get_ans

class Grenrate(BaseGenerate):
    def generate_one(self):
        n = random_int(100,1000)
        first = [0 if random_int(1,100)<random_int(60,100) else 1 for _ in range(n)]
        first[0] = 0
        if n == 1:
            first[len(first)-1] = 0
            print(n)
            print_line(first)
            return

        print(n)
        print_line(first)
        for i in range(1,n):
            line = [0 if random_int(0,100)<random_int(60,100) else 1 for _ in range(n)] #random_int_list(n,0,1)
            if i == n -1:
                line[n-1] = 0
            print_line(line)


        



if __name__ == "__main__":
    # 获取文件名
    file_name = os.path.basename(__file__).replace(".py", "")

    # g = Grenrate(f".\\data\\{file_name}",21,30)
    # g.do_generate()
    get_ans(f".\\data\{file_name}",f".\\testcpp\{file_name}.cpp")

    