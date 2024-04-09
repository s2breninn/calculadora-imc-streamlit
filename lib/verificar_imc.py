def verificar_imc(imc, imc_delta):
    if imc < 18.5:
        resultado = {
            'classe': 'Abaixo do peso',
            'delta': imc_delta
        }
    elif 18.5 <= imc < 25:
        resultado = {
            'classe': 'Peso ideal',
            'delta': imc_delta
        }
    elif 25 <= imc < 30:
        resultado = {
            'classe': 'Sobrepeso',
            'delta': imc_delta
        }