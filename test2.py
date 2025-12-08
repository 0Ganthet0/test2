from smtplib import bCRLF
from tkinter import *
import bcrypt
from tkinter import messagebox
# https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt
# pip install bcrypt
def zaszyfrujHaslo(haslo):
    bajty = haslo.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bajty, salt)
    return hash
def zaloguj_sie():
    messagebox.showinfo("Udalo sie!", "Pomyslnie zalogowano!")

def nie_pokazuj_hasla():
    entry_haslo.config(show="*")
    pokaz_haslo_button.config(text="Pokaz", command=pokaz_haslo)

def pokaz_haslo():
    entry_haslo.config(show="")
    pokaz_haslo_button.config(text="Nie pokazuj", command=nie_pokazuj_hasla)

def klik():
    print("Tutaj zmieni na rejestracje")

okno = Tk()

okno.title("Księgarnia")
okno.geometry('430x300')

tekst_zaloguj = Label(okno, text="Zaloguj")
tekst_zaloguj.grid(row=0,padx=5, pady=5)

tekst_login = Label(okno, text="Login: ")
tekst_login.grid(row=1,padx=5, pady=5)

entry_login = Entry(okno)
entry_login.grid(row=2,padx=5, pady=5)


tekst_haslo = Label(okno, text="Hasło: ")
tekst_haslo.grid(row=3,padx=5, pady=5)

entry_haslo = Entry(okno, show="*")
entry_haslo.grid(row=4,column=0,padx=5, pady=5)


pokaz_haslo_button = Button(okno, text="Pokaz", command=pokaz_haslo)
pokaz_haslo_button.grid(row=5,padx=15, pady=5)



zaloguj = Button(okno, text="Zaloguj", command=zaloguj_sie)
tekst_rejestracja = Label(okno, text=f"Jesli nie masz konta to")
rejestracja = Label(okno, text=f"Stwórz Konto", fg='blue', cursor="hand2")

zaloguj.grid(row=6,padx=5, pady=5)

tekst_rejestracja.grid(row=7)
rejestracja.grid(row=8)
rejestracja.bind("<Button-1>",lambda event:klik())

okno.grid_columnconfigure(0,weight=1)


okno.mainloop()
