def hello(a):
    print("Hello " + a)

def rec(a):
    print(a)
    if a < 1:
        return a
    return rec(a-1)

def main():
    hello('Dani')
    print(rec(4))

if __name__ == '__main__':
    main()