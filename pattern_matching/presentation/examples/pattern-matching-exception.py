# Strukturální pattern matching:
# - reakce na ruzne typy vyjimek

def parse_generic_llm_error(e: Exception) -> tuple[int, str, str]:
    """Try to parse generic LLM error."""
    match e:
        case BadRequestError():
            return parse_openai_error(e)
        case ApiResponseException():
            return parse_bam_error(e)
        case ApiRequestFailure():
            return parse_watsonx_error(e)
        case _:
            return DEFAULT_STATUS_CODE, DEFAULT_ERROR_MESSAGE, str(e)
