import streamlit as st  # Librería para crear aplicaciones web interactivas
import pandas as pd  # Librería para manejo de datos en estructuras como DataFrames
import matplotlib.pyplot as plt  # Librería para crear gráficos

# Título de la aplicación
st.title("Empleatronix")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Carga un archivo CSV con datos de empleados
file_path = "csv/employees.csv"  # Ruta al archivo CSV
df_employees = pd.read_csv(file_path)  # Cargamos los datos del CSV en un DataFrame

# Mostramos los datos del DataFrame en la interfaz de Streamlit
df_employees

# Creamos tres columnas para los controles interactivos
color, nombre, sueldo = st.columns(3)

# Selector de color para las barras del gráfico
with color:
    color = st.color_picker("Elige un color para las barras", "#00f900")

# Checkbox para mostrar u ocultar los nombres de los empleados en el gráfico
with nombre:
    nombre = st.toggle("Mostrar Nombre")

# Checkbox para mostrar los sueldos directamente sobre las barras del gráfico
with sueldo:
    sueldo = st.toggle("Mostrar sueldo en la barra")

# Ordenamos el DataFrame por su índice (opcional, puede ayudar si los datos no están ordenados)
df_employees_sorted = df_employees.sort_index()

# Creamos una figura para el gráfico de barras horizontales
fig, ax = plt.subplots()

# Dibujamos las barras con los nombres de los empleados en el eje Y y los sueldos en el eje X
bars = ax.barh(df_employees['full name'], df_employees['salary'], color=color)

# Ocultamos los nombres en el eje Y si la opción correspondiente está desmarcada
if not nombre:
    ax.set_yticklabels([''] * len(df_employees['full name']))  # Vacía las etiquetas del eje Y

# Mostramos los sueldos sobre las barras si la opción está marcada
if sueldo:
    for bar, salary in zip(bars, df_employees['salary']):  # Iteramos sobre las barras y los sueldos
        ax.text(
            bar.get_width() + 50,  # Posición del texto (ligeramente a la derecha de la barra)
            bar.get_y() + bar.get_height() / 2,  # Posición vertical centrada
            f'{salary} €',  # Texto que muestra el sueldo con el símbolo €
            va='center'  # Alineación vertical centrada
        )

# Limpiamos las etiquetas de los ejes X e Y (puedes personalizarlas si es necesario)
ax.set_xlabel('')
ax.set_ylabel('')

# Ajustamos el límite del eje X (puede depender del rango de sueldos)
ax.set_xlim(0, 4500)

# Mostramos el gráfico en la aplicación Streamlit
st.pyplot(fig)
