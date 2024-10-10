import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns
import os

def filter_columns(df):
    ''' Function grabs all of the columns from the raw csv file that we are interested in keeping.'''
    columns = [
        'SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDBORN4', 'DMDEDUC2', 'DMDMARTZ', 'DMDHHSIZ', 'INDFMPIR',    # DEMO_L.XPT
        'LBDTCSI',  # TCHOL_L.XPT
        'DIQ010', 'DID040', 'DIQ160',  # DIQ_L.XPT
        'DBQ930', 'DBQ940', 'DBQ945',  # DBQ_L.XPT
        'BPQ020', 'BPQ080', 'BPQ101D', 'BPQ150',  # BPQ_L.XPT
        'PAD680', 'PAD810U', 'PAD790U',  # PAQ_L.XPT
        'ALQ130', 'ALQ142', 'ALQ280',  # ALQ_L.XPT
        'INDFMMPC',  # INQ_L.XPT
        'DPQ010', 'DPQ020', 'DPQ030', 'DPQ040', 'DPQ050', 'DPQ060', 'DPQ070', 'DPQ080', 'DPQ090', 'DPQ100',  # DPQ_L.XPT
        'SMQ040',  # SMQ_L.XPT
    ]

    # Filter the merged dataframe to keep only the desired columns
    filtered_df = df[columns]

    return filtered_df

def convert_to_null(df):
    ''' Function converts all of the values that are not applicable to NaN.'''
    # Convert all values that are not applicable to NaN
    cols_above_7 = ['RIDRETH3', 'DMDEDUC2', 'DMDMARTZ', 'DIQ010', 'DIQ160',
    'DBQ930', 'DBQ940', 'DBQ945', 'BPQ020', 'BPQ080', 'BPQ101D', 'BPQ150',
    'SMQ040', 'DPQ010', 'DPQ020', 'DPQ030', 'DPQ040', 'DPQ050', 'DPQ060',
    'DPQ070', 'DPQ080', 'DPQ090', 'DPQ100']
    
    df.loc[:, cols_above_7] = df.loc[:, cols_above_7].apply(lambda col: col.map(lambda x: np.nan if x > 7 else x))

    df.loc[:, 'PAD680'] = df['PAD680'].map(lambda x: np.nan if x > 1380 else x)
    df.loc[:, 'ALQ130'] = df['ALQ130'].map(lambda x: np.nan if x > 15 else x)
    df.loc[:, 'ALQ142'] = df['ALQ142'].map(lambda x: np.nan if x > 10 else x)
    df.loc[:, 'ALQ280'] = df['ALQ280'].map(lambda x: np.nan if x > 10 else x)
    df.loc[:, 'DID040'] = df['DID040'].map(lambda x: np.nan if x > 80 else x)

    return df

