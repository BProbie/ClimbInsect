# 依赖包
import ast
import time
import json
import textwrap
import requests
import fake_useragent
from data.args import getArgs

# 脚本信息
NAME = "ClimbInsect"
VERSION = "v1.0.0"

# 变量
url = None
type = None
data = None
file = None
byte = None

# GET 请求
def get(url: str, params: dict = None, data: dict = None) -> bytes: return requests.get(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, params=params, data=data).content

# POST 请求
def post(url: str, data: dict = None, params: dict = None) -> bytes: return requests.post(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, params=params, data=data).content

# 爬虫函数
def climbInsect():

    # 发起请求
    response = get(url=url, params=data) if str(type).lower().__contains__("get") else post(url=url, data=data)

    # 处理响应
    if file is None:
        if str(byte).lower().__contains__("true"):
            print(response)
        else:
            print(response.decode())
    else:
        if str(byte).lower().__contains__("true"):
            with open(file, "wb") as f:
                f.write(response)
        else:
            with open(file, "w") as f:
                f.write(response.decode())

    # 终止程序
    pass

# 展示函数
def show():
    print(textwrap.dedent(f"""
    Thanks For Using {NAME}-{VERSION}
    Url: {url}
    Type: {type}
    Data: {data}
    File: {file}
    Byte: {byte}
    """))
    time.sleep(1)

# 主函数
def main(args):

    # 初始化数据
    global url, type, data, file, byte
    url = input("url: ") if args.url is None else args.url
    type = "POST" if args.type is None else args.type
    try:
        data = None if args.data is None else json.loads(args.data)
    except json.decoder.JSONDecodeError:
        data = ast.literal_eval(args.data)
    file = None if args.file is None else args.file
    byte = False if args.byte is None else args.byte

    # 展示信息
    show()

    # 执行爬虫
    climbInsect()

# 启动程序
if __name__ == "__main__":
    main(getArgs())