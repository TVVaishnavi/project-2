import pandas as pd
from textblob import TextBlob
from nltk.tokenize import word_tokenize

easy_word=[]
medium_word=[]
hard_word=[]
excel_file="Book2.xlsx"
#column_to_read=['Question Passage','Prompt','Choice A','Choice B','Choice C','Choice D']
df=pd.read_excel(excel_file)

#all_text=' '.join(df.stack().astype(str))
def categorize_word(word):
    blob=TextBlob(word)
    if 3<len(blob.words)<=5:
       easy_word.append(words)
    elif 5<len(blob.words)<=7:
        medium_word.append(word)
    else:
        hard_word.append(word)

def classify_words(cell):
    if isinstance(cell,str):
        words=TextBlob(cell).words
        categorize_words={'Easy':[],'Medium':[],'Hard':[]}
        for word in words:
            category=categorize_word(word)
            categorize_words[category].append(word)
        return categorize_words
    else:
        return {'Easy':[], 'Medium':[], 'Hard':[]}














