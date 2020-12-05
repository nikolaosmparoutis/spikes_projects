# jenkins exposes the workspace directory through env. with this code can do import
# sys.path.append(os.environ['WORKSPACE'])

def func(a, b):
    if a == b:
        print("are equal")
        return True
    if a == 0:
        print("a = 0")
        return True
    print("a non zero and  dif than b")
    return False

