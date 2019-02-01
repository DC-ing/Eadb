# eadb
**eadb=easy adb**</br>
封装常用的adb命令，提高使用效率，仅限：macOS、Linux使用

## 背景
在使用adb命令时，获取设备名、设备版本号、截屏等功能，输入的终端命令比较长，效率比较低，所以才有了这个小工具的诞生。

## 安装环境
 1. 搭建 Java 开发环境
 2. 搭建 Android-SDK 开发环境
 3. 安装 Python 3 环境，推荐使用3.7

## 安装

 ```
pip install eadb        # 安装
pip install -U eadb     # 更新版本
 ```

## 使用
### 查看版本号

```
$ eadb -v
0.0.5       # 安装成功
```

### 获取当前连接设备

```
$ eadb --devices
['012332EF', 'dj23df']

```

### 获取连接的设备版本号

```
# 获取当前电脑连接的所有设备的系统版本号
$ eadb --version
{
    "012332EF": "4.2.2",
    "dj23df": "7.1.1"
}

# 获取指定连接设备的系统版本号
$ eadb --version 012332EF
{
    "012332EF": "4.2.2"
}

# 获取当前电脑连接的所有设备的系统版本号
$ adversion
{
    "012332EF": "4.2.2",
    "dj23df": "7.1.1"
}

# 获取指定连接设备的系统版本号
$ adversion --id 012332EF
{
    "012332EF": "4.2.2"
}

```

# 获取连接的设备名称

```
# 获取当前电脑连接的所有设备的设备名称
$ eadb --name
{
    "012332EF": "Coolpad-9976A",
    "dj23df": "google-Nexus_6P"
}

# 获取指定连接设备的设备名称
$ eadb --name 012332EF
{
    "012332EF": "Coolpad-9976A"
}

# 获取当前电脑连接的所有设备的设备名称
$ adname
{
    "012332EF": "Coolpad-9976A",
    "dj23df": "google-Nexus_6P"
}

# 获取指定连接设备的设备名称
$ adname --id 012332EF
{
    "012332EF": "Coolpad-9976A"
}

```

# 获取连接设备的截屏

```
# 获取当前电脑连接的所有设备的截屏
$ eadb ----screenshot
'Coolpad-9976A'截屏成功，存放路径为'/your/path/save/Coolpad-9976A-4.2.2-20190201-111100.png'
'google-Nexus_6P'截屏成功，存放路径为'/your/path/save/google-Nexus_6P-7.1.1-20190201-111104.png'

# 获取指定连接设备的截屏
$ eadb ----screenshot 012332EF
'Coolpad-9976A'截屏成功，存放路径为'/your/path/save/Coolpad-9976A-4.2.2-20190201-111100.png'

# 获取当前电脑连接的所有设备的截屏
$ adscreen
'Coolpad-9976A'截屏成功，存放路径为'/your/path/save/Coolpad-9976A-4.2.2-20190201-111100.png'
'google-Nexus_6P'截屏成功，存放路径为'/your/path/save/google-Nexus_6P-7.1.1-20190201-111104.png'

# 获取指定连接设备的截屏
$ adscreen --id 012332EF
'Coolpad-9976A'截屏成功，存放路径为'/your/path/save/Coolpad-9976A-4.2.2-20190201-111100.png'

```

## 版本规划

- 完成自定义命令设置（完成）
- adb基本命令封装（完成devices、name、version、screenshot）
- 优化终端命令行输出（完成）
- 命令行尝试采用第三方库click(暂未完成)
- 封装更多的命令行（暂未有规划）