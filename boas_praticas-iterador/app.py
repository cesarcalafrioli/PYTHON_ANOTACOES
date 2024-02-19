""" Uma alternativa para a lista (e também para a funcionalidade de compreensão de lista!) que consegue poupar memória,
trabalhando de outro jeito. Podemos até concluir que é boa prática usar iteradores em leitura de arquivos, por garantia."""
class IteradorHttp():
    def __init__(self):
        self.registro = open('acessos.log', 'r')
        self.linha_atual = ''
    def __iter__(self):
        return self
    def __next__(self):
        self.linha_atual = self.registro.readline()
        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()
        if self.linha_atual:
            return self.linha_atual
        raise StopIteration
    
iterador = IteradorHttp()

for url in iterador:
    print(url)