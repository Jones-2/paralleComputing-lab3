from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
#checks for words only using python's inbuilt regular expression
wordings= re.compile(r"[\w']+")
#using the list of python stop words from the natural language tool kit (nltk) module
stop_words=stopwords.words('english')

'''frequency word count class'''

class wordCounter(MRJob):
    def steps(self):
        '''Indicates the number of mappers and reducers needed to execute this program'''
        return[
            MRStep(mapper=self.mapping, reducer=self.reducing)
            ]
    def mapping(self, key, text):
        
        '''mapper function that take two parameters, a key and a text.
            The function coverts all words into lower case to make it case insensitive
'''
        for key in wordings.findall(text):
             
             #ignore if word is a stopword
            if key in stop_words:
                continue
            yield (key.lower(), 1)     

    def reducing(self, key, values):
        yield (key, sum(values))

if __name__ == '__main__':
     wordCounter.run()

