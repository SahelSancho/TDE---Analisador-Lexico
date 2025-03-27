import re

tokens = [
    (r'\b(inteiro|real|cadeia|se|senao|enquanto|procedimento|funcao|retorna|inicio|fim|escreva|leia)\b', 'PALAVRA_CHAVE'),
    (r'\d+\.\d+', 'NUM_REAL'),
    (r'\d+', 'NUM_INTEIRO'),
    (r'"[^"]*"', 'CADEIA'),
    (r'\b[a-zA-Z_]\w*\b', 'IDENTIFICADOR'),
    (r'[+\-*/%]', 'OPERADOR_ARITMETICO'),
    (r'&&|\|\||!', 'OPERADOR_LOGICO'),
    (r'>=|<=|!=|==|>|<', 'OPERADOR_COMPARACAO'),
    (r'[;{}()=]', 'SIMBOLO')
]

def analisador_lexico(codigo):
    resultado = []
    while codigo:
        codigo = codigo.lstrip()
        if not codigo:
            break
        
        for padrao, tipo in tokens:
            match = re.match(padrao, codigo)
            if match:
                resultado.append((tipo, match.group(0)))
                codigo = codigo[len(match.group(0)):]
                break
        else:
            if codigo:
                raise ValueError(f"Erro léxico: símbolo desconhecido '{codigo[0]}'")
            else:
                break

    return resultado


codigo_exemplo = """
inteiro x;
x = 10;
se (x > 5) {
    escreva("Valor maior que 5");
}
enquanto (x < 100) {
    x = x + 1;
}
"""

resultado = analisador_lexico(codigo_exemplo)
for token in resultado:
    print(token)