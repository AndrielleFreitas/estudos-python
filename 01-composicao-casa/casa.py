class Quarto:
    def __init__(self, qnt_camas):
        self.qnt_camas = qnt_camas
        
class Cozinha:
    def __init__(self, tem_geladeira):
        self. tem_geladeira = tem_geladeira

class Banheiro:
    def __init__(self, qnt_chuveiro):
        self.qnt_chuveiro = qnt_chuveiro
        
class Casa:
    def __init__(self, quarto, cozinha, banheiro):
        self.quarto = quarto
        self.cozinha = cozinha
        self.banheiro = banheiro
    def exibir_comodos(self):
        print(f'INFORMAÇÕES DA CASA')
        print(f'Quarto: {self. quarto. qnt_camas} cama(s)')
        print(f'Cozinha: {"Possui geladeira" if self.cozinha.tem_geladeira else "Não possui"}')
        print (f'Banheiro: {self.banheiro.qnt_chuveiro} chuveiro(s)')
    
quarto = Quarto (2)
cozinha = Cozinha (True)
banheiro = Banheiro (2)

casa1 = Casa(quarto, cozinha, banheiro)
casa1.exibir_comodos()
