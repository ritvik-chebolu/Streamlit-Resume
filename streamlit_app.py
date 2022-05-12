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
- Incoming *Data Science Co-op* at *Carrier Global* 
- Data Science graduate student at Rochester Institute of Technology, New York
- Bachelor's degree from Indian Institute of Technology Dharwad (IIT Dharwad)
- I love playing Football(Soccer), Badminton, Basketball, Cricket and I'm also a Chess geek
''')

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

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
        <a class="nav-link" href="shorturl.at/hsBZ4">Resume</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#courses-and-certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#positions-of-responsibility">Responsibilities</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#activities-and-achievements">Achievements</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact-me">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown('''
## Quick Links
''')
txt3('Resume', 'https://shorturl.at/hsBZ4')
txt3('LinkedIn', 'https://www.linkedin.com/in/ritvik-chebolu/')
txt3('GitHub', 'https://github.com/ritvik-chebolu')
txt3('Twitter', 'https://twitter.com/ritvikteja')

#####################
st.markdown('''
## Education
''')

txt('**Master of Science** (Data Science), *Rochester Institute of Technology*, New York',
    'Aug 2021 - Expected May 2023')
st.markdown('''
- GPA: `3.84`
- Coursework: Foundations of Data Science, Applied Statistics, Database Design Implementation, Software Construction, Visual Analytics
''')

txt('**Bachelor of Technology** (Mechanical Engineering), *Indian Institute of Technology Dharwad*, Karnataka, India',
    'Aug 2017 - May 2021')
st.markdown('''
- GPA: `3.8` (equivalent WES score, 7.78 on a scale of 10)
- Relevant coursework: Calculus, Linear Algebra, Ordinary Differential Equations, Data Analysis, Numerical Analysis
- Research work in the field of computational advanced manufacturing
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `SQL`, `Java`, `R`, `C++`, `JavaScript`, `XML`, `MATLAB`')
txt3('Technologies', '`Tableau`, `Excel`, `MySQL`, `PowerBI`, `Hadoop`, `Microsoft Office`, `Android Studio`')
txt3('Libraries',
     '`TensorFlow`, `Keras`, `Scikit Learn`, `OpenCV`, `Streamlit`, `Seaborn`, `plotly`, `Pandas`, `NumPy`, '
     '`ggplot2`, `Beautiful Soup`')

#####################
st.markdown('''
## Projects
''')

txt('**Sequence Classification using NLP** '
    '[*GitHub repo link*](https://github.com/ritvik-chebolu/Sentiment-Analysis-App)',
    'Mar 2022')
st.markdown('''
- Classifying user's input statements based on their polarity and subjectivity scores to get a sense of the user's expression.
- Built with TextBlob library built on NLTK which has a predefined set of words classified as positive, negative and neutral alonng with a score assigned to each tokenized word.
''')

txt('**Acute Ischemic Stroke Prediction** [*GitHub repo link*](https://github.com/ritvik-chebolu/Acute-Ischemic-Stroke-Prediction)',
    'Dec 2021')
st.markdown('''
- Predicted patient's stroke severity based on their prior medical history and biological details.
- A Voting Classifier Ensemble model was used to decrease bias and variance, and also fine-tuned the model using GridSearchCV to achieve an accuracy of 97.5%.
- Gathered primary patient data from an Indian Government hospital to train several models and understand their performance metrics on the dataset.
''')

txt('**User Feedback Sentiment Analysis** [*GitHub repo link*](https://github.com/ritvik-chebolu/Feedback-Sentiment-Analysis)',
    'Dec 2021')
st.markdown('''
- Built a user feedback evaluation system using python.
- Statistical Natural Language Processing using Natural Language Toolkit library (NLTK) to analyze user feedback and determine if they make a positive, negative or neutral sense based on sentiment and polarity scores.  
''')

txt('**LinkedIn Social Media Analytics** [*A data visualization hackathon*](https://public.tableau.com/app/profile/ritvik4126/viz/FestMan05-20-2021/Inferences)',
    'May 2021')
st.markdown('''
- Marketing analytics for the LinkedIn social media page of FestMan
- Built a dashboard to draw inferences from the LinkedIn page data in the year 2020 to derive insights about their followers/visitors counts and click through rate. 
''')

txt('**Behavioral Analysis of Shape Memory Alloys for 4D Printing** [*Research Project*](https://drive.google.com/drive/folders/1-YI1nSfaayxFkQvQMFZIia3nRsu2A11J?usp=sharing )',
    'May 2021')
