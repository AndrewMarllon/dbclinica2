import mysql.connector
from datetime import date

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdclinica2',
)

#//CONSULTA////////////////////////////////////////////////////////////////////////////////

#cursor = conexao.cursor()
#nome_paciente = str(input("Digite o nome do paciente: "))
#especialista = int(input("escolha o especialista:"
      #"\n1- neurologista"
      #"\n2- olftamologista"
      #"\n3- ortopedista: \n "))

#if especialista == 1:
    #valor = 120
    #area = "Neurologista"
#elif especialista == 2:
   #valor = 150
   #area = "Olftamologista"
#elif especialista == 3:
    #valor = 200
    #area = "Ortopedista"
#else:
    #print("erro. digite o numero entre 1 e 3")
#comando = f'INSERT INTO consultas (nome_paciente, consulta, valor) VALUES ("{nome_paciente}", "{area}", "{valor}")'
#cursor.execute(comando)
#conexao.commit()
#resultado = cursor.fatchall()

#cursor = conexao.cursor()
#nome_paciente = "andrew"
#comando = f'DELETE FROM consultas WHERE nome_paciente = "{nome_paciente}"'
#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#nome_paciente = "mauricio"
#consulta = 1
#comando = f'UPDATE consultas SET nome_paciente = "{nome_paciente}" WHERE consulta = "{consulta}"'
#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#comando = f'SELECT * FROM consultas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

#//PACIENTE//////////////////////////////////////////////////////////////////////////

#cursor = conexao.cursor()
#nome_paciente = str(input("digite o nome do paciente: "))
#idade = int(input("digite a idade do paciente: "))
#CPF = int(input("digite o cpf: "))
#endereco = str(input("digite o endereço do paciente: "))
#cidade = str(input("digite a cidade: "))
#telefone = int(input("digite o numero de telefone: "))
#consulta = str(input("digite a consulta: "))

#comando = f'INSERT INTO paciente (nome_paciente, idade, CPF, endereco, bairro, cidade, telefone, consulta) VALUES ("{nome_paciente}", {idade}, {CPF}, "{endereco}", "{bairro}", "{cidade}", {telefone}, "{consulta}") '

#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#nome_paciente = "martlon"
#comando = f'DELETE FROM paciente WHERE nome_paciente = "{nome_paciente}"'
#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#nome_paciente = "ANDREWMBS"
#idade = 18
#comando = f'UPDATE paciente SET idade= {idade} WHERE nome_paciente = "{nome_paciente}"'
#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#comando = f'SELECT * FROM paciente'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)


#//MEDICO////////////////////////////////////////////////////////////////////////////////////////////////

#cursor = conexao.cursor()
#nome = str (input("digite o nome do medico: "))
#especialidade = str (input(" digite a especialidade: "))
#CRN = int (input("digite o CRN: "))
#CPF = int (input("digite o CPF: "))

#comando = f'INSERT INTO medico (nome, especialidade,CRN, CPF) VALUES ("{nome}", "{especialidade}",{CRN}, {CPF})'
#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#nome = "selem brandão"
#comando = f'DELETE FROM medico WHERE nome = "{nome}"'
#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#nome = ""
#CRN = ""
#comando = f'UPDATE medico SET CRN = {CRN} WHERE nome = "{nome}"'
#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#comando = f'SELECT * FROM medico'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)


#//EXAME////////////////////////////////////////////////////////////////////////////////////

#cursor = conexao.cursor()
#nome = str(input("digte o nome do paciente: "))
#CPF = int(input("digite o CPF: "))
#exame = str(input("exame: "))
#data = str(input("data do exame: "))
#medico = str(input(" medico: "))
#comando = f'INSERT INTO exames (nome, CPF, exame, data, medico) VALUES ("{nome}", {CPF}, "{exame}", {data}, "{medico}")'

#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#nome = "andrew"
#comando = f'DELETE FROM exames WHERE nome = "{nome}"'
#ursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#nome = ""
#medico = ""
#comando = f'UPDATE exames SET nome = {nome} WHERE medico = "{medico}"'
#cursor.execute(comando)
#conexao.commit()

#cursor = conexao.cursor()
#comando = f'SELECT * FROM exames'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

cursor.close()
conexao.close()

