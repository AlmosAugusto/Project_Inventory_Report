from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mock = Product(
        17,
        'PS5',
        'Sony',
        '01/01/2020',
        '01/01/2023',
        '123456789',
        'Com cuidado'
    )

    assert str(mock) == (
        f"O produto {mock.nome_do_produto} "
        f"fabricado em {mock.data_de_fabricacao} por {mock.nome_da_empresa} "
        f"com validade até {mock.data_de_validade} precisa ser "
        f"armazenado {mock.instrucoes_de_armazenamento}."
    )
