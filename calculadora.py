def adicao(n1, n2):
    return n1 + n2
def subtracao(n1, n2):
    return n1 - n2
def multiplicacao(n1, n2):
    return n1 * n2
def divisao(n1, n2):
    return n1 / n2

print(' +-+-+-+-+-+-+-+-+-+-+-CALCULADORA+-+-+-+-+-+-+-+-+-+-+')
print('__________________________________________________________')
print('')
print('1. Adição • 2. Subtração • 3. Multiplicação • 4. Divisão ')
print('•••••••• Para encerrar a aplicação, pressione 0 •••••••••')
print('__________________________________________________________')
print('')

count = 0


while True:
    
    operacao = int(input('Escolha sua operação seguindo os parâmetros acima: 1, 2, 3, 4 ou 0.'))

    if operacao == 0:
        print('Você encerrou a calculadora.')
        break

    elif operacao != 0:

        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))

        if operacao == 1:
            print(f'O resultado da operção {numero1} + {numero2} é = {adicao(numero1, numero2)}') 
        if operacao == 2:
            print(f'O resultado da operção {numero1} - {numero2} é = {subtracao(numero1, numero2)}')
        if operacao == 3:
            print(f'O resultado da operção {numero1} * {numero2} é = {multiplicacao(numero1, numero2)}')
        if operacao == 4 and numero2 == 0:
            print('Não é possível efetuar a divisão por 0')
        elif operacao == 4:
            print(f'O resultado da operção {numero1} / {numero2} é = {divisao(numero1, numero2)}')
        print('__________________________________________________________')
    
count += 1
