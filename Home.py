#Bring Library
import streamlit as st

#Header area
#-제목
st.title("The EL Company🔆", anchor=False, help=None)
st.divider()
home_col_1, home_col_2 = st.columns([0.65,0.35])
with home_col_1:
    #-부제목
    st.subheader("We are :red[the East Light from sun.]", anchor=False, help=None)
    st.write("We are a data specialist company that constantly observes and discovers what others are missing in a world where everything is already in place, and creates new values ​​that did not exist before.")
    st.write("EL is a company comprised of leaders who can maximize infinite value creation for you and your company even in a zero-base environment.")
    st.write("The danger is always in the details we take for granted. EL is constantly curious about natural situations and reality and can provide you with valuable insights and value.")
with home_col_2:
    st.subheader("", anchor=False, help=None)
    st.subheader("", anchor=False, help=None)
    #-이미지
    #--스트림릿 상에서 직접 css 조정을 원할시 unsafe_allow_html 파라메터 True 지정
    st.image("useData/EL_img/HOME_EL_NEW.png")
st.divider()

home_col_3, home_col_4 = st.columns([0.35,0.65])
with home_col_3:
    st.subheader("", anchor=False, help=None)
    st.subheader("", anchor=False, help=None)
    st.image("useData/EL_img/data_crawling.png")
with home_col_4:
    st.subheader("The Double S of DataCrawling", anchor=False, help=None)
    st.markdown("#### :green[S]niping the data you need based on your requirements.")
    st.write("We quickly and accurately collect and process the data you need from websites that have the required information.")
    st.markdown("#### :green[S]aving your resources is our priority.")
    st.write("Save the physical time and resources required for data collection, and use the remaining resources elsewhere.")
st.markdown("###### :red[**Please be aware that data crawling is only possible on websites where crawling is permitted, and we absolutely do not engage in illegal crawling.]")
st.divider()

home_col_5, home_col_6 = st.columns([0.65,0.35])
with home_col_5:
    st.subheader("EL Company's ELOBOT", anchor=False, help=None)
    st.write("Our ELOBOT will become your personal assistant and your most trusted team member.")
    st.write("Stop struggling on your own. Work with ELOBOT to handle various tasks like employee training, marketing planning, and more.")
    st.write("Concerned about ELOBOT or worried about the implementation cost? Just let us know, and EL Company will create a custom AI-based automation solution just for you.")
    st.markdown("###### :red[Chatbots, business automation, marketing planning, data analysis, and more.]")
with home_col_6:
    st.subheader("", anchor=False, help=None)
    st.subheader("", anchor=False, help=None)
    st.image("useData/EL_img/HOME_AUTO.png")
st.divider()

home_col_6, home_col_7 = st.columns([0.35,0.65])
with home_col_6:
    st.subheader("", anchor=False, help=None)
    st.subheader("", anchor=False, help=None)
    st.image("useData/EL_img/HOME_MODELING.png")
with home_col_7:
    st.subheader("From DB modeling to website development, resolved with one key.")
    st.write("Many companies underestimate the importance of DB modeling during website planning, leading to data quality issues over time. This neglect makes implementing ML, deep learning, and AI costly. We prioritize meticulous DB modeling from the start to ensure successful website development and effective data analysis, machine learning, and AI integration.")
    st.markdown("###### :red[Prioritizing the basics and executing them flawlessly is what truly defines an expert.]")

end_container = st.container(border=True)
with end_container:
    st.write('<div style="text-align:center;"><h4 style="color:yellow;">We don\'t just stop at thinking. We take action and create something out of nothing. This is the spirit that EL strives for.</h4></div>', unsafe_allow_html=True)
    st.image("useData/EL_img/EL_HOME_LEADER.png")