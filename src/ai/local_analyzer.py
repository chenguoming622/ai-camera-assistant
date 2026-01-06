# -*- coding: utf-8 -*-
"""
本地分析模块 - 简化版（不依赖OpenCV和TensorFlow）
"""

from kivy.logger import Logger
import numpy as np


class LocalAnalyzer:
    """本地分析器 - 简化版"""
    
    def __init__(self, config):
        self.config = config
        self.enabled = config.get('local_analysis', {}).get('enabled', True)
        Logger.info("LocalAnalyzer: 初始化本地分析器（简化版）")
    
    def initialize(self):
        """初始化分析器"""
        Logger.info("LocalAnalyzer: 分析器初始化完成")
        return True
    
    def analyze_frame(self, frame):
        """分析帧 - 简化版实现"""
        if not self.enabled:
            return None
        
        try:
            # 简单的亮度和对比度分析
            if isinstance(frame, np.ndarray):
                brightness = np.mean(frame)
                contrast = np.std(frame)
                
                # 简单评分算法
                score = self._calculate_simple_score(brightness, contrast)
                
                # 生成建议
                suggestions = self._generate_suggestions(brightness, contrast, score)
                
                return {
                    'score': score,
                    'brightness': brightness,
                    'contrast': contrast,
                    'suggestions': suggestions
                }
            
            return None
        except Exception as e:
            Logger.error(f"LocalAnalyzer: 分析失败: {e}")
            return None
    
    def _calculate_simple_score(self, brightness, contrast):
        """计算简单评分"""
        # 理想亮度范围: 100-150
        brightness_score = 10 - abs(brightness - 125) / 12.5
        brightness_score = max(0, min(10, brightness_score))
        
        # 理想对比度范围: 40-80
        contrast_score = 10 - abs(contrast - 60) / 6
        contrast_score = max(0, min(10, contrast_score))
        
        # 综合评分
        score = (brightness_score * 0.4 + contrast_score * 0.6)
        return round(score, 1)
    
    def _generate_suggestions(self, brightness, contrast, score):
        """生成建议"""
        suggestions = []
        
        if brightness < 80:
            suggestions.append("光线较暗，建议增加曝光")
        elif brightness > 170:
            suggestions.append("光线过亮，建议降低曝光")
        
        if contrast < 30:
            suggestions.append("画面对比度较低，建议调整角度")
        elif contrast > 90:
            suggestions.append("对比度过高，注意光线平衡")
        
        if score >= 8:
            suggestions.append("✓ 构图优秀，可以拍摄")
        elif score >= 6:
            suggestions.append("构图良好，可适当调整")
        else:
            suggestions.append("建议调整构图")
        
        return suggestions if suggestions else ["继续调整以获得更好效果"]
