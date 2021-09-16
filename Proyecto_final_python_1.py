import streamlit as st 
import pandas as pd 
import lasio
import matplotlib.pyplot as plt
from PIL import Image
from io import StringIO
import matplotlib.pyplot as plt
from PIL import Image

#TITULO
st.title("ANALISIS DE DATOS")
cargar=st.sidebar.file_uploader("Cargar archivo LAS" , type=['.las', '.LAS'], key=None)

if cargar is None:
	st.write("Suba un archivo con extencion .las")
if cargar is not None:
	bytes_data = cargar.read()
	str_io = StringIO(bytes_data.decode('Windows-1252'))
	las_file = lasio.read(str_io)
	df = las_file.df()

inicio = Image.open("IMA1.png")
inicio1 = Image.open("image2.jpg")
inicio2=Image.open('a.jpg')
#SECCION UNO
opciones_inicio=st.sidebar.radio('SELECCIONE UNA OPCION',['Inicio','Data informacion','Analisis y visualizacion'])
if opciones_inicio=='Inicio':
	st.title('INICIO')
	st.image(inicio)
	a=st.sidebar.radio('SELECCIONE UNA OPCION', ['Instructivo del uso del aplicativo','Descripcion de cada seccion'])
	if a=='Instructivo del uso del aplicativo':
		st.header('Instrucciones del aplicativo')
		st.write("""
			1. Cargar una archivo LAS para que el aplicativo pueda extraer informacion especifica.
			2. Escoger las variables de importancia para filtrar.
			3. Seleccionar el rango de profundidad para visualizar los datos.
			4. Visualizar las graficas de las variables escogidas.



			""")

		st.header('Descripcion')
		st.image(inicio1)
		st.write("""

			El objetivo de este aplicativo es analizar diferentes valores del registro de pozos acorde a un rango de
			profundidad, permite extraer valores de acuerdo a limites inferiores y superiores colocados por el usuario.
			Se muestra graficas de los valores de pozos vs el rango de profundidad escogido.


		 """)
	if a=='Descripcion de cada seccion':
		st.write('La secciones consta de INICIO, .....ANALISIS')
	st.info("""
	Autor: Juan Carlos Figueroa Guevara

	Ingenieria en Petroquimica - ESPE
	
	jcfigueroa3@espe.edu.ec
	
	Telefono: 0996307536""")

#SECCION DOS
if opciones_inicio=='Data informacion':
	st.title('SECCION DOS')
	st.header('DATA FRAME')
	b=st.sidebar.radio('SELECCIONE UNA OPCION',['Data frame','Variables',])
	st.image(inicio2)
	if b=='Data frame':
		
		df
		st.header('Seleccione las variables (izquierda)')
	if b=='Variables':
		df
		lista_columnas = list(df.columns)
		ba=st.multiselect('Seleccione una variable de su interes',options=lista_columnas)
		dataframe=df[ba]
		st.header("Multiselect filtro")
		st.write(dataframe)
		df['DEPTH']=df.index
		pmin=dataframe.min()
		pmax=dataframe.max()
		pco=dataframe.count()
		prof_min=df.index.values[0]
		prof_max=df.index.values[-1]
		st.header('Informacion del registro de pozos')
		st.write("Este registro fue medido desde una profundidad de :", prof_min , "[ft]")
		st.write("Hasta una profundidad de :", prof_max , "[ft]")
		st.write("Los siguientes registros contiene un VALOR MINIMO de :", pmin )
		st.write("Los siguientes registros contiene un VALOR MAXIMO de :", pmax )
		st.write("Numero de datos :", pco )

		


#SECCION TRES
if opciones_inicio=='Analisis y visualizacion':
	st.title('SECCION TRES')
	st.title("Estadisticas breves")
	df_estadisticas=df.describe()
	df_estadisticas

	st.title("Evaluación del Registro")
	st.header("Establezca los limites de los valores")
	prof_min=df.index.values[0]
	prof_max=df.index.values[-1]
	limite_superior = st.slider("Seleccione el limte INFERIOR de la formacion a analizar", int(prof_min) , int(prof_max) )
	limite_inferior = st.slider("Seleccione el limte SUPERIOR de la formacion a analizar", int(prof_min) , int(prof_max)  )
	df_limites=df[limite_superior:limite_inferior]
	st.header("Data Frame de la zona a evaluar")

	lista_columnas1= list(df.columns)
	ba1=st.multiselect('Seleccione DOS variables para GRAFICAR',options=lista_columnas1)
	dataframe1=df[ba1]
	df_filtrado = df_limites[ba1]
	df_filtrado
	#SECCION CUATRO
	#GRAFICAS
	st.header("Limpieza de datos")
	df_clean=dataframe1.dropna(subset=ba1,axis=0, how='any')
	df_clean


	st.header("Graficas: Variable A, Variable B")
	f, ax = plt.subplots(nrows=2, ncols=1, figsize=(12,8) )
	logs = ba1
	colors = ['green','blue']
	for i,log,color in zip(range(2),logs,colors):
		ax[i].plot(df_clean.index,df_clean[log], color=color)
		ax[0].set_ylabel("Valores del registro de pozos (log)")

	for i,log,color in zip(range(3),logs,colors):
		ax[i].set_xlabel(log)
		ax[1].set_ylabel("Valores del registro de pozos (log)")
		ax[0].set_xlabel("Profundidad (ft)")
		ax[1].set_xlabel("Profundidad (ft)")
		ax[i].grid()
	st.pyplot(f)
	st.info("""
	Autor: Juan Carlos Figueroa Guevara

	Ingenieria en Petroquimica - ESPE
	
	jcfigueroa3@espe.edu.ec
	
	Telefono: 0996307536""")


	
	


