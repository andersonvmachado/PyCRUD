def parser_pessoa(pessoa):
    if not pessoa:
        return
    return {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'email': pessoa.email,
            'salario': pessoa.salario,
            'dt_nascimento': str(pessoa.dt_nascimento)
            }