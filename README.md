
# Notes Crawler

## 使用库

- selenium 4.0.0

## 使用步骤

0. 安装 Python3

2. 安装 selenium

进入命令行，使用如下命令安装

```bash
pip3 install selenium
```

如果提示找不到 `pip3` 可以尝试:

```bash
pip install selenium
```

如果仍然提示安装错误，请尝试[百度](https://baidu.com)/[谷歌](https://google.com)搜索解决问题

2. 配置 chrome 内核

前往 [https://chromedriver.chromium.org/home](https://chromedriver.chromium.org/home) 下载 Chrome 内核，并将下载好的程序放在一个路径简单的位置

3. 修改 main.py 参数

- 修改代码 25 行为你的下载目录 （该路径作用为判断下载是否完成）
- 修改代码 35 行内的路径为你的 chrome 内核路径
- 修改代码 37 行内的 url 为想要爬取的资源地址

4. 运行脚本

```bash
python3 main.py
```

## 说明

主要是自用，所以写的比较简洁，如有需要可以随意使用代码。