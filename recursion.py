n=int(input()) # u can take an input
global a
a=-n

def print_series(n):
    if n<a:
        return
    else:
        print(n)
        return print_series(n-3)

print_series(n)