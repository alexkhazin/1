def tag(tag):
    def decorator(func):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<{tag}>{result}</{tag}>'
        return wrapper
    return decorator

@tag('tag')
def rap():
    return 'rap'
rap()