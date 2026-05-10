import argparse

# 获取命令行参数
def getArgs():
    parser = argparse.ArgumentParser("命令行参数")
    parser.add_argument("-url", "-u", type=str, required=False, help="请求网址"+" "+"https://www.baidu.com/")
    parser.add_argument("-type", "-t", type=str, required=False, help="请求类型"+" "+"POST/GET")
    parser.add_argument("-data", "-d", type=str, required=False, help="数据词典"+" "+"{\'key\':\'value\'}")
    parser.add_argument("-file", "-f", type=str, required=False, help="本地文件"+" "+"C:\\Users\\probie\\Desktop\\txt.txt")
    parser.add_argument("-byte", "-b", type=str, required=False, help="是否二进"+" "+"True/False")
    return parser.parse_args()