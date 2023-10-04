import pyautogui as pg
import time

#Digite o nome do contato ou grupo
contato = input("Digite o nome do contato ou grupo: ")

# Numero de mensagens
quantidade = int(input("Digite a quantidade de mensagens que deseja enviar: "))

# Mensagens a serem enviadas
mensagens = []
for i in range(0, quantidade):
    print("Obs: Não digite acentos")
    print("Mensagem", i+1)
    msg = input("Digite a mensagem a ser enviada: ")
    mensagens.append(msg)

# Quantidade de vezes que a mensagem será enviada
quantidade = int(input("Digite a quantidade de vezes que deseja enviar a(s) mensagem(s): "))

# Tempo para abrir o chat no whatsapp web
print("Programa iniciando em...")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Iniciando...")

pg.press("win")
pg.write("Google Chrome")
pg.press("enter")
time.sleep(1)
pg.write("https://web.whatsapp.com/")
pg.press("enter")
time.sleep(10)
pg.press("tab", presses=7)
pg.write(contato)
time.sleep(1)
pg.press("tab", presses=2)
pg.press("enter")
time.sleep(1)

# Loop para enviar a mensagem
for i in range(0, quantidade):
    for msg in mensagens:
        pg.write(msg)
        time.sleep(0.5)
        pg.press("enter")
        time.sleep(0.5)

print("Mensagens enviadas com sucesso!")