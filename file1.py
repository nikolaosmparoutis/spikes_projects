import sys, os
# jenkins exposes the workspace directory through env. with this code can do import
sys.path.append(os.environ['WORKSPACE'])

def compare(a, b):
    if a == b:
        print("are equal")
        return True
    if a == 0:
        print("a = 0")
        return True
    print("a non zero and  dif than b")
    return


compare(2,3)



a=2
b=3
if a == b:
    print("are equal")
    f=True
if a == 0:
    print("a = 0")
    print("a non zero and  dif than b")
    f=False







