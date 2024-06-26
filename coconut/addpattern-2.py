# Compiled Coconut: -----------------------------------------------------------

try:  #1 (line in Coconut source)
    _coconut_addpattern_0 = _coconut_addpattern(factorial)  # type: ignore  #1 (line in Coconut source)
except _coconut.NameError:  #1 (line in Coconut source)
    _coconut_addpattern_0 = lambda f: f  #1 (line in Coconut source)
@_coconut_addpattern_0  #1 (line in Coconut source)
@_coconut_mark_as_match  #1 (line in Coconut source)
def factorial(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #1 (line in Coconut source)
    _coconut_match_check_0 = False  #1 (line in Coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1 (line in Coconut source)
    if _coconut_match_first_arg is not _coconut_sentinel:  #1 (line in Coconut source)
        _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #1 (line in Coconut source)
    if _coconut.len(_coconut_match_args) == 1:  #1 (line in Coconut source)
        if _coconut_match_args[0] == 0:  #1 (line in Coconut source)
            if not _coconut_match_kwargs:  #1 (line in Coconut source)
                _coconut_match_check_0 = True  #1 (line in Coconut source)
    if not _coconut_match_check_0:  #1 (line in Coconut source)
        raise _coconut_FunctionMatchError('addpattern def factorial(0) = 1', _coconut_match_args)  #1 (line in Coconut source)

    return 1  #1 (line in Coconut source)

try:  #2 (line in Coconut source)
    _coconut_addpattern_1 = _coconut_addpattern(factorial)  # type: ignore  #2 (line in Coconut source)
except _coconut.NameError:  #2 (line in Coconut source)
    _coconut_addpattern_1 = lambda f: f  #2 (line in Coconut source)
@_coconut_addpattern_1  #2 (line in Coconut source)
@_coconut_mark_as_match  #2 (line in Coconut source)
def factorial(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #2 (line in Coconut source)
    _coconut_match_check_1 = False  #2 (line in Coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #2 (line in Coconut source)
    if _coconut_match_first_arg is not _coconut_sentinel:  #2 (line in Coconut source)
        _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #2 (line in Coconut source)
    if _coconut.len(_coconut_match_args) == 1:  #2 (line in Coconut source)
        if _coconut_match_args[0] == 1:  #2 (line in Coconut source)
            if not _coconut_match_kwargs:  #2 (line in Coconut source)
                _coconut_match_check_1 = True  #2 (line in Coconut source)
    if not _coconut_match_check_1:  #2 (line in Coconut source)
        raise _coconut_FunctionMatchError('addpattern def factorial(1) = 1', _coconut_match_args)  #2 (line in Coconut source)

    return 1  #2 (line in Coconut source)

try:  #3 (line in Coconut source)
    _coconut_addpattern_2 = _coconut_addpattern(factorial)  # type: ignore  #3 (line in Coconut source)
except _coconut.NameError:  #3 (line in Coconut source)
    _coconut_addpattern_2 = lambda f: f  #3 (line in Coconut source)
@_coconut_addpattern_2  #3 (line in Coconut source)
@_coconut_mark_as_match  #3 (line in Coconut source)
def factorial(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #3 (line in Coconut source)
    _coconut_match_check_2 = False  #3 (line in Coconut source)
    _coconut_match_set_name_n = _coconut_sentinel  #3 (line in Coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #3 (line in Coconut source)
    if _coconut_match_first_arg is not _coconut_sentinel:  #3 (line in Coconut source)
        _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #3 (line in Coconut source)
    if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "n" in _coconut_match_kwargs)) == 1):  #3 (line in Coconut source)
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("n")  #3 (line in Coconut source)
        _coconut_match_set_name_n = _coconut_match_temp_0  #3 (line in Coconut source)
        if not _coconut_match_kwargs:  #3 (line in Coconut source)
            _coconut_match_check_2 = True  #3 (line in Coconut source)
    if _coconut_match_check_2:  #3 (line in Coconut source)
        if _coconut_match_set_name_n is not _coconut_sentinel:  #3 (line in Coconut source)
            n = _coconut_match_set_name_n  #3 (line in Coconut source)
    if _coconut_match_check_2 and not (n > 1):  #3 (line in Coconut source)
        _coconut_match_check_2 = False  #3 (line in Coconut source)
    if not _coconut_match_check_2:  #3 (line in Coconut source)
        raise _coconut_FunctionMatchError('addpattern def factorial(n if n>1) = n * factorial(n - 1)', _coconut_match_args)  #3 (line in Coconut source)

    return n * factorial(n - 1)  #3 (line in Coconut source)


for n in range(11):  #5 (line in Coconut source)
    print("{n}!={f}".format(n=n, f=factorial(n)))  #6 (line in Coconut source)

print(factorial(-1))  #8 (line in Coconut source)
