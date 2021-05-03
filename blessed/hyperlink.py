import blessed

terminal = blessed.Terminal()

print(f"Odkaz: {terminal.link('https://www.root.cz', 'Stránky Root.cz')}")
