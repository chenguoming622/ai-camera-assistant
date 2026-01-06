# -*- coding: utf-8 -*-
"""
网格叠加层模块 - 绘制构图辅助线
"""

from kivy.graphics import Color, Line, Rectangle
from kivy.logger import Logger


class GridOverlay:
    """网格叠加层"""
    
    def __init__(self, config):
        self.config = config.get('ui', {})
        self.grid_color = self.config.get('grid_color', [255, 255, 255, 128])
        
        # 归一化颜色值
        self.grid_color = [c / 255.0 for c in self.grid_color]
        
        Logger.info("GridOverlay: 初始化网格叠加层")
    
    def draw_rule_of_thirds(self, canvas, width, height):
        """绘制三分法网格"""
        if not self.config.get('show_grid', True):
            return
        
        with canvas:
            Color(*self.grid_color)
            
            # 垂直线
            third_w = width / 3
            Line(points=[third_w, 0, third_w, height], width=1.5)
            Line(points=[2 * third_w, 0, 2 * third_w, height], width=1.5)
            
            # 水平线
            third_h = height / 3
            Line(points=[0, third_h, width, third_h], width=1.5)
            Line(points=[0, 2 * third_h, width, 2 * third_h], width=1.5)
    
    def draw_golden_ratio(self, canvas, width, height):
        """绘制黄金分割线"""
        if not self.config.get('show_golden_ratio', True):
            return
        
        golden_ratio = 0.618
        
        with canvas:
            Color(*self.grid_color)
            
            # 垂直黄金分割线
            golden_w = width * golden_ratio
            Line(points=[golden_w, 0, golden_w, height], width=1.2, dash_length=5, dash_offset=2)
            
            # 水平黄金分割线
            golden_h = height * golden_ratio
            Line(points=[0, golden_h, width, golden_h], width=1.2, dash_length=5, dash_offset=2)
    
    def draw_horizon_line(self, canvas, width, height):
        """绘制水平参考线"""
        if not self.config.get('show_horizon', True):
            return
        
        with canvas:
            Color(1, 1, 0, 0.5)  # 黄色
            
            # 中心水平线
            center_h = height / 2
            Line(points=[0, center_h, width, center_h], width=1, dash_length=10, dash_offset=5)
    
    def draw_subject_box(self, canvas, subject_info):
        """绘制主体框"""
        if not self.config.get('show_subject_box', True) or not subject_info:
            return
        
        bbox = subject_info.get('bbox')
        if not bbox:
            return
        
        x, y, w, h = bbox
        box_color = self.config.get('subject_box_color', [255, 0, 0, 200])
        box_color = [c / 255.0 for c in box_color]
        
        with canvas:
            Color(*box_color)
            
            # 绘制矩形框
            Line(rectangle=(x, y, w, h), width=2)
            
            # 绘制中心点
            center = subject_info.get('center')
            if center:
                cx, cy = center
                # 绘制十字标记
                cross_size = 10
                Line(points=[cx - cross_size, cy, cx + cross_size, cy], width=2)
                Line(points=[cx, cy - cross_size, cx, cy + cross_size], width=2)
    
    def draw_all(self, canvas, width, height, subject_info=None):
        """绘制所有辅助线"""
        canvas.clear()
        
        self.draw_rule_of_thirds(canvas, width, height)
        self.draw_golden_ratio(canvas, width, height)
        self.draw_horizon_line(canvas, width, height)
        
        if subject_info:
            self.draw_subject_box(canvas, subject_info)
