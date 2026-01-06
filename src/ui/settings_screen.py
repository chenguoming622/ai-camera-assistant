# -*- coding: utf-8 -*-
"""
设置屏幕
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.logger import Logger


class SettingsScreen(Screen):
    """设置屏幕"""
    
    def __init__(self, config, **kwargs):
        super().__init__(**kwargs)
        self.config = config
        self.build_ui()
        
        Logger.info("SettingsScreen: 设置屏幕初始化完成")
    
    def build_ui(self):
        """构建界面"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 标题
        title = Label(
            text='设置',
            size_hint=(1, 0.1),
            font_size='24sp',
            bold=True
        )
        layout.add_widget(title)
        
        # 显示设置
        layout.add_widget(self.create_section_title('显示设置'))
        layout.add_widget(self.create_switch_item('显示网格线', 'show_grid'))
        layout.add_widget(self.create_switch_item('显示黄金分割', 'show_golden_ratio'))
        layout.add_widget(self.create_switch_item('显示评分', 'show_local_score'))
        
        # 云端API设置
        layout.add_widget(self.create_section_title('云端API'))
        layout.add_widget(self.create_switch_item('启用腾讯云API', 'cloud_enabled'))
        
        # API密钥输入
        api_layout = BoxLayout(size_hint=(1, 0.08), spacing=10)
        api_layout.add_widget(Label(text='API Key:', size_hint=(0.3, 1)))
        self.api_key_input = TextInput(
            text=self.config.get('tencent_cloud', {}).get('api_key', ''),
            multiline=False,
            size_hint=(0.7, 1)
        )
        api_layout.add_widget(self.api_key_input)
        layout.add_widget(api_layout)
        
        # 返回按钮
        back_button = Button(
            text='返回',
            size_hint=(1, 0.1),
            background_color=(0.3, 0.7, 0.3, 1)
        )
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    def create_section_title(self, text):
        """创建分节标题"""
        return Label(
            text=text,
            size_hint=(1, 0.06),
            font_size='18sp',
            bold=True,
            halign='left'
        )
    
    def create_switch_item(self, label_text, config_key):
        """创建开关项"""
        item_layout = BoxLayout(size_hint=(1, 0.08), spacing=10)
        
        label = Label(text=label_text, size_hint=(0.7, 1), halign='left')
        label.bind(size=label.setter('text_size'))
        item_layout.add_widget(label)
        
        switch = Switch(
            active=self.get_config_value(config_key),
            size_hint=(0.3, 1)
        )
        switch.bind(active=lambda instance, value: self.on_switch_change(config_key, value))
        item_layout.add_widget(switch)
        
        return item_layout
    
    def get_config_value(self, key):
        """获取配置值"""
        if key == 'cloud_enabled':
            return self.config.get('tencent_cloud', {}).get('enabled', False)
        else:
            return self.config.get('ui', {}).get(key, True)
    
    def on_switch_change(self, key, value):
        """开关变化时"""
        Logger.info(f"SettingsScreen: {key} = {value}")
        # 这里应该保存配置到文件
    
    def go_back(self, instance):
        """返回相机屏幕"""
        self.manager.current = 'camera'
