def test_funktion():
    def inner_funktion():
        print('Я в области видимости функции test_funktion')
    inner_funktion()


test_funktion()
inner_funktion()