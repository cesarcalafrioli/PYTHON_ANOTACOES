import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url(url)

    # Sanitização da url
    def sanitiza_url(self, url):
        if type(url) == url:
            return url.strip()
        else:
            return ""

    def valida_url(self, url):
        if not self.url:
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida")
        
    def get_url_baser(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        tamanho_parametro = len(parametro_busca)
        indice_valor = indice_parametro + tamanho_parametro + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

#extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real")

extrator_url = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)