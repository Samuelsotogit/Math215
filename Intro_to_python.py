#Lab_1

my_first_var = (118+(11*2))/(9-2)

def arithmetic(i):
     j=i+2
     k=3*j
     w=k-5
    #  print(w)
     return w

def arithmetic2(i):
    return arithmetic(i)

# arithmetic2(-10)

def triple(x):
     y = 3*x
    #  print(y)
     return y

def avg(x,y):
    z = (x+y)/2
    # print(z)
    return z

def combine(x,y):
    # print(avg(x,triple(y)))
    return (avg(x,triple(y)))

w = [1,2,3,4,5]
g = [6,7,8,9,10,11,12]
h = [1]
k = []

def first(c):
    # print(c[0])
    return c[0]

def first_last(c):
    # print(first(c), c[-1])
    return first(c), c[-1]

def middle(c):
    c.remove(c[0])
    c.remove(c[-1])
    # print(c)
    return c


def swap(c):
    new_list=c.copy()
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    # print(new_list)
    return new_list

# OR

    # new_list=c.copy()
    # temp = new_list[0]
    # new_list[0] = new_list[-1]
    # new_list[-1] = temp
    # print(new_list)
    # return new_list


def absolute_value(x):
    if x < 0:
        # print(x * (-1))
        return x * (-1)
    # print(x)
    return x

def indicator(lower,upper,n):
    if lower <= n <= upper:
        # print(1)
        return 1
    # print(0)
    return 0

def trunc_max(x,y):
    if x >= 0 and y >= 0:
        if x > y:
            print(x)
            return x
        elif x < y:
            print(y)
            return y
        elif x == y:
            print(x)
            return x
        print(0)
        return 0
    if x < 0 or y < 0:
        if x > 0:
            print(x)
            return x
        elif y > 0:
            print(y)
            return y
        print(0)
        return 0
    print(0)
    return 0

trunc_max(8,8)