from functools import wraps


def log(predicate, error_message, filename=None):
    """Декоратор, выдающий лог успешного или неуспешного завершения функции"""

    def wrapper(function):
        @wraps(function)
        def inner(a):
            if not filename:
                try:
                    result = function(a)
                    print(f"{function.__name__} ok")
                except Exception as e:
                    print(f"{function.__name__} error: {type(e).__name__}. Inputs: {a}, {e}")
                    raise ValueError(error_message)
                return result
            else:
                with open(filename, "w") as file:
                    try:
                        result = function(a)
                        file.write(f"{function.__name__} ok")
                    except Exception as e:
                        file.write(f"{function.__name__} error: {type(e).__name__}. Inputs: {a}, {e}")
                        raise ValueError(error_message)
                    return result

        return inner

    return wrapper
