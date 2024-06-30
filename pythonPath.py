import os

path_list = os.environ['PATH'].split(os.pathsep)
print("Python path is: ", path_list[0])