#!/usr/bin/env python
# cording: Shift_JIS

import os

# before text ***********************************************
before_text = """LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

$(call import-add-path,$(LOCAL_PATH)/../../cocos2d)
$(call import-add-path,$(LOCAL_PATH)/../../cocos2d/external)
$(call import-add-path,$(LOCAL_PATH)/../../cocos2d/cocos)

LOCAL_MODULE := cocos2dcpp_shared

LOCAL_MODULE_FILENAME := libcocos2dcpp

LOCAL_SRC_FILES := hellocpp/main.cpp \\
"""
# ********************************************** before text

# after text ***********************************************
after_text = """


LOCAL_C_INCLUDES := $(LOCAL_PATH)/../../Classes

# _COCOS_HEADER_ANDROID_BEGIN
# _COCOS_HEADER_ANDROID_END


LOCAL_STATIC_LIBRARIES := cocos2dx_static

# _COCOS_LIB_ANDROID_BEGIN
# _COCOS_LIB_ANDROID_END

include $(BUILD_SHARED_LIBRARY)

$(call import-module,.)

# _COCOS_LIB_IMPORT_ANDROID_BEGIN
# _COCOS_LIB_IMPORT_ANDROID_END
"""
# ****************************************** after text

file = open('proj.android/jni/Android.mk', 'w')
file.write(before_text)

# add paths
for dir_path, dire_names, file_names in os.walk('Classes'):
    for file_name in file_names:
        root, exten = os.path.splitext(file_name)
        if exten != '.cpp':
            continue

        file_path = dir_path + '\\' + file_name
        file_full_path = os.path.abspath(file_path)

        base_path = 'proj.android\jni'
        base_full_path = os.path.abspath(base_path)

        relative_path_base2file = os.path.relpath(file_full_path, base_full_path)
        relative_path_base2file = relative_path_base2file.replace('\\', '/')

        line = relative_path_base2file + ' \\\n'
        file.write(line)


file.write(after_text)
file.close()

raw_input('finished!')