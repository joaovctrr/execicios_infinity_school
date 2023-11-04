lista_ocorrencia = []

def ocorrencia():

    ocorrencias = {
        'Batalhao' : input('Area do Batalhao:'),
        'Turno' : int(input('Turno: 1,2 ou 3')),
        'Número de integrantes da guarnição': int(input('Número de integrantes da guarnição: ')),
        'Comandante da guarnição': input('Comandante da guarnição: '),
        'Integrante da guarnição 2': None,
        'Integrante da guarnição 3': None,
        'Integrante da guarnição 4': None,
        'Integrante da guarnição 5': None,
        'Integrante da guarnição 6': None,
        'Quantidade de ocorrências atendidas' : int(input('Quantidade de ocorrencias de trânsito registradas: ')),
        'Fatal' : input('Houve ocorrência fatal? S/N'),
        'Quantidade de ocorrências com vítimas fatais' : 0,
        'Quantidade de ocorrências com vitima' : int(input('Quantidade de ocorrências de trânsito com vítima: ')),
        'Quantidade de ocorrêcias sem vítima': 0,
        'Quantidade de TIP': int(input('Número de ocorrências envolvendo Transporte Irregular de Passageiros: ')),
        'Veículos Recuperados': 0,
        'Veículos Removidos': int(input('Número de veículos removidos: ')),
        'Ocorrências sem envolvimento com trânsito' : input('Houve registros alheios à trânsito? S/N: '),
        'Receptação': 0,
        'Uso e consumo' : 0,
        'Tráfico de drogas' : 0,
        'Porte ilegal de arma de fogo' : 0
    	}

    ocorrencias['Quantidade de ocorrêcias sem vítima'] = ocorrencias['Quantidade de ocorrências atendidas'] - ocorrencias['Quantidade de ocorrências com vitima']
    
    if (ocorrencias['Fatal']).lower() == 's':
        ocorrencias['Quantidade de ocorrências com vítimas fatais'] = int(input('Quantas ocorrencias fatais?'))
        ocorrencias['Quantidade de ocorrências com vitima'] -= ocorrencias['Quantidade de ocorrências com vítimas fatais']
    elif (ocorrencias['Fatal']).lower() == 'n':
        ocorrencias['Quantidade de ocorrências com vítimas fatais'] = 0

    if ocorrencias['Número de integrantes da guarnição'] == 2:
        ocorrencias[ 'Integrante da guarnição 2'] = input('Integrante da guarnição: ')
    elif ocorrencias['Número de integrantes da guarnição'] == 3:
        ocorrencias[ 'Integrante da guarnição 2'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 3'] = input('Integrante da guarnição: ')
    elif ocorrencias['Número de integrantes da guarnição'] == 4:
        ocorrencias[ 'Integrante da guarnição 2'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 3'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 4'] = input('Integrante da guarnição: ')
    elif ocorrencias['Número de integrantes da guarnição'] == 5:
        ocorrencias[ 'Integrante da guarnição 2'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 3'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 4'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 5'] = input('Integrante da guarnição: ')
    elif ocorrencias['Número de integrantes da guarnição'] == 6:
        ocorrencias[ 'Integrante da guarnição 2'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 3'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 4'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 5'] = input('Integrante da guarnição: ')
        ocorrencias[ 'Integrante da guarnição 6'] = input('Integrante da guarnição: ')

    if ocorrencias['Ocorrências sem envolvimento com trânsito'].lower() == 's':
        ocorrencias['Veículos Recuperados'] = int(input('Quantidada de veículos recuperados: '))
        ocorrencias['Receptação'] = int(input('Numero de ocorrências envolvendo receptação: '))
        ocorrencias['Uso e consumo'] = int(input('Numero de ocorrências envolvendo uso e consumo: '))
        ocorrencias['Tráfico de drogas'] = int(input('Numero de ocorrências envolvendo tráfico de drogas: '))
        ocorrencias['Porte ilegal de arma de fogo'] = int(input('Numero de ocorrências envolvendo porte ilegal de armas de fogo: '))
    elif ocorrencias['Ocorrências sem envolvimento com trânsito'].lower() == 'n':
        ocorrencias['Veículos Recuperados'] = 0
        ocorrencias['Receptação'] = 0
        ocorrencias['Uso e consumo'] = 0
        ocorrencias['Tráfico de drogas'] = 0
        ocorrencias['Porte ilegal de arma de fogo'] = 0



    return ocorrencias


while True:
    
    comando = input('Iniciar ou Finalizar')
    
    if comando == 'iniciar':

        ocorrencias = ocorrencia()

        lista_ocorrencia.append(ocorrencias)

    elif comando == 'finalizar':

        break
