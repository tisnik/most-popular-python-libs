# Compiled Coconut: -----------------------------------------------------------

def complex_number(value):  #1 (line in Coconut source)
    """Test, o jakou variantu komplexního čísla se jedná."""  #2 (line in Coconut source)
    _coconut_case_match_to_0 = value  #3 (line in Coconut source)
    _coconut_case_match_check_0 = False  #3 (line in Coconut source)
    if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == 0) and (_coconut_case_match_to_0[1] == 0):  #3 (line in Coconut source)
        _coconut_case_match_check_0 = True  #3 (line in Coconut source)
    if _coconut_case_match_check_0:  #3 (line in Coconut source)
        print("Zero")  #5 (line in Coconut source)
    if not _coconut_case_match_check_0:  #6 (line in Coconut source)
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[1] == 0):  #6 (line in Coconut source)
            _coconut_match_temp_0 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #6 (line in Coconut source)
            _coconut_case_match_check_0 = True  #6 (line in Coconut source)
        if _coconut_case_match_check_0:  #6 (line in Coconut source)
            _coconut_case_match_check_0 = False  #6 (line in Coconut source)
            if not _coconut_case_match_check_0:  #6 (line in Coconut source)
                _coconut_match_set_name_real = _coconut_sentinel  #6 (line in Coconut source)
                if (_coconut_match_temp_0) and (_coconut.isinstance(_coconut_case_match_to_0[0], int)) and (_coconut.len(_coconut_case_match_to_0[0]) >= 1):  #6 (line in Coconut source)
                    _coconut_match_set_name_real = _coconut_case_match_to_0[0][0]  #6 (line in Coconut source)
                    _coconut_match_temp_1 = _coconut.len(_coconut_case_match_to_0[0]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_0[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_0[0][i] == _coconut.getattr(_coconut_case_match_to_0[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_0[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0[0], "__match_args__") else _coconut.len(_coconut_case_match_to_0[0]) == 1  # type: ignore  #6 (line in Coconut source)
                    if _coconut_match_temp_1:  #6 (line in Coconut source)
                        _coconut_case_match_check_0 = True  #6 (line in Coconut source)
                if _coconut_case_match_check_0:  #6 (line in Coconut source)
                    if _coconut_match_set_name_real is not _coconut_sentinel:  #6 (line in Coconut source)
                        real = _coconut_match_set_name_real  #6 (line in Coconut source)

            if not _coconut_case_match_check_0:  #6 (line in Coconut source)
                if (not _coconut_match_temp_0) and (_coconut.isinstance(_coconut_case_match_to_0[0], int)):  #6 (line in Coconut source)
                    _coconut_case_match_check_0 = True  #6 (line in Coconut source)
                if _coconut_case_match_check_0:  #6 (line in Coconut source)
                    _coconut_case_match_check_0 = False  #6 (line in Coconut source)
                    if not _coconut_case_match_check_0:  #6 (line in Coconut source)
                        _coconut_match_set_name_real = _coconut_sentinel  #6 (line in Coconut source)
                        if _coconut.type(_coconut_case_match_to_0[0]) in _coconut_self_match_types:  #6 (line in Coconut source)
                            _coconut_match_set_name_real = _coconut_case_match_to_0[0]  #6 (line in Coconut source)
                            _coconut_case_match_check_0 = True  #6 (line in Coconut source)
                        if _coconut_case_match_check_0:  #6 (line in Coconut source)
                            if _coconut_match_set_name_real is not _coconut_sentinel:  #6 (line in Coconut source)
                                real = _coconut_match_set_name_real  #6 (line in Coconut source)

                    if not _coconut_case_match_check_0:  #6 (line in Coconut source)
                        _coconut_match_set_name_real = _coconut_sentinel  #6 (line in Coconut source)
                        if not _coconut.type(_coconut_case_match_to_0[0]) in _coconut_self_match_types:  #6 (line in Coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #6 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #6 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #6 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 1:  #6 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #6 (line in Coconut source)
                            _coconut_match_temp_3 = _coconut.getattr(_coconut_case_match_to_0[0], _coconut_match_temp_2[0], _coconut_sentinel)  #6 (line in Coconut source)
                            if _coconut_match_temp_3 is not _coconut_sentinel:  #6 (line in Coconut source)
                                _coconut_match_set_name_real = _coconut_match_temp_3  #6 (line in Coconut source)
                                _coconut_case_match_check_0 = True  #6 (line in Coconut source)
                        if _coconut_case_match_check_0:  #6 (line in Coconut source)
                            if _coconut_match_set_name_real is not _coconut_sentinel:  #6 (line in Coconut source)
                                real = _coconut_match_set_name_real  #6 (line in Coconut source)




        if _coconut_case_match_check_0:  #6 (line in Coconut source)
            print("Real number {_coconut_format_0}".format(_coconut_format_0=(real)))  #7 (line in Coconut source)
    if not _coconut_case_match_check_0:  #8 (line in Coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #8 (line in Coconut source)
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[1] == 0):  #8 (line in Coconut source)
            _coconut_match_set_name_real = _coconut_case_match_to_0[0]  #8 (line in Coconut source)
            _coconut_case_match_check_0 = True  #8 (line in Coconut source)
        if _coconut_case_match_check_0:  #8 (line in Coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #8 (line in Coconut source)
                real = _coconut_match_set_name_real  #8 (line in Coconut source)
        if _coconut_case_match_check_0:  #8 (line in Coconut source)
            print("Strange real number {_coconut_format_0}, value is not integer".format(_coconut_format_0=(real)))  #9 (line in Coconut source)
    if not _coconut_case_match_check_0:  #10 (line in Coconut source)
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == 0):  #10 (line in Coconut source)
            _coconut_match_temp_4 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #10 (line in Coconut source)
            _coconut_case_match_check_0 = True  #10 (line in Coconut source)
        if _coconut_case_match_check_0:  #10 (line in Coconut source)
            _coconut_case_match_check_0 = False  #10 (line in Coconut source)
            if not _coconut_case_match_check_0:  #10 (line in Coconut source)
                _coconut_match_set_name_imag = _coconut_sentinel  #10 (line in Coconut source)
                if (_coconut_match_temp_4) and (_coconut.isinstance(_coconut_case_match_to_0[1], int)) and (_coconut.len(_coconut_case_match_to_0[1]) >= 1):  #10 (line in Coconut source)
                    _coconut_match_set_name_imag = _coconut_case_match_to_0[1][0]  #10 (line in Coconut source)
                    _coconut_match_temp_5 = _coconut.len(_coconut_case_match_to_0[1]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_0[1].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0[1], "_coconut_data_defaults", {}) and _coconut_case_match_to_0[1][i] == _coconut.getattr(_coconut_case_match_to_0[1], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_0[1].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0[1], "__match_args__") else _coconut.len(_coconut_case_match_to_0[1]) == 1  # type: ignore  #10 (line in Coconut source)
                    if _coconut_match_temp_5:  #10 (line in Coconut source)
                        _coconut_case_match_check_0 = True  #10 (line in Coconut source)
                if _coconut_case_match_check_0:  #10 (line in Coconut source)
                    if _coconut_match_set_name_imag is not _coconut_sentinel:  #10 (line in Coconut source)
                        imag = _coconut_match_set_name_imag  #10 (line in Coconut source)

            if not _coconut_case_match_check_0:  #10 (line in Coconut source)
                if (not _coconut_match_temp_4) and (_coconut.isinstance(_coconut_case_match_to_0[1], int)):  #10 (line in Coconut source)
                    _coconut_case_match_check_0 = True  #10 (line in Coconut source)
                if _coconut_case_match_check_0:  #10 (line in Coconut source)
                    _coconut_case_match_check_0 = False  #10 (line in Coconut source)
                    if not _coconut_case_match_check_0:  #10 (line in Coconut source)
                        _coconut_match_set_name_imag = _coconut_sentinel  #10 (line in Coconut source)
                        if _coconut.type(_coconut_case_match_to_0[1]) in _coconut_self_match_types:  #10 (line in Coconut source)
                            _coconut_match_set_name_imag = _coconut_case_match_to_0[1]  #10 (line in Coconut source)
                            _coconut_case_match_check_0 = True  #10 (line in Coconut source)
                        if _coconut_case_match_check_0:  #10 (line in Coconut source)
                            if _coconut_match_set_name_imag is not _coconut_sentinel:  #10 (line in Coconut source)
                                imag = _coconut_match_set_name_imag  #10 (line in Coconut source)

                    if not _coconut_case_match_check_0:  #10 (line in Coconut source)
                        _coconut_match_set_name_imag = _coconut_sentinel  #10 (line in Coconut source)
                        if not _coconut.type(_coconut_case_match_to_0[1]) in _coconut_self_match_types:  #10 (line in Coconut source)
                            _coconut_match_temp_6 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #10 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_6, _coconut.tuple):  #10 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #10 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_6) < 1:  #10 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_6),))  #10 (line in Coconut source)
                            _coconut_match_temp_7 = _coconut.getattr(_coconut_case_match_to_0[1], _coconut_match_temp_6[0], _coconut_sentinel)  #10 (line in Coconut source)
                            if _coconut_match_temp_7 is not _coconut_sentinel:  #10 (line in Coconut source)
                                _coconut_match_set_name_imag = _coconut_match_temp_7  #10 (line in Coconut source)
                                _coconut_case_match_check_0 = True  #10 (line in Coconut source)
                        if _coconut_case_match_check_0:  #10 (line in Coconut source)
                            if _coconut_match_set_name_imag is not _coconut_sentinel:  #10 (line in Coconut source)
                                imag = _coconut_match_set_name_imag  #10 (line in Coconut source)




        if _coconut_case_match_check_0:  #10 (line in Coconut source)
            print("Imaginary number {_coconut_format_0}".format(_coconut_format_0=(imag)))  #11 (line in Coconut source)
    if not _coconut_case_match_check_0:  #12 (line in Coconut source)
        _coconut_match_set_name_imag = _coconut_sentinel  #12 (line in Coconut source)
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == 0):  #12 (line in Coconut source)
            _coconut_match_set_name_imag = _coconut_case_match_to_0[1]  #12 (line in Coconut source)
            _coconut_case_match_check_0 = True  #12 (line in Coconut source)
        if _coconut_case_match_check_0:  #12 (line in Coconut source)
            if _coconut_match_set_name_imag is not _coconut_sentinel:  #12 (line in Coconut source)
                imag = _coconut_match_set_name_imag  #12 (line in Coconut source)
        if _coconut_case_match_check_0:  #12 (line in Coconut source)
            print("Strange imaginary number {_coconut_format_0}, value is not integer".format(_coconut_format_0=(imag)))  #13 (line in Coconut source)
    if not _coconut_case_match_check_0:  #14 (line in Coconut source)
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2):  #14 (line in Coconut source)
            _coconut_match_temp_8 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #14 (line in Coconut source)
            _coconut_match_temp_12 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #14 (line in Coconut source)
            _coconut_case_match_check_0 = True  #14 (line in Coconut source)
        if _coconut_case_match_check_0:  #14 (line in Coconut source)
            _coconut_case_match_check_0 = False  #14 (line in Coconut source)
            if not _coconut_case_match_check_0:  #14 (line in Coconut source)
                _coconut_match_set_name_real = _coconut_sentinel  #14 (line in Coconut source)
                if (_coconut_match_temp_8) and (_coconut.isinstance(_coconut_case_match_to_0[0], int)) and (_coconut.len(_coconut_case_match_to_0[0]) >= 1):  #14 (line in Coconut source)
                    _coconut_match_set_name_real = _coconut_case_match_to_0[0][0]  #14 (line in Coconut source)
                    _coconut_match_temp_9 = _coconut.len(_coconut_case_match_to_0[0]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_0[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_0[0][i] == _coconut.getattr(_coconut_case_match_to_0[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_0[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0[0], "__match_args__") else _coconut.len(_coconut_case_match_to_0[0]) == 1  # type: ignore  #14 (line in Coconut source)
                    if _coconut_match_temp_9:  #14 (line in Coconut source)
                        _coconut_case_match_check_0 = True  #14 (line in Coconut source)
                if _coconut_case_match_check_0:  #14 (line in Coconut source)
                    if _coconut_match_set_name_real is not _coconut_sentinel:  #14 (line in Coconut source)
                        real = _coconut_match_set_name_real  #14 (line in Coconut source)

            if not _coconut_case_match_check_0:  #14 (line in Coconut source)
                if (not _coconut_match_temp_8) and (_coconut.isinstance(_coconut_case_match_to_0[0], int)):  #14 (line in Coconut source)
                    _coconut_case_match_check_0 = True  #14 (line in Coconut source)
                if _coconut_case_match_check_0:  #14 (line in Coconut source)
                    _coconut_case_match_check_0 = False  #14 (line in Coconut source)
                    if not _coconut_case_match_check_0:  #14 (line in Coconut source)
                        _coconut_match_set_name_real = _coconut_sentinel  #14 (line in Coconut source)
                        if _coconut.type(_coconut_case_match_to_0[0]) in _coconut_self_match_types:  #14 (line in Coconut source)
                            _coconut_match_set_name_real = _coconut_case_match_to_0[0]  #14 (line in Coconut source)
                            _coconut_case_match_check_0 = True  #14 (line in Coconut source)
                        if _coconut_case_match_check_0:  #14 (line in Coconut source)
                            if _coconut_match_set_name_real is not _coconut_sentinel:  #14 (line in Coconut source)
                                real = _coconut_match_set_name_real  #14 (line in Coconut source)

                    if not _coconut_case_match_check_0:  #14 (line in Coconut source)
                        _coconut_match_set_name_real = _coconut_sentinel  #14 (line in Coconut source)
                        if not _coconut.type(_coconut_case_match_to_0[0]) in _coconut_self_match_types:  #14 (line in Coconut source)
                            _coconut_match_temp_10 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #14 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_10, _coconut.tuple):  #14 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #14 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_10) < 1:  #14 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_10),))  #14 (line in Coconut source)
                            _coconut_match_temp_11 = _coconut.getattr(_coconut_case_match_to_0[0], _coconut_match_temp_10[0], _coconut_sentinel)  #14 (line in Coconut source)
                            if _coconut_match_temp_11 is not _coconut_sentinel:  #14 (line in Coconut source)
                                _coconut_match_set_name_real = _coconut_match_temp_11  #14 (line in Coconut source)
                                _coconut_case_match_check_0 = True  #14 (line in Coconut source)
                        if _coconut_case_match_check_0:  #14 (line in Coconut source)
                            if _coconut_match_set_name_real is not _coconut_sentinel:  #14 (line in Coconut source)
                                real = _coconut_match_set_name_real  #14 (line in Coconut source)




        if _coconut_case_match_check_0:  #14 (line in Coconut source)
            _coconut_case_match_check_0 = False  #14 (line in Coconut source)
            if not _coconut_case_match_check_0:  #14 (line in Coconut source)
                _coconut_match_set_name_imag = _coconut_sentinel  #14 (line in Coconut source)
                if (_coconut_match_temp_12) and (_coconut.isinstance(_coconut_case_match_to_0[1], int)) and (_coconut.len(_coconut_case_match_to_0[1]) >= 1):  #14 (line in Coconut source)
                    _coconut_match_set_name_imag = _coconut_case_match_to_0[1][0]  #14 (line in Coconut source)
                    _coconut_match_temp_13 = _coconut.len(_coconut_case_match_to_0[1]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_0[1].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0[1], "_coconut_data_defaults", {}) and _coconut_case_match_to_0[1][i] == _coconut.getattr(_coconut_case_match_to_0[1], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_0[1].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0[1], "__match_args__") else _coconut.len(_coconut_case_match_to_0[1]) == 1  # type: ignore  #14 (line in Coconut source)
                    if _coconut_match_temp_13:  #14 (line in Coconut source)
                        _coconut_case_match_check_0 = True  #14 (line in Coconut source)
                if _coconut_case_match_check_0:  #14 (line in Coconut source)
                    if _coconut_match_set_name_imag is not _coconut_sentinel:  #14 (line in Coconut source)
                        imag = _coconut_match_set_name_imag  #14 (line in Coconut source)

            if not _coconut_case_match_check_0:  #14 (line in Coconut source)
                if (not _coconut_match_temp_12) and (_coconut.isinstance(_coconut_case_match_to_0[1], int)):  #14 (line in Coconut source)
                    _coconut_case_match_check_0 = True  #14 (line in Coconut source)
                if _coconut_case_match_check_0:  #14 (line in Coconut source)
                    _coconut_case_match_check_0 = False  #14 (line in Coconut source)
                    if not _coconut_case_match_check_0:  #14 (line in Coconut source)
                        _coconut_match_set_name_imag = _coconut_sentinel  #14 (line in Coconut source)
                        if _coconut.type(_coconut_case_match_to_0[1]) in _coconut_self_match_types:  #14 (line in Coconut source)
                            _coconut_match_set_name_imag = _coconut_case_match_to_0[1]  #14 (line in Coconut source)
                            _coconut_case_match_check_0 = True  #14 (line in Coconut source)
                        if _coconut_case_match_check_0:  #14 (line in Coconut source)
                            if _coconut_match_set_name_imag is not _coconut_sentinel:  #14 (line in Coconut source)
                                imag = _coconut_match_set_name_imag  #14 (line in Coconut source)

                    if not _coconut_case_match_check_0:  #14 (line in Coconut source)
                        _coconut_match_set_name_imag = _coconut_sentinel  #14 (line in Coconut source)
                        if not _coconut.type(_coconut_case_match_to_0[1]) in _coconut_self_match_types:  #14 (line in Coconut source)
                            _coconut_match_temp_14 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #14 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_14, _coconut.tuple):  #14 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #14 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_14) < 1:  #14 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_14),))  #14 (line in Coconut source)
                            _coconut_match_temp_15 = _coconut.getattr(_coconut_case_match_to_0[1], _coconut_match_temp_14[0], _coconut_sentinel)  #14 (line in Coconut source)
                            if _coconut_match_temp_15 is not _coconut_sentinel:  #14 (line in Coconut source)
                                _coconut_match_set_name_imag = _coconut_match_temp_15  #14 (line in Coconut source)
                                _coconut_case_match_check_0 = True  #14 (line in Coconut source)
                        if _coconut_case_match_check_0:  #14 (line in Coconut source)
                            if _coconut_match_set_name_imag is not _coconut_sentinel:  #14 (line in Coconut source)
                                imag = _coconut_match_set_name_imag  #14 (line in Coconut source)




        if _coconut_case_match_check_0:  #14 (line in Coconut source)
            print("Complex number {_coconut_format_0}+i{_coconut_format_1}".format(_coconut_format_0=(real), _coconut_format_1=(imag)))  #15 (line in Coconut source)
    if not _coconut_case_match_check_0:  #16 (line in Coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #16 (line in Coconut source)
        _coconut_match_set_name_imag = _coconut_sentinel  #16 (line in Coconut source)
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2):  #16 (line in Coconut source)
            _coconut_match_set_name_real = _coconut_case_match_to_0[0]  #16 (line in Coconut source)
            _coconut_match_set_name_imag = _coconut_case_match_to_0[1]  #16 (line in Coconut source)
            _coconut_case_match_check_0 = True  #16 (line in Coconut source)
        if _coconut_case_match_check_0:  #16 (line in Coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #16 (line in Coconut source)
                real = _coconut_match_set_name_real  #16 (line in Coconut source)
            if _coconut_match_set_name_imag is not _coconut_sentinel:  #16 (line in Coconut source)
                imag = _coconut_match_set_name_imag  #16 (line in Coconut source)
        if _coconut_case_match_check_0:  #16 (line in Coconut source)
            print("Strange complex number {_coconut_format_0}+i{_coconut_format_1}, real and imaginary part should be integers".format(_coconut_format_0=(real), _coconut_format_1=(imag)))  #17 (line in Coconut source)
    if not _coconut_case_match_check_0:  #18 (line in Coconut source)
        _coconut_case_match_check_0 = True  #18 (line in Coconut source)
        if _coconut_case_match_check_0:  #18 (line in Coconut source)
            raise ValueError("Not a complex number")  #19 (line in Coconut source)



complex_number((0, 0))  #22 (line in Coconut source)
complex_number((1, 0))  #23 (line in Coconut source)
complex_number((0, 1))  #24 (line in Coconut source)
complex_number((1, 1))  #25 (line in Coconut source)

complex_number(("x", 0))  #27 (line in Coconut source)
complex_number((0, "y"))  #28 (line in Coconut source)
complex_number(("x", "y"))  #29 (line in Coconut source)

complex_number("foo")  #31 (line in Coconut source)
complex_number("foo")  #32 (line in Coconut source)
