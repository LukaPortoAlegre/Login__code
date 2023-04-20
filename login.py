from time import sleep
print('-----> Seja Bem-vindo <-----\n')
usuário=input('Vamos criar seu usuário, insira seu nome sem @ e hotmail/gmail: ')+'@hotmail.com'
print(usuário + '', 'Criado\n')
sleep(1)

senha=input('insira uma senha que contenha @ com no minimo 5 letras e máximo 9 letras: ')
    
while '@' not in senha or (len(senha) <=5 or len(senha) >12):
    print=('Senha muito curta')
    senha=input('insira uma senha que contenha @ com no minimo 5 letras e máximo 9 letras: ')
else:
    print('Usuário criado\n')

sleep(1)

acesso=input("Login: ")
while acesso!=usuário:
    print('Conta inexistente') 
    acesso=input('Login: ')

login_senha=input('Senha: ')   

while login_senha != senha:
    print("SENHA INCORRETA")
    login_senha=input("Senha: ")
else:
    print('Acessando...\n')
sleep(2)
print("--------> Bem vindo <--------\n") 