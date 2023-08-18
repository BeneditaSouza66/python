from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtde_funcionarios):
        super().__init__(nome, cpf , salario, senha)
        self._qtde_funcionarios = qtde_funcionarios    
