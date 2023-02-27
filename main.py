import streamlit as st
import pandas

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Fernando Hernandez')
    content = """
    Hola, soy Fernando Hernandez, Ingeniero 
    informatico, empresario y deportista. 
    Actualmenteme encuentro estudiando el 
    grado superior de Ingenieria Informatica
    en la universidad internacional
    de Valencia.
    En este portfolio ire subiendo los proyectos que vaya realizando tanto en los cursos realizados como
    los que sean desarrollados con fines personales o empresariales.
    No todos los proyectos presentaran un nivel profesional ya que hay algunos que se realizaron
    hace tiempo antes de perfeccionar las tecnicas de programación
    """
    st.info(content)

content2 = """
A continuación puedes encontrar los proyectos que he ido desarrollando desde la finalizacion
de mis estudios hasta el dia de hoy, estos contenidos se iran actualizando conforme se 
realicen nuevos proyentos
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

# Obtenemos el numero total de proyectos y lo dividimos entre el numero de columnas
project_counter = len(df)
split_col_value = int(project_counter/2)

print(project_counter)
with col3:
    for index, row in df[1:split_col_value].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[split_col_value:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
