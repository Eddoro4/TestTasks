def memoize(fn):
    cache = {}

    def wrapper(*args, **kwargs):
        keys = (args, tuple(sorted(kwargs.items())))
        print(keys)
        if keys in cache:
            return cache[keys]
        else:
            result = fn(*args,**kwargs)
            cache[keys] = result
            return result
        pass

    return wrapper

calls = []
add = memoize(lambda a=0, b=0: calls.append(1) or a + b)
add(a=1, b=2)
add(b=2, a=1)

len(calls)