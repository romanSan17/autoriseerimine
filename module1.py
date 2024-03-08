from gtts import *
from os import system

def loe_failist(fail:str)->list:
    """Loeme failist read ja salvestame järjendisse. Funktsioon tagastab järjend
    :param str fail:
    :rtype: list
    """
    f=open(fail,'r',encording="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str,jarjend=[]):
    """
    """
    n=int(input("Sisesta mitu elementi: "))
    for i in range(n):
        jarjend.append(input(f"{i+1}. element: "))
    f=open(fail,'w',encording="utf-8")
    for el in jarjend:
        f.write(el+"\n")
    f.close()

def heli(tekst:str,kell:str):
    obj=gTTS(text=tekst,lang=kell,slow=False).save("heli.mp3")
    system("heli.mp3")

tekst=input("Sisesta tekst: ")
heli(tekst, 'en')

kirjuta_failisse("Text.txt")

paevad=loe_failist("Paevad.txt")
print(paevad)