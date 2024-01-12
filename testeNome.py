nome = 'Victor'
sobrenome = 'Tavares'
nascimento = 1988
ano_atual = 2024
aniversario_ano_atual = False

idade = ano_atual - nascimento if aniversario_ano_atual else (ano_atual - 1 - nascimento)

print(f'Estou fazendo aniversario {aniversario_ano_atual}')

lista = [['Por', 'fes', 'sor'], 'da', 'ByLearn', ':)']

if idade >= 18:
    dirigir = True
else:
    dirigir = False

animais = 'Gatos'

print(idade)

print(f'Tenho esses animais: {animais}')

print("posso dirigir? ", "Sim" if dirigir else "Não")