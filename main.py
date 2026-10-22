import pygame
import os
import time

def limpar():
    os.system('cls' if os.name == "nt" else 'clear')

play = True

pygame.init()
limpar()
base = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(base, "music")
pasta = os.listdir(caminho)

def tocar():
    try:
        music = input("digite o numero da musica que gostaria de ouvir:\n")
        if music.isnumeric():
            if int(music) == len(pasta)+1:
                print("Saindo...")
                limpar()
                global play
                play = False
                return
            music = pasta[int(music)-1].replace('.mp3','')
        print(f"Tocando {music}...")
        time.sleep(1)

        pygame.mixer.music.load(f"{caminho}/{music}.mp3")
        pygame.mixer.music.play()

        input("aperte ENTER para parar a musica")
        parar()

    except:
        print("Musica não encontrada, tente novamente")
        return tocar()

def parar():
    pygame.mixer.music.stop()
    limpar()
    return

while play == True:
    print(20*"=")
    print("Discoteca virtual")
    print(20*"=")
    print("\nAtualmente suas musicas são:")

    for i,musicas in enumerate(pasta, start=1):
        print(f"{i} - {musicas.replace('.mp3','')}")
    print(f"{len(pasta)+1} - Sair")
    tocar()
