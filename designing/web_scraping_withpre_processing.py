from bs4 import BeautifulSoup
import requests
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import nltk
from nltk.corpus import stopwords

url="https://en.wikipedia.org/wiki/University_of_Strathclyde"

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response=requests.get(url,headers=headers)


#The HTTP response code 200 is OK code and means our request succeeded. Since we used the HTTP Request GET, it means a resource was retrieved
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the main content of the page
    main_content = soup.find('p')  #Excract the paragraphs
    
    if main_content: #We concatenate the paragraphs
        paragraphs = [
        p.get_text(separator=" ", strip=True)
        for p in soup.find_all("p")
        if p.get_text(strip=True)
        ]

        text = " ".join(paragraphs)  # we add space between paragraphs
        print(text)
    else:
        print("Main content not found.") # Nothing in the response
else:
    print("Failed to retrieve the webpage.") #Our request was not successful


sorted_text_stream = ' '.join(sorted(text.split(), key=str.lower))
print(sorted_text_stream)

cleaned_text = re.sub(r'[^a-zA-Z\s]', '', sorted_text_stream)
cleaned_text = cleaned_text.lower()
print(cleaned_text)

word_counts = Counter(cleaned_text.split())

# Sort by frequency (highest first)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print each word and frequency on a new line
for word, frequency in sorted_word_counts:
    print(f"{word}: {frequency}")

ranks = range(1, len(sorted_word_counts) + 1)
frequencies = [frequency for _, frequency in sorted_word_counts]

log_frequencies = np.log(frequencies)
log_ranks = np.log(ranks)


# Plot (a) - Frequency vs. Rank in log-log scale
plt.figure(figsize=(6, 3))

# Plot the scatter of log frequency vs. log rank
plt.subplot(1, 2, 1)
plt.scatter(log_ranks, log_frequencies, color='blue', s=1, alpha=0.5, label='Data')

# Fit a line to the log-log data
slope, intercept, r_value, _, _ = linregress(log_ranks, log_frequencies)
plt.plot(log_ranks, slope * log_ranks + intercept, color='red', linewidth=2, label=f'Fit: slope={slope:.2f}')

plt.xlabel(r"$\log_{e}$ rank")
plt.ylabel(r"$\log_{e}$ frequency")
plt.legend()



plt.tight_layout()
plt.show()

nltk.download('stopwords')

words = cleaned_text.lower().split()

# Get stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered_words = [word for word in words if word not in stop_words]

# Result
print(filtered_words)

print(len(cleaned_text))
print(len(filtered_words))