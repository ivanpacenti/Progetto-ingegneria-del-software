

class Partita():
    def __init__(self, perdente,punteggioGiocatoreDue,PunteggioGiocatoreUno,vincitore):
        self.perdente=perdente
        self.punteggioGiocatoreDue=punteggioGiocatoreDue
        self.PunteggioGiocatoreUno=PunteggioGiocatoreUno
        self.vincitore=vincitore

    def getPerdente(self):
        return  self.perdente

    def setPerdente(self):
        self.perdente=perdente

    def getPunteggioGiocatoreDue(self):
        return punteggioGiocatoreDue

    def setPunteggioGiocatoreDue(self):
        self.punteggioGiocatoreDue=punteggioGiocatoreDue

    def getPunteggioGiocatoreUno(self):
        return self.punteggioGiocatoreUno

    def setPunteggioGiocatoreUno(self):
        self.punteggioGiocatoreUno=punteggioGiocatoreUno

    def getVincitore(self):
        return self.vincitore

    def setVincitore(self):
        self.vincitore=vincitore



