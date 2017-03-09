import json
from flask import request, Response
from functools import wraps
from jsonschema import validate, ValidationError, FormatChecker


def process_params(param_config=None, *args, **kwargs):
    def deco(f):
        def incorrect_input_fields_error(msg):
            body = {
                "s": 0,
                "m": msg,
                "d": {}
            }
            response = Response(
                json.dumps(body), status=400, content_type='application/json')
            return response

        def extract_params(request):
            if request.method == 'POST':
                return request.get_json()
            else:
                return request.args

        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                params = extract_params(request)
                validate(params, param_config, format_checker=FormatChecker())
                return f(params=params, *args, **kwargs)
            except (ValidationError, ValueError) as e:
                return incorrect_input_fields_error(e.message)
        return decorated_function
    return deco

