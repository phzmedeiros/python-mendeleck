from machine import Pin
from utime import sleep

vermelho_esquerdo = Pin(4, Pin.OUT)
amarelo_esquerdo = Pin(2, Pin.OUT)
verde_esquerdo = Pin(15, Pin.OUT)

vermelho_direito = Pin(14, Pin.OUT)
amarelo_direito = Pin(12, Pin.OUT)
verde_direito = Pin(13, Pin.OUT)

while True:
    verde_esquerdo.on(); amarelo_esquerdo.off(); vermelho_esquerdo.off()
    verde_direito.off(); amarelo_direito.off(); vermelho_direito.on()
    sleep(5)

    verde_esquerdo.off(); amarelo_esquerdo.on(); vermelho_esquerdo.off()
    verde_direito.off(); amarelo_direito.off(); vermelho_direito.on()
    sleep(5)

    verde_esquerdo.off(); amarelo_esquerdo.off(); vermelho_esquerdo.on()
    verde_direito.on(); amarelo_direito.off(); vermelho_direito.off()
    sleep(5)

    verde_esquerdo.off(); amarelo_esquerdo.off(); vermelho_esquerdo.on()
    verde_direito.off(); amarelo_direito.on(); vermelho_direito.off()
    sleep(5)
