class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._arvot_lista = []

    def miinus(self, operandi):
        self._arvot_lista.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvot_lista.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvot_lista.append(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def kumoa(self):
        self._arvo = self._arvot_lista.pop()

