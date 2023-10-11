import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdclinica2',
)
cursor = conexao.cursor()
nome_paciente = str(input("Digite o nome do paciente: "))
especialista = int(input("escolha o especialista:"
      "\n1- neurologista"
      "\n2- olftamologista"
      "\n3- ortopedista: \n "))
if especialista == 1:
    valor = 120
elif especialista == 2:
   valor = 150
elif especialista == 3:
    valor = 200
else:
    print("erro. digite o numero entre 1 e 3")
comando = f'INSERT INTO consultas (nome_paciente, consulta, valor) VALUES ("{nome_paciente}", "{especialista}", "{valor}")'
cursor.execute(comando)
conexao.commit()
#resultado = cursor.fatchall()


cursor.close()
conexao.close()