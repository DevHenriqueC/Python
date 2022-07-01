from datetime import date
an = int(input('Em qual ano você nasceu?\n'))
ae = date.today().year
if ae - an == 18:
    print('Você ja pode se alistar!!!')
elif ae - an < 18:
    ad = 18 - (ae-an)
    print('Você nao precisa se alistar agora, so daqui {} anos!'.format(ad))
elif ae - an > 18:
    at = (ae-an-18)
    print('Você ja deveria ter se alistado a {} anos atras!'.format(at))
