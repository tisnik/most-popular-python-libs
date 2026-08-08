from lupa import LuaRuntime

lua = LuaRuntime()

with open("greet.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua.execute(lua_script)
greet = lua.globals().greet

print(greet())
