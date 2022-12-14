import time

import streamlit as st
from auto_gene import read_txt, random_gene, random_gene_words
from replace_nlp import change_sentence
from dict import get_batch_idioms
#  pip3 freeze requirements.txt
# markdown

from PIL import Image
image1 = Image.open('pic/上条纹.png')
image2 = Image.open('pic/下条纹.png')
# 设置网页标题
st.title('浮于野的狄俄尼索斯')
st.subheader('Dionysus in No.46 Anju Str.')
st.image(image1)

# 展示一级标题
#st.subheader('献礼工程')

#image2 = Image.open('v2-3420614c84c85bba28ec098d771fb27d_1440w.jpg')

lucky_num = st.slider('请选择你的幸运数字', min_value=0, max_value=100, value=50,
                          step=1)

crazy_level = st.slider('请制定酒神精神 [0 分清醒 - 100 分疯狂]', min_value=0.00, max_value=1.00, value=0.5,
                          step=0.01)

if st.button('我想写一首！'):
    with st.spinner("生成中........"):
        time.sleep(5)

        st.balloons()

        result = read_txt('词库/存档.txt')
        text = random_gene(lucky_num, result)
        text = list(filter(None, text))
        count = 0

        for i in text:
            #st.success(text)
            text = change_sentence(i, lucky_num+count, crazy_level)
            st.markdown(text)
            count = count + 1
else:
    st.warning('酒神在沉默... ...')

st.image(image2)