from golos.amount import Amount


def test_amount_init():
    a = Amount('1 GOLOS')
    assert dict(a) == {'amount': 1.0, 'asset': 'GOLOS'}
