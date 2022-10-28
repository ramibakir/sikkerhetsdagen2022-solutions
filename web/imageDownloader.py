import hashlib
import subprocess

f = open("md5hash.txt", "r+")

for i in range(0, 39):
    num = str(i)
    f.write((hashlib.md5(num.encode())).hexdigest() + "\n")

base = "http://ctf.uiactf.no:3003/"
ext = ".jpg"
hash = f.readlines()
url = ""
f.close()

for line in hash:
    line.rstrip()
    url = base + line.strip() + ext
    print(subprocess.run(["wget", url]))
