from lupa import LuaRuntime

lua = LuaRuntime()

LUA_SCRIPT = "6 * 7"

print(lua.eval(LUA_SCRIPT))
