# Operation-Diabetes-Prevention

# Describe project, purpose, and goals

## Setting Up the Virtual Enviornment
1. Clone the Project Repository
    - git clone <repository_url>
    - cd <repository_directory>
2. Create Virtual Environment
    - python -m venv venv
3. Activate the Virtual Environment
    Windows: 
    - venv\Scripts\activate
    MacOS
    - source venv/bin/activate
4. Install Required Packages
    - pip install -r requirements.txt
5. Deactivate the Virtual Environment when finished working
    - deactivate

## Dataset Citation
Our project uses the following datasets: 

Centers for Disease Control and Prevention. (2023). National Health and Nutrition Examination Survey (NHANES): August 2021 to August 2023 [Data file]. https://www.cdc.gov/nchs/nhanes/index.htm. Accessed October 5, 2024.


### Data Files

Data File    | Data FileName                                                | Key Variables                    
-------------|--------------------------------------------------------------|----------------
'DEMO_L.XPT' |Demographics data: Demographic variables and sample weights   | 
`TCHOL_L.XPT'|Laboratory data: Cholesterol - Total                          |
'DIQ_L.XPT'  |Questionnaire data: Diabetes                                  |
'DBQ_L.XPT'  |Questionnaire data: Diet Behavior and Nutrition               |
'BPQ_L.XPT'  |Questionnaire data: Blood Pressure and Cholesterol            |
'PAQ_L.XPT'  |Questionnaire data: Physical Activity                         |
'ALQ_L.XPT'  |Questionnaire data: Alcohol Use                               |
'HSQ_L.XPT'  |Questionnaire data: Current Health Status                     |
'INQ_L.XPT'  |Questionnaire data: Income                                    |
'DPQ_L.XPT'  |Questionnaire data: Mental Health - Depression Screener       |
'SMQ_L.XPT   |Questionnaire data: Smoking - Cigarette Use                   |

