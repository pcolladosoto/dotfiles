import builtins

def print(*args, **kwargs):
    builtins.print(*args, **kwargs, end = " :)\n")

if __name__ == "__main__":
    print("Foo")
