import random
import tkinter as tk
from tkinter import simpledialog


class Devinette:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de devinette")

        self.frame1 = tk.Frame(self.master)
        self.frame1.pack()

        self.label1 = tk.Label(
            self.frame1, text="Nombre de tentatives [0..100]: ")
        self.label1.pack(side=tk.LEFT)

        self.tentatives = tk.Entry(self.frame1)
        self.tentatives.pack(side=tk.LEFT)

        self.button = tk.Button(
            self.master, text="Commencer", command=self.commencer)
        self.button.pack()

        self.master.bind("<Return>", self.commencer)

        self.frame2 = tk.Frame(self.master)
        self.frame2.pack(pady=10)

        self.label2 = tk.Label(self.frame2, text="Tentatives: ")
        self.label2.pack()

        self.text = tk.Text(self.frame2, width=60, height=30)
        self.text.pack()

    def commencer(self, event=None):
        self.text.delete("1.0", tk.END)
        n = random.randint(0, 100)
        nbreTentative = int(self.tentatives.get())
        NbCoups = nbreTentative
        while nbreTentative > 0:
            nbreTentative -= 1
            val = self.saisir_nombre()
            if val is None:
                continue  # l'utilisateur a annulé la saisie
            elif val < n:
                self.ajouter_ligne("Plus petit !")
            elif val > n:
                self.ajouter_ligne("Plus grand !")
            else:
                break
        if nbreTentative != 0:
            self.ajouter_ligne("Bravo!, Vous avez trouvé {} en {} essais".format(
                val, NbCoups-nbreTentative))
        else:
            self.ajouter_ligne(
                "Oups!, Vous avez dépassé les {} tentatives autorisés. Le nombre était : {}".format(NbCoups, n))

    def saisir_nombre(self):
        val = None
        while val is None:
            reponse = simpledialog.askstring(
                "Devinette", "Entrer un nombre : ")
            if reponse is None:
                break
            try:
                val = int(reponse)
            except ValueError:
                pass  # la réponse n'est pas un entier
        return val

    def ajouter_ligne(self, ligne):
        self.text.insert(tk.END, ligne + "\n")
        self.text.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Devinette(root)
    root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    