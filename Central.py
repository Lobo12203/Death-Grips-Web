# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="Death Grips",
    page_icon=":pirate_flag:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

# Configuración de Logo
st.logo("deathlogo.gif")

pg = st.navigation(["Home.py", "Albums.py", "Web.py", "Concerts.py", "Conclusion.py" ])
pg.run()