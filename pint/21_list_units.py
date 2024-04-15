from pint import UnitRegistry

ureg = UnitRegistry()

print("<tr>", end="")

c = 0
for item in dir(ureg):
    if item[0] != "_":
        print(f"<td>{item}</td>", end="")
        c += 1
        if c == 6:
            print("</tr>\n<tr>", end="")
            c=0
