import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 

st.write('''
# Ritvik Chebolu
##### *M.Sc. in Data Science | Analytics Engineer at Wayfair* 
''')

image = Image.open('circle_cropped.png')
st.image(image, width=150)

# image_path = 'square.jpg'
# image = Image.open(image_path)
# st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Data Science graduate student at Rochester Institute of Technology, New York, USA
- Analytics Engineer Co-op at Wayfair
- Ex-Data Scientist Co-op at Carrier Corporation
- Previous Graduate Teaching Assistant at RIT
- Bachelor's degree from Indian Institute of Technology Dharwad (IIT Dharwad)
- A chess geek who also loves playing Football(Soccer), Badminton, Basketball, Cricket and Ping Pong
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
        <a class="nav-link" href="https://bit.ly/gdrive-resume">Resume</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experience">Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
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
txt3('Resume', 'https://bit.ly/gdrive-resume')
txt3('LinkedIn', 'https://www.linkedin.com/in/ritvik-chebolu')
txt3('Substack', 'https://ritvikchebolu.substack.com')
txt3('GitHub', 'https://github.com/ritvik-chebolu')
txt3('Twitter', 'https://twitter.com/ritvikteja')

#####################
st.markdown('''
## Education
''')

txt('**Master of Science** (Data Science), *Rochester Institute of Technology*, New York',
    'Aug 2021 - May 2024')
st.markdown('''
- GPA: `3.70`
- Coursework: Applied Data Science, Information Retrieval and Text Mining, Software Engineering for Data Science, Non-Relational Data Management, Database Design Implementation, Data Management and Analytics, Foundations of Data Science and Analytics, Applied Statistics, Software Construction, Visual Analytics
''')

txt('**Bachelor of Technology** (Mechanical Engineering), *Indian Institute of Technology Dharwad*, Karnataka, India',
    'Aug 2017 - May 2021')
