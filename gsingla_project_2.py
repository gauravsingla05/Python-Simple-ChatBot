# For understanding the chatbot working and vecotorization of data.
# Sharma, Shubham (2020, December 4). Creating a simple chatbot with zero-knowledge base for question-answering. Medium. Retrieved April 26, 2022, from https://shubhjd.medium.com/creating-a-simple-chatbot-with-zero-knowledge-base-for-question-answering-222d65719d2b 

import pandas as pd
import string
import io
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob.en import Spelling
import re
from nltk.corpus import stopwords

# Reading the bot training file and setting queston, answer variables

File_path = "G:\TTU\Intelligent system\chatbot\QA_Data\QA_Data\dev_data\\real.csv"
model_file_path = "G:\TTU\Intelligent system\chatbot\QA_Data\QA_Data\dev_data\\model.txt"


data = pd.read_csv(File_path,encoding="cp1252" )
question= list(data['question'])
answer= list(data['answer'])

# Creating spell checker mode file and train the bot
# Popovic, Kristina (2021, July 15). Spelling correction in python with textblob. Stack Abuse. Retrieved April 26, 2022, from https://stackabuse.com/spelling-correction-in-python-with-textblob/ 

model_words = re.findall("[a-z]+", str(question).lower()) 
spelling = Spelling(path = model_file_path)
spelling.train(" ".join(model_words), model_file_path)



# FUNCTION NAME: lemmatize
# PARAMETERS: text
# PURPOSE: Lemmatization of data 


def lemmatize(data):
    data = ''.join([d for d in data if d not in string.punctuation])
    tokens = nltk.word_tokenize(data)
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

# FUNCTION NAME: chatFxn
# PARAMETERS: text
# PURPOSE: responsible for finding the answers for user input

def chatFxn(input_text):
    input_len = len(input_text.split())
    input_text = input_text.lower()
    split_ques = input_text.split()
    try_again_text = "Oops! Try again with another question 😟 :"
    
#   Correcting the sentence spellings
#   Popovic, K. (2021, July 15). Spelling correction in python with textblob. Stack Abuse. Retrieved April 26, 2022, from https://stackabuse.com/spelling-correction-in-python-with-textblob/ 
    input_text_correct = " "
    for i in split_ques :
        input_text_correct = input_text_correct +" "+ spelling.suggest(i)[0][0]
           
#   Check if spellings are correct or not    
#   For removing punctuation from string using regex.
#   Manjeet, (2021, June 30). Python | Remove punctuation from string. GeeksforGeeks. Retrieved April 26, 2022, from https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
    input_text_correct_reg = re.sub(r'[^\w\s]', '', input_text_correct.lower().replace(" ", ""))
    input_text_reg = re.sub(r'[^\w\s]', '', input_text.lower().replace(" ", ""))
    if(input_text_correct_reg != input_text_reg ): 
        print('Check Spelling, Did you mean : '+str(input_text_correct) + ' ?')
        yes_or_no = input("Type yes or no: ") 
        if(yes_or_no.lower()=="yes"):
            print("Showing results for : " + str(input_text_correct))
            input_text = input_text_correct
        else:
            return try_again_text
            input_text = ''

        
# Check if user input data is not empty
    
    if(input_text):
        reply=''
        
# Input text should be more than one word

        if(input_len<=1):
            return reply+"Please enter more than 1 keyword"
        
# Vectorizing the data and finding possible correct answer    
# Sharma, Shubham (2020, December 4). Creating a simple chatbot with zero-knowledge base for question-answering. Medium. Retrieved April 26, 2022, from https://shubhjd.medium.com/creating-a-simple-chatbot-with-zero-knowledge-base-for-question-answering-222d65719d2b 
        question.append(input_text)    

        vectorizer = TfidfVectorizer(tokenizer=lemmatize,stop_words='english')
        vectorized_data = vectorizer.fit_transform(question)
        posibility_matrix = cosine_similarity(vectorized_data[-1], vectorized_data)
        index=posibility_matrix.argsort()[0][-2]
        matrix_to_single_array = posibility_matrix.flatten()
        matrix_to_single_array.sort()
        result = matrix_to_single_array[-2]
        
# Confirmation : Compare user's question with actual question in dataset 
       
        if(lemmatize(question[index].lower())!=lemmatize(input_text.lower())):        
            print('Confirmation, Did you mean : '+str(question[index]))
            yes_or_no = input("Type yes or no: ") 
            if(yes_or_no.lower()=="yes"):
                print("Showing results for : " + str(question[index]))
                input_text = input_text_correct
            else:

                return try_again_text
                input_text = ''
        
        if(index<0):
            return reply+try_again_text

        if(result==0):
            bot_response=reply+try_again_text
            return bot_response
        else:
            if(answer[index]!=' ' or answer[index]!='.'):
                reply = reply+answer[index]
                return reply
            else:
                print(try_again_text)
        
                

# Main loop to call chatFxn function and keep on running until exit

while(1):
    user_input = input("Ask me or say bye to exit: 🕵️ ") 
    if(user_input=="bye"):
        print("Bot Shut Down") 
        break
    else:
        print(chatFxn(str(user_input))) 