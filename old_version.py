
'''

with st.sidebar:
    add_radio = st.radio(
        '你想要：',
        ("电子唱诗", "来点儿词汇")
    )

if add_radio == "电子唱诗":

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

elif "来点儿词汇":

    lucky_num = st.slider('选择你的幸运数字吧！', min_value=0, max_value=100, value=50,
                          step=1)

    if st.button('我要献礼！'):
        with st.spinner("召唤来的文字在被重新组合，请稍等........"):

            st.balloons()

            result = read_txt('词库/存档.txt')
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
        st.write('还没写呢')

st.image(image2)
'''