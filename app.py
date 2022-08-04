import streamlit as st
from auto_gene import read_txt, random_gene, random_gene_words
from replace_nlp import change_sentence
from dict import get_batch_idioms
#  pip freeze requirements.txt
# markdown

from PIL import Image
#image1 = Image.open('WX20220528-134651@2x.png')
# 设置网页标题
st.title('《献礼工程》 -- 电子诗人')

#st.image(image1)

# 展示一级标题
#st.subheader('献礼工程')

#image2 = Image.open('v2-3420614c84c85bba28ec098d771fb27d_1440w.jpg')

with st.sidebar:
    add_radio = st.radio(
        '你想要：',
        ("电子唱诗", "来点儿词汇")
    )

if add_radio == "电子唱诗":

    lucky_num = st.slider('选择你的幸运数字吧！', min_value=0, max_value=100, value=50,
                          step=1)

    crazy_level = st.slider('癫狂程度 【0 分清醒 - 100 分疯狂】', min_value=0.00, max_value=1.00, value=0.5,
                          step=0.01)

    if st.button('我要献礼！'):
        with st.spinner("生成中........"):

            st.balloons()

            result = read_txt('存档.txt')
            text = random_gene(lucky_num, result)
            text = list(filter(None, text))
            count = 0
            for i in text:
                #st.success(text)
                text = change_sentence(i, lucky_num+count, crazy_level)
                st.markdown(text)
                count = count + 1
    else:
        st.warning('还没献礼呢！')

elif "来点儿词汇":

    lucky_num = st.slider('选择你的幸运数字吧！', min_value=0, max_value=100, value=50,
                          step=1)

    if st.button('我要献礼！'):
        with st.spinner("生成中........"):

            st.balloons()

            result = read_txt('存档.txt')
            a, b, c , d= random_gene_words(lucky_num)
            e = get_batch_idioms()
            st.subheader(a)
            st.subheader(b)
            st.subheader(c)
            st.subheader(d)
            st.subheader(e)
            #for i in text:
                # st.success(text)
                #st.markdown(i)

    else:
        st.write('还没献礼')




#st.image(image2)
