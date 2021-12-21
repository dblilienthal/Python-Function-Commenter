from langdetect import detect_langs
def detectEnglish(input):
    try:
        if(detect_langs(input)[0].lang=="en"):
            return True
        else: 
            return False
    except:
        return False

def add_features(df):       
    df['docstring_isEnglish'] = df['docstring'].apply(lambda x: detectEnglish(str(x)))
    return df