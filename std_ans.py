import subprocess
import time
import os
from concurrent.futures import ProcessPoolExecutor
def compile_cpp(source_file, executable_name):
    try:
        result = subprocess.run(['g++',"-std=c++11", source_file, '-o', executable_name,"-static-libgcc","-static-libstdc++"], check=True)
        print(f"{source_file} 编译成功，生成 {executable_name}")
    except subprocess.CalledProcessError as e:
        print(f"编译失败: {e}")
        assert e

def run_cpp(executable_name, input_file, output_file):
    try:

            result = subprocess.Popen(executable_name, shell=True,stdin=open(input_file, 'r'), stdout=open(output_file, 'w'),stderr=subprocess.PIPE, text=True)
            code =  result.wait()
            if code!=0:
                os.remove(output_file)
                return f"code error : input_file：{input_file}\n output_file：{output_file}\ncode:{code}\n\n"
            return code
           
        
    except subprocess.CalledProcessError as e:
        # print(f"运行失败: {e}")
        os.remove(output_file)
        return f"error : input_file：{input_file}\n output_file：{output_file}\ne:{e}\n\n"


def get_ans(data_path,source_path):
    executable_name = source_path.replace(".cpp",".exe")

    compile_cpp(source_path,executable_name)


    futures = []
    # for filename in os.listdir(data_path):
    #     if filename.endswith(".in"):
    #         # 构造完整的文件路径
    #         input_file = os.path.join(data_path, filename)
    #         output_file = os.path.join(data_path, filename.replace(".in", ".out"))
    #         code = run_cpp(executable_name,input_file,output_file)
    #         print(code)
    with ProcessPoolExecutor(max_workers=1) as executor:
        for filename in os.listdir(data_path):
            if filename.endswith(".in"):
                # 构造完整的文件路径
                input_file = os.path.join(data_path, filename)
                output_file = os.path.join(data_path, filename.replace(".in", ".out"))
                future = executor.submit(run_cpp,executable_name,input_file,output_file)
                futures.append(future)
    for future in futures:
        code = future.result()
        print(code)


if __name__ == "__main__":
    get_ans(r".\data\璃月琉璃铺砖记",r".\testcpp\璃月琉璃铺砖记.cpp")


