# -*- coding: utf-8 -*-
from operator import truediv
import subprocess
import re

cmd = ["node", "script/t2.js"]
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

try:
    out, errs = proc.communicate(timeout=15)
except subprocess.TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()

outStr = out.decode('gbk')
print(outStr)

oldUrl, newUrlPart = outStr.split("\n")[0], outStr.split("\n")[1]

newUrl = "![image-20220202234522365]({})".format(newUrlPart)

# print(oldUrl)
# print(newUrl)
# data1 = json.loads(outStr)
with open(r"source\_posts\t1.md", "r", encoding='utf8') as f:
    content = f.read()
    content = content.replace(oldUrl, newUrl)
    print(content)

with open(r"source\_posts\t1_out.md", "w", encoding='utf8') as f:
    f.write(content)
