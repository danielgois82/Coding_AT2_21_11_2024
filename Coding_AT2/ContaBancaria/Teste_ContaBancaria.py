# Teste dos métodos da classe ContaBancaria

from ContaBancaria import ContaBancaria

print('Testando a classe ContaBancaria:\n')

conta = ContaBancaria(1, 'Daniel')
print('Dados da Conta Bancaria ao Criar o Objeto ContaBancaria:')
print(f'Numero da conta: {conta.getNumeroConta()}, Titular: {conta.getTitular()}, Saldo R$: {conta.getSaldo():.2f}\n')

print('Depositando R$ 100,00:')
conta.depositar(100)
print(f'Saldo R$: {conta.getSaldo():.2f}\n')

print('Sacando R$ 50,00:')
conta.sacar(50)
print(f'Saldo R$: {conta.getSaldo():.2f}\n')

print('Tentando sacar R$ 200,00 e recebendo o aviso de saldo insuficiente:')
conta.sacar(200)
print(f'Saldo R$: {conta.getSaldo():.2f}\n')

print('Alterando os dados do numero da conta e nome do titular:')
conta.setNumeroConta(10)
conta.setTitular('Daniel Gois')
print('Dados da Conta Bancaria Alterados:')
print(f'Numero da conta: {conta.getNumeroConta()}, Titular: {conta.getTitular()}, Saldo R$: {conta.getSaldo():.2f}\n')
