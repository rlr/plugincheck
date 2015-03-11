from functools import wraps


# This decorator was lifted from fjord - https://github.com/mozilla/fjord
# Thanks willkg!
def cors_enabled(origin, methods=['GET']):
    """A simple decorator to enable CORS."""
    def decorator(f):
        @wraps(f)
        def decorated_func(request, *args, **kwargs):
            if request.method == 'OPTIONS':
                # preflight
                if ('HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META and
                        'HTTP_ACCESS_CONTROL_REQUEST_HEADERS' in request.META):

                    response = HttpResponse()
                    response['Access-Control-Allow-Methods'] = ", ".join(
                        methods)

                    # TODO: We might need to change this
                    response['Access-Control-Allow-Headers'] = \
                        request.META['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']
                else:
                    return HttpResponseBadRequest()
            elif request.method in methods:
                response = f(request, *args, **kwargs)
            else:
                return HttpResponseBadRequest()

            response['Access-Control-Allow-Origin'] = origin
            return response
        return decorated_func
    return decorator
