import pyautogui as pg
import time

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


# Loop para enviar a mensagem
for i in range(0, quantidade):
    for msg in mensagens:
        pg.write(msg)
        time.sleep(0.5)
        pg.press("enter")
        time.sleep(0.5)

print("Mensagens enviadas com sucesso!")