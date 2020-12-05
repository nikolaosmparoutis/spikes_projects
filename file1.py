import sys
import os
# jenkins exposes the workspace directory through env. with this code can do import
sys.path.append(os.environ['WORKSPACE'])

def func(a,b):
    if a == b:
        print("are equal")
        return True
    return False