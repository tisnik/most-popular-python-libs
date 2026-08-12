from lupa import LuaRuntime

lua1 = LuaRuntime()
lua2 = LuaRuntime()

with open("global_vars.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua1.execute(lua_script)
lua2.execute(lua_script)

set_x_1 = lua1.globals().set_x
get_x_1 = lua1.globals().get_x
set_x_2 = lua2.globals().set_x
get_x_2 = lua2.globals().get_x

print("orig x1:", get_x_1())
print("orig x2:", get_x_2())
set_x_1(6502)
print("new x1:", get_x_1())
print("new x2:", get_x_2())
set_x_2(8080)
print("new x1:", get_x_1())
print("new x2:", get_x_2())
