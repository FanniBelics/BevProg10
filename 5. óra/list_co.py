#https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818d

def main():
    li = [n*2 for n in range(0,10)]

    li.clear()
    for n in range(10):
        li.append(n*2)
    print(li)

    li2 = ['auto', 'villamos', 'metro']
    li2 = [s.upper()+"!" for s in li2]

    li2.clear()
    for s in li2:
        s2 = li2.lpop()
        s2 = s2.upper() + "!"
        li2.append(s2)

    print(li2)

    pystr = "python is an awesome language" 
    lipy = [s[0] for s in pystr.split()]
    print(lipy)

    lipy2 = []
    for s in pystr.split():
        lipy2.append(s[0])

    print(lipy2)

    linegyzet = [n**2 for n in range(1,20)] #[1;20[ 
    print(linegyzet)


if __name__ == '__main__':
    main()