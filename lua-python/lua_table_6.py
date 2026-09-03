from lupa import LuaRuntime

lua = LuaRuntime()

with open("table6.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua.execute(lua_script)
gen_table = lua.globals().gen_table

t = gen_table()
d = dict(t)

print(type(d))
print(d)
