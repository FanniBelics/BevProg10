import json

def main():
    d = {
        "name": 'Fanni',
        "age": 21,
        "favPokemon": 'Bulbasaur'
    }

    f = open('jsonki.json','w')
    json.dump(d,f, indent=2)
    f.close()

    f2= open('txtki.json','w')
    jsontxt = json.dumps(d)
    print(jsontxt, file=f2)
    f2.close()


if __name__ == "__main__":
    main()