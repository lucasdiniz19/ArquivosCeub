pagamentos = {
    "joao lucas": 300.00,
    "gabriel": 127.09 + 48 + 67.91 + 30,
    "marcus": 210.00,
    "leo": 31.19,
    "celia": 0,
    "estefano": 0,
    "vinicius": 0,
    "taina": 0,
    "pedro": 0,
    "leticia": 0,
    "matheus": 0,
    "beatriz": 0,
    "juraci": 0,
    "diana": 0,
    "jaqueline": 0,
}

num_pessoas = len(pagamentos)

total_gasto = sum(pagamentos.values())

valor_por_pessoa = total_gasto / num_pessoas

saldos = {nome: round(pago - valor_por_pessoa, 2) for nome, pago in pagamentos.items()}

a_receber = {nome: saldo for nome, saldo in saldos.items() if saldo > 0}
a_pagar = {nome: -saldo for nome, saldo in saldos.items() if saldo < 0}

a_receber = dict(sorted(a_receber.items(), key=lambda x: x[1], reverse=True))
a_pagar = dict(sorted(a_pagar.items(), key=lambda x: x[1], reverse=True))

transacoes = []
a_receber_copy = a_receber.copy()

for pagador, valor_pagar in a_pagar.items():
    while valor_pagar > 0 and a_receber_copy:
        recebedor, valor_receber = next(iter(a_receber_copy.items()))


        pagamento = min(valor_pagar, valor_receber)
        transacoes.append((pagador, recebedor, pagamento))

       
        valor_pagar = round(valor_pagar - pagamento, 2)
        a_receber_copy[recebedor] = round(valor_receber - pagamento, 2)

       
        if a_receber_copy[recebedor] == 0:
            del a_receber_copy[recebedor]


print(transacoes)