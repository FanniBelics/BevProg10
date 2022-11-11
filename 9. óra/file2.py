def main():
    with open("barmi.txt", 'r') as f, open('barmi2.txt','w') as f2:
        txt = f.read()
        print(txt)
        print(txt, file=f2)

if __name__ == "__main__":
    main()