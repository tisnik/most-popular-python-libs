// The module function definitions.
static PyObject *impl___main__$$$function__1_add_two_numbers(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_x = python_pars[0];
    PyObject *par_y = python_pars[1];
    struct Nuitka_FrameObject *frame_e30d4ff187a891f7d48af8b5b7fa0636;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_e30d4ff187a891f7d48af8b5b7fa0636 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_e30d4ff187a891f7d48af8b5b7fa0636)) {
        Py_XDECREF(cache_frame_e30d4ff187a891f7d48af8b5b7fa0636);

#if _DEBUG_REFCOUNTS
        if (cache_frame_e30d4ff187a891f7d48af8b5b7fa0636 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_e30d4ff187a891f7d48af8b5b7fa0636 = MAKE_FUNCTION_FRAME(tstate, codeobj_e30d4ff187a891f7d48af8b5b7fa0636, module___main__, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_e30d4ff187a891f7d48af8b5b7fa0636->m_type_description == NULL);
    frame_e30d4ff187a891f7d48af8b5b7fa0636 = cache_frame_e30d4ff187a891f7d48af8b5b7fa0636;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_e30d4ff187a891f7d48af8b5b7fa0636);
    assert(Py_REFCNT(frame_e30d4ff187a891f7d48af8b5b7fa0636) == 2);

    // Framed code:
    {
        PyObject *tmp_add_expr_left_1;
        PyObject *tmp_add_expr_right_1;
        CHECK_OBJECT(par_x);
        tmp_add_expr_left_1 = par_x;
        CHECK_OBJECT(par_y);
        tmp_add_expr_right_1 = par_y;
        tmp_return_value = BINARY_OPERATION_ADD_OBJECT_OBJECT_OBJECT(tmp_add_expr_left_1, tmp_add_expr_right_1);
        if (tmp_return_value == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 2;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        goto frame_return_exit_1;
    }


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_1;
    frame_return_exit_1:

    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto function_return_exit;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_e30d4ff187a891f7d48af8b5b7fa0636, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_e30d4ff187a891f7d48af8b5b7fa0636->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_e30d4ff187a891f7d48af8b5b7fa0636, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_e30d4ff187a891f7d48af8b5b7fa0636,
        type_description_1,
        par_x,
        par_y
    );


    // Release cached frame if used for exception.
    if (frame_e30d4ff187a891f7d48af8b5b7fa0636 == cache_frame_e30d4ff187a891f7d48af8b5b7fa0636) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_e30d4ff187a891f7d48af8b5b7fa0636);
        cache_frame_e30d4ff187a891f7d48af8b5b7fa0636 = NULL;
    }

    assertFrameObject(frame_e30d4ff187a891f7d48af8b5b7fa0636);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_x);
    Py_DECREF(par_x);
    CHECK_OBJECT(par_y);
    Py_DECREF(par_y);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_x);
    Py_DECREF(par_x);
    CHECK_OBJECT(par_y);
    Py_DECREF(par_y);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}
