#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
下载AI模型文件的脚本
"""

import os
import sys

def download_nima_model():
    """下载NIMA模型"""
    print("=" * 50)
    print("AI模型下载脚本")
    print("=" * 50)
    
    models_dir = "models"
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
        print(f"✓ 创建模型目录: {models_dir}")
    
    print("\n注意：")
    print("1. NIMA模型需要手动下载")
    print("2. 推荐使用以下开源实现：")
    print("   - https://github.com/idealo/image-quality-assessment")
    print("   - https://github.com/TianYangCai/NIMA-Image-assessment")
    print("\n3. 下载后将.tflite文件放入models/目录")
    print("   文件名：nima_mobile.tflite")
    
    print("\n4. 或者使用MobileNetV2作为替代：")
    print("   - 从TensorFlow Hub下载预训练模型")
    print("   - 转换为TFLite格式")
    
    print("\n当前项目可以在没有模型的情况下运行")
    print("将使用简化的评分算法")
    print("=" * 50)

if __name__ == "__main__":
    download_nima_model()
