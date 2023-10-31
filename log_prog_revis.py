numero_de_alunos = int(input('Quantos alunos há na sala? '))
soma_idade = 0
count = 0

for aluno in range(numero_de_alunos):
    idade = int(input('Qual a idade do aluno?'))

    while count <= aluno:
        soma_idade += idade 
        count += 1
        

print(f'A soma das idades dos alunos desta turma é: {soma_idade} anos.')
print(f'A média de idade da turma é: {soma_idade/numero_de_alunos} anos')
