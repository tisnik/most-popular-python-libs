def bar(arg = ...):
    if arg is ...:
       print("No value provided!")
    else:
       print("Value provided", arg)


bar(42)
bar(Ellipsis)
bar(...)
bar()
