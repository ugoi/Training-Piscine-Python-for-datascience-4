def callLimit(limit: int):
    """Decorator to limit the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """The actual decorator that checks the function's call count."""
        def limit_function(*args: any, **kwds: any):
            """Wrapper function to enforce the call limit."""
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                error_msg = (f"Error: <function {function.__name__} "
                             f"at {hex(id(function))}> call too many times")
                print(error_msg)

        return limit_function
    return callLimiter
