Paleidžiamasis failas yra ziniu_testavimas.py

importuojami moduliai:
from tkinter import *
from PIL import Image, ImageTk
from docxtpl import DocxTemplate
import jinja2
import datetime
import os

testas.txt
Čia užrašomi testo klausimai. Žemiau paaiškinimai:
Klausimų gali būti betkiek;
Klausimo atsakymų variantų turi būti maksimum 5;
Klausimas prasideda (aaa-klausimo eilės numeris): 	Eil. nr. - aaa.
Jei klausime naudojamas paveiksliukas, tai
jis yra įrašomas į šakninį katalogą (maks plotis 250 px).
įrašomas tokiu būdu (aaa.jpg - jūsų paveiksliukas)	img - aaa.jpg
Klausimas užduodamas iškarto po: 			Klausimas - 
Atsakymų variantai surašomi A., B., C., D., E.
Būtinai po klausimo dedama žvaigždutė			*

atsakymai.txt
Čia surašomi atsakymai tokiu būdu:
1. : ['A'] 
2. : ['A', 'B']
 
Kur 1, 2 - klausimų numeriai
['A'], ['A', 'B'] - atitinkamų klausimų teisingi variantai

certificate.docx

Tai testo išlaikymo sertifikatas
jame automatiškai įrašomas testuojamojo vardas, pavardė bei data.
Užpildytas sertifikatas įrašomas vardu generated_doc.docx

user_answ.txt

Vartotojo parašyti atsakymai


README retai kas skaito, tai tada anekdotas:
Sėdi liūtas ir burba:
- Ech, priėmė į armiją, nuskuto plikai...
- Ne tave vieną!
Pasižiūri liūtas žemyn ir sako:
- Ko žiūri, žiurke?
- Aš ne žiurkė! Aš ežiukas!