import streamlit as st
from lib.calc_imc import calcular_imc
from lib.verificar_imc import verificar_imc

def strealit_front():
    with st.sidebar:
        st.title('Calculador IMC')
        st.header('IMC: Qual definição?')

        st.write('Indice de Massa Corporal')
        st.write('É um indice que relaciona peso e altura de uma pessoa')
        st.write('Utilizado como uma medida de saúde geral e para determinar se uma pessoa está em um peso ideal')

    st.title('Calculadora')

    peso = st.number_input(label='Digite o seu peso em KG (Quilogramas):', min_value=0.0)
    altura = st.number_input(label='Digite a sua altura em metros:', min_value=0.0)

    if st.button('Calcular'):
        imc, imc_ideal, imc_delta = calcular_imc(peso, altura) # return args function 

        resultado = verificar_imc(imc, imc_delta)

        st.code(f'O resultado: {resultado}')

        col1, col2 = st.columns(2)
        col1.metric('IMC Classificado', resultado['classe'], resultado['delta'], delta_color='inverse')
        col2.metric('IMC Calculado', round(imc, 2), resultado["delta"], delta_color='off')

if __name__ == '__main__':
    strealit_front()