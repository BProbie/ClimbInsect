# ⭐原创开源脚本

### 软件名称：ClimbInsect（网安爬虫脚本）

### 软件版本：v1.0.0（稳定版）

### 开发语言：Python（Python-3.13.0）

### 开发时间：2026年05月10日 ~ 至今持续更新！

### 开源地址（Github）：https://github.com/BProbie/ClimbInsect/

### 开源协议（MIT）：https://github.com/BProbie/ClimbInsect/raw/refs/heads/master/LICENSE/

### 下载地址（Github）：https://github.com/BProbie/ClimbInsect/releases/tag/1.0.0/

### 依赖工具：pip

### 依赖技术：

- ##### requests~=2.32.5

- ##### fake-useragent~=2.2.0



# ⭐脚本简介

### 用于网络空间安全学习以及测试的Python爬虫脚本



# ⭐快速开始

### GIT

##### 克隆项目

```shell
git clone https://github.com/BProbie/ClimbInsect.git
```

##### 安装依赖

```shell
cd ClimbInsect
python.exe -m pip install --upgrade pip
python.exe -m pip install -r requirements.txt
```

##### 构建工具

```shell
cd scripts
build
```

##### 运行爬虫

```shell
cd ../dist
main -u https://www.baidu.com
```



# ⭐使用教程

```shell
ClimbInsect -h
```

```shell
usage: 命令行参数 [-h] [-url URL] [-type TYPE] [-data DATA] [-file FILE] [-byte BYTE]

options:
  -h, --help      show this help message and exit
  -url, -u URL    请求网址 https://www.baidu.com/
  -type, -t TYPE  请求类型 POST/GET
  -data, -d DATA  数据词典 {'key':'value'}
  -file, -f FILE  本地文件 C:\Users\probie\Desktop\txt.txt
  -byte, -b BYTE  是否二进 True/False
```

|   名称   | 参数  | 简化 |         作用         |                             示例                             |
| :------: | :---: | :--: | :------------------: | :----------------------------------------------------------: |
|   帮助   | -help |  -h  |       查看帮助       |                      ClimbInsect -help                       |
| 请求网址 | -url  |  -u  |       设置网址       |             ClimbInsect -u https://www.baidu.com             |
| 请求类型 | -type |  -t  |       设置类型       |         ClimbInsect -u https://www.baidu.com -t POST         |
| 请求数据 | -data |  -d  |       设置数据       | ClimbInsect -u https://www.baidu.com -t POST -d {'key':'value'} |
| 下载文件 | -file |  -f  |   设置文件下载路径   | ClimbInsect -u https://www.baidu.com -t POST -d {'key':'value'} -f C:\Users\probie\Desktop\txt.txt |
| 是否二进 | -byte |  -b  | 设置是否为二进制形式 | ClimbInsect -u https://www.baidu.com -t POST -d {'key':'value'} -f C:\Users\probie\Desktop\txt.txt -b True |



# ⭐项目结构

```markdown
ClimbInsect/
├── .github/
│   └── workflows/
│       └── build.yml
├── .idea/ # 已在仓库中删除
├── build/ # 已在仓库中删除
├── dist/ # 已在仓库中删除
├── scripts/
│   ├── build.bat
│   ├── build.sh
├── src/
│   └── climbinsect/
│       ├── data/
│       │   ├── args.py
│       │   └── __init__.py
│       ├── main.py
│       └── __init__.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```



# ⭐技术细节

### ① 工具做了多终端的适配

### ② 工具做了跨平台的适配



# ⭐作者介绍

### 作者：probie

### 贡献：\[probie, probie, probie]



# ⭐疑问交流联系

### 如有疑问请通过提交Issue阐述，作者能看到且会经常查看！



# ❤❤❤