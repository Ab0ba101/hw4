import colorama
import inspect

attributes_methods = dir(colorama)

for item in attributes_methods:
    print(item)

important_items = [
    'Fore',
    'Back',
    'Style',
    'init',
    'deinit'
]

for item in important_items:
    print(f'Важливий елемент: {item}')
    print(inspect.getdoc(getattr(colorama, item)))
