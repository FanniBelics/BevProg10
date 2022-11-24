# Házi feladat

## Groot!
Készíts egy programot, amely meghívásakor a Groot nevet írja ki. A Groot szót nem használhatod a programban :D
(Lehet akár Hodorral is vagy Squirtle-lel)

## Prímek
Készítsünk egy modult ahol a következő függvényt definiáljuk:
def is_prime(n):
    """
    Decide whether a number is prime or not.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True

Majd készítsünk 2 programot a segítségével,  az egyikben a 100-nál kisebb prímeket írjuk ki, a másikban
pedig a 200-nál kisebb prímszámok összegét számoljuk ki.

### PokéAPI
Kérjünk be a felhasználótól egy Pokémont, majd a PokéApi segítségével kérdezzük le az adatait.
Válaszként egy JSON-t fogunk kapni, ebből a JSON fájlból írjuk ki a Pokémon fontosabb adatait