args = [0, 1, 4, 9]

def func(a,b,c):
    return a + b + c

func(*args)

# TypeError: func() takes 3 positional arguments but 4 were given