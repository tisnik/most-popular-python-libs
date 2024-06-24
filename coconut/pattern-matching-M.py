# Compiled Coconut: -----------------------------------------------------------

def list_type(value):  #1 (line in Coconut source)
    _coconut_case_match_to_0 = value  #2 (line in Coconut source)
    _coconut_case_match_check_0 = False  #2 (line in Coconut source)
    _coconut_match_set_name_x = _coconut_sentinel  #2 (line in Coconut source)
    if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) >= 3) and (_coconut_case_match_to_0[0] == 1) and (_coconut_case_match_to_0[1] == 2) and (_coconut_case_match_to_0[2] == 3):  #2 (line in Coconut source)
        _coconut_match_temp_0 = _coconut.list(_coconut_case_match_to_0[3:])  #2 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_match_temp_0  #2 (line in Coconut source)
        _coconut_case_match_check_0 = True  #2 (line in Coconut source)
    if _coconut_case_match_check_0:  #2 (line in Coconut source)
        if _coconut_match_set_name_x is not _coconut_sentinel:  #2 (line in Coconut source)
            x = _coconut_match_set_name_x  #2 (line in Coconut source)
    if _coconut_case_match_check_0:  #2 (line in Coconut source)
        print("List starting with expected head, followed by item(s) = {_coconut_format_0}".format(_coconut_format_0=(x)))  #4 (line in Coconut source)
    if not _coconut_case_match_check_0:  #5 (line in Coconut source)
        print("Unexpected value {_coconut_format_0}".format(_coconut_format_0=(value)))  #6 (line in Coconut source)



(list_type)([])  #9 (line in Coconut source)
(list_type)([1,])  #10 (line in Coconut source)
(list_type)([1, 2])  #11 (line in Coconut source)
(list_type)([1, 2, 3])  #12 (line in Coconut source)
(list_type)([1, 2, 3, 4])  #13 (line in Coconut source)
(list_type)([1, 2, 3, 4, 5])  #14 (line in Coconut source)
(list_type)([2, 2, 3, 4, 5])  #15 (line in Coconut source)
