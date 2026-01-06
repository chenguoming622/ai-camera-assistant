[app]

# 应用名称
title = AI Camera

# 包名
package.name = aicamera

# 包域名
package.domain = org.example

# 源代码目录
source.dir = .

# 源代码包含的文件
source.include_exts = py,png,jpg,kv,atlas,json

# 版本
version = 1.0

# 应用需求 - 使用稳定版本
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,numpy,requests,android,pyjnius

# 支持的架构
android.archs = arm64-v8a

# 权限
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET

# Android API版本
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31

# 启动模式
android.entrypoint = org.kivy.android.PythonActivity

# 屏幕方向
orientation = portrait

# 全屏
fullscreen = 0

# Android主题
android.theme = @android:style/Theme.NoTitleBar

# 接受SDK许可
android.accept_sdk_license = True

# 跳过更新
android.skip_update = False

# 自动接受许可
android.auto_accept_license = True

[buildozer]

# 日志级别
log_level = 2

# 警告级别
warn_on_root = 1

# 构建目录
build_dir = ./.buildozer

# 二进制目录
bin_dir = ./bin
