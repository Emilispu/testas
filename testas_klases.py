from tkinter import *
from PIL import Image, ImageTk
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
                pasirinkimaiABC=[]
            else:
                pasirinkimaiABC.append(line.rstrip('\n'))
        failas.close()
        return testas
    def __repr__(self):
        return self.konvertavimas()
testas = Is_txt_i_list()
klausimas = testas.konvertavimas()

