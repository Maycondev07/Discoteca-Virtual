import pygame
import os
import time

pygame.init()
os.system('cls' if os.name == "nt" else 'clear')
base = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(base, "music")
pasta = os.listdir(caminho)

def tocar():
    try:
        music = input("digite exatamente o nome da musica que gostaria de ouvir:\n")
        print(f"Tocando {music}...")
        time.sleep(1)

        pygame.mixer.music.load(caminho+"/"+music+".mp3")
        pygame.mixer.music.play()

        input("aperte ENTER para parar a musica")
        parar()

    except:
        print("Musica não encontrada, tente novamente")
        return tocar()

def parar():
    pygame.mixer.music.stop()
    os.system('cls' if os.name == "nt" else 'clear')
    return inicio()

def inicio():
    print(20*"=")
    print("Discoteca virtual")
    print(20*"=")
    print("\nAtualmente suas musicas são:")

    for i,musicas in enumerate(pasta, start=1):
        print(f"{i} - {musicas.replace('.mp3','')}")
    tocar()

inicio()
