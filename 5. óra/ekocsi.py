class eJarmu():
    def __init__(self, tipus, loero, szin, marka, hatotav) -> None:
        self.tipus = tipus
        self.loero = loero
        self.szin = szin
        self.marka = marka
        self.hatotav = hatotav

    def kiir(self):
        print("marka, {0}, tipus {1}".format(self.marka, self.tipus))

    def atfest(self, szin):
        self.szin = szin

    def romlas(self):
        self.hatotav -= 15

    def uj_aksi(self, aksi):
        self.hatotav = aksi
    
    def eredeti(self):
        if self.marka != "Mitsubishi" and self.marka != "Renault" and self.marka != "Opel":
            print("eredeti")
        else:
            print("Kinai")