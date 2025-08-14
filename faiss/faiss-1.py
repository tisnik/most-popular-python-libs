# Knihovna FAISS
#
# - konstrukce dvou vektorů se souřadnicemi bodů v rovině
# - výpis obsahu obou vektorů na standardní výstup
# - konstrukce seznamu souřadnic vytvořených z obou vektorů

# x-ove souradnice bodu v rovine
x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

# y-ove souradnice bodu v rovine
y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

# vypis obsahu obou vektoru
print(x)
print(y)

# konstrukce seznamu souradnic
print(list(zip(x, y)))
