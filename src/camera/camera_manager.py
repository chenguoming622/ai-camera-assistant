# -*- coding: utf-8 -*-
"""
相机管理模块 - 负责相机的初始化、预览和拍照
"""

from kivy.logger import Logger
from kivy.clock import Clock
import numpy as np

try:
    from android.permissions import request_permissions, Permission
    ANDROID = True
except ImportError:
    ANDROID = False
    Logger.warning("CameraManager: 非Android环境，使用模拟模式")


class CameraManager:
    """相机管理器"""
    
    def __init__(self, config):
        self.config = config
        self.camera = None
        self.is_active = False
        self.preview_callback = None
        
        Logger.info("CameraManager: 初始化相机管理器")
        
    def initialize(self):
        """初始化相机"""
        if ANDROID:
            self._request_permissions()
        
        try:
            self._setup_camera()
            Logger.info("CameraManager: 相机初始化成功")
            return True
        except Exception as e:
            Logger.error(f"CameraManager: 相机初始化失败: {e}")
            return False
    
    def _request_permissions(self):
        """请求Android权限"""
        Logger.info("CameraManager: 请求相机权限")
        request_permissions([
            Permission.CAMERA,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE
        ])
    
    def _setup_camera(self):
        """设置相机"""
        from kivy.uix.camera import Camera
        
        camera_config = self.config.get('camera', {})
        resolution = camera_config.get('preview_resolution', [1280, 720])
        
        self.camera = Camera(
            resolution=resolution,
            play=False
        )
        
        Logger.info(f"CameraManager: 相机设置完成，分辨率: {resolution}")
    
    def start_preview(self, callback=None):
        """开始预览"""
        if not self.camera:
            Logger.error("CameraManager: 相机未初始化")
            return False
        
        try:
            self.camera.play = True
            self.is_active = True
            self.preview_callback = callback
            
            # 启动帧捕获定时器
            fps = self.config.get('local_analysis', {}).get('analysis_fps', 2)
            Clock.schedule_interval(self._capture_frame, 1.0 / fps)
            
            Logger.info("CameraManager: 相机预览已启动")
            return True
        except Exception as e:
            Logger.error(f"CameraManager: 启动预览失败: {e}")
            return False
    
    def stop_preview(self):
        """停止预览"""
        if self.camera:
            self.camera.play = False
            self.is_active = False
            Clock.unschedule(self._capture_frame)
            Logger.info("CameraManager: 相机预览已停止")
    
    def _capture_frame(self, dt):
        """捕获当前帧"""
        if not self.is_active or not self.camera:
            return
        
        try:
            # 获取相机纹理
            texture = self.camera.texture
            if texture:
                # 转换为numpy数组
                frame = self._texture_to_numpy(texture)
                
                # 调用回调函数
                if self.preview_callback:
                    self.preview_callback(frame)
        except Exception as e:
            Logger.error(f"CameraManager: 捕获帧失败: {e}")
    
    def _texture_to_numpy(self, texture):
        """将Kivy纹理转换为numpy数组"""
        # 获取像素数据
        pixels = texture.pixels
        size = texture.size
        
        # 转换为numpy数组
        frame = np.frombuffer(pixels, dtype=np.uint8)
        frame = frame.reshape(size[1], size[0], 4)  # RGBA
        
        # 转换为RGB
        frame = frame[:, :, :3]
        
        return frame
    
    def capture_photo(self):
        """拍摄照片"""
        if not self.camera or not self.is_active:
            Logger.error("CameraManager: 无法拍照，相机未激活")
            return None
        
        try:
            texture = self.camera.texture
            if texture:
                frame = self._texture_to_numpy(texture)
                Logger.info("CameraManager: 照片拍摄成功")
                return frame
            return None
        except Exception as e:
            Logger.error(f"CameraManager: 拍照失败: {e}")
            return None
    
    def get_camera_widget(self):
        """获取相机控件"""
        return self.camera
    
    def release(self):
        """释放相机资源"""
        self.stop_preview()
        self.camera = None
        Logger.info("CameraManager: 相机资源已释放")
