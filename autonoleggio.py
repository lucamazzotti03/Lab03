class Automobile:
    def __init__(self, codice, marca, modello, anno, nPosti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = int(anno)
        self.nPosti = int(nPosti)

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.Automobile = []


        """Inizializza gli attributi e le strutture dati"""
        # TODO


    def carica_file_automobili(self, file_path):
        try:
            file = open(file_path, 'r')
        except FileNotFoundError:
            print(f"file {file_path} non trovato")
        for riga in file:
            riga = riga.rstrip().split(",")
            auto = Automobile(riga[0], riga[1], riga[2], riga[3], riga[4])
            print(auto.codice, auto.marca, auto.modello, auto.anno, auto.nPosti)
            self.Automobile.append(auto)

        """Carica le auto dal file"""
        # TODO

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        auto = Automobile(codice, marca, modello, anno, num_posti)
        self.Automobile.append(auto)
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
