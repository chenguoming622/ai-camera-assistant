# AI智能构图相机

基于Python的Android智能拍摄辅助应用，通过AI实时分析相机画面，提供专业构图建议。

## 功能特点

- 📸 **实时构图辅助** - 相机预览时实时显示构图建议
- 🎯 **智能主体识别** - 自动识别画面主体并标注
- 📐 **专业辅助线** - 三分法网格、黄金分割线、水平参考线
- 🤖 **AI美学评分** - 本地NIMA模型实时评分
- ☁️ **云端精准分析** - 可选腾讯云API获取专业评分
- 💡 **智能建议** - 实时提示调整角度、位置、构图

## 技术架构

### 混合AI方案
- **本地处理**: OpenCV + NIMA轻量模型（实时，0延迟）
- **云端增强**: 腾讯云图像分析API（按需调用，精准评分）

### 技术栈
- **框架**: Kivy + Buildozer
- **AI模型**: TensorFlow Lite (NIMA)
- **图像处理**: OpenCV
- **云端API**: 腾讯云AI
- **目标平台**: Android 6.0+

## 项目结构

```
ai-camera-assistant/
├── main.py                 # 应用入口
├── buildozer.spec         # Android打包配置
├── requirements.txt       # Python依赖
├── models/               # AI模型文件
│   └── nima_mobile.tflite
├── src/
│   ├── camera/           # 相机模块
│   │   ├── camera_manager.py
│   │   └── frame_processor.py
│   ├── ai/              # AI分析模块
│   │   ├── local_analyzer.py
│   │   ├── nima_model.py
│   │   └── cloud_api.py
│   ├── composition/     # 构图分析模块
│   │   ├── grid_overlay.py
│   │   ├── subject_detector.py
│   │   └── composition_rules.py
│   └── ui/             # 界面模块
│       ├── camera_screen.py
│       ├── overlay_renderer.py
│       └── settings_screen.py
├── assets/             # 资源文件
│   ├── icons/
│   └── fonts/
└── config/            # 配置文件
    └── config.json
```

## 安装说明

### 开发环境要求
- Python 3.8+
- Android SDK
- Buildozer

### 安装步骤
```bash
# 克隆项目
git clone <repository-url>
cd ai-camera-assistant

# 安装依赖
pip install -r requirements.txt

# 下载AI模型（首次运行）
python scripts/download_models.py
```

## 使用说明

### 开发模式（PC测试）
```bash
python main.py
```

### 打包Android APK
```bash
buildozer android debug
```

## 配置说明

编辑 `config/config.json` 配置腾讯云API：

```json
{
  "tencent_cloud": {
    "api_key": "your_api_key",
    "api_secret": "your_api_secret",
    "enabled": true
  },
  "local_analysis": {
    "fps": 2,
    "show_grid": true,
    "show_score": true
  }
}
```

## 开发计划

- [x] 项目架构设计
- [ ] 相机预览功能
- [ ] 本地AI模型集成
- [ ] 构图辅助线绘制
- [ ] 实时分析与建议
- [ ] 腾讯云API集成
- [ ] UI界面优化
- [ ] Android打包测试

## 许可证

MIT License
