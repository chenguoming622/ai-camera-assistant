# WSL安装与Android打包指南

## 方法1：启用WSL（Windows 10/11）

### 步骤1：启用WSL功能

以**管理员身份**运行PowerShell，执行：

```powershell
# 启用WSL功能
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# 启用虚拟机平台
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

### 步骤2：重启电脑

重启后，再次以管理员身份运行PowerShell：

```powershell
# 设置WSL 2为默认版本
wsl --set-default-version 2

# 安装Ubuntu
wsl --install -d Ubuntu-22.04
```

### 步骤3：配置Ubuntu

首次启动Ubuntu会要求设置用户名和密码，设置完成后：

```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装必要工具
sudo apt install -y python3 python3-pip git openjdk-11-jdk unzip
```

---

## 方法2：手动下载Ubuntu（如果wsl命令不可用）

### 1. 从Microsoft Store安装

1. 打开Microsoft Store
2. 搜索"Ubuntu 22.04"
3. 点击"获取"安装
4. 安装完成后点击"启动"

### 2. 或者手动下载

访问：https://aka.ms/wslubuntu2204
下载后双击安装

---

## 在WSL中打包Android应用

### 步骤1：进入WSL

```powershell
# 在PowerShell中启动WSL
wsl
```

### 步骤2：访问Windows文件

```bash
# Windows的C盘在WSL中的路径是 /mnt/c/
cd /mnt/c/Users/Administrator/Desktop/AIGOUTU
```

### 步骤3：安装Python依赖

```bash
# 安装pip
sudo apt install python3-pip -y

# 安装项目依赖
pip3 install -r requirements.txt

# 安装Buildozer
pip3 install buildozer

# 安装Buildozer依赖
sudo apt install -y \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good
```

### 步骤4：修改requirements.txt（重要！）

Android打包需要使用headless版本的OpenCV：

```bash
# 编辑requirements.txt
nano requirements.txt
```

将 `opencv-python==4.8.1.78` 改为 `opencv-python-headless==4.8.1.78`

### 步骤5：打包APK

```bash
# 首次打包（需要30-60分钟）
buildozer android debug

# 如果遇到问题，先清理再打包
buildozer android clean
buildozer android debug
```

### 步骤6：获取APK

打包完成后，APK文件在：
```
bin/aicompositioncamera-1.0.0-debug.apk
```

在Windows中访问：
```
C:\Users\Administrator\Desktop\AIGOUTU\bin\aicompositioncamera-1.0.0-debug.apk
```

---

## 方法3：如果WSL无法安装（备选方案）

### 使用GitHub Actions自动打包

我可以帮你创建GitHub Actions配置文件，推送到GitHub后自动在云端打包APK。

优点：
- 不需要本地安装WSL
- 自动化打包
- 可以随时下载APK

缺点：
- 需要GitHub账号
- 需要推送代码到GitHub

---

## 常见问题

### Q: WSL安装失败
A: 确保Windows版本是Windows 10 1903或更高版本，或Windows 11

### Q: 权限不足
A: 必须以管理员身份运行PowerShell

### Q: buildozer打包失败
A: 
1. 检查是否修改了requirements.txt使用opencv-python-headless
2. 运行 `buildozer android clean` 清理后重试
3. 确保网络畅通（需要下载SDK/NDK）

### Q: 下载SDK很慢
A: 可以配置代理或使用国内镜像

---

## 下一步

1. 按照上述方法安装WSL
2. 在WSL中打包APK
3. 将APK传输到手机安装测试

如有问题，随时询问！
