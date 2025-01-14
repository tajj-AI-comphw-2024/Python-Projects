# Skills Used: Strings, loops, dictionaries.
# Analyze lyrics to find and count the frequency of each word.
# Add functionality to ignore common words like "the" or "and" (a precursor to text analysis in AI).
# Goal: Explore text processing concepts foundational to AI and NLP (Natural Language Processing).

import os
import re

def analyze_lyrics(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        return "Error: File not found."
    
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            # Convert the line to lowercase and split it into words
            words = line.lower().split()
            
            # Iterate over each word
            for word in words:
                # Remove punctuation marks from the word
                word = re.sub(r'[^\w\s]', '', word)
                
                # Ignore common words like "the" or "and"
                if word not in ['the', 'and']:
                    # If the word is already in the dictionary, increment its count
                    if word in word_freq:
                        word_freq[word] += 1
                    # Otherwise, add the word to the dictionary with a count of 1
                    else:
                        word_freq[word] = 1
    
    # Sort the dictionary by word frequency in descending order
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    
    # Return the sorted dictionary
    return sorted_word_freq

# Example usage

file_path = 'example_lyrics.txt'
result = analyze_lyrics(file_path)
print(result)