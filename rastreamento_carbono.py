# Sistema Simples de Rastreamento de Carbono
usuarios = {}
atividades = {}
sugestoes = {
    "energia": ["Troque lâmpadas comuns por LEDs.", "Desligue aparelhos da tomada quando não usados."],
    "transporte": ["Use transporte público.", "Adote caronas ou bicicleta para trajetos curtos."]
}


def registrar_usuario():
    print("\n--- Registro de Usuário ---")
    username = input("Digite seu nome de usuário: ")
    if username in usuarios:
        print("Usuário já existe!")
        return
    senha = input("Digite sua senha: ")
    usuarios[username] = senha
    atividades[username] = []
    print("Usuário registrado com sucesso!")


def login():
    print("\n--- Login ---")
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if username in usuarios and usuarios[username] == senha:
        print("Login realizado com sucesso!")
        return username
    else:
        print("Usuário ou senha incorretos!")
        return None


def registrar_atividade(usuario):
    print("\n--- Registro de Atividades ---")
    tipo = input("Digite o tipo de atividade (energia, transporte): ").lower()
    valor = float(input("Digite o valor da atividade (exemplo: kWh ou km): "))

    atividades[usuario].append({"tipo": tipo, "valor": valor})
    print("Atividade registrada com sucesso!")


def gerar_relatorio(usuario):
    print("\n--- Relatório de Emissões ---")
    if not atividades[usuario]:
        print("Nenhuma atividade registrada!")
        return

    relatorio = {}
    for atividade in atividades[usuario]:
        tipo = atividade["tipo"]
        relatorio[tipo] = relatorio.get(tipo, 0) + atividade["valor"]

    for tipo, total in relatorio.items():
        print(f"{tipo.capitalize()}: {total} unidades")
    print("Relatório gerado com sucesso!")


def sugerir_acoes(usuario):
    print("\n--- Sugestões de Redução ---")
    if not atividades[usuario]:
        print("Nenhuma atividade registrada para gerar sugestões!")
        return

    for atividade in atividades[usuario]:
        tipo = atividade["tipo"]
        if tipo in sugestoes:
            print(f"\nSugestões para {tipo.capitalize()}:")
            for sugestao in sugestoes[tipo]:
                print(f"- {sugestao}")


def menu_principal():
    print("\n--- Sistema de Rastreamento de Carbono ---")
    print("1. Registrar Usuário")
    print("2. Login")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")
    return opcao


def menu_usuario(usuario):
    while True:
        print("\n--- Menu do Usuário ---")
        print("1. Registrar Atividade")
        print("2. Gerar Relatório")
        print("3. Sugerir Ações")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            registrar_atividade(usuario)
        elif opcao == "2":
            gerar_relatorio(usuario)
        elif opcao == "3":
            sugerir_acoes(usuario)
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")


# Fluxo Principal
while True:
    opcao = menu_principal()
    if opcao == "1":
        registrar_usuario()
    elif opcao == "2":
        usuario = login()
        if usuario:
            menu_usuario(usuario)
    elif opcao == "3":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida!")