st.markdown('''
- Advanced manufacturing using shape shifting alloys to study the thermal and mechanical cycles of a Nitinol wire.
- Performed experiments to collect primary data for a 3 point mechanical bending system, cleaned and analyzed datasets using Microsoft Excel to draw inferences based on stress-strain curves for different temperature distributions to distinguish between two material compositions.
- Formulated a mathematical model to determine the stress-strain relation for the three-point bending mechanical system.
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
    'Dec 2018')
st.markdown('''
- Repair analysis for a torpedo ladle car used to carry molten steel from a blast furnace. 
- Worked with a senior engineer to measure the structural integrity and strength of a torpedo ladle post the welding phase.    
''')

#####################
st.markdown('''
## Courses and Certifications
''')
st.markdown('''
### Relevant Coursework and Expertise
Visual Analytics, Database Design Implementation, Software Construction, Foundations of Data Science and Analytics, Applied Statistics, Computer Programming using C++, Calculus, Linear Algebra, Ordinary Differential Equations, Data Analysis, Numerical Analysis, Probability and Statistics
''')
st.markdown('''
### Certifications 
''')
txt3('Link to all the certifications:',
     '[Certificates](https://drive.google.com/drive/folders/1zeoSvGmipYM5Hw2IStvybJilhFgNT0FR?usp=sharing)')

st.markdown('''
#### LinkedIn
Data Ethics - Managing private customer data  
Building Analytical Skills with Statistical Analysis  
Advanced SQL for Data Scientists  
Master SQL for Data Science  
SQL: Tips, Tricks and Techniques  
SQL: Data Reporting and Analysis  
Statistics Foundations
Probability
Presto Essentials: Data Science  
Essential Math for Machine Learning  
Introduction to Data Science  
Learning SQL Programming  
Python for Data Science: Tips, Tricks and Techniques  
Python for Data Visualization  
SQL Essential Training  

#### IBM  
Data Science Methodologies  
Machine Learning with Python  
Python for Data Science  

#### GUVI - IIT Madras  
Descriptive Statistics  
Engineering Data Science Systems  
Statistics
''')

#####################
st.markdown('''
## Positions of Responsibility 
''')

txt('**Public Relations and Outreach Coordinator** for an Entrepreneurship Cell',
    '2018 - 2021')
st.markdown('''
- Sole point of contact to manage public relations with industry experts, guest speakers and university directors
- Coordinate with Event Management team to host events, talks, competitions and entrepreneurial activities
- Lead and developed the [Institute Innovation Council at IIT Dharwad](https://www.iitdh.ac.in/iic/) since it was formed in 2018
''')

txt('**Class Representative** for an Undergraduate Program',
    '2017 - 2021')
st.markdown('''
- Manage the class schedules and events for a Mechanical Engineering undergraduate degree program
- Co-ordinated with the Dean, professors and students to organize academic and non-academic events
''')

txt('**Formula Student (FSAE)** for Formula Bharat',
    '2018 - 2020')
st.markdown('''
- Electrical team lead directly managing a team to work on the inner harness and wiring for all electrical elements in the car
- Co-ordinated with the Dean, professors and students to organize academic and non-academic events
''')

txt('**Career Development Cell Volunteer**',
    'Aug 2020')
st.markdown('''
- Hosted Career events for undergraduate students to help build connections and establish a network with industry professionals 
''')

#####################
st.markdown('''
## Activities and Achievements
''')

st.markdown('''
- Bagged 3rd in Intramurals Badminton Tournament (an Inter-RIT league) in April 2022
- Achieved 4th place in DevHack 2.0 (an annual tech-fest hackathon at IIT Dharwad) for designing a "Smart Closet" that sanitizes and dries laundry in a closet space.
- Ranked 8th in Chess at the Inter IIT Sports Meet (national inter-college event) at Indian Institute of Technology, Madras, India in December 2017
- Placed 2nd twice in Inter-Departmental Football League at IIT Dharwad in 2018 and 2020
- College topper for one of the courses (Mechanical Measurements), which involves data collection and descriptive analysis of the data collected from various experiments and equipment.
''')

#####################
st.markdown('''
  ## Contact Me
  ''')
st.markdown('''
Got a catchy idea for a project collab or want to get in touch to know more about my interests?   
Hit me up! I'm all ears.   
Email me at ritvik.teja@gmail.com   
''')