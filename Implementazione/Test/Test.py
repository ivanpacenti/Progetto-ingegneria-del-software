import unittest

from Implementazione.Generali.Utente import Utente
from Implementazione.Gestione.GestoreUtenti import GestoreUtenti
from Implementazione.Gestione.GestorePrenotazioni import GestorePrenotazioni
from Implementazione.Generali.Prenotazione import Prenotazione
from Implementazione.Generali.Campo import Campo


class MyTestCase(unittest.TestCase):

    def testLogin(self):
        # Controlla che gli utenti appena creati non sono amministratori di default.
        self.utente = Utente("Ivan", "prova", "08/06/1991", "333222556", "password", "asd")
        GestoreUtenti.setUtenteConnesso(self.utente)
        self.assertEqual(GestoreUtenti.utenteConnesso.isAdmin, False)

    def testPrenotazione(self):
        #Controlla che una prenotazione viene trovata con il metodo cercaPrenotazione
        #da un utente connesso non amministratore
        self.campo = GestorePrenotazioni.paddle
        self.utente = Utente("Ivan", "prova", "08/06/1991", "333222556", "password", "asd")
        self.prenotazioneuno = Prenotazione("2021 ,7 ,8", "10:00", self.campo, self.utente)
        GestorePrenotazioni.collectionPrenotazioni.append(self.prenotazioneuno)
        GestoreUtenti.utenteConnesso=self.utente
        self.assertEqual(GestorePrenotazioni.cercaPrenotazione("2021 ,7 ,8", 2, 3), self.prenotazioneuno)

    def testCopiaTesseramento(self):
        #Controlla che alla modifica di un utente venga portato il tesseramento
        self.utente = Utente("Ivan", "prova", "08/06/1991", "333222556", "password", "asd")
        self.utente.setTesseramento("prova@google.com","PCNVNI91H08I608S","Paddle")
        GestoreUtenti.collectionUtenti.append(self.utente)
        GestoreUtenti.utenteConnesso=self.utente
        self.utentemodificato=Utente("Mario", "Franchi", "08/06/1991", "333222556", "password", "asd")
        GestoreUtenti.modificaUtente(self.utente,self.utentemodificato)
        self.assertEqual(self.utente.getTesseramento(),self.utentemodificato.getTesseramento())


if __name__ == '__main__':
    unittest.main()
