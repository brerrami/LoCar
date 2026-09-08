# LoCar

Sistema de locação de veículos desenvolvido em Python para gerenciar clientes, veículos, reservas e histórico de operações.

## Funcionalidades

- Cadastro, listagem, busca e remoção de clientes
- Cadastro, listagem, busca e remoção de veículos
- Registro de reservas com controle de disponibilidade
- Fila FIFO para reservas
- Registro de devoluções
- Histórico de operações com estrutura LIFO
- Menu interativo no terminal

## Estrutura do projeto

- `pyfacu/main.py` - código principal da aplicação

## Requisitos

- Python 3.8 ou superior

## Como usar

1. Abra o terminal na raiz do projeto.
2. Execute o programa:

```bash
python pyfacu/main.py
```

3. No menu, escolha uma opção digitando o número correspondente:
   - 1: Cadastrar cliente
   - 2: Listar clientes
   - 3: Buscar cliente
   - 4: Remover cliente
   - 5: Cadastrar veículo
   - 6: Listar veículos
   - 7: Buscar veículo
   - 8: Remover veículo
   - 9: Fazer reserva
   - 10: Mostrar fila de reservas
   - 11: Atender próxima reserva
   - 12: Registrar devolução
   - 13: Mostrar histórico
   - 0: Sair

## Exemplo de uso

```text
========================================
LOCAR - SISTEMA DE LOCAÇÃO DE VEÍCULOS
========================================
1. Cadastrar cliente
2. Listar clientes
3. Buscar cliente
...
0. Sair
========================================
Escolha uma opção: 1
```

A partir daí, siga as instruções exibidas no terminal para cadastrar clientes, veículos e reservas.

## Observações

- O programa salva os dados apenas em memória durante a execução.
- Ao fechar o programa, os dados cadastrados são perdidos.
- A aplicação foi criada como um projeto simples de estudo/gerenciamento de locadora.
