def fn5(arg1, arg2, arg3=0, *args, **kwargs):
    print("arg1 = ", arg1)
    print("arg2 = ", arg2)
    print("arg3 = ", arg3)
    print("args = ", args)
    print("kwargs = ", kwargs)


fn5(1, 2, 10, 20, 30, x=10, y=20, z="ahoj")
