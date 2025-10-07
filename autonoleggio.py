class Automobile:
    def __init__(self, codice, marca, modello, anno, nPosti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = int(anno)
        self.nPosti = int(nPosti)

    def __str__(self):
        return f"{self.codice} - {self.marca} {self.modello} ({self.anno}), {self.nPosti} posti"

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.automobili = []
        self.noleggi = {}


        """Inizializza gli attributi e le strutture dati"""
        # TODO


    def carica_file_automobili(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for riga in file:
                    riga = riga.rstrip().split(",")
                    auto = Automobile(riga[0], riga[1], riga[2], riga[3], riga[4])
                    #print(auto.codice, auto.marca, auto.modello, auto.anno, auto.nPosti)
                    self.automobili.append(auto)
        except FileNotFoundError:
            print(f"file {file_path} non trovato")


        """Carica le auto dal file"""
        # TODO

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        numeri = []
        for a in self.automobili:
            numeri.append(int(a.codice[1:]))
        max_num = max(numeri)
        codice = f"A{max_num+1}"
        auto = Automobile(codice, marca, modello, anno, num_posti)
        self.automobili.append(auto)
        print(auto.codice, auto.marca, auto.modello, auto.anno, auto.nPosti)
        return auto
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def automobili_ordinate_per_marca(self):
        return sorted(self.automobili, key=lambda a: a.marca.lower())
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        for a in self.automobili:
            if a.codice == id_automobile:
                for id_noleggio in self.noleggi:
                    noleggio = self.noleggi[id_noleggio]
                    if noleggio["auto"].codice == id_automobile and noleggio["attivo"]:
                        raise ValueError(f"L'automobile {id_automobile} non è disponibile: già noleggiata")
                auto_obj = None
                for i in range(len(self.automobili)):
                    if self.automobili[i].codice == id_automobile:
                        auto_obj = self.automobili.pop(i)
                        break

                noleggio = {"data" : data,
                            "auto" : auto_obj,
                            "cliente" : cognome_cliente,
                            "attivo" : True}

            id_noleggio = f"N{len(self.noleggi)+1}"
            self.noleggi[id_noleggio] = noleggio
            return {"id_noleggio": id_noleggio,
                    "data": noleggio["data"],
                    "auto": str(noleggio["auto"]),
                    "cliente": noleggio["cliente"],
                    "attivo": noleggio["attivo"]
                                                }
                

        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        if not self.noleggio:
            raise ValueError(f"Noleggio {id_noleggio} non trovato")
        if id_noleggio in self.noleggi:
            noleggio = self.noleggi[id_noleggio]
            if not noleggio["attivo"]:
                # rimuovo il record e dico che non esiste
                del self.noleggi[id_noleggio]
                raise ValueError(f"Noleggio con ID {id_noleggio} non trovato")

                # Prendo l'auto dal noleggio e la riaggiungo alle disponibili (se non già presente)
            auto = noleggio["auto"]
            trovata = False
            for a in self.automobili:
                if a.codice == auto.codice:
                    trovata = True
                    break
            if not trovata:
                self.automobili.append(auto)

            # Rimuovo il record del noleggio (così una seconda terminazione con lo stesso id darà "non trovato")
            del self.noleggi[id_noleggio]

            # Esco: il main stamperà "Noleggio ... terminato con successo."
            return

            # Se l'id non è presente
        raise ValueError(f"Noleggio con ID {id_noleggio} non trovato")



        """Termina un noleggio in atto"""
        # TODO
