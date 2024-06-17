# Compiled Coconut: -----------------------------------------------------------

def factorial_variant_A(n):  #1 (line in Coconut source)
    _coconut_case_match_to_0 = n  #2 (line in Coconut source)
    _coconut_case_match_check_0 = False  #2 (line in Coconut source)
    if _coconut_case_match_to_0 == 0:  #2 (line in Coconut source)
        _coconut_case_match_check_0 = True  #2 (line in Coconut source)
    if _coconut_case_match_check_0:  #2 (line in Coconut source)
        return 1  #4 (line in Coconut source)
    if not _coconut_case_match_check_0:  #5 (line in Coconut source)
        if _coconut_case_match_to_0 == 1:  #5 (line in Coconut source)
            _coconut_case_match_check_0 = True  #5 (line in Coconut source)
        if _coconut_case_match_check_0:  #5 (line in Coconut source)
            return 1  #6 (line in Coconut source)
    if not _coconut_case_match_check_0:  #7 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #7 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_case_match_to_0  #7 (line in Coconut source)
        _coconut_case_match_check_0 = True  #7 (line in Coconut source)
        if _coconut_case_match_check_0:  #7 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #7 (line in Coconut source)
                x = _coconut_match_set_name_x  #7 (line in Coconut source)
        if _coconut_case_match_check_0:  #7 (line in Coconut source)
            return x * factorial_variant_A(x - 1)  #8 (line in Coconut source)



for n in range(11):  #11 (line in Coconut source)
    print("{n}!={f}".format(n=n, f=factorial_variant_A(n)))  #12 (line in Coconut source)
