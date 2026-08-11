from lupa import LuaRuntime

lua = LuaRuntime()

LUA_SCRIPT = """
function greet(name)
    return "Hello from " .. name .. "!"
end
"""

lua.execute(LUA_SCRIPT)
greet = lua.globals().greet

print(greet("Lua"))
