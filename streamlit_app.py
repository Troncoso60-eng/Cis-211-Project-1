import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Nicolas Troncoso | Portfolio',
  page_icon='😁',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '🧐 About', '💼 Projects', '🛠 Skills' ,'📝 Resume', '📩 Contact' ])

# Home Page
if page == '🏠 Home':
  st.markdown('<p class="main-header">Nicolas Troncoso</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Future Invester | CEO</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.5', '📚')
  with col2:
      st.metric('Projects', '1', '💻')
  with col3:
      st.metric('Skills', '13+', '🚀')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I am a general business student passionate about product development and corperation mangagement. Currently learning
                marketing, accounting, business law, and Python to develop techincal  skills.
            
                🎯 **Current Focus:** Building interactive web applications with Streamlit
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
                🌱 **Fun Fact:** I work with theactical lighting equipment for my church!
            ''')
  with col2:
    # Placeholder for image
    st.image()

# About Page
elif page == '🧐 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2024 - Present: UPS Worker'):
    st.write('''
                - Major: General Business and Administration
                - Relevant Coursework: Internet & Emerging Technologies, Marketing, data analysis, and accounting 
                - Activities: Swimming, Gamer, Creative design
            ''')

  with st.expander('2022 - present: CUNY Medgar Evers College'):
    st.write('''
                - Dean Listed
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests = ['Web Development', 'Gaming', 'Creative Design', 'Swimming', 'Travel', 'Thearical lighting techinican']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fbetopperdj.com%2Fblogs%2Fnews%2Ftypes-of-theater-lights-the-role-in-stage-lighting&psig=AOvVaw2GGyW3bC0_RjEkDQCIyCUq&ust=1762877474718000&source=images&cd=vfe&opi=89978449&ved=0CBkQjhxqFwoTCKDIzd3855ADFQAAAAAdAAAAABAK')
    with col2:
        st.subheader('🔦 Thearical lighting Course 101')
        st.write('The basics of lighting from Tik Tok videos to the theater')
        st.caption('**Equipment:** Philips, Cree Lighting, ADJ Lighting')












