# 安装指南

## 系统要求

### 开发环境
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8 或更高版本
- **磁盘空间**: 至少 5GB（用于Android SDK）
- **内存**: 建议 8GB 或以上

### 目标设备
- **Android**: 6.0 (API 23) 或更高版本
- **相机**: 支持自动对焦
- **存储**: 至少 100MB 可用空间

## 安装步骤

### 1. 安装Python依赖

```bash
# 进入项目目录
cd ai-camera-assistant

# 安装依赖
pip install -r requirements.txt
```

如果遇到问题，可以逐个安装：

```bash
pip install kivy==2.2.1
pip install kivymd==1.1.1
pip install opencv-python==4.8.1.78
pip install numpy==1.24.3
pip install Pillow==10.1.0
pip install requests==2.31.0
```

### 2. 配置应用

复制示例配置文件：

```bash
# Windows
copy config\config.example.json config\config.json

# macOS/Linux
cp config/config.example.json config/config.json
```

编辑 `config/config.json`，根据需要修改配置。

### 3. 安装Buildozer（用于Android打包）

```bash
pip install buildozer
```

**注意**: Windows用户建议使用WSL（Windows Subsystem for Linux）或虚拟机。

### 4. 安装Android开发工具

Buildozer会自动下载Android SDK和NDK，但首次运行会比较慢。

确保安装了以下工具：
- Java JDK 8 或更高版本
- Git

#### 验证Java安装

```bash
java -version
```

应该显示Java版本信息。

### 5. 下载AI模型（可选）

```bash
python scripts/download_models.py
```

这会显示如何获取NIMA模型的说明。

**注意**: 没有模型也可以运行，将使用简化的评分算法。

## 运行应用

### PC测试（有限功能）

```bash
python main.py
```

**注意**: PC上相机功能可能受限，建议直接在Android设备上测试。

### Android打包

#### 首次打包（需要较长时间）

```bash
buildozer android debug
```

这个过程会：
1. 下载Android SDK（约1GB）
2. 下载Android NDK（约1GB）
3. 下载Python-for-Android
4. 编译依赖库
5. 打包APK

**预计时间**: 30-60分钟（取决于网络速度）

#### 后续打包（快速）

```bash
buildozer android debug
```

后续打包只需要几分钟。

### 安装到设备

#### 方法1: 使用ADB

```bash
# 连接Android设备，开启USB调试
adb devices

# 安装APK
adb install bin/aicompositioncamera-1.0.0-debug.apk
```

#### 方法2: 直接传输

1. 将 `bin/aicompositioncamera-1.0.0-debug.apk` 复制到手机
2. 在手机上点击APK文件安装

## 常见问题

### Q1: pip install 失败

**问题**: 某些包安装失败

**解决方案**:
```bash
# 升级pip
pip install --upgrade pip

# 使用国内镜像（中国用户）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

### Q2: buildozer命令不存在

**问题**: 运行buildozer时提示命令不存在

**解决方案**:
```bash
# 确保pip安装路径在PATH中
pip install --user buildozer

# 或使用python -m
python -m buildozer android debug
```

### Q3: Java版本问题

**问题**: buildozer提示Java版本不对

**解决方案**:
```bash
# 安装Java JDK 8
# Ubuntu/Debian
sudo apt-get install openjdk-8-jdk

# macOS
brew install openjdk@8

# Windows
# 从Oracle官网下载安装
```

### Q4: Android SDK下载慢

**问题**: SDK下载速度很慢或失败

**解决方案**:
1. 使用VPN或代理
2. 手动下载SDK并配置路径
3. 使用国内镜像源

### Q5: OpenCV在Android上不工作

**问题**: 打包后OpenCV功能异常

**解决方案**:
```bash
# 使用headless版本
pip install opencv-python-headless
```

修改 `requirements.txt`:
```
opencv-python-headless==4.8.1.78
```

### Q6: 权限被拒绝

**问题**: 应用无法访问相机

**解决方案**:
1. 在手机设置中手动授予相机权限
2. 检查 `buildozer.spec` 中的权限配置

### Q7: 应用闪退

**问题**: 打开应用后立即闪退

**解决方案**:
```bash
# 查看日志
adb logcat | grep python

# 检查是否缺少依赖
# 重新打包
buildozer android clean
buildozer android debug
```

## 配置腾讯云API

### 1. 注册腾讯云账号

访问: https://cloud.tencent.com/

### 2. 开通图像分析服务

1. 进入控制台
2. 搜索"图像分析"
3. 开通服务

### 3. 获取API密钥

1. 进入"访问管理" → "API密钥管理"
2. 创建密钥
3. 记录 SecretId 和 SecretKey

### 4. 配置到应用

编辑 `config/config.json`:

```json
{
  "tencent_cloud": {
    "api_key": "你的SecretId",
    "api_secret": "你的SecretKey",
    "enabled": true
  }
}
```

## 验证安装

### 检查Python环境

```bash
python --version
pip list | grep kivy
pip list | grep opencv
```

### 检查Buildozer

```bash
buildozer --version
```

### 检查Android工具

```bash
adb version
java -version
```

## 卸载

### 卸载Python包

```bash
pip uninstall -r requirements.txt -y
```

### 清理Buildozer缓存

```bash
rm -rf .buildozer/
rm -rf bin/
```

### 卸载Android应用

在手机上长按应用图标，选择卸载。

## 更新

### 更新代码

```bash
git pull origin main
```

### 更新依赖

```bash
pip install --upgrade -r requirements.txt
```

### 重新打包

```bash
buildozer android clean
buildozer android debug
```

## 获取帮助

如果遇到问题：

1. 查看 [常见问题](#常见问题)
2. 阅读 [开发文档](docs/开发文档.md)
3. 搜索 [GitHub Issues](https://github.com/your-repo/issues)
4. 提交新的Issue
5. 发送邮件: support@example.com

## 下一步

安装完成后，请阅读：
- [快速开始](QUICKSTART.md) - 5分钟快速体验
- [使用说明](docs/使用说明.md) - 详细功能说明
- [开发文档](docs/开发文档.md) - 技术细节

祝您使用愉快！📸
