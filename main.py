def get_handler(handler):
    try:
        file_name = '%s_handler' % handler.lower()
        obj = '%sHandler' % handler.title()
        path = 'handlers.%s.%s' % (file_name, obj)
        from importlib import import_module
        module_path, _, class_name = path.rpartition('.')
        mod = import_module(module_path)
        handler_class = getattr(mod, class_name)
        return handler_class
    except KeyError:
        return None

def hello():
    handler_class = get_handler('test')
    print(handler_class.test_echo('test'))
    print(handler_class.test2_field)

if __name__ == '__main__':
    hello()
