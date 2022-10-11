from turtle import onclick
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar

st.write("# Domain Specific answer grading and scoring")

# st.code(body='''keywords = st_tags(
#     label='# Enter Keywords:',
#     text='Press enter to add more',
#     value=['Zero', 'One', 'Two'],
#     suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
#     maxtags = 4,
#     key='1')''',
#         language="python")

# maxtags = st.slider('Number of Keywords allowed?', 1,
#                     10, 3, key='jfnkerrnfvikwqejn')

keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    # maxtags=maxtags,
    key="aljnf")

st.write("### Keywords:")

s = ''
for i in keywords:
    s += "- " + i + "\n"

st.markdown(s)

st.write("### Reference answer:")
ref_answer = st.text_area(label="Reference answer",
                          placeholder="please type the referennce answer here")
st.button(label="Submit")

st.write("#### The reference answer being considered is:\n", ref_answer)


st.write("### Student answer:")
ref_answer = st.text_area(label="Student answer",
                          placeholder="please enter the student answer here")
st.button(label="Compute Similiarity")
