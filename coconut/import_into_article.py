with open("y") as fin:
    lines = fin.readlines()

for line in lines:
    line = line.strip()
    if line == "":
        continue
    print("<h3>" + line + "</h3>\n")
    print("<pre>")
    with open(line, "r") as fin:
        for x in fin:
            x = x.rstrip()
            x = x.replace("&", "&amp;")
            x = x.replace("<", "&lt;")
            x = x.replace(">", "&gt;")
            if x == "":
                x = "&nbsp;"
            print(x)
    print("</pre>\n\n")
