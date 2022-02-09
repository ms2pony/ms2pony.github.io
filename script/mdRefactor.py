"""
改图片名改图片路径
"""
from hashlib import new
import json
import sys
import os

# 读取json字符串并解码成python对象
sys.stdin.reconfigure(encoding='utf-8')
jsonStr = sys.stdin.read()
jsonItems = json.loads(jsonStr)


# 更换图片代码的路径
newImgPaths = []
for item in jsonItems:
    imgPath = item["href"]
    imgName = os.path.split(imgPath)[1]
    newImgPath = os.path.join(
        r"https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/", imgName)
    newImgPaths.append(newImgPath)
# 更换图片代码的图片名称
newImgNames = []
i = ord('a')
j = ord('a')
for path in newImgPaths:
    newImgName = os.path.split(path)[1]
    newImgName = "windows-"+chr(j)+chr(i)+os.path.splitext(newImgName)[1]
    i += 1
    if i > ord('z'):
        i = ord('a')
        j += 1
    newImgNames.append(newImgName)

newImgCodes = []
for name, path in zip(newImgNames, newImgPaths):
    newImgCode = "![{}]({})".format(name, path)
    newImgCodes.append(newImgCode)

print(newImgCodes)
print(jsonItems)

with open(r"C:\Users\tam\OneDrive\Documents\GitHub\blog\source\_posts\windows.md", "r", encoding="utf8") as f:
    content = f.read()
    for oldLink, newLink in zip(jsonItems, newImgCodes):
        content = content.replace(oldLink["raw"], newLink)

with open(r"C:\Users\tam\OneDrive\Documents\GitHub\blog\source\_posts\windows.md", "w", encoding="utf8") as f:
    f.write(content)
