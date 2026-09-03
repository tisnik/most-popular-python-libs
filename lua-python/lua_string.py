from lupa import LuaRuntime

lua = LuaRuntime()

with open("strings.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua.execute(lua_script)

set_filler = lua.globals().set_filler("*")
gen_string = lua.globals().gen_string

for _ in range(10):
    s = gen_string()
    print(type(s), s)

set_filler = lua.globals().set_filler("ΔěščΔ")

for _ in range(10):
    s = gen_string()
    print(type(s), s)

