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
        st.image('data:image/jpeg;base64,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')
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
        st.image('https://iprx-cms-content.ams1.vultrobjects.com/Blog_How_To_Crawl_4_capcha_ded9206d5f.png', use_column_width = True)

    with col2:
        st.subheader('🛒 E-Commerce Price Tracker')
        st.write('Python web scraper that monitors Amazon prices and sends alerts')
        st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')


  # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('https://www.publicdomainpictures.net/pictures/90000/nahled/calculator-black-clipart.jpg', use_column_width = True)
    with col2:
      st.subheader('📊 Student Grade Calulator')
      st.write('Interactive web app for calculating and visualizing grades')
      st.caption('**Technologies:** Python, Pandas, Plotly')

elif page == '🛠 Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Programming Languages')

  skills_data = {
    'Python' : 85,
    'HTML/CSS' : 70,
    'JavaScript' : 60,
    'SQL' : 50,
    'Technical Writing' : 40
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
    st.success('Excel')
    st.info('Word')
    st.warning('Access')

  with col2:
    st.success('PowerPoint')
    st.info('Google Docs')
    st.warning('ChatGPT/AI Tools')
    
  with col3:
    st.success('Presentations')
    st.info('Writing')
    st.warning('Social Media')

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
        📧 **Email:** yourname@email.com

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
    



      












