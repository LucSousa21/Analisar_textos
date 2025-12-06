class AnalisadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def texto_minusculo(self):
        texto_minusculo = self.texto.lower()
        print(f"Texto em minúsculas: {texto_minusculo}")

    def numero_caracteres(self):
        numero_caracteres = len(self.texto)
        print(f"Número de caracteres: {numero_caracteres}")    

    def numero_palavras(self):
        numero_palavras = len(self.texto.split())
        print(f"Número de palavras: {numero_palavras}")

    def numero_frases(self):
        numero_frases = self.texto.count('.') + self.texto.count('!') + self.texto.count('?')
        print(f"Número de frases: {numero_frases}")

    def frequencia_palavras(self):
        dicionario_frequencia = {} 
        
        for palavra in self.texto.split():
            palavra = palavra.strip('.,!?;"\'()')
            if palavra:
                dicionario_frequencia[palavra] = dicionario_frequencia.get(palavra, 0) + 1
        
        print("Frequência das palavras:")
        for palavra, freq in sorted(dicionario_frequencia.items(), key=lambda x: x[1], reverse=True):
            print(f"  {palavra}: {freq}")



texto = AnalisadorTexto(input("Digite o texto a ser analisado: "))

texto.texto_minusculo()
texto.numero_caracteres()
texto.numero_palavras()
texto.numero_frases()
texto.frequencia_palavras()
