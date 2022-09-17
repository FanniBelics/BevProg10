def main():
    li = ['alma', 'korte', 'barack']
    li2 = li.copy()
    li.append('mango')
    print(li)
    e = li.pop()
    print(e)
    li.sort()
    print(li)
    print(li.index('barack'))
    
if __name__ == "__main__":
    main()
