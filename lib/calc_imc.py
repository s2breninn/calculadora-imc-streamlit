def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    imc_ideal = 21.7
    imc_delta = imc - imc_ideal
    
    return imc, imc_ideal, imc_delta