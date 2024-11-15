# EDA and Preprocessing of French Text

## Overview
This project focuses on exploring and preprocessing French text to prepare it for natural language processing tasks. It covers tokenization, removal of stopwords, stemming, and other preprocessing techniques to clean and transform the data into a format suitable for further analysis or model training.

## Project Structure

1. **Text Cleaning and Tokenization**
   - Converted the original text to lowercase for consistency.
   - Tokenized the text using both the NLTK library and custom regular expressions to handle specific tokenization rules for French language features like contractions (e.g., "d'où", "qu'il").

2. **Stopword Removal**
   - Removed common French stopwords using NLTK's French stopword list.
   - Customized the stopword list to include additional words deemed irrelevant for further analysis.

3. **Stemming**
   - Applied stemming using the Snowball Stemmer for French to reduce words to their root forms, making the text more uniform and easier to analyze.

## Key Skills Demonstrated
- **Text Tokenization**: Implemented tokenization with both standard NLTK tools and custom regular expressions to handle unique aspects of French grammar.
- **Stopword Removal**: Removed standard and customized stopwords to focus on meaningful content in the text.
- **Text Normalization**: Converted text to lowercase and stemmed words to ensure uniformity.
- **Handling Special Cases**: Managed common contractions in French for accurate tokenization.

## Technologies Used
- **Python**: Programming language for text processing.
- **NLTK**: Tokenization, stopword removal, and stemming.
- **RegexpTokenizer**: Customized tokenization using regular expressions.

## How to Run the Project
1. **Requirements**: Ensure you have Python installed with the following libraries: `nltk`.
2. **Run the Code**: Execute the script in your preferred IDE or environment (e.g., Jupyter Notebook, Google Colab).

## Project Highlights
- **Tokenization with Custom Regex**: Implemented regular expressions to accurately tokenize French text, considering unique contractions.
- **Stopword Removal and Customization**: Refined the stopword list to improve the relevance of the cleaned text.
- **Stemming for Text Normalization**: Utilized the Snowball Stemmer for French to reduce inflected words to their root forms, improving text consistency.

## Future Improvements
- **Lemmatization**: Implement lemmatization to provide more meaningful reductions of words compared to stemming.
- **Named Entity Recognition (NER)**: Add NER to identify proper nouns and important entities in the text.
- **Data Enrichment**: Analyze additional French texts to improve tokenization rules and preprocessing pipelines.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for any questions or collaboration opportunities.