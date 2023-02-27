import streamlit as st
import email_send
import pandas

st.header("Contact me")

df = pandas.read_csv('./topics.csv')

with st.form(key='contact'):
    user_email = st.text_input("Tu direccion de correo")
    select = st.selectbox("Opciones", df["topic"])
    raw_message = st.text_area("Escribe tus consultas")
    message = f"""\
Subject: Nuevo correo de {user_email}
        
From: {user_email}
{raw_message}
"""
    enviar = st.form_submit_button("Enviar")
    if enviar:
        email_send.send_email(message)
        st.info("Correo enviado correctamente")