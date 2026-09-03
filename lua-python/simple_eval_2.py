from lupa import LuaRuntime

lua = LuaRuntime()

LUA_SCRIPT = """
'foo' .. 'bar'
"""

print(LUA_SCRIPT)
print(lua.eval(LUA_SCRIPT))
