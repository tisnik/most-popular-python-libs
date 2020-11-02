from pygame.colordict import THECOLORS

for i, color in enumerate(sorted(THECOLORS)):
    if i % 5 == 0:
        print("<tr>", end="")
    print("<td>" + color + "</td>", end="")
    if i % 5 == 4:
        print("</tr>")
