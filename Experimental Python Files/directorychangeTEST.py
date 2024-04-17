import os
import shutil

print('hellooo')

file = os.listdir()[1]
print(file)
os.chdir(os.path.dirname(os.getcwd()))
target = os.getcwd()
os.mkdir("data")
os.chdir("Experimental Python Files")
print(os.getcwd())
# target=os.getcwd()
print(target)
# os.chdir(os.path.abspath(file))
# print(os.getcwd())
# file = os.path.abspath(file)

shutil.copy(file, dst=target+"/data")



