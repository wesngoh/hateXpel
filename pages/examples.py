import streamlit as st

st.set_page_config(page_title='a little help?', page_icon=':no_entry_sign:')
st.title(':clipboard: examples')

st.write("Try out the hate speech classifier using the examples below!")

st.write('**Hate Speech Examples:**')
st.code("Chinese people are taking over Singapore and pushing out other races. #StopChinesePrivilege")
st.code("Muslims are terrorists and should not be allowed to practice their religion in Singapore.")
st.code("Mixed-race relationships are destroying our culture, they should be abiding by their ancestors' religious beliefs and should be banned in Singapore.")

st.write('**Non-Hate Speech Examples:**')
st.code("It's heartwarming to see Singaporeans coming together to support the LGBTQ+ community. Love is love and everyone deserves to be happy. #pride #singaporelove")
st.code("It's time for Singapore to have a female Prime Minister. We have capable and qualified women leaders who can lead our country to greater heights. #genderrepresentation #womeninpower")
st.code("Why do we still have gender pay gap in Singapore? It's time for equal pay for equal work. ")