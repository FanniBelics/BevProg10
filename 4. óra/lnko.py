def lnko(a,b):
    while not (a == b):
        if a > b:
            a -= b # a = a-b
        elif a < b:
            b -=a 

    return a

def lnkorec(a,b):
    if a == b:
        return a
    elif a > b:
        return lnkorec(a-b, b)
    else:
        return lnkorec(a, b-a)

def szum(li):
    if len(li) == 1:
        return li[0]
    return li[0] + szum(li[1:])

def main():
    print(szum([1,2,3,4,5]))

if __name__ == '__main__':
    main()