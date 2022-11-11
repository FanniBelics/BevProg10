def main():
    try:
        d1 = int(input("szam1: "))
        d2 = int(input("szam2: "))
        print(d1/d2)
    except ZeroDivisionError as e:
        print(e)
    except (ValueError,KeyboardInterrupt):
        pass
    # except KeyboardInterrupt:
    #     print("KeyboardInterrupt") 
    except:
        print("Ha nem megy hát nem megy")
    print("Vege")

if __name__ == "__main__":
    main()