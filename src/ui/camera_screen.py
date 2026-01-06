# -*- coding: utf-8 -*-
"""
相机屏幕 - 主界面
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Canvas
from kivy.logger import Logger
from kivy.clock import Clock

from src.camera.camera_manager import CameraManager
from src.ai.local_analyzer import LocalAnalyzer
from src.ai.cloud_api import TencentCloudAPI
from src.composition.grid_overlay import GridOverlay


class CameraScreen(Screen):
    """相机屏幕"""
    
    def __init__(self, config, **kwargs):
        super().__init__(**kwargs)
        self.config = config
        
        # 初始化组件
        self.camera_manager = CameraManager(config)
        self.local_analyzer = LocalAnalyzer(config)
        self.cloud_api = TencentCloudAPI(config)
        self.grid_overlay = GridOverlay(config)
        
        # 分析结果
        self.current_analysis = None
        
        # 构建界面
        self.build_ui()
        
        Logger.info("CameraScreen: 相机屏幕初始化完成")
    
    def build_ui(self):
        """构建用户界面"""
        layout = FloatLayout()
        
        # 初始化相机
        if self.camera_manager.initialize():
            camera_widget = self.camera_manager.get_camera_widget()
            if camera_widget:
                layout.add_widget(camera_widget)
        
        # 评分标签
        self.score_label = Label(
            text='评分: --',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'x': 0.02, 'top': 0.98},
            color=(1, 1, 1, 1),
            font_size='20sp',
            bold=True
        )
        layout.add_widget(self.score_label)
        
        # 建议标签
        self.suggestion_label = Label(
            text='',
            size_hint=(0.96, None),
            height=100,
            pos_hint={'center_x': 0.5, 'y': 0.15},
            color=(1, 1, 0, 1),
            font_size='16sp',
            halign='center',
            valign='middle'
        )
        self.suggestion_label.bind(size=self.suggestion_label.setter('text_size'))
        layout.add_widget(self.suggestion_label)
        
        # AI精准评分按钮
        self.cloud_button = Button(
            text='AI精准评分',
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={'x': 0.02, 'y': 0.02},
            background_color=(0.2, 0.6, 1, 1)
        )
        self.cloud_button.bind(on_press=self.request_cloud_analysis)
        layout.add_widget(self.cloud_button)
        
        # 拍照按钮
        self.capture_button = Button(
            text='📸',
            size_hint=(None, None),
            size=(80, 80),
            pos_hint={'center_x': 0.5, 'y': 0.02},
            background_color=(1, 0.3, 0.3, 1),
            font_size='40sp'
        )
        self.capture_button.bind(on_press=self.capture_photo)
        layout.add_widget(self.capture_button)
        
        # 设置按钮
        self.settings_button = Button(
            text='⚙',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'right': 0.98, 'y': 0.02},
            font_size='30sp'
        )
        self.settings_button.bind(on_press=self.open_settings)
        layout.add_widget(self.settings_button)
        
        self.add_widget(layout)
        self.layout = layout
    
    def on_enter(self):
        """进入屏幕时"""
        Logger.info("CameraScreen: 进入相机屏幕")
        
        # 初始化分析器
        self.local_analyzer.initialize()
        
        # 启动相机预览
        self.camera_manager.start_preview(callback=self.on_frame_captured)
    
    def on_leave(self):
        """离开屏幕时"""
        Logger.info("CameraScreen: 离开相机屏幕")
        self.camera_manager.stop_preview()
    
    def on_frame_captured(self, frame):
        """处理捕获的帧"""
        # 本地分析
        analysis = self.local_analyzer.analyze_frame(frame)
        
        if analysis:
            self.current_analysis = analysis
            self.update_ui(analysis)
    
    def update_ui(self, analysis):
        """更新界面显示"""
        # 更新评分
        score = analysis.get('score', 0)
        self.score_label.text = f'评分: {score:.1f}/10'
        
        # 更新建议
        suggestions = analysis.get('suggestions', [])
        if suggestions:
            self.suggestion_label.text = '\n'.join(suggestions[:3])  # 最多显示3条
        
        # 绘制辅助线
        # 注意：实际绘制需要在相机widget的canvas上进行
        # 这里简化处理
    
    def request_cloud_analysis(self, instance):
        """请求云端分析"""
        Logger.info("CameraScreen: 请求云端精准评分")
        
        if not self.cloud_api.is_enabled():
            self.show_message("云端API未配置")
            return
        
        # 检查配额
        quota = self.cloud_api.check_quota()
        if quota['remaining'] <= 0:
            self.show_message("API配额已用完")
            return
        
        # 捕获当前画面
        frame = self.camera_manager.capture_photo()
        if frame is None:
            self.show_message("无法获取画面")
            return
        
        # 显示加载状态
        self.cloud_button.text = '分析中...'
        self.cloud_button.disabled = True
        
        # 异步调用API
        Clock.schedule_once(lambda dt: self.do_cloud_analysis(frame), 0.1)
    
    def do_cloud_analysis(self, frame):
        """执行云端分析"""
        result = self.cloud_api.analyze_image(frame)
        
        # 恢复按钮状态
        self.cloud_button.text = 'AI精准评分'
        self.cloud_button.disabled = False
        
        if result:
            self.show_cloud_result(result)
        else:
            self.show_message("云端分析失败")
    
    def show_cloud_result(self, result):
        """显示云端分析结果"""
        score = result.get('aesthetic_score', 0)
        rating = result.get('overall_rating', '')
        suggestions = result.get('suggestions', [])
        
        message = f"云端评分: {score:.1f}/10 {rating}\n"
        message += '\n'.join(suggestions[:3])
        
        self.suggestion_label.text = message
        Logger.info(f"CameraScreen: 云端评分: {score}")
    
    def capture_photo(self, instance):
        """拍摄照片"""
        Logger.info("CameraScreen: 拍摄照片")
        
        photo = self.camera_manager.capture_photo()
        if photo is not None:
            # 保存照片
            self.save_photo(photo)
            self.show_message("照片已保存")
        else:
            self.show_message("拍照失败")
    
    def save_photo(self, photo):
        """保存照片"""
        from PIL import Image
        from datetime import datetime
        
        try:
            # 生成文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"photo_{timestamp}.jpg"
            
            # 转换为PIL Image并保存
            img = Image.fromarray(photo)
            img.save(filename)
            Logger.info(f"CameraScreen: 照片已保存: {filename}")
        except Exception as e:
            Logger.error(f"CameraScreen: 保存照片失败: {e}")
    
    def show_message(self, message):
        """显示消息"""
        self.suggestion_label.text = message
        Logger.info(f"CameraScreen: {message}")
    
    def open_settings(self, instance):
        """打开设置"""
        self.manager.current = 'settings'
