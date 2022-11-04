from inventory_report.inventory.product import Product


def test_cria_produto():
    mock = Product(
        17,
        'PS5',
        'Sony',
        '01/01/2020',
        '01/01/2023',
        '123456789',
        'Com cuidado'
    )

    assert mock.id == 17
    assert mock.nome_do_produto == 'PS5'
    assert mock.nome_da_empresa == 'Sony'
    assert mock.data_de_fabricacao == '01/01/2020'
    assert mock.data_de_validade == '01/01/2023'
    assert mock.numero_de_serie == '123456789'
    assert mock.instrucoes_de_armazenamento == 'Com cuidado'
