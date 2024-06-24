# Compiled Coconut: -----------------------------------------------------------

def foo(lst=[]):  #1 (line in Coconut source)
    lst.append("*")  #2 (line in Coconut source)
    return lst  #3 (line in Coconut source)


@_coconut_mark_as_match  #5 (line in Coconut source)
def bar(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #5 (line in Coconut source)
    _coconut_match_check_0 = False  #5 (line in Coconut source)
    _coconut_match_set_name_lst = _coconut_sentinel  #5 (line in Coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #5 (line in Coconut source)
    if _coconut_match_first_arg is not _coconut_sentinel:  #5 (line in Coconut source)
        _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #5 (line in Coconut source)
    if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "lst" in _coconut_match_kwargs)) <= 1):  #5 (line in Coconut source)
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("lst") if "lst" in _coconut_match_kwargs else _coconut_sentinel  #5 (line in Coconut source)
        if _coconut_match_temp_0 is _coconut_sentinel:  #5 (line in Coconut source)
            _coconut_match_temp_1 = _coconut.globals().copy()  #5 (line in Coconut source)
            _coconut_match_temp_1.update(_coconut.locals())  #5 (line in Coconut source)
            _coconut_exec('_coconut_match_temp_0 = []', _coconut_match_temp_1)  #5 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_temp_1["_coconut_match_temp_0"]  #5 (line in Coconut source)
        _coconut_match_set_name_lst = _coconut_match_temp_0  #5 (line in Coconut source)
        if not _coconut_match_kwargs:  #5 (line in Coconut source)
            _coconut_match_check_0 = True  #5 (line in Coconut source)
    if _coconut_match_check_0:  #5 (line in Coconut source)
        if _coconut_match_set_name_lst is not _coconut_sentinel:  #5 (line in Coconut source)
            lst = _coconut_match_set_name_lst  #5 (line in Coconut source)
    if not _coconut_match_check_0:  #5 (line in Coconut source)
        raise _coconut_FunctionMatchError('match def bar(lst = []):', _coconut_match_args)  #5 (line in Coconut source)

    lst.append("*")  #6 (line in Coconut source)
    return lst  #7 (line in Coconut source)



print("foo#1", foo())  #10 (line in Coconut source)
print("foo#2", foo())  #11 (line in Coconut source)
print("foo#3", foo())  #12 (line in Coconut source)

print("bar#1", bar())  #14 (line in Coconut source)
print("bar#2", bar())  #15 (line in Coconut source)
print("bar#3", bar())  #16 (line in Coconut source)
