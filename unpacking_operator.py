## * args allow passing positional arguments to a function
def add(*args):
    total = 0
    for arg in args[0]:
        total += arg
    print(total)

## ** kwargs allow passing keyword arguments to a function.
def add2(**kwargs):
    total_scores = 0
    for i, score in kwargs.items():
        total_scores += score
    print(total_scores)

def add3(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)

if __name__ == "__main__":
    l = [10,20,30]
    add(l)
    add2(a=100,b=200,c=300)

    ## unpacking with * operator
    print(*l)
    l2 = [40,50]
    add3(*l, *l2)

    ## unpacking with ** operator
    dict_a = {"A":1,"B":2}
    dict_b = {"a":3,"b":4}
    print({**dict_a, **dict_b})
