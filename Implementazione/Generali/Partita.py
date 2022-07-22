

class Partita():
    def __init__(self, giocatoreuno, punteggiouno, giocatoredue,punteggiodue):
        self.giocatoreuno=giocatoreuno
        self.punteggiouno=punteggiouno
        self.punteggiodue=punteggiodue
        self.giocatoredue=giocatoredue

    def getPunteggioUno(self):
        return self.punteggiouno

    def getPunteggioDue(self):
        return self.punteggiodue