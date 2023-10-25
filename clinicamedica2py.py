import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdclinica2',
)
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



cursor.close()
conexao.close()

