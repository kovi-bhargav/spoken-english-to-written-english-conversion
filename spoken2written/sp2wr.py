import numpy as np
import re

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

def preprocess_text(sentance):
    sent = decontracted(sentance)
    sent = sent.replace('\\r', ' ')
    sent = sent.replace('\\n', ' ')
    sent = sent.replace('\\"', ' ')
    return sent 

class spoken_to_word:
    currency = {'dollar': '$', 'pound': '£', 'rupee': '₹','rupees': '₹','dollars': '$'}
    abbrevations = { 'PMO' : "Prime Minister's Office" ,
                    'WHO' : "World Health Organisation"}
    tuples =  {
                         "single": 1,
                         "double": 2,
                         "triple": 3,
                         "quadruple":4,
                         "quintuple":5,
                         "sextuple":6,
                         "septuple":7,
                         "octuple":8,
                         "nonuple":9,
                         "decuple":10
                      }      
    general =      {
                          "C M": "CM",
                          "P M O" : "PMO",
                          "P M": "PM",
                          "D M": "DM",
                          "A M": "AM",
                          "W H O": "WHO"
                       }                        

    def __init__(self , text):
      self.text = text  
        
    def expansion_of_words(self, sent):
      # Triple A => AAA
      text = sent.split()
      new_text = [ ]
      i = 0
      while i < len(text):
        if self.tuples.get(text[i]) and i+1 < len(text) and len(text[i+1]) == 1 :
          word = text[i+1]*self.tuples.get(text[i])
          new_text.append(word)
          i = i+1 
        else:
          new_text.append(text[i])
        i = i+1
      return ' '.join(new_text)
    
    def currency_conversion(self, sent):
      text = sent.split()
      new_text = [ ]
      for word in text:
        if word.lower() in list(self.currency.keys()):
          new_text.append(self.currency.get(word.lower()))
        else:
          new_text.append(word)
      return ' '.join(new_text)

    def general_abbrevations(self, sent):
        keys_cap = list(self.general.keys())
        keys_small = []
        for word in  keys_cap:
          keys_small.append(word.lower())
        for i in range(len( keys_cap)):
          if keys_cap[i] in sent :
            sent = sent.replace(keys_cap[i],self.general.get(keys_cap[i]))
          if keys_small[i] in sent :
            sent = sent.replace(keys_small[i],self.general.get(keys_small[i].upper()))

        return sent

    def expandAbbrevations(self,sent):
      text = sent.split()
      for i in range(len(text)) :
        if self.abbrevations.get(text[i]):
          text[i] = self.abbrevations.get(text[i])
      return ' '.join(text)


    def driver(self):
        #Here we can add any rule which need to be applied on the entire sentence in the preprocess_text function 
        sentence = preprocess_text(self.text)
        sentence = self.currency_conversion(sentence)
        # sentence = self.check_front_last_part_word(sentence)
        sentence = self.expansion_of_words(sentence)
        sentence = self.general_abbrevations(sentence)
        
        # output = self.combineAbbrevations(output)
        sentence = self.expandAbbrevations(sentence)


        return sentence
    
#main function 
def sp_to_wr():
    input_text = input("Enter Your paragraph of spoken english:\n\t")

    if not input_text:
      raise ValueError("[Error]: You entered nothing.")  
     #creating class object
    obj_s2w = spoken_to_word(input_text)

    output_text = obj_s2w.driver()

    print("Input: ", input_text)
    print("Output: ", output_text)
