# -*- coding: utf-8 -*-
"""
本地AI分析模块 - 使用OpenCV和轻量级模型进行实时分析
"""

import cv2
import numpy as np
from kivy.logger import Logger


class LocalAnalyzer:
    """本地AI分析器"""
    
    def __init__(self, config):
        self.config = config
        self.nima_model = None
        
        Logger.info("LocalAnalyzer: 初始化本地分析器")
    
    def initialize(self):
        """初始化分析器"""
        try:
            # 这里将来会加载NIMA模型
            # self.nima_model = load_nima_model()
            Logger.info("LocalAnalyzer: 分析器初始化成功")
            return True
        except Exception as e:
            Logger.error(f"LocalAnalyzer: 初始化失败: {e}")
            return False
    
    def analyze_frame(self, frame):
        """分析单帧图像"""
        if frame is None or frame.size == 0:
            return None
        
        try:
            results = {
                'subject': self._detect_subject(frame),
                'horizon': self._detect_horizon(frame),
                'brightness': self._analyze_brightness(frame),
                'score': self._calculate_aesthetic_score(frame),
                'suggestions': []
            }
            
            # 生成建议
            results['suggestions'] = self._generate_suggestions(results)
            
            return results
        except Exception as e:
            Logger.error(f"LocalAnalyzer: 分析失败: {e}")
            return None
    
    def _detect_subject(self, frame):
        """检测画面主体"""
        try:
            # 转换为灰度图
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            
            # 边缘检测
            edges = cv2.Canny(gray, 50, 150)
            
            # 查找轮廓
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            if contours:
                # 找到最大轮廓
                largest_contour = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(largest_contour)
                
                # 计算中心点
                center_x = x + w // 2
                center_y = y + h // 2
                
                return {
                    'bbox': (x, y, w, h),
                    'center': (center_x, center_y),
                    'area': w * h
                }
            
            return None
        except Exception as e:
            Logger.error(f"LocalAnalyzer: 主体检测失败: {e}")
            return None
    
    def _detect_horizon(self, frame):
        """检测水平线"""
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            
            # 霍夫直线检测
            edges = cv2.Canny(gray, 50, 150)
            lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
            
            if lines is not None:
                # 找到最接近水平的线
                horizontal_lines = []
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    angle = abs(np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi)
                    if angle < 10 or angle > 170:  # 接近水平
                        horizontal_lines.append((x1, y1, x2, y2, angle))
                
                if horizontal_lines:
                    # 返回最长的水平线
                    longest = max(horizontal_lines, key=lambda l: np.sqrt((l[2]-l[0])**2 + (l[3]-l[1])**2))
                    return {
                        'line': longest[:4],
                        'angle': longest[4],
                        'is_level': longest[4] < 2
                    }
            
            return None
        except Exception as e:
            Logger.error(f"LocalAnalyzer: 水平线检测失败: {e}")
            return None
    
    def _analyze_brightness(self, frame):
        """分析亮度"""
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            mean_brightness = np.mean(gray) / 255.0
            
            return {
                'value': mean_brightness,
                'level': self._get_brightness_level(mean_brightness)
            }
        except Exception as e:
            Logger.error(f"LocalAnalyzer: 亮度分析失败: {e}")
            return {'value': 0.5, 'level': 'normal'}
    
    def _get_brightness_level(self, value):
        """获取亮度等级"""
        if value < 0.3:
            return 'dark'
        elif value < 0.7:
            return 'normal'
        else:
            return 'bright'
    
    def _calculate_aesthetic_score(self, frame):
        """计算美学评分"""
        # 简化版评分算法，将来会使用NIMA模型
        try:
            # 基于多个因素的简单评分
            score = 5.0
            
            # 亮度因素
            brightness = self._analyze_brightness(frame)
            if brightness['level'] == 'normal':
                score += 1.0
            
            # 对比度因素
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            contrast = np.std(gray) / 255.0
            if 0.2 < contrast < 0.8:
                score += 1.0
            
            # 边缘清晰度
            edges = cv2.Canny(gray, 50, 150)
            edge_density = np.sum(edges > 0) / edges.size
            if 0.05 < edge_density < 0.3:
                score += 1.0
            
            return min(10.0, max(0.0, score))
        except Exception as e:
            Logger.error(f"LocalAnalyzer: 评分计算失败: {e}")
            return 5.0
    
    def _generate_suggestions(self, results):
        """生成构图建议"""
        suggestions = []
        
        # 主体位置建议
        if results['subject']:
            frame_width = 1280  # 从配置获取
            frame_height = 720
            center = results['subject']['center']
            
            # 三分法检查
            third_x = frame_width / 3
            third_y = frame_height / 3
            
            if center[0] < third_x:
                suggestions.append("主体偏左，建议向右移动")
            elif center[0] > 2 * third_x:
                suggestions.append("主体偏右，建议向左移动")
            
            if center[1] < third_y:
                suggestions.append("主体偏上，建议向下移动")
            elif center[1] > 2 * third_y:
                suggestions.append("主体偏下，建议向上移动")
        
        # 水平线建议
        if results['horizon']:
            if not results['horizon']['is_level']:
                angle = results['horizon']['angle']
                suggestions.append(f"画面倾斜{angle:.1f}度，请调整水平")
        
        # 亮度建议
        brightness = results['brightness']
        if brightness['level'] == 'dark':
            suggestions.append("光线较暗，建议增加曝光")
        elif brightness['level'] == 'bright':
            suggestions.append("光线过亮，建议降低曝光")
        
        # 评分建议
        score = results['score']
        if score >= 8.0:
            suggestions.append("✓ 构图优秀，可以拍摄")
        elif score >= 6.0:
            suggestions.append("构图良好，可适当调整")
        else:
            suggestions.append("建议调整构图")
        
        return suggestions if suggestions else ["继续调整以获得更好的构图"]
