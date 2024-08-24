def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print(f'{a}{b}')


add_everything_up(1, 2)
add_everything_up('cow', 296)
add_everything_up(1, 'wow')
add_everything_up(2.25, 4)
