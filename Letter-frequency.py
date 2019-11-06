#Written by: Eunsoo Jang
#Date: Sep 10, 2019

import re
import nltk
from nltk.corpus import gutenberg
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


def Asst2 (text):
    raw_txt = gutenberg.raw(text)

    #deleting all spaces in the text 
    split_txt = re.sub('(\n)+', '',raw_txt)
    split_txt = re.sub(' ','', split_txt)
    #leaving only letters
    split_txt = "".join(re.findall("[a-zA-Z]+", split_txt))
    #making all letters to lower case
    split_txt = split_txt.lower()
    #counting all the letters
    counter = Counter(split_txt)

    #calculating the frequency of each letter and puting it into a Counter called prob_counter
    prob_counter = probability(counter)
    #making the prob_counter into an ordered list
    prob_counter_sorted = prob_counter.most_common()

    #making a bar plot of the frequency of each letter
    letter = []
    frequency = []
    letter, frequency = zip(*prob_counter_sorted)
    indices = np.arange(len(prob_counter_sorted))
    plt.bar(indices, frequency, color='b')
    plt.xticks(indices, letter, rotation='horizontal')
    plt.tight_layout()
    plt.show()

#probability: a function that returns the Counter that contains the frequencies of each letter
def probability(counts):
    sum_count = float(sum(counts.values()))
    for key in counts:
        counts[key]/=sum_count
    return counts
        
