
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from streamlit_tags import st_tags
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from csv import writer

st.write("# Autograder")

model = SentenceTransformer('bert-base-nli-mean-tokens')

ans_arr = []


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

    with st.form("autograder_form", clear_on_submit=True):

        st.write("### Question:")
        ques = st.text_area(label="Question",
                            placeholder="please type the question here")

        st.write("### Reference answer:")
        ref_answer = st.text_area(label="Reference answer",
                                  placeholder="please type the reference answer here")

        ans_arr.append(ref_answer)

        st.write("### Student answer:")
        stu_answer = st.text_area(label="Student answer",
                                  placeholder="please enter the student answer here")

        ans_arr.append(stu_answer)
        
        submit = st.form_submit_button("Submit")

        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
        # To read file as bytes:
            bytes_data = uploaded_file.getvalue()
            st.write(bytes_data)

        # To convert to a string based IO:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            st.write(stringio)

        # To read file as string:
            string_data = stringio.read()
            st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)
                       
                       
        if uploaded_file:
            score = []
            ans_embed = model.encode(ans_arr)
            result = cosine_similarity([ans_embed[0]], ans_embed[1:])
            st.write("the similarity score is :", round(result[0][0], 1))
            st.write("the score (out of 5) is:", round(result[0][0]*5, 1))
            st.success("answer evaluated successfully!!")
            score.append(round(result[0][0]*5, 1))
        
        if(score>=4.5 and score<=5.0):
            st.write("Grade - A")
        elif(score>=4.0 and score<=4.5):
            st.write("Grade - B")
        elif(score>=3.5 and score<=4.0):
            st.write("Grade - C")
        else:
            st.write("Grade - D")
            
# Open our existing CSV file in append mode Create a file object for this file
        with open(uploaded_file, 'a') as f_object:
 
    # Pass this file object to csv.writer() and get a writer object
            writer_object = writer(f_object)
 
    # Pass the list as an argument into the writerow()
            writer_object.writerow(score)
 
    # Close the file object
            f_object.close()
            
            text_contents = '''
                            reference_answer, student_answer
                            123, 456
                            789, 000
                            '''

            st.download_button('Download file', text_contents)  # Defaults to 'text/plain'
            with open(uploaded_file) as f:
                dataframe.to_csv(uploaded_file, index=False, compression="zip")

                st.download_button('Download file', f)
            if st.download_button(...):
                st.write('Thanks for downloading!')

                
            # res2 = euclidean_distances([ans_embed[0]], ans_embed[1:])
            # st.write("the similarity score is :", res2[0][0])




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
