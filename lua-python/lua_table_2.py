from lupa import LuaRuntime

lua = LuaRuntime()

with open("table2.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua.execute(lua_script)
gen_table = lua.globals().gen_table

t = gen_table()
l = [t[i] for i in range(1, len(t) + 1)]

print(type(l))
print(l)
