import streamlit as st

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