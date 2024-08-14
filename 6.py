import streamlit as st

class VacinaTracker:
    def __init__(self):
        self.vacinas = {}

    def registrar_dose(self, usuario, vacina, dose):
        if usuario not in self.vacinas:
            self.vacinas[usuario] = {}
        self.vacinas[usuario][vacina] = dose
        st.write(f"Dose {dose} da vacina {vacina} registrada para o usuário {usuario}.")

    def consultar_doses(self, usuario):
        if usuario in self.vacinas:
            st.write(f"Doses registradas para o usuário {usuario}:")
            for vacina, dose in self.vacinas[usuario].items():
                st.write(f"{vacina}: {dose}")
        else:
            st.write(f"Nenhuma dose registrada para o usuário {usuario}.")

if __name__ == "__main__":
    tracker = VacinaTracker()

    # Exemplo de uso:
    tracker.registrar_dose("João", "COVID-19", 1)
    tracker.registrar_dose("Maria", "Gripe", 2)

    tracker.consultar_doses("João")
    tracker.consultar_doses("Maria")
