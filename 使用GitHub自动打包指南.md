# 使用GitHub Actions自动打包Android APK

由于你的Windows系统无法启用WSL，我为你创建了GitHub Actions自动打包方案。这样可以在云端自动构建APK，无需本地配置复杂环境。

## 优势
✅ 无需安装WSL或Linux虚拟机
✅ 自动化构建，推送代码即可
✅ 云端资源，不占用本地电脑
✅ 可以随时下载构建好的APK
✅ 完全免费（GitHub Actions免费额度充足）

## 使用步骤

### 1. 创建GitHub仓库

1. 访问 https://github.com/new
2. 创建一个新仓库（可以是私有仓库）
3. 记下仓库地址，例如：`https://github.com/你的用户名/ai-camera-assistant.git`

### 2. 初始化Git并推送代码

在项目目录下打开PowerShell，执行：

```powershell
# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit"

# 添加远程仓库（替换成你的仓库地址）
git remote add origin https://github.com/你的用户名/ai-camera-assistant.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

### 3. 触发自动构建

推送代码后，GitHub Actions会自动开始构建APK。

你可以在GitHub仓库页面查看构建进度：
- 点击仓库顶部的 **Actions** 标签
- 查看正在运行的工作流

### 4. 下载APK

构建完成后（大约20-30分钟）：

1. 进入 **Actions** 页面
2. 点击最新的构建任务
3. 在页面底部找到 **Artifacts** 区域
4. 下载 `android-apk` 文件
5. 解压后得到APK文件

### 5. 安装到手机

将下载的APK传输到手机并安装。

## 手动触发构建

如果你修改了代码但不想推送，可以手动触发构建：

1. 进入GitHub仓库的 **Actions** 页面
2. 点击左侧的 **Build Android APK** 工作流
3. 点击右上角的 **Run workflow** 按钮
4. 选择分支，点击 **Run workflow**

## 配置说明

我已经创建了 `.github/workflows/build-android.yml` 配置文件，包含：

- ✅ 自动安装所有依赖
- ✅ 使用缓存加速后续构建
- ✅ 自动上传APK文件
- ✅ 支持手动触发构建
- ✅ 如果打tag会自动创建Release

## 常见问题

### Q: 构建失败怎么办？
A: 
1. 查看Actions页面的构建日志
2. 检查是否有依赖问题
3. 确保buildozer.spec配置正确

### Q: 构建时间太长？
A: 首次构建需要下载SDK/NDK，约20-30分钟。后续构建有缓存，只需5-10分钟。

### Q: 如何加速构建？
A: GitHub Actions会自动缓存.buildozer目录，后续构建会快很多。

### Q: 可以构建Release版本吗？
A: 可以，修改workflow文件中的 `buildozer android debug` 为 `buildozer android release`

### Q: 需要付费吗？
A: GitHub Actions对公开仓库完全免费，私有仓库每月有2000分钟免费额度。

## 本地测试（可选）

虽然无法打包APK，但可以在Windows上测试基本逻辑：

```powershell
# 安装依赖
pip install -r requirements.txt

# 运行（相机功能会受限）
python main.py
```

## 下一步

1. 创建GitHub仓库
2. 推送代码
3. 等待自动构建完成
4. 下载APK并安装到手机测试

如有问题，随时询问！