st.markdown('''
- GPA: `3.88` 
- Relevant coursework: Calculus, Linear Algebra, Ordinary Differential Equations, Data Analysis, Numerical Analysis
- Research work in the field of computational advanced manufacturing
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `SQL`, `Java`, `R`, `C++`, `JavaScript`, `XML`, `MATLAB`')
txt3('Technologies', '`GCP`, `AWS`, `Tableau`, `Excel`, `MySQL`, `PowerBI`, `Microsoft Office`, `Android Studio`')
txt3('Libraries',
     '`TensorFlow`, `Keras`, `Scikit Learn`, `OpenCV`, `Streamlit`, `Seaborn`, `plotly`, `Pandas`, `NumPy`, '
     '`ggplot2`, `Beautiful Soup`')

#####################
st.markdown('''
## Experience 
''')

txt('**Analytics Engineer Co-op @ Wayfair**', 'July 2023 - Present')
st.markdown('''
- Developed and optimized algorithms for the Outlet store Pricing tool and Inventory Management (Operations) forecasting, increasing the quantity on hand by 10% and revenue generated by 15% on a weekly basis. 
- Utilized inventory forecasting analytics to yield a 24% improvement in supply chain efficiency, resulting in a monthly cost savings of $100k in inventory management.
- Set up an analytics workflow to extract Point of Sales data with APIs, setting up KPI dashboards and sales reports that were used to make data-driven decisions that improved outlet store operations.
''')

txt('**Auxiliary Services Analyst @ RIT**', 'May 2023 - June 2023')
st.markdown('''
- Cleaning duplicated data records from the RIT Dining Services database for demand forecasting.
- Extending Technical Support to the dining cafes by modifying their software to create, update and delete items from the menus.
- Developing an end-to-end framework to set up kiosks in dining areas, and assist with hardware and software installation.
''')

txt('**Graduate Teaching Assistant @ RIT**', 'Jan 2023 - May 2023')
st.markdown('''
- Teaching Assistant for the courses `Database Design Implementation` (ISTE 608) and `Data Modeling` (ISTE 230) at RIT.
- Grading assignments, holding office hours, and assisting 50 students with their coursework.
''')

txt('**Junior Machine Learning Engineer @ Omdena - (Open Source Contribution)**', 'Dec 2022 - Jan 2023')
st.markdown('''
- Contributed to the development of a Recommendation Engine to create a self learning user experience with relevant chess puzzles for beginners to mid-level players on the ChessX platform.
- Developed a Machine Learning model using player stats and game history in a vectorized format to match with the most relevant puzzles and game analysis.
''')

txt('**Data Scientist Co-op @ Carrier Corporation**, Pittsford, New York',
    'May 2022 - Nov 2022')
st.markdown('''
- Developing and formulating a problem statement by investigation to identify user pain points and decrease customer's investment in security personnel by about $175k annually. 
- Leveraging data science methodologies to deploy machine learning models which reduce false alarm notifications in security systems by around 38%.
- Worked with the product and business teams, and collaborated with customer's for direct feedback on pain-points to develop an analytical/predictive model using LSTM (Recurrent Neural Network) and a time-series k-means clustering algorithm to detect potential security threats in buildings.
- Analyzing a 330 GB database consisting of a customer's live security monitoring system data collected and utilizing cloud architecture (AWS) to store, clean, process, analyze, transform, predict and finally deploy a machine learning model into production.
- Predictive analytics for device health and strategize maintenance shutdowns for security devices and systems.
''')

txt('**Thermal Engineering Intern @ Visakhapatnam Steel Plant**, India',
    'July 2019')
st.markdown('''
- Dashboard analytics from turbine blades lead to a 12% increase in operational efficiency in terms of response time.
- Analysis of variation of blade temperature over time for steam and gas turbines.
- Inferred and drew plots of theoretical velocity profiles and turbine blade temperatures at different lengths of turbines to validate the data with simulation results from measurement systems. 
- This intern was closely linked to my previous internship at BHEL Hyderabad because BHEL Hyderabad deals with the manufacturing and assembly phase of Steam turbines whereas this intern throws light on the inner workings (control and operation) of Steam and Gas Turbines and the associated power generation aspects.
''')

txt('**Steam Turbine Engineering Intern @ Bharat Heavy Electronics Ltd**, Hyderabad, India',
    'May 2019')
st.markdown('''
- Inferential analysis of blade profile to suggest a 3% reduction in fluid drag for 1.4% decrement in overall thermal loss.
- Analysis of the variation in blade profiles of a turbine over length for various turbine capacities to examine the flow rates, temperature distribution and stress-strain curves from theoretical data.
- Understanding the inner workings and control of a steam turbines of different capacities and cross-validate their operational parameters with real-time data collected from testing sensors.
''')

txt('**Manufacturing Engineering Intern @ Visakhapatnam Steel Plant**, India',
    'Dec 2018')
st.markdown('''
- Repair analysis for a green sand casting material to replace with a material to speed up molding by 13 seconds/m3.
- Repair analysis for a torpedo ladle car used to carry molten steel from a blast furnace. 
- Mechanics involved with part manufacture and assembly fixture for materials with varying compositions and to determine the best material in terms of stress and fatigue levels.
''')

#####################
st.markdown('''
## Projects
''')

txt('**National Hockey League Database Application Design** ',
    'May 2023')
st.markdown('''
- Developed an end-to-end database application with views, reports, forms and dashboards to store and display information about NHL season games.
''')

txt('**Sequence Classification using NLP** '
    '[*Sentiment Analysis Web Application*](https://sequence-classification-nlp.streamlitapp.com/)',
    'Mar 2022')
st.markdown('''
- Classifying user's input statements based on their polarity and subjectivity scores to get a sense of the user's expression.
- Built with TextBlob library built on NLTK which has a predefined set of words classified as positive, negative and neutral alonng with a score assigned to each tokenized word.
''')

txt('**Visual Analytics 2019 (VAST) Challenge** '
    '[*Disaster Management Analysis Webpage*](https://ritvik-chebolu.github.io/VAST-2019-MC1/)',
    'Mar 2022')
st.markdown('''
- A visual analytics approach to solve a crisis management problem, carry rescue operations and address issues reported in a city.
- Providing timely updates to rescue teams using interactive radar time-series plots and tableau dashboards for real-time city surveillance and understanding the user (citizens) pain-points from a remote location.
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

txt('**Customer Behavior Pattern Analysis for Revenue Generation** '
    '[*Tableau Dashboard*](https://public.tableau.com/app/profile/ritvik7660/viz/CustomerRevenueAnalysis_16727974077450/RevenueAnalysis)',
    'Nov 2021')
st.markdown('''
- Assembled a Tableau dashboard to analyze revenue generation using data on customer behavior and purchase patterns to identify growth opportunities and supply chain trends.
''')

txt('**LinkedIn Social Media Analytics** [*Tableau Dashboard*](https://public.tableau.com/app/profile/ritvik4126/viz/FestMan05-20-2021/Inferences)',
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
## Courses and Certifications
''')
st.markdown('''
### Relevant Coursework and Expertise
Prompt Engineering for Developers, Visual Analytics, Database Design Implementation, Software Construction, Foundations of Data Science and Analytics, Applied Statistics, Computer Programming using C++, Calculus, Linear Algebra, Ordinary Differential Equations, Data Analysis, Numerical Analysis, Probability and Statistics
''')
st.markdown('''
### Certifications 
''')
txt3('Link to all the certifications:',
     '[Certificates](https://drive.google.com/drive/folders/1zeoSvGmipYM5Hw2IStvybJilhFgNT0FR?usp=sharing)')

st.markdown('''
#### AWS (Amazon Web Services)
AWS Technical Essentials Training  

#### Carrier
Professional Scrum Master Certification  

#### LinkedIn
Advanced AI: Transformers for NLP using Large Language Models  
Transformers: Text Classification for NLP using BERT  
Data Analytics: Dashboards vs. Data Stories  
Data Analytics: Graph Analytics  
Data Visualization: Storytelling  
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

txt('**Speaker Support Lead** at **Open Data Science Conference (ODSC) West 2023**',
    'Nov 2022')
st.markdown('''
- Helped set up speaker sessions for ODSC West 2023 along with other fun networking events for the attendees and speakers at the conference.
- Hosted the ODSC West '23 conference collaborating with the event staff to ensure speaker's readiness before talks.
''')

txt('**Public Relations and Outreach Coordinator** for an Entrepreneurship Cell',
    '2018 - 2021')
st.markdown('''
- Sole point of contact to manage public relations with industry experts, guest speakers and university directors.
- Coordinate with Event Management team to host events, talks, competitions and entrepreneurial activities.
- Lead and developed the [Institute Innovation Council at IIT Dharwad](https://www.iitdh.ac.in/iic/) since it was formed in 2018.
''')

txt('**Class Representative** for an Undergraduate Program',
    '2017 - 2021')
st.markdown('''
- Manage the class schedules and events for a Mechanical Engineering undergraduate degree program.
- Co-ordinated with the Dean, professors and students to organize academic and non-academic events.
''')

txt('**Formula Student (FSAE)** for Formula Bharat',
    '2018 - 2020')
st.markdown('''
- Electrical team lead directly managing a team to work on the inner harness and wiring for all electrical elements in the car.
- Co-ordinated with the Dean, professors and students to organize academic and non-academic events.
''')

txt('**Career Development Cell Volunteer**',
    'Aug 2020')
st.markdown('''
- Hosted Career events for undergraduate students to help build connections and establish a network with industry professionals.
''')

#####################
st.markdown('''
## Activities and Achievements
''')

st.markdown('''
- Runner's Up for the Men's Doubles category in Intramurals Badminton Tournament (an RIT league) in Novemeber 2022 and chosen to be a Varisty Athlete until the 2023 season. 
- Bagged 3rd for the Men's Doubles category in Intramurals Badminton Tournament (an RIT league) in April 2022.
- Achieved 4th place in DevHack 2.0 (an annual tech-fest hackathon at IIT Dharwad) for designing a "Smart Closet" that sanitizes and dries laundry in a closet space.
- Ranked 8th in Chess at the Inter IIT Sports Meet (national inter-college event) at Indian Institute of Technology, Madras, India in December 2017.
- Placed 2nd twice in Inter-Departmental Football League at IIT Dharwad in 2018 and 2020.
- College topper for one of the courses (Mechanical Measurements), which involves data collection and descriptive analysis of the data collected from various experiments and equipment.
''')

#####################
st.markdown('''
  ## Contact Me
  ''')
st.markdown('''
Got a catchy idea for a project collab or want to get in touch to know more about my interests?   
Hit me up! I'm all ears.   
Email me at ritvik.teja@gmail.com or connect with me on [LinkedIn](https://www.linkedin.com/in/ritvik-chebolu) ^_~
''')