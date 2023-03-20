import streamlit as st
import pandas as pd
import numpy as np

st.header("Tugas 1")
st.subheader("Bar Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.header("Tugas 2")
st.subheader("3-Charts and maps:")

st.write("Latihan 1 : Membuat Chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['1', '2', '3'])
st.bar_chart(chart_data)

st.subheader("Latihan 2 : Membuat Widget")

st.write("Slider Luas Segitiga")
alas_segitiga = st.slider('Masukkan alas segitiga')
tinggi_segitiga = st.slider('Masukkan tinggi segitiga')
st.write('luas segitiga adalah :', alas_segitiga * tinggi_segitiga / 2)

st.subheader("Latihan 3 : Membuat Layout")
st.write("5A: Sidebar")

add_selectbox = st.sidebar.selectbox(
    'Bagaimana perasaan anda hari ini?',
    ('Senang', 'Sedih', 'Ga punya uang')
)

add_slider = st.sidebar.slider(
    'Nilai kebagusan web ini?',
    0.0, 10.0 
)

st.header("Tugas 3")
st.subheader("1 : st.write dan magic")

st.write('5 + 5 = ', 10)
df = pd.DataFrame({'col1': [1,2,3]})
df 

st.subheader("2 : Text element")

st.header("ini title")
st.subheader("ini subheader")
st.caption("ini caption")

st.subheader("3 : Data display element")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "26 °C", "-0.7 °C")
col2.metric("Wind", "11 mph", "5%")
col3.metric("Humidity", "91%", "2.7%")

st.subheader("4 : Chart elements")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

st.subheader("5 : Input widget")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.subheader("6 : Media elements")

st.image('https://live.staticflickr.com/2888/11269034823_02e2a0aa18_b.jpg', caption='Beach on the Maldives')

st.subheader("7 : Layout and Container")

Container = st.empty()
Container.text("Ini adalah sebuah container")

st.subheader("8 : Status Element")

st.balloons()
st.snow()

st.write("Ketika program berjalan, akan muncul balon dan salju")

st.subheader("9 : Control Flow")

form = st.form("my_form")
form.slider("Slider dalam kotak")

form.form_submit_button("Submit")

st.subheader("10 : Utilities")

with st.echo():
    st.write('Kode ini akan tercopy ke bawah')


st.title ("Connect to Database")
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

st.table(df)