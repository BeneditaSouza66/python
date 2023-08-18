from funcionario import Funcionario
from gerente import Gerente
from diretor import Diretor
from secretario import Secretario
from presidente import Presidente

func1 = Funcionario('Maria', '111.111.111-11', 2500.00, '123456')
#func1.Autentica()
#func1.Cadastro()

ger1 = Gerente('José', '222.222.222-22', 3500.00, '123456789', 10)
#ger1.Autentica()
#ger1.Cadastro()

dir1 = Diretor('Marcos', '333.333.333-33', 4500.00, '1234')
#dir1.Autentica()
#dir1.Cadastro()

sec1 = Secretario('Josefa', '444.444.444-44', 2000.00, '123456')
#sec1.Autentica()
#sec1.Cadastro()

pre1 = Presidente('Paulo', '555.555.555-55', 10000.00, '1234567')
#pre1.Autentica()
pre1.Cadastro()
