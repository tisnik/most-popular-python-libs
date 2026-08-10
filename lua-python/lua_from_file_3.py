from lupa import LuaRuntime

lua = LuaRuntime()

LUA_SCRIPT = """
dofile("greet_name.lua")
"""

lua.execute(LUA_SCRIPT)
greet = lua.globals().greet

print(greet("Lua"))
