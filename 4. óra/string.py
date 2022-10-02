def both_ends(txt):
    if len(txt) < 2:
        return ''
    return txt[:2] + txt[-2:]

def main():
    txt = 'Hello, world!'
    tobbsoros = """tobb
    sorban
    van"""

    print(txt[5])
    # for x in txt:
    #     print(x)

    # print(len(txt))
    # print(txt.upper())
    # print(txt.lower())
    # print(txt.capitalize())
    # print(txt.title())
    # print("         hehe           ".strip())
    # print(txt.replace("ll", "nl"))
    # print(txt.replace("o", "a"))
    # print(txt.replace("ll", "nl"))
    # print(txt.split())
    # print("1;2;3;4;5".split(sep=';'))
    # print("Hello "+"World!")
    # print(txt.rfind('o'))
    # print(txt[1:8])  #[1;5[
    print("a".isalpha())
    print("henlo".join(txt))

    print(both_ends("fecske"))



if __name__ == '__main__':
    main()