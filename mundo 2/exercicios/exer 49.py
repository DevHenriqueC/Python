from time import sleep
tabuada = int(input('Quer saber a tabuada de qual numero?\n'))
for c in range(1, 11):
    print('{} x {} = {}'.format(tabuada, c, (tabuada * c)))
    sleep(1)
