import inspect


def introspection_info(obj):
    result = dict()                         # создаем пустой словарь
    result['type'] = str(type(obj))[8:-2]   # получаем тип обьекта
    mixx = dir(obj)             # получаем микс из атрибутов и методов
    attrs = []
    meths = []
    for i in mixx:             # сортируем
        if i[0] == '_':
            meths.append(i)
        else:
            attrs.append(i)
    result['attributes'] = attrs
    result['methods'] = meths
    module = inspect.getmodule(obj) # получаем модули функций
    if module == None:             
        module = '__main__'
    result['module'] = module
    return result


number_info = introspection_info(42)
print(number_info)
