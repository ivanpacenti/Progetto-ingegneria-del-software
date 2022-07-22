import pickle
from Implementazione.Gestione.GestoreUtenti import GestoreUtenti
from Implementazione.Gestione.GestorePrenotazioni import GestorePrenotazioni

class GestoreBackup():



    def salvaDati():
        pickle.dump(GestorePrenotazioni.collectionPrenotazioni,open( "backupPrenotazioni.p", "wb" ))
        pickle.dump(GestoreUtenti.collectionUtenti, open( "backupUtenti.p", "wb" ))
        print("fatto")





    def caricaDati():
            GestorePrenotazioni.collectionPrenotazioni = pickle.load(open( "backupPrenotazioni.p", "rb" ))
            GestoreUtenti.collectionUtenti = pickle.load(open( "backupUtenti.p", "rb" ))

