from lupa import LuaRuntime

lua = LuaRuntime()

with open("numbers.lua", "r", encoding="utf-8") as fin:
    lua_script = fin.read()

lua.execute(lua_script)

reset_counter = lua.globals().reset_counter
gen_int = lua.globals().gen_int
gen_double = lua.globals().gen_double

reset_counter()
for _ in range(10):
    i = gen_int()
    print(type(i), i)

print()

reset_counter()
for _ in range(10):
    f = gen_double()
    print(type(f), f)
