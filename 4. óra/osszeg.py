def sum(li):
    if len(li) == 1:
        return li[0]
    return li[0] + sum(li[1:])

def main():
    print(sum([100,4,30,-10,32]))

if __name__ == '__main__':
    main()