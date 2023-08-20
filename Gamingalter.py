import streamlit as st
import pandas as pd
import altair as alt

st.header("Verteilung der Videogamer in Deutschland nach Alter im Jahr 2023")
st.subheader("Gaming nach Alter")

source = pd.DataFrame({
        'Anteil(%)': [8, 16, 14, 18, 15, 18, 12],
        'Alter': ['6-9 Jahre', '10-19 Jahre', '20-29 Jahre', '30-39 Jahre', '40-49 Jahre', '50-59 Jahre', '60-69 Jahre']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Alter:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    August 2023, Deutschland
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: game; GfK")