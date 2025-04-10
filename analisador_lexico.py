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


def exportar_tabela_simbolos_html(tokens):
    html_content = """
    <html>
    <head>
        <title>Tabela de Símbolos</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>Tabela de Símbolos</h1>
        <table>
            <thead>
                <tr>
                    <th>Tipo</th>
                    <th>Valor</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for tipo, valor in tokens:
        html_content += f"""
        <tr>
            <td>{tipo}</td>
            <td>{valor}</td>
        </tr>
        """
    
    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """
    
    with open("tabela_simbolos.html", "w") as f:
        f.write(html_content)
    print("Tabela de símbolos exportada para tabela_simbolos.html")


# Exemplo de código
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

# Exibindo os tokens
for token in resultado:
    print(token)

# Exportando a tabela de símbolos para HTML
exportar_tabela_simbolos_html(resultado)
