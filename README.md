### Processing编程学习指南 示例代码

迁移到processing-py

![封面](cover.jpg)

#### 环境配置

```
$ pip install processing-py --upgrade
```

或者本地安装processing_py的whl文件
```
$ pip install wheel
$ pip install processing_py-0.3.7-py3-none-any.whl
```

#### 环境配置 Ubuntu 16.04

Ubuntu 16.04上默认的python版本是3.5, processing-py依赖的最低版本为python3.6
所以需要先在ubuntu 16.04上安装python3.6以及python3.6-pip

安装python3.6
```
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6
```

安装python3.6-pip
```
$ curl https://bootstrap.pypa.io/get-pip.py | sudo python3.6
```

然后安装processing_py, 安装成功后验证一下
```
$ python3.6
>>> import processing_py
```

如果提示
```
ImportError: cannot import name 'urllib3'
```
说明需要安装urllib3
```
$ sudo pip uninstall urllib3
$ sudo pip install --upgrade urllib3
```


#### 参考文档

- <https://py.processing.org/tutorials/>
- <https://pypi.org/project/processing-py/>
