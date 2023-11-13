import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('Barra lateral e gráficos')

st.sidebar.header('Tipos de Gráficos')

graficos = ('Linha','Barras','Barras_H')

GRAF = st.sidebar.radio('Selecione um grafico',
                 options = graficos)

if GRAF == 'Linha':
    x = np.linspace(0,1,1000)
    y1 = np.sin(2*np.pi*x)
    y2 = np.cos(2*np.pi*x)
    st.header('Grafico de Linha ou série temporal')
    fig = plt.figure(figsize = (4,2))
    plt.style.use('ggplot')
    plt.plot(x,y1)
    plt.plot(x,y2,'--')
    st.write(fig)

elif GRAF == 'Barras':
    x = np.array([2,4,6,8,10])
    y = 10*x
    st.header('Grafico de Barras')
    fig = plt.figure(figsize = (4,2))
    plt.style.use('ggplot')
    plt.bar(x,y)
    st.write(fig)

else:
    x = np.array([2,4,6,8,10])
    y = 10*x
    st.header('Grafico de Barras Horizontais')
    fig = plt.figure(figsize = (4,2))
    plt.style.use('ggplot')
    plt.barh(x,y)
    st.write(fig)

with st.expander('Clique para saber mais!'):
    st.write('''Este texto fica escondiddo até que o usuário o chame.
             A Tarifa Social de Energia Elétrica é um benefício que
             oferece descontos de até 65% na conta de energia de luz
             para as famílias de baixa renda''')

#foto = st.camera_input('Tire uma Foto')
#st.image(foto)
    









    

