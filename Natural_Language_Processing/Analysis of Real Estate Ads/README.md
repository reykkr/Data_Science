# Case Study: Analysis and Extraction of Information from Real Estate Ads

## Overview
This project involves analyzing real estate ads to extract meaningful information that can be used by sales staff. The goal is to break down each ad into distinct components such as price, number of rooms, salesperson, and location to create a structured dataset. The project showcases the use of natural language processing (NLP) to clean and transform unstructured real estate descriptions into actionable data.

## Project Structure
1. **Data Extraction and Tokenization**
   - Extracted individual real estate ads from a larger text collection.
   - Tokenized each ad into sentences and words using NLTK's tokenization tools.

2. **Named Entity Recognition (NER)**
   - Used Stanford NER to identify and extract locations, salesperson names, and room types from each ad.
   - Reconstructed multi-token locations to ensure accurate representation (e.g., "Cherry Creek State Park").

3. **Feature Extraction**
   - Extracted key features from the ads, including the number of bedrooms, bathrooms, and other room types using a custom-trained NER model.
   - Identified whether an ad is still active based on the phrasing in the description.

4. **Data Structuring**
   - Created a structured dataset with fields such as ID, locations, number of bedrooms, number of bathrooms, salesperson, price, and ad status.
   - Exported the data to a CSV file for easy access and further analysis.

## Key Skills Demonstrated
- **Text Tokenization and Cleaning**: Extracted meaningful sentences and words from real estate ads using NLTK and custom regular expressions.
- **Named Entity Recognition (NER)**: Leveraged pre-trained and custom NER models to identify important entities like locations, room types, and salespersons.
- **Feature Engineering**: Created meaningful features from unstructured text, such as the number of rooms and ad status.
- **Data Structuring and Export**: Organized extracted information into a Pandas DataFrame and exported it to CSV for further use.

## Technologies Used
- **Python**: Main programming language for data extraction and processing.
- **NLTK**: Text processing tasks such as tokenization and stopword removal.
- **Stanford NER**: Named Entity Recognition to extract information like locations and people.
- **Pandas**: Data manipulation and structuring.

## How to Run the Project
1. **Requirements**: Ensure you have Python installed along with the following libraries: `nltk`, `pandas`, and `stanford-ner`.
2. **Data File**: Place the dataset file containing real estate ads in the working directory.
3. **Run the Code**: Execute the script in your preferred IDE or environment (e.g., Jupyter Notebook, Google Colab).

## Project Highlights
- **Multi-token Entity Reconstruction**: Developed an approach to merge split location names, ensuring accuracy in location extraction.
- **Custom NER Training**: Created and trained a custom NER model to identify room types, enhancing the feature extraction process.
- **Salesperson Identification**: Automatically extracted the name of the salesperson responsible for each listing.

## Future Improvements
- **Sentiment Analysis**: Implement sentiment analysis to gauge how positively or negatively each property is described.
- **Property Comparison Tool**: Develop a feature that allows comparison between properties based on extracted data such as price, features, and location.
- **Enhanced NER**: Improve the NER model by adding more training data to capture additional important entities, such as neighborhood quality or proximity to amenities.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for any questions or collaboration opportunities.