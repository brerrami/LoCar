from collections import deque
from datetime import datetime

# Estruturas do sistema
clientes = []
clientes_por_cpf = {}
veiculos = []
veiculos_por_placa = {}
reservas = deque()
historico = []


def registrar_operacao(tipo, descricao):
    historico.append({
        "tipo": tipo,
        "descricao": descricao,
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })


def cadastrar_cliente():
    print("\n=== CADASTRO DE CLIENTE ===")
    nome = input("Digite o nome do cliente: ").strip()
    cpf = input("Digite o CPF do cliente: ").strip()
    telefone = input("Digite o telefone do cliente: ").strip()

    if not nome or not cpf:
        print("Nome e CPF são obrigatórios.")
        return

    if cpf in clientes_por_cpf:
        print("CPF já cadastrado.")
        return

    cliente = {"nome": nome, "cpf": cpf, "telefone": telefone}
    clientes.append(cliente)
    clientes_por_cpf[cpf] = cliente

    registrar_operacao("cliente", f"Cliente cadastrado: {nome} ({cpf})")
    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    print("\n=== CLIENTES CADASTRADOS ===")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for indice, cliente in enumerate(clientes, start=1):
        print(f"{indice}. Nome: {cliente['nome']} | CPF: {cliente['cpf']} | Tel: {cliente['telefone']}")


def buscar_cliente():
    print("\n=== BUSCAR CLIENTE ===")
    cpf = input("Digite o CPF do cliente: ").strip()
    cliente = clientes_por_cpf.get(cpf)

    if not cliente:
        print("Cliente não encontrado.")
        return

    print(f"Nome: {cliente['nome']}")
    print(f"CPF: {cliente['cpf']}")
    print(f"Telefone: {cliente['telefone']}")


def remover_cliente():
    print("\n=== REMOVER CLIENTE ===")
    cpf = input("Digite o CPF do cliente: ").strip()
    cliente = clientes_por_cpf.get(cpf)

    if not cliente:
        print("Cliente não encontrado.")
        return

    clientes.remove(cliente)
    del clientes_por_cpf[cpf]
    registrar_operacao("cliente", f"Cliente removido: {cliente['nome']} ({cpf})")
    print("Cliente removido com sucesso!")


def cadastrar_veiculo():
    print("\n=== CADASTRO DE VEÍCULO ===")
    marca = input("Digite a marca: ").strip()
    modelo = input("Digite o modelo: ").strip()
    placa = input("Digite a placa: ").strip().upper()
    ano = input("Digite o ano: ").strip()
    categoria = input("Digite a categoria: ").strip()
    diaria = input("Digite o valor da diária (ex.: 150.00): ").strip().replace(",", ".")

    if not marca or not modelo or not placa:
        print("Marca, modelo e placa são obrigatórios.")
        return

    try:
        diaria = float(diaria)
    except ValueError:
        print("Valor da diária inválido.")
        return

    if placa in veiculos_por_placa:
        print("Placa já cadastrada.")
        return

    veiculo = {
        "marca": marca,
        "modelo": modelo,
        "placa": placa,
        "ano": ano,
        "categoria": categoria,
        "diaria": diaria,
        "disponivel": True,
    }

    veiculos.append(veiculo)
    veiculos_por_placa[placa] = veiculo
    registrar_operacao("veiculo", f"Veículo cadastrado: {marca} {modelo} - {placa}")
    print("Veículo cadastrado com sucesso!")


def listar_veiculos():
    print("\n=== VEÍCULOS CADASTRADOS ===")
    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return

    for indice, veiculo in enumerate(veiculos, start=1):
        status = "Disponível" if veiculo["disponivel"] else "Alugado"
        print(f"{indice}. {veiculo['marca']} {veiculo['modelo']} | Placa: {veiculo['placa']} | Status: {status} | Diária: R$ {veiculo['diaria']:.2f}")


def buscar_veiculo():
    print("\n=== BUSCAR VEÍCULO ===")
    placa = input("Digite a placa do veículo: ").strip().upper()
    veiculo = veiculos_por_placa.get(placa)

    if not veiculo:
        print("Veículo não encontrado.")
        return

    status = "Disponível" if veiculo["disponivel"] else "Alugado"
    print(f"Marca: {veiculo['marca']}")
    print(f"Modelo: {veiculo['modelo']}")
    print(f"Placa: {veiculo['placa']}")
    print(f"Ano: {veiculo['ano']}")
    print(f"Categoria: {veiculo['categoria']}")
    print(f"Diária: R$ {veiculo['diaria']:.2f}")
    print(f"Status: {status}")


