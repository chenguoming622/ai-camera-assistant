# 快速开始指南

## 🚀 5分钟快速体验

### 步骤1：安装依赖

```bash
# 克隆或下载项目
cd ai-camera-assistant

# 安装Python依赖
pip install -r requirements.txt
```

### 步骤2：配置（可选）

如果要使用腾讯云API，编辑 `config/config.json`：

```json
{
  "tencent_cloud": {
    "api_key": "你的API密钥",
    "api_secret": "你的API密钥",
    "enabled": true
  }
}
```

不配置也可以运行，将只使用本地分析功能。

### 步骤3：运行（PC测试）

```bash
python main.py
```

注意：PC上相机功能可能受限，建议直接打包到Android测试。

### 步骤4：打包Android APK

```bash
# 首次运行需要下载Android SDK（较慢）
buildozer android debug

# 生成的APK在 bin/ 目录
# 文件名类似：aicompositioncamera-1.0.0-debug.apk
```

### 步骤5：安装到手机

```bash
# 方法1：使用adb安装
adb install bin/aicompositioncamera-1.0.0-debug.apk

# 方法2：直接传输APK到手机安装
```

## 📱 Android使用流程

1. **打开应用** → 授予相机权限
2. **看到预览** → 屏幕显示辅助线和评分
3. **调整角度** → 根据提示移动手机
4. **点击拍摄** → 保存照片到相册

## ⚙️ 配置腾讯云API

### 获取API密钥

1. 访问 [腾讯云控制台](https://console.cloud.tencent.com/)
2. 注册/登录账号
3. 进入"访问管理" → "API密钥管理"
4. 创建密钥，获取 SecretId 和 SecretKey
5. 开通"图像分析"服务

### 配置到应用

方法1：修改配置文件
```json
{
  "tencent_cloud": {
    "api_key": "你的SecretId",
    "api_secret": "你的SecretKey",
    "enabled": true
  }
}
```

方法2：在应用设置中输入
- 打开应用 → 点击⚙设置 → 输入API密钥

## 🔧 常见问题

### Q: buildozer命令不存在？
```bash
pip install buildozer
```

### Q: 打包失败？
1. 确保安装了Java JDK
2. 确保有足够磁盘空间（至少5GB）
3. 首次打包需要下载很多文件，耐心等待

### Q: 相机权限被拒绝？
在手机设置中手动授予应用相机权限

### Q: 没有辅助线显示？
检查设置中是否开启了"显示网格线"

## 📚 下一步

- 阅读 [使用说明](docs/使用说明.md) 了解详细功能
- 阅读 [开发文档](docs/开发文档.md) 了解技术细节
- 查看 [README.md](README.md) 了解项目架构

## 🎯 功能演示

### 本地实时分析（无需网络）
- ✅ 三分法网格线
- ✅ 黄金分割线
- ✅ 主体识别
- ✅ 水平检测
- ✅ 实时评分（0-10分）
- ✅ 构图建议

### 云端精准分析（需要配置API）
- ⭐ 专业美学评分
- ⭐ 详细构图分析
- ⭐ 色彩平衡评估
- ⭐ 专业建议

## 💡 提示

1. **首次使用**建议先在光线充足的环境测试
2. **拍摄风景**时，将地平线放在三分之一处
3. **拍摄人物**时，将人物放在黄金分割点
4. **保持水平**，避免画面倾斜
5. **云端评分**每月有10000次免费额度，合理使用

## 🆘 获取帮助

- 查看文档：`docs/` 目录
- 提交Issue：GitHub Issues
- 邮件联系：support@example.com

祝您拍出精彩照片！📸
