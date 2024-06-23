# Compiled Coconut: -----------------------------------------------------------

def say_hello(about_me):  #1 (line in Coconut source)
    _coconut_case_match_to_0 = about_me  #2 (line in Coconut source)
    _coconut_case_match_check_0 = False  #2 (line in Coconut source)
    _coconut_match_set_name_name = _coconut_sentinel  #2 (line in Coconut source)
    if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.str)) and (_coconut.len(_coconut_case_match_to_0) >= 12) and (_coconut_case_match_to_0.startswith("My name is ")) and (_coconut_case_match_to_0.endswith(".")):  #2 (line in Coconut source)
        _coconut_match_temp_0 = _coconut_case_match_to_0[11:-1]  #2 (line in Coconut source)
        _coconut_match_set_name_name = _coconut_match_temp_0  #2 (line in Coconut source)
        _coconut_case_match_check_0 = True  #2 (line in Coconut source)
    if _coconut_case_match_check_0:  #2 (line in Coconut source)
        if _coconut_match_set_name_name is not _coconut_sentinel:  #2 (line in Coconut source)
            name = _coconut_match_set_name_name  #2 (line in Coconut source)
    if _coconut_case_match_check_0:  #2 (line in Coconut source)
        print("Hello {_coconut_format_0}!".format(_coconut_format_0=(name)))  #4 (line in Coconut source)



say_hello("My name is Marvin.")  #7 (line in Coconut source)
