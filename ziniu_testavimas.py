# importuojame konvertavimo klasę
# from testas_klases import Is_txt_i_list
from tkinter import *
from PIL import Image, ImageTk
from docxtpl import DocxTemplate
import jinja2
import datetime
import os

atsakymo_failas = open('user_answ.txt', 'w')
atsakymo_failas.close()


class Klausimynas():

    def __init__(self, klausimai, width=700, heigth=500,
                 title='Bendrasis pirmosios med. pagalbos žinių patikrinimo testas', resizable=[False, False], bg=None,
                 fg=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{heigth}+200+200')
        self.root.resizable(resizable[0], resizable[1])
        self.klausimai = klausimai

        self.atsA = IntVar()
        self.atsB = IntVar()
        self.atsC = IntVar()
        self.atsD = IntVar()
        self.atsE = IntVar()

        self.variantasA = Checkbutton(self.root, text=klausimai['Variantai'][0], variable=self.atsA, onvalue=1,
                                      offvalue=0)
        self.variantasB = Checkbutton(self.root, text=klausimai['Variantai'][1], variable=self.atsB, onvalue=1,
                                      offvalue=0)
        if len(klausimai['Variantai']) > 2:
            self.variantasC = Checkbutton(self.root, text=klausimai['Variantai'][2], variable=self.atsC, onvalue=1,
                                          offvalue=0)
        if len(klausimai['Variantai']) > 3:
            self.variantasD = Checkbutton(self.root, text=klausimai['Variantai'][3], variable=self.atsD, onvalue=1,
                                          offvalue=0)
        if len(klausimai['Variantai']) > 4:
            self.variantasE = Checkbutton(self.root, text=klausimai['Variantai'][4], variable=self.atsE, onvalue=1,
                                          offvalue=0)

        self.eil_nr = Label(text=f"{self.klausimai['Eilės numeris']}", font=('Arial', 14))
        if klausimai['Img'] != 'None':
            self.image = ImageTk.PhotoImage(Image.open(f"{klausimai['Img']}"))
            self.panel = Label(self.root, image=self.image)
        self.question = Label(text=klausimai['Klausimas'], font=('Arial', 12))

    def draw_widgets(self):
        self.eil_nr.pack()
        if klausimai['Img'] != 'None':
            self.panel.pack(anchor='nw', expand="no")
        self.question.pack(anchor='nw')
        Label(text='-------------------------------------------').pack(anchor='nw')
        self.variantasA.pack(anchor='nw')
        self.variantasB.pack(anchor='nw')
        if len(klausimai['Variantai']) > 2:
            self.variantasC.pack(anchor='nw')
        if len(klausimai['Variantai']) > 3:
            self.variantasD.pack(anchor='nw')
        if len(klausimai['Variantai']) > 4:
            self.variantasE.pack(anchor='nw')
        Button(text='Kitas klausimas', command=self.Get_answer).pack(anchor='w')
        Button(text='Išeiti', command=self.exitas).pack(anchor='c')

    def exitas(self):
        exit()

    def Get_answer(self):
        self.ats = {}
        atsakymo_failas = open('user_answ.txt', 'a')
        self.atsakymas = []
        if self.atsA.get() == 1:
            self.atsakymas.append('A')
        if self.atsB.get() == 1:
            self.atsakymas.append('B')
        if self.atsC.get() == 1:
            self.atsakymas.append('C')
        if self.atsD.get() == 1:
            self.atsakymas.append('D')
        if self.atsE.get() == 1:
            self.atsakymas.append('E')

        atsakymo_failas.write(f"{klausimai['Eilės numeris']}: {self.atsakymas} \n")
        atsakymo_failas.close()
        self.root.destroy()

    def RunFunc(self):
        self.draw_widgets()
        self.root.mainloop()


class Rezultatai():
    """
Ši klasė apskaičiuoja jūsų taškus.
Palygina jūsų atsakymus su testo atsakymais.
sėkmingai išlaikius, įvedamas vardas ir pavardė bei atsisiųnčiamas sertifikatas
    """

    def __init__(self, width=700, heigth=500, title='Bendrasis pirmosios med. pagalbos žinių patikrinimo testas',
                 resizable=[False, False], bg=None, fg=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{heigth}+200+200')
        self.root.resizable(resizable[0], resizable[1])

        self.antraste = Label(text='Žnių patikrinimo testo rezultatas:', font=('Arial', 14))

        self.yes_info = Label(text='Sveikiname išlaikius testą.', bg='LimeGreen', font=('Arial', 12))
        self.vardas = Label(text='Įveskite savo vardą ir pavardę: ', font=('Arial', 12))
        self.entry_vardas = Entry(width=15)

        self.no_info = Label(text='Apgailėstaujame. Testo neišlaikėte. Bandykite dar kartą.', bg='Coral',
                             font=('Arial', 12))

    def palyginimas(self):
        self.i = 0
        user_ats_failas = open('user_answ.txt', 'r')
        testo_ats_failas = open('atsakymai.txt', 'r')
        for line1, line2 in zip(user_ats_failas, testo_ats_failas):
            if line1.strip() == line2.strip():
                self.i += 1

        return self.i

    def open_file(self):
        os.system('generated_doc.docx')

    def getas(self):
        self.vpavarde = self.entry_vardas.get()
        doc = DocxTemplate("certificate.docx")
        context = {'vardas': self.vpavarde, "data": datetime.date.today()}  # Where the magic happens
        jinja_env = jinja2.Environment(autoescape=True)
        doc.render(context)
        doc.save("generated_doc.docx")

    def draw_widgets(self):

        self.taskai = self.palyginimas()
        self.procentai = round((self.taskai / 10 * 100), 0)

        if self.procentai >= 80:
            self.yes_info.grid(row=0, column=0, sticky=W, pady=5)
            Label(self.root, text=f"Jūs surinkote {self.taskai} taškų iš 10 galimų").grid(row=1, column=0, sticky=W,
                                                                                          pady=5)
            self.vardas.grid(row=2, column=0, sticky=W, pady=5)
            self.entry_vardas.grid(row=2, column=1, sticky=W, pady=5)
            Button(self.root, text='Patvirtinti vardą', bg='lightgray', command=self.getas).grid(row=3, column=0,
                                                                                                 sticky=E, padx=15,
                                                                                                 pady=5)
            Button(self.root, text='Atsisiųsti sertifikatą', bg='lightgray', command=self.open_file).grid(row=3,
                                                                                                          column=1,
                                                                                                          sticky=W,
                                                                                                          pady=5)

        else:
            self.no_info.grid(row=0, column=0, sticky=W, pady=5)
            Label(text=f"Jūs surinkote {self.taskai} taškų iš 10 galimų").grid(row=1, column=0, sticky=W, pady=5)

    def RunFunc(self):

        self.draw_widgets()
        self.root.mainloop()


class Is_txt_i_list():
    """
    Ši klasė konvertuoja testą, įrašytą txt formatu, į listą. \n
    Klasės def __init__(self, failo_vardas) \n
    Klasės funkcijos: __init__, konvertavimas, __repr__\n
    def konvertavimas returnina galutinį listą: testas\n
    listą testas sudaro žodynai klausimas\n
    Žodyne klausimas naudojami raktai: 'Eilės numeris', 'Img', 'Klausimas', 'Variantai'\n
    Img - naudojamas paveikslėlio pavadinimas, jei jo nėra, rašoma None\n

    """

    def konvertavimas(self):
        pasirinkimaiABC = []
        klausimas = {}
        testas = []
        failas = open('testas.txt', 'r')

        for line in failas:
            if line.startswith('Eil. nr.'):
                line = line.rstrip('\n')
                lines = line.split(' - ')
                klausimas['Eilės numeris'] = lines[1]
            elif line.startswith('img'):
                line = line.rstrip('\n')
                lines = line.split(' - ')
                klausimas['Img'] = lines[1]
            elif line.startswith('Klausimas'):
                line = line.rstrip('\n')
                lines = line.split(' - ')
                klausimas['Klausimas'] = lines[1]
            elif line.rstrip('\n') == '*':
                klausimas['Variantai'] = pasirinkimaiABC
                testas.append(klausimas)
                klausimas = {}
                pasirinkimaiABC = []
            else:
                pasirinkimaiABC.append(line.rstrip('\n'))
        failas.close()
        return testas

    def __repr__(self):
        return self.konvertavimas()


# iššaukiame konvertavimo į listą klasę
testas = Is_txt_i_list()
klausimas = testas.konvertavimas()

for klausimai in klausimas:
    if __name__ == '__main__':
        window = Klausimynas(klausimai)
        window.RunFunc()

window1 = Rezultatai()
window1.RunFunc()
