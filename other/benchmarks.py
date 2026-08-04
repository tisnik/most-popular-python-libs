import matplotlib.pyplot as plt


tools = ["Mypy", "Pyright", "ty"]
times = [18.8, 32.46, 3.96]

plt.xlabel("Tool")
plt.ylabel("Time (sec)")
plt.bar(tools, times)

# přidání legendy
plt.legend(loc="upper left")

# povolení zobrazení mřížky
#plt.grid(True)

plt.savefig("benchmark.png")

# zobrazení grafu
plt.show()
