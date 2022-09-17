def main():
    age = int(input("Kor: "))

    if age >= 18:
        print("fogyaszthat")
    elif age == 17:
        print('Majdnem fogyaszthat')
    else:
        print('Nem fogyaszthat')
if __name__ == "__main__":
    main()