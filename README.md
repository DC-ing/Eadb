# eadb
**eadb=easy adb**</br>
封装常用的Android和iOS终端命令，提高使用效率，仅限：macOS、Linux使用

## 背景
在使用adb命令时，获取设备名、设备版本号、截屏等功能，输入的终端命令比较长，效率比较低；所以才有了这个小工具的诞生。在这之后，完善了对iOS设备的支持。

## 安装环境
 1. 搭建 Java 开发环境
 2. 搭建 Android-SDK 开发环境
 3. 安装 Python 3 环境，推荐使用3.7
 4. 安装iOS开发环境以及第三方库：`Xcode`, `Xcode Command Line Tools`, `libimobliedevice`, `usbmuxd`, `ideviceinstaller`

```
# 仅在 macOS 系统上有效。
# iOS 手机需连上xcode，在【设置->开发者】选项中，打开Enable UI Automation开关
brew uninstall ideviceinstaller
brew uninstall libimobiledevice
brew uninstall usbmuxd
brew install usbmuxd --HEAD
brew install --HEAD libimobiledevice
brew unlink libimobiledevice && brew link libimobiledevice
brew install --HEAD ideviceinstaller
brew unlink ideviceinstaller && brew link ideviceinstaller
sudo chmod -R 777 /var/db/lockdown
```


## 安装

 ```
pip install eadb        # 安装
pip install -U eadb     # 更新版本
 ```

## 使用方法

目前包含命令行有`eadb`,`ename`,`eversion`,`escreen`,`einfo`,`esize`.<br>
具体使用文档可参照【命令行+`-h`】命令

```
$ eadb --devices
['012332EF', 'dj23df']


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


## 版本规划

- 完成自定义命令设置（完成）
- adb基本命令封装（完成devices、name、version、screenshot、info、wm_size）
- 优化终端命令行输出（完成，以json格式输出）
- 封装ios的命令行（已完成）
- 自动识别Android或iOS，一个命令即可完成（已完成）
- logging融入到命令输出上（未完成，添加参数`--verbose`）
