limit = 8

password = "Hello world" 

if (length := len(password)) < limit:
    print(f"Password should be longer than {length} chars")
