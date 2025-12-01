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
    st.image('')

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
  interests = ['Web Development', 'Gaming', 'Creative Design', 'Swimming', 'Travel', 'Thearical lighting']

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
        st.image('https://www.robertjuliat.com/imgs-news/2016/614SX_profiles_for_Netherlands_Royal_Theatre_02.jpg')
    with col2:
        st.subheader('🔦 Thearical lighting Course 101')
        st.write('The basics of lighting from Tik Tok videos to the theater')
        st.caption('**Equipment:** Philips, Cree Lighting, ADJ Lighting')
      
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('', use_column_width = True)

    with col2:
        st.subheader('Basic lighting kit ')
        st.write('from learning to practice, everything you need for your first lighting rig')
        st.caption('**Technologies:** DMX, Lighting Key, Color theory')


  # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('', use_column_width = True)
    with col2:
      st.subheader('🎨 Color Hue Graphic')
      st.write('Interactive app for calculating and visualizing color hues')
      st.caption('**Technologies:** DMX systems, Lightkey, lighting AI')

elif page == '🛠 Skills':
  st.title('Lighting Technical Skills')

  # Skills with progress bars
  st.subheader('Visual Storytelling')

  skills_data = {
    'Color Theroy' : 85,
    'lighting intergration' : 70,
    'Fixture Placement' : 63,
    'Cue design' : 52,
    'Training ' : 30
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
  with col1:
    st.success('My DMX Go')
    st.info('Software')
    st.warning('Easy user interface')

  with col2:
    st.success('Lighting Key')
    st.info('Software')
    st.warning('DMX/lighting AI Tools')
    
  with col3:
    st.success('led ellipsoidal light')
    st.info('Hardware')
    st.warning('High voltage')

elif page == '📝 Resume':
  st.title('Resume')

  # Read PDF from my GitHub repository
  with open('my_resume.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
  
  st.download_button(
    label ='🔻 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'my_resume.pdf',
    mime ='application/pdf'
  )

elif page == '📩 Contact':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** LightingGuy23@Gmail.com

        🏢 **LinkedIn:** [linkedin.com/in/yourname](https://linkedin.com)

        👩‍💻 **Github:** [https://github.com/avinashjairam](https://github.com)

    ''')

    # Fun interative element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '📑 Planning Economic Domination',
            '📕 Studying Marketing Trends',
            '✈️ Traveling Always',
            '🎮 Gaming',
            '😴 Trying to sleep'
        ]
    )


    st.info(f'Status: {status}')

    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made using Streamlit | © {datetime.now().year} Avinash Jairam </center>',
        unsafe_allow_html = True
    )
    



      












