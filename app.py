import streamlit as st
import streamlit.components.v1 as components
import pickle
st.set_page_config(page_title='Student Subscription Predictor')
st.title(":child:Student Subscription Predictor:chart:")
minutes_watched = st.number_input("Numbers of Minutes Watched")
day = st.number_input("Numbers of Days Engaged")
engaged_quiz = st.radio("Student Engaged with Quiz",('Yes','No'))
if engaged_quiz=='Yes':
    quiz = 1
else:
    quiz = 0
engaged_exam = st.radio("Student Engaged with Exam",('Yes','No'))
if engaged_exam=='Yes':
    exam = 1
else:
    exam = 0
engaged_question = st.radio("Student Engaged with Questions ",('Yes','No'))
if engaged_question =='Yes':
    ques = 1
else:
    ques = 0
if st.button("Predict"):
    model = pickle.load(open('model.pkl','rb'))
    result = model.predict([[minutes_watched,day,quiz,exam,ques]])
    if result == 1:
        st.header('Students can take Subscription')
    else:
        st.header("Student is not going to take Subscription")