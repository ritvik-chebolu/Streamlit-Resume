import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Ritvik Chebolu
##### *M.Sc. in Data Science* 
''')

image = Image.open('circle-cropped.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Activey applying for internships and co-ops for Summer and/or Fall 2022 
- Data Science graduate student at Rochester Institute of Technology, New York
- Bachelor's degree from Indian Institute of Technology Dharwad (IIT Dharwad) in Mechanical Engineering
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/ritvik-chebolu/" target="_blank">Ritvik Chebolu</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills and Technologies</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Science** (Data Science), *Rochester Institute of Technology*, New York',
'2021-Expected 2023')
st.markdown('''
- GPA: `3.11`
- Coursework: Foundations of Data Science, Applied Statistics, Database Design Implementation, Software Construction, Visual Analytics
''')

txt('**Bachelor of Technology** (Mechanical Engineering), *Indian Institute of Technology Dharwad*, Karnataka, India',
'2017-2021')
st.markdown('''
- GPA: `3.8` (equivalent WES score, 7.78 on a scale of 10)
- Relevant coursework: Calculus, Linear Algebra, Ordinary Differential Equations, Data Analysis, Numerical Analysis
- Research work in the field of computational advanced manufacturing
''')

#####################
st.markdown('''
## Work Experience 
''')

txt('**Internship in Thermal Power Plant**, Visakhapatnam Steel Plant, Visakhapatnam, India',
'July 2019')
st.markdown('''
- Analysis of variation of blade temperature over time for steam and gas turbines.
- Investigated the velocity flow and temperature profile over the length of the turbine for various turbine lengths and capacities.
''')

txt('**Steam Turbine Engineering Internship**, Bharat Heavy Electronics Ltd - Hyderabad, Hyderabad, India',
'May 2019')
st.markdown('''
- Analysis of the blade profile variation for a steam turbine over length for various turbine capacities.
- Understanding the inner workings and control of a Steam Turbine and its operation.
''')

txt('**Internship on Manufacturing Processes**, Visakhapatnam Steel Plant, Visakhapatnam, India',
'December 2018')
st.markdown('''
- Repair analysis for a torpedo ladle car used to carry molten steel from a blast furnace. 
- Worked with a senior engineer to measure the structural integrity and strength of a torpedo ladle post the welding phase.    
''')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `SQL`, `Java`, `R`, `C++`, `JavaScript`, `XML`, `MATLAB`')
txt3('Technologies', '`Tableau`, `Excel`, `MySQL`, `PowerBI`, `Hadoop`, `Microsoft Office`, `Android Studio`')
txt3('Libraries', '`TensorFlow`, `Keras`, `Scikit Learn`, `OpenCV`, `Streamlit`, `Seaborn`, `plotly`, `Pandas`, `NumPy`, `ggplot2`, `Beautiful Soup`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/ritvik-chebolu/')
txt2('GitHub', 'https://github.com/ritvik-chebolu')
txt2('Twitter', 'https://twitter.com/ritvikteja')
txt2('Email', 'rc2388@rit.edu')
