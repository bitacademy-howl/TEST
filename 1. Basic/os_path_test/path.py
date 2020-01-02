# -*- coding : utf-8 -*-
import os

# 파일명과 폴더명은 동일할 수 없다....
# 아래는 data 라는 파일이 있을 경우 폴더에 관한 처리를 어떻게 할 것인가 Test

print("###############################################################################################################")
data_folder = "./data"

if not os.path.exists(data_folder):
    os.mkdir(data_folder)
if os.path.exists(data_folder):
    if os.path.isdir(data_folder):
        os.chdir(data_folder)
        print(os.getcwd())
    else:
        print(os.getcwd())
print("###############################################################################################################")
data_folder = "./ex"

if not os.path.exists(data_folder):
    os.mkdir(data_folder)
if os.path.exists(data_folder):
    if os.path.isdir(data_folder):
        os.chdir(data_folder)
        print(os.getcwd())
    else:
        print(os.getcwd())
print("###############################################################################################################")