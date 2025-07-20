import random


default_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
upper_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_str = "abcdefghijklmnopqrstuvwxyz"
number_str = "1234567890"

def random_string(length,data:str=default_str):
    
    random_string = ''.join(random.choice(data) for _ in range(length))
    return random_string

def random_en(length):
    return random_string(length,data=lower_str+upper_str)

def random_number(length,data:str=number_str):
    
    random_string = ''.join(random.choice(data) for _ in range(length))
    return random_string

def random_upper(length,data:str=upper_str):
    
    random_string = ''.join(random.choice(data) for _ in range(length))
    return random_string

def random_lower(length,data:str=lower_str):
   
    random_string = ''.join(random.choice(data) for _ in range(length))
    return random_string

def random_int(min,max):
    return random.randint(min,max)

def random_float(min,max):
    return random.uniform(min,max)

# 生成随机数列表
def random_float_list(length,min,max):
    return [random_float(min,max) for _ in range(length)]

def random_int_list(length,min,max):
    return [random_int(min,max) for _ in range(length)]

def print_line(data:list):
    for index,item in enumerate(data):
        print(item,end="\n" if index == len(data)-1 else " ")
