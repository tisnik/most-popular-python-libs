from lupa import LuaRuntime

lua = LuaRuntime()

with open("table1.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua.execute(lua_script)
sum = lua.globals().sum

l = [1, 2, 3, 4]
t = lua.table_from(l)

print(sum(t))