def map_cat_vars(df):
    ''' Function maps the categorical variables to their actual meaning.'''
    # Map categorical variables to their actual meaning
    df['RIDRETH3'] = df['RIDRETH3'].map({
        # Race-Ethnicity
        1: 'Mexican American',
        2: 'Other Hispanic',
        3: 'Other Hispanic',
        4: 'Non-Hispanic White',
        5: 'Non-Hispanic Black',
        6: 'Non-Hispanic Asian',
        7: 'Other Race (Including Multiracial)'
    })

    df['DMDBORN4'] = df['DMDBORN4'].map({
        # Country of Birth
        1: 'Born in 50 US States or Washington, DC',
        2: 'Born in Other Countries, including U.S. territories',
    })

    df['DMDEDUC2'] = df['DMDEDUC2'].map({
        # Education Level
        1: 'Less than 9th grade',
        2: '9-11th grade (Includes 12th grade with no diploma)',
        3: 'High school graduate/GED or equivalent',
        4: 'Some college or AA degree',
        5: 'College graduate or above',
    })

    df['DMDMARTZ'] = df['DMDMARTZ'].map({
        # Marital Status
        1: 'Married/Living with partner',
        2: 'Widowed/Divorced/Separated',
        3: 'Never married',
    })

    df['DMDHHSIZ'] = df['DMDHHSIZ'].map({
        # Household Size
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7 or more people',
})

    df['DIQ010'] = df['DIQ010'].map({
        # Diabetes
        1: 'Yes', 2: 'No', 3: 'Borderline'})

    df['DIQ160'] = df['DIQ160'].map({
        # Told you have prediabetes
        1: 'Yes', 2: 'No'  })

    df['DBQ930'] = df['DBQ930'].map({
        # Main meal planner/preparer
        1: 'Yes', 2: 'No' })

    df['DBQ940'] = df['DBQ940'].map({
        # Main food shopper
        1: 'Yes', 2: 'No' })

    df['DBQ945'] = df['DBQ945'].map({
        # Shared food shopping duty
        1: 'Yes', 2: 'No' })
    
    df['BPQ020'] = df['BPQ020'].map({
        # Ever told you had high blood pressure
        1: 'Yes', 2: 'No' })
    
    df['BPQ080'] = df['BPQ080'].map({
        # high cholesterol level
        1: 'Yes', 2: 'No' })
    
    df['BPQ101D'] = df['BPQ101D'].map({
        # taking medication to lower blood cholesterol
        1: 'Yes', 2: 'No' })

    df['BPQ150'] = df['BPQ150'].map({
        # taking high blood pressure medication
        1: 'Yes', 2: 'No' })
    
    df['ALQ142'] = df['ALQ142'].map({
        # num of days 4/5 drinks consumed in the past 12 months
        0: 'Never in the last year',
        1: 'Every day',
        2: 'Nearly every day',
        3: '3 to 4 times a week',
        4: '2 times a week',
        5: 'Once a week',
        6: '2 to 3 times a month',
        7: 'Once a month',
        8: '7 to 11 times in the last year',
        9: '3 to 6 times in the last year',
        10: '1 to 2 times in the last year',
    })

    df['ALQ280'] = df['ALQ280'].map({
        # num of times 8+ drinks in 1 day/past 12 months 
        0: 'Never in the last year',
        1: 'Every day',
        2: 'Nearly every day',
        3: '3 to 4 times a week',
        4: '2 times a week',
        5: 'Once a week',
        6: '2 to 3 times a month',
        7: 'Once a month',
        8: '7 to 11 times in the last year',
        9: '3 to 6 times in the last year',
        10: '1 to 2 times in the last year',
    })

    df['INDFMMPC'] = df['INDFMMPC'].map({
        # family monthly poverty level category
        1: 'Monthly poverty level index <= 1.30',
        2: '1:30 < Monthly poverty level index < 1:85',
        3: 'Monthly poverty level index > 1.85',
    })

    df['DPQ010'] = df['DPQ010'].map({
        # have little interest in doing things
        0: 'Not at all', 1: 'Several days', 2: 'More than half the days', 3: 'Nearly every day' })

    df['DPQ020'] = df['DPQ020'].map({
        # feeling down, depressed, or hopeless
        0: 'Not at all', 1: 'Several days', 2: 'More than half the days', 3: 'Nearly every day' })
    
    df['DPQ030'] = df['DPQ030'].map({
        # trouble sleeping or sleeping too much
        0: 'Not at all', 1: 'Several days', 2: 'More than half the days', 3: 'Nearly every day' })
    
    df['DPQ040'] = df['DPQ040'].map({
        # feeling tired or having little energy
        0: 'Not at all', 1: 'Several days', 2: 'More than half the days', 3: 'Nearly every day' })
    
    df['DPQ050'] = df['DPQ050'].map({
        # poor appetite or overeating
        0: 'Not at all', 1: 'Several days', 2: 'More than half the days', 3: 'Nearly every day' })
    
    df['DPQ060'] = df['DPQ060'].map({
        # feeling bad about yourself
        0: 'Not at all', 1: 'Several days', 2: 'More than half the days', 3: 'Nearly every day' })
    
    df['DPQ070'] = df['DPQ070'].map({
        # trouble concentrating on things
        0: 'Not at all', 1: 'Several days', 2: 'More than half the days', 3: 'Nearly every day' })
    
    df['DPQ080'] = df['DPQ080'].map({
        # moving or speaking slowly or too fast
        0: 'Not at all', 1: 'Several days', 2: 'More than half the days', 3: 'Nearly every day' })
    
    df['DPQ090'] = df['DPQ090'].map({
        # thoughts that you would be better off dead
        0: 'Not at all', 1: 'Several days', 2: 'More than half the days', 3: 'Nearly every day' })
    
    df['DPQ100'] = df['DPQ100'].map({
        # difficulty these problems have caused
        0: 'Not difficult at all', 1: 'Somewhat difficult', 2: 'Very difficult', 3: 'Extremely difficult' })
    
    df['SMQ040'] = df['SMQ040'].map({
        # smoking status
        1: 'Every day', 2: 'Some days', 3: 'Not at all' })
    
    return df
