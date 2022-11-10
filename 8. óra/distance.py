from enum import Enum


class Type(Enum):
    HOUSE = 'house'
    BOF = 'Block of Flats'
    TREE = 'tree'
    FREE = 'free'

class Place:
    def __init__(self, begin, end, type = Type.FREE) -> None:
        self.begin = min(begin,end)
        self. end = max(begin,end)
        self.type = type

    def distance(self) -> float:
        return self.end-self.begin

    def __str__(self) -> str:
        return '({0};{1})'.format(self.begin, self.end)

    def __add__(self, b): # self + b
        newElement = Place(min(self.begin, b.begin),max(self.end,b.end))
        return newElement

    def __sub__ (self,b): # self - b
        newElement = Place(max(self.begin, b.begin),min(self.end,b.end))
        return newElement

    def __ge__ (self, b): #greater than,equal self >= b
        if self.distance() >= b.distance():
            return True
        else:
            return False
#__gl__ (Greater than, less), __lt__(Less than), __le__(Less equal)
# __eq__ (equal) __ne__ (not equal)

    def __iadd__(self, b): # self += b
        newElement = Place(min(self.begin, b.begin),max(self.end,b.end))
        return newElement


def main():
    print(Type.BOF.value)
    print(Type.BOF.name)

if __name__ == '__main__':
    main()