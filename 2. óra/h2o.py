def main():
    hidrogen = int(input("Hidrogen: "))
    oxigen = int(input("Oxigen: "))
    h2o = 0
    excessOxigen = 0
    excessHidrogen = 0

    if hidrogen == oxigen *2: 
        h2o = oxigen * 2
    elif hidrogen > oxigen * 2:
        h2o = oxigen * 2
        excessHidrogen = (hidrogen - oxigen*2)*2
    else:
        h2o = hidrogen
        excessOxigen = oxigen*2 - hidrogen

    print("Létrejött víz: {0},\nmaradék hidrogénatom: {1},\nmaradék oxigénatom: {2}".format(h2o, excessHidrogen, excessOxigen))

if __name__ == "__main__":
    main()