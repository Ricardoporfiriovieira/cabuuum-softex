from time import sleep

tempo = int(input("Inofrme a quantidade de segundos para a bomba explodir: "))
print("Iniciando contagem regressiva...")
for i in range(tempo, 0, -1):
    print(f"{i}")
    sleep(1)
print("BUM")