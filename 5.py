import streamlit as st

# Definindo o cardápio com códigos e preços
menu = {
    101: 8.50,  # Cachorro Quente
    102: 4.50,  # Bauru Simples
    104: 5.50,  # Hambúrguer
    105: 6.60,  # Cheeseburger
    106: 6.00   # Refrigerante
}

# Título da aplicação
st.title("Calculadora de Pedido da Lanchonete")

# Inputs do usuário
item_code = st.number_input("Código do Item", min_value=1, max_value=999, step=1)
quantity = st.number_input("Quantidade", min_value=1, step=1)

# Botão para calcular o valor total
if st.button("Calcular Valor"):
    # Verifica se o código do item está no menu
    if item_code in menu:
        price = menu[item_code]
        total_amount = price * quantity
        st.write(f"Total a pagar: R$ {total_amount:.2f}")
    else:
        st.error("Código do lanche é inválido.")
