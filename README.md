# Movie Analyzer Exercise

## Exercise Overview 

We're building a Python-backed movie analyzer. It's still in its early stages of implementation. Currently, the application ingests data (simulated for this exercise, but intended to be from a CSV file) with the following fields for each movie:  

*  `id`: `int`

*  `rating`: `float` (assumed to be on a scale of 0.0-10.0)

*  `movie_title`: `str`

*  `certified_fresh`: `bool`
  

This data is intended to be stored in a PSQL database to provide calculated suggestions (like Netflix's "recommended for you"). As part of an initial ingestion step or for an interim process, this movie data is currently represented as a list of lists called `movie_list`. 

### Example of Current Data Structure:

```python
movie_list = [[1, 9.0, 'Interstellar', True], [2, 8.5, 'Fast and the Furious', True]]
``` 

## Problem #1 | Organization and Look Up 🔍

We'd like to:
REFACTOR THE DATA into a more readable structure for our list of movies.
CREATE A FUNCTION that takes in our movie_list (or the refactored structure) and returns the top 10 highest-rated movies that are certified_fresh

## The solution
To run the solution just execute in your terminal:
``` bash
python solution.py
```

To run the tests:
``` bash
pytest tests.py
```

It is possible to use pytest installing it in your OS using
``` bash
pip install -r requirements.txt
```