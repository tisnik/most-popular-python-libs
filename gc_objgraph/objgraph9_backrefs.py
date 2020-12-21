import objgraph

x = {}
y = {}

objgraph.show_backrefs(globals(), filename='objgraph9_backrefs.png')
