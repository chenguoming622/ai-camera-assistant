#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI智能构图相机 - 主入口
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.logger import Logger
import json
import os

from src.ui.camera_screen import CameraScreen
from src.ui.settings_screen import SettingsScreen


class AICompositionCameraApp(App):
    """主应用类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config_data = None
        self.screen_manager = None
        
    def build(self):
        """构建应用界面"""
        Logger.info("App: 启动AI智能构图相机")
        
        # 加载配置
        self.load_config()
        
        # 设置窗口
        Window.clearcolor = (0, 0, 0, 1)
        
        # 创建屏幕管理器
        self.screen_manager = ScreenManager()
        
        # 添加相机屏幕
        camera_screen = CameraScreen(name='camera', config=self.config_data)
        self.screen_manager.add_widget(camera_screen)
        
        # 添加设置屏幕
        settings_screen = SettingsScreen(name='settings', config=self.config_data)
        self.screen_manager.add_widget(settings_screen)
        
        Logger.info("App: 应用界面构建完成")
        return self.screen_manager
    
    def load_config(self):
        """加载配置文件"""
        config_path = 'config/config.json'
        try:
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    self.config_data = json.load(f)
                Logger.info(f"App: 配置文件加载成功")
            else:
                Logger.warning(f"App: 配置文件不存在，使用默认配置")
                self.config_data = self.get_default_config()
        except Exception as e:
            Logger.error(f"App: 加载配置文件失败: {e}")
            self.config_data = self.get_default_config()
    
    def get_default_config(self):
        """获取默认配置"""
        return {
            "app": {"name": "AI智能构图相机", "version": "1.0.0"},
            "local_analysis": {"enabled": True, "analysis_fps": 2},
            "ui": {"show_grid": True, "show_local_score": True},
            "tencent_cloud": {"enabled": False}
        }
    
    def on_pause(self):
        """应用暂停时"""
        Logger.info("App: 应用暂停")
        return True
    
    def on_resume(self):
        """应用恢复时"""
        Logger.info("App: 应用恢复")
    
    def on_stop(self):
        """应用停止时"""
        Logger.info("App: 应用停止")


if __name__ == '__main__':
    AICompositionCameraApp().run()
