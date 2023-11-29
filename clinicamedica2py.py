import mysql.connector
from datetime import date

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdclinica2',
)

#//CONSULTA////////////////////////////////////////////////////////////////////////////////


cursor = conexao.cursor()
variavel =int(input("O QUE VOCE DESEJA FAZER? \n1-consultas \n2-cadastrar paciente \n3-cadastrar medico \n4-adicionar exames \nESCOLHA UM!: "))

if variavel == 1:
    print("VOCE ESCOLHEU CONSULTAS!\n1_cadastrar\n2_deletar\n3_aterar\n4_vizualizar, ")
    variavel1 = int(input("digite um dos numeros, entre 1 e 4: "))
    if variavel1 == 1:
        nome_paciente = str(input("Digite o nome do paciente: "))
        especialidade = float(input("escolha o especialista:"
        "\n01- neurologista"
        "\n02- olftamologista"
        "\n03- ortopedista: \n "))

        if especialidade == 1:
            valor = 120
            area = "Neurologista"
        elif especialidade == 2:
            valor = 150
            area = "Olftamologista"
        elif especialidade == 3:
            valor = 200
            area = "Ortopedista"

            comando = f'INSERT INTO consultas (nome_paciente, consulta, valor) VALUES ("{nome_paciente}", "{area}", "{valor}")'
            cursor.execute(comando)
            conexao.commit()
            resultado = cursor.fetchall()
        else:
            print("erro. digite o numero entre 1 e 3")

    elif variavel1 == 2:
#cursor = conexao.cursor()
        nome_paciente = str(input("DIGITE O NOME DO PACIENTE: "))
        comando = f'DELETE FROM consultas WHERE nome_paciente = "{nome_paciente}"'
        cursor.execute(comando)
        conexao.commit()
    elif variavel1 == 3:
#cursor = conexao.cursor()

        nome_paciente = str(input("DIGITE O NOME DO PACIENTE: "))
        consulta = str(input("digite o nome da consulta: "))
        comando = f'UPDATE consultas SET nome_paciente = "{nome_paciente}" WHERE consulta = "{consulta}"'
        cursor.execute(comando)
        conexao.commit()
    elif variavel1:
#cursor = conexao.cursor()
        comando = f'SELECT * FROM consultas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)

#//PACIENTE//////////////////////////////////////////////////////////////////////////



elif variavel == 2:
    print("VOCE ESCOLHEU PACIENTE!\n1_cadastrar\n2_deletar\n3_aterar\n4_vizualizar, ")
    variavel2 = int(input("digite um dos numeros, entre 1 e 4: "))
#cursor = conexao.cursor()
    if variavel2 == 1:
        nome_paciente = str(input("digite o nome do paciente: "))
        idade = int(input("digite a idade do paciente: "))
        CPF = int(input("digite o cpf: "))
        endereco = str(input("digite o endereço do paciente: "))
        bairro = str(input("nome do bairro: "))
        cidade = str(input("digite a cidade: "))
        telefone = int(input("digite o numero de telefone: "))
        consulta = str(input("digite a consulta: "))
        comando = f'INSERT INTO paciente (nome_paciente, idade, CPF, endereco, bairro, cidade, telefone, consulta) VALUES ("{nome_paciente}", {idade}, {CPF}, "{endereco}", "{bairro}", "{cidade}", {telefone}, "{consulta}") '
        cursor.execute(comando)
        conexao.commit()
    elif variavel2 == 2:
#cursor = conexao.cursor()
        nome_paciente = str(input("DIGITE O NOME DO PACIENTE: "))
        comando = f'DELETE FROM paciente WHERE nome_paciente = "{nome_paciente}"'
        cursor.execute(comando)
        conexao.commit()
    elif variavel2 == 3:
#cursor = conexao.cursor()
        nome_paciente = "ANDREWMBS"
        idade = 18
        comando = f'UPDATE paciente SET idade= {idade} WHERE nome_paciente = "{nome_paciente}"'
        cursor.execute(comando)
        conexao.commit()
    elif variavel2 == 4:
#cursor = conexao.cursor()
        comando = f'SELECT * FROM paciente'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)


#//MEDICO////////////////////////////////////////////////////////////////////////////////////////////////



elif variavel == 3:
    print("VOCE ESCOLHEU MEDICO!\n1_cadastrar\n2_deletar\n3_aterar\n4_vizualizar, ")
    variavel3 = int(input("digite um dos numeros, entre 1 e 4: "))
#cursor = conexao.cursor()
    if variavel3 == 1:
        nome=str(input("digite o nome do medico: "))
        especialidade=str(input("digite a especialidade: "))
        CRN=int(input("digite o CRN: "))
        CPF=int(input("digite o CPF: "))
        comando = f'INSERT INTO medico (nome, especialidade,CRN, CPF) VALUES ("{nome}", "{especialidade}",{CRN}, {CPF})'
        cursor.execute(comando)
        conexao.commit()
    elif variavel3 == 2:
#cursor = conexao.cursor()
        nome = str(input("DIGITE O NOME DO PACIENTE: "))
        comando = f'DELETE FROM medico WHERE nome = "{nome}"'
        cursor.execute(comando)
        conexao.commit()
    elif variavel3 == 3:
#cursor = conexao.cursor()
        nome =str(input("DIGITE O NOME DO PACIENTE: "))
        CRN = int(input("DIGITE O CRN DO PACIENTE: "))
        comando = f'UPDATE medico SET CRN = {CRN} WHERE nome = "{nome}"'
        cursor.execute(comando)
        conexao.commit()
    elif variavel3 == 4:
#cursor = conexao.cursor()
        comando = f'SELECT * FROM medico'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)


#//EXAME////////////////////////////////////////////////////////////////////////////////////



elif variavel == 4:
    print("VOCE ESCOLHEU EXAMES!\n1_cadastrar\n2_deletar\n3_aterar\n4_vizualizar, ")
    variavel4 = int(input("digite um dos numeros, entre 1 e 4: "))
#cursor = conexao.cursor()
    if variavel4 == 1:
        nome = str(input("digte o nome do paciente: "))
        CPF = int(input("digite o CPF: "))
        exame = str(input("exame: "))
        data = str(input("data do exame: "))
        medico = str(input(" medico: "))
        comando = f'INSERT INTO exames (nome, CPF, exame, data, medico) VALUES ("{nome}", {CPF}, "{exame}", {data}, "{medico}")'

        cursor.execute(comando)
        conexao.commit()
    elif variavel4 == 2:
#cursor = conexao.cursor()
        nome = str(input("DIGITE O NOME DO PACIENTE: "))
        comando = f'DELETE FROM exames WHERE nome = "{nome}"'
        cursor.execute(comando)
        conexao.commit()
    elif variavel4 == 3:
#cursor = conexao.cursor()
        nome = str(input("DIGITE O NOME DO PACIENTE: "))
        medico = str(input("DIGITE O NOME DO MEDICO: "))
        comando = f'UPDATE exames SET nome = {nome} WHERE medico = "{medico}"'
        cursor.execute(comando)
        conexao.commit()
    elif variavel4 == 4:
#cursor = conexao.cursor()
        comando = f'SELECT * FROM exames'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)

cursor.close()
conexao.close()

