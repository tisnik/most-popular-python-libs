import dis


def say_hello():
    print("Hello world")


def main():
    say_hello()


main()

print("say_hello")
dis.dis(say_hello)

print("main")
dis.dis(main)
