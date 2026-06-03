def bar(arg = None):
    if arg is None:
       print("No value provided!")
    else:
       print("Value provided", arg)


bar(42)
bar(None)
bar()
