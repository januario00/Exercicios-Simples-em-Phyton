#Faça um programa em Phyton que abre e reproduza o audio de um arquivo MP3.


#NAO RODOU
#import pygame
#pygame.init()
#pygame.mixer.music.load('ex021.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()



import pygame
import time   # O import time é usado para controlar o tempo de espera enquanto o áudio ainda está sendo reproduzido.

# Inicializa o pygame (necessário para qualquer funcionalidade do pygame)
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("ex021.mp3")

# Inicia a reprodução do áudio
pygame.mixer.music.play()

# Enquanto a música estiver tocando, o loop continua
while pygame.mixer.music.get_busy():
    time.sleep(1)  # Espera 1 segundo antes de verificar novamente se a música ainda está tocando


