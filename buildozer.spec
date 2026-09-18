[app]
title = Mert AI
package.name = mertai
package.domain = org.mert.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
api = 33
minapi = 24
ndk = 25b
android.ndk = 25b
android.archs = arm64-v8a
