usuario_correto = "admin"
senha_correta = "123456"
tentativas = 3

while tentativas > 0:
    print(f"\n--- Login (Tentativas restantes: {tentativas}) ---")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso! Bem-vindo.")
        break  
    else:
        tentativas -= 1  
        if tentativas > 0:
            print("Usuário ou senha incorretos. Tente novamente.")

if tentativas == 0:
    print("\nNúmero de tentativas excedido. Acesso bloqueado!")