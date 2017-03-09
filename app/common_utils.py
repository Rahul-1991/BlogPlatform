from flask import Response
import json

header_config = {
    'with_auth': {
        "Authorization": str,
        "X-VERSION-CODE": int,
    },
    'without_auth': {
        "X-Session": str,
        "X-VERSION-CODE": str
    },
    'without_session': {
        "X-VERSION-CODE": str
    }
}


def get_success_response(s, m, d):
    body = {
        "s": s,
        "m": m,
        "d": d
    }
    response = Response(
        json.dumps(body), status=200, content_type='application/json')
    return response
