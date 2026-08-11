from lupa import LuaRuntime

lua = LuaRuntime()

LUA_SCRIPT = """
function greet()
    return "Hello from Lua!"
end
"""

lua.execute(LUA_SCRIPT)
greet = lua.globals().greet

print(greet())
