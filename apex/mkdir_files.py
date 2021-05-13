import os

if not os.path.exists("test/"):
    os.mkdir("test")

path = "test/"

for i in range(10):
    os.mkdir(path + str(i))
