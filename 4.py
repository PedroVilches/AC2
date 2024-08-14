import streamlit as st

def main():
    st.title("Calculadora de Idade")
    
    ano_nascimento = st.numero_input("Informe o ano de seu nascimento:", min_value=1900, max_value=2024, step=1)
    
    ano_atual = st.numero_input("Informe o ano atual:", min_value=1900, max_value=2024, step=1)
    
    idade_anos = ano_atual - ano_nascimento
    st.write(f"A idade em anos é: {idade_anos}")
    
    idade_meses = idade_anos * 12
    st.write(f"A idade em meses é: {idade_meses}")
    
    idade_dias = idade_anos * 365
    st.write(f"A idade em dias é: {idade_dias}")

if __nome__ == "__main__":
    main()
