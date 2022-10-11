
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import yaml
from streamlit_tags import st_tags


st.write("# Autograder")


def stinit():

    # keywords = st_tags(
    #     label='# Enter Keywords:',
    #     text='Press enter to add more',
    #     value=['Zero', 'One', 'Two'],
    #     # maxtags=maxtags,
    #     key="aljnf")

    # st.write("### Keywords:")

    # s = ''
    # for i in keywords:
    #     s += "- " + i + "\n"

    #     st.markdown(s)

    st.write("### Question:")
    ques = st.text_area(label="Question",
                              placeholder="please type the question here")

    st.write("### Reference answer:")
    ref_answer = st.text_area(label="Reference answer",
                              placeholder="please type the reference answer here")

    st.write("### Student answer:")
    ref_answer = st.text_area(label="Student answer",
                              placeholder="please enter the student answer here")
    result = st.button(label="Get Score")
    if result:
        st.success("answers evaluated successfully!!")


hashed_passwords = stauth.Hasher(['admin', 'lorem']).generate()
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

option = st.sidebar.selectbox(
    'Login/SignUp',
    ('Login', 'SignUp'))

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized'])

if option == "Login":

    name, authentication_status, username = authenticator.login(
        'Login', 'main')
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main')

        # data = pd.read_csv("ds.csv")
        # df = pd.DataFrame(data)
        # st.write(df)
        stinit()
    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')

if option == "SignUp":
    try:
        if authenticator.register_user('Register user', preauthorization=True):
            st.success('User registered successfully, you can login now')

            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)