def remover_veiculo():
    print("\n=== REMOVER VEÍCULO ===")
    placa = input("Digite a placa do veículo: ").strip().upper()
    veiculo = veiculos_por_placa.get(placa)

    if not veiculo:
        print("Veículo não encontrado.")
        return

    veiculos.remove(veiculo)
    del veiculos_por_placa[placa]
    registrar_operacao("veiculo", f"Veículo removido: {veiculo['marca']} {veiculo['modelo']} - {placa}")
    print("Veículo removido com sucesso!")


def fazer_reserva():
    print("\n=== FAZER RESERVA ===")
    cpf = input("Digite o CPF do cliente: ").strip()
    placa = input("Digite a placa do veículo: ").strip().upper()
    data_inicio = input("Digite a data de início (DD/MM/AAAA): ").strip()
    data_fim = input("Digite a data final (DD/MM/AAAA): ").strip()

    cliente = clientes_por_cpf.get(cpf)
    veiculo = veiculos_por_placa.get(placa)

    if not cliente:
        print("Cliente não cadastrado.")
        return

    if not veiculo:
        print("Veículo não encontrado.")
        return

    if not veiculo["disponivel"]:
        print("Veículo indisponível para reserva.")
        return

    reserva = {
        "cliente": cliente["nome"],
        "cpf": cpf,
        "veiculo": f"{veiculo['marca']} {veiculo['modelo']}",
        "placa": placa,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
    }

    reservas.append(reserva)
    veiculo["disponivel"] = False
    registrar_operacao("reserva", f"Reserva registrada: {cliente['nome']} - {placa} ({data_inicio} a {data_fim})")
    print("Reserva registrada com sucesso!")


def mostrar_fila_reservas():
    print("\n=== FILA DE RESERVAS (FIFO) ===")
    if not reservas:
        print("Nenhuma reserva em espera.")
        return

    for indice, reserva in enumerate(reservas, start=1):
        print(f"{indice}. Cliente: {reserva['cliente']} | CPF: {reserva['cpf']} | Veículo: {reserva['veiculo']} | Placa: {reserva['placa']} | Período: {reserva['data_inicio']} até {reserva['data_fim']}")


def atender_proxima_reserva():
    print("\n=== ATENDER PRÓXIMA RESERVA ===")
    if not reservas:
        print("Nenhuma reserva na fila.")
        return

    reserva = reservas.popleft()
    placa = reserva["placa"]

    veiculo = veiculos_por_placa.get(placa)
    if veiculo:
        veiculo["disponivel"] = True

    registrar_operacao("locacao", f"Reserva atendida: {reserva['cliente']} - {placa}")
    print(f"Próxima reserva atendida: {reserva['cliente']} | {reserva['veiculo']} | {reserva['placa']}")


def registrar_devolucao():
    print("\n=== REGISTRAR DEVOLUÇÃO ===")
    placa = input("Digite a placa do veículo devolvido: ").strip().upper()
    veiculo = veiculos_por_placa.get(placa)

    if not veiculo:
        print("Veículo não encontrado.")
        return

    veiculo["disponivel"] = True
    registrar_operacao("devolucao", f"Veículo devolvido: {placa}")
    print("Devolução registrada com sucesso!")


def mostrar_historico():
    print("\n=== HISTÓRICO DE OPERAÇÕES (PILHA/LIFO) ===")
    if not historico:
        print("Nenhum registro de operação.")
        return

    for operacao in reversed(historico):
        print(f"{operacao['data_hora']} | {operacao['tipo']} | {operacao['descricao']}")


def menu():
    while True:
        print("\n========================================")
        print("LOCAR - SISTEMA DE LOCAÇÃO DE VEÍCULOS")
        print("========================================")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Remover cliente")
        print("5. Cadastrar veículo")
        print("6. Listar veículos")
        print("7. Buscar veículo")
        print("8. Remover veículo")
        print("9. Fazer reserva")
        print("10. Mostrar fila de reservas")
        print("11. Atender próxima reserva")
        print("12. Registrar devolução")
        print("13. Mostrar histórico")
        print("0. Sair")
        print("========================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "4":
            remover_cliente()
        elif opcao == "5":
            cadastrar_veiculo()
        elif opcao == "6":
            listar_veiculos()
        elif opcao == "7":
            buscar_veiculo()
        elif opcao == "8":
            remover_veiculo()
        elif opcao == "9":
            fazer_reserva()
        elif opcao == "10":
            mostrar_fila_reservas()
        elif opcao == "11":
            atender_proxima_reserva()
        elif opcao == "12":
            registrar_devolucao()
        elif opcao == "13":
            mostrar_historico()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
