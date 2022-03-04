import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys



# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()



def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    word_count = {}
    final_text = []
    
    for word in file_contents.split():
        text = ""
        for letter in word.lower():
            if letter not in punctuations and letter.isalpha():
                text += letter
            
        if word not in uninteresting_words:
            final_text.append(text)
            
    for word in final_text:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
                      
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_count)
    return cloud.to_array()



# Display your wordcloud image

myimage = calculate_frequencies("Humpty Dumpty is a character in an English nursery rhyme,probably originally a riddle and one of the best known in the English-speaking world. He is typically portrayed as an anthropomorphic egg, though he is not explicitly described as such.")
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
