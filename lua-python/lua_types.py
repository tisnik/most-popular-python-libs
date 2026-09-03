from lupa import LuaRuntime

lua = LuaRuntime()

with open("types.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua.execute(lua_script)

get_nil = lua.globals().get_nil
get_true = lua.globals().get_true
get_false = lua.globals().get_false

n = get_nil()
print(type(n), n)

t = get_true()
print(type(t), t)

f = get_false()
print(type(f), f)
