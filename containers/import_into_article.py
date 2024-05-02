with open("x") as fin:
    lines = fin.readlines()

for line in lines:
    line = line.strip()
    print("<pre>")
    with open(line) as fin:
        x = fin.read()
        print(x.strip())
    print("</pre>\n")
    a = f"https://github.com/tisnik/most-popular-python-libs/blob/master/containers/{line}"
    print(f"<p><div class=\"rs-tip-major\">Zdroj: <a href=\"{a}\">{a}</a></div></p>\n")
