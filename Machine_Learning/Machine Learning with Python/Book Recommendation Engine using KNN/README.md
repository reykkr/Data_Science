# Book Recommendation System

## Overview
The **Book Recommendation System** is a data science project that utilizes the **Book-Crossings** dataset, containing 1.1 million ratings for over 270,000 books provided by 90,000 users. The primary goal of this project was to create a recommendation algorithm using **K-Nearest Neighbors (k-NN)** to find books similar to a given title. This project was part of my data science journey through **freeCodeCamp**.

## Purpose
The purpose of this project is to:

- Develop a recommendation system to suggest books based on a given title using **collaborative filtering**.
- Apply machine learning techniques to analyze users' preferences and find similar books.
- Demonstrate the practical application of **K-Nearest Neighbors** for similarity-based recommendations.

## Key Skills Demonstrated
1. **Data Preprocessing**
   - Filtering users and books based on rating counts for more accurate and computationally efficient recommendations.

2. **Collaborative Filtering**
   - Utilizing user ratings to create book recommendations using **K-Nearest Neighbors**.

3. **Model Training and Evaluation**
   - Training a k-NN model to find similar books using **cosine similarity** as the distance metric.

## Tools Used
- **Python**: Data analysis and recommendation model development.
- **Pandas**: Data manipulation and preprocessing.
- **scikit-learn**: Implementing the k-NN algorithm.
- **scipy**: Efficient matrix representation using sparse matrices.

## Project Components
1. **Data Filtering and Preprocessing**
   - Users with fewer than 200 ratings and books with fewer than 100 ratings were filtered to ensure the statistical significance of the recommendations.

2. **User-Book Matrix Construction**
   - Constructed a user-book matrix for collaborative filtering using **Pandas**, then converted it into a sparse matrix for efficiency.

3. **Model Training**
   - Used **NearestNeighbors** from `scikit-learn` with cosine similarity to train the recommendation model.

4. **Book Recommendation Function**
   - Implemented the `get_recommends()` function that takes a book title and returns five similar books along with their similarity distances.

## Notes
This project highlights the power of collaborative filtering to generate personalized book recommendations. By leveraging users' historical ratings, it successfully identifies books that are most similar based on the preferences of the reading community.

## Example Output
```python
get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
```
Returns:
```
["Where the Heart Is (Oprah's Book Club (Paperback))", [
    ["The Lovely Bones: A Novel", 0.72],
    ["I Know This Much Is True", 0.77],
    ["The Surgeon", 0.77],
    ["The Weight of Water", 0.77],
    ["I'll Be Seeing You", 0.8]
]]
```

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.