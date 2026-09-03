from lupa import LuaRuntime

lua = LuaRuntime()

with open("table4.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua.execute(lua_script)
full_name = lua.globals().full_name

d = {"id": 42, "name": "John", "surname": "Doe", "address": None}
n = full_name(d)

print(n)
