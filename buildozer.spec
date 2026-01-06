[app]

# 应用名称
title = AI智能构图相机

# 包名
package.name = aicompositioncamera

# 包域名
package.domain = com.aicamera

# 源代码目录
source.dir = .

# 源代码包含的文件
source.include_exts = py,png,jpg,kv,atlas,json,tflite

# 版本
version = 1.0.0

# 应用需求
requirements = python3,kivy==2.3.0,kivymd==1.1.1,opencv-python-headless,numpy,pillow,requests,android

# 支持的架构
android.archs = arm64-v8a,armeabi-v7a

# 权限
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET,ACCESS_NETWORK_STATE

# 功能
android.features = android.hardware.camera,android.hardware.camera.autofocus

# Android API版本
android.api = 31
android.minapi = 21
android.ndk = 25b

# 启动模式
android.entrypoint = org.kivy.android.PythonActivity

# 屏幕方向
orientation = portrait

# 全屏
fullscreen = 0

# 图标和启动画面
#icon.filename = %(source.dir)s/assets/icon.png
#presplash.filename = %(source.dir)s/assets/presplash.png

# Android主题
android.theme = @android:style/Theme.NoTitleBar

[buildozer]

# 日志级别
log_level = 2

# 警告级别
warn_on_root = 1
