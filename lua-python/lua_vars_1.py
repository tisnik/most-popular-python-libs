from lupa import LuaRuntime

lua = LuaRuntime()

with open("global_vars.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua.execute(lua_script)

set_x = lua.globals().set_x
get_x = lua.globals().get_x

print("orig:", get_x())
set_x(-1)
print("new:", get_x())
