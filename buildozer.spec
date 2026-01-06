[app]

title = AI Camera
package.name = aicamera
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
