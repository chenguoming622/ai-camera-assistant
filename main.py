#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI智能构图相机 - 主入口（简化版）
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.logger import Logger


class AICompositionCameraApp(App):
    """主应用类"""
    
    def build(self):
        """构建应用界面"""
        Logger.info("App: 启动AI智能构图相机")
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 标题
        title = Label(
            text='AI智能构图相机',
            font_size='32sp',
            size_hint=(1, 0.3)
        )
        layout.add_widget(title)
        
        # 版本信息
        version = Label(
            text='版本 1.0.0\n\n这是一个简化的测试版本\n完整功能正在开发中',
            font_size='18sp',
            size_hint=(1, 0.5)
        )
        layout.add_widget(version)
        
        # 测试按钮
        button = Button(
            text='点击测试',
            size_hint=(1, 0.2),
            font_size='24sp'
        )
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)
        
        Logger.info("App: 应用界面构建完成")
        return layout
    
    def on_button_press(self, instance):
        """按钮点击事件"""
        Logger.info("App: 按钮被点击")
        instance.text = '测试成功！'
    
    def on_pause(self):
        """应用暂停时"""
        return True
    
    def on_resume(self):
        """应用恢复时"""
        pass


if __name__ == '__main__':
    AICompositionCameraApp().run()
