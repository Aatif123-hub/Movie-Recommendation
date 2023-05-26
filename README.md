
# Movie Genre Recommendation

This code demonstrates a movie genre recommendation system using the Kollywood Movie Dataset. It recommends similar movies based on the cosine similarity score of movie genres.

## Prerequisites

- Python 3.x
- pandas
- scikit-learn

## Installation

1. Make sure you have Python installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

2. Install the required packages using pip. Open a terminal/command prompt and run the following command: !pip install -r  requirements.txt


## Usage

1. Place the 'Kollywood Movie Dataset (2011 - 2017).csv' file in the same directory as the code file.

2. Run the code in a Python environment.

3. The code will read the dataset, perform TF-IDF vectorization on the movie genres, and calculate cosine similarity scores.

4. To get movie recommendations based on a movie's title, call the `genre_recommendations` function and pass the movie title as an argument. For example:

```python
recommendations = genre_recommendations('Chennai 2 Singapore')
print(recommendations)
```
5.This will display a list of recommended movies similar to 'Chennai 2 Singapore' based on genre.

## License

This project is licensed under the MIT License.
