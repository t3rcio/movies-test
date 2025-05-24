
import sys

TOP_MOVIES = 10

class Movie:
    '''
    A simple class to encapsule the data
    '''
    def __init__(self, *args):        
        self.id = args[0]
        self.rating = args[1]
        self.movie_title = args[2]
        self.certified_fresh = args[3]
    
    def to_dict(self):
        return {
            'id': self.id,
            'certified_fresh': self.certified_fresh,
            'movie_title': self.movie_title,
            'rating': self.rating
        }

def refactor_data(movies_list):
    '''
    A dict is more readable format for humans, computers, Terminators, Vulcanos, etc
    So, let's use it
    '''
    result = []
    for item in movies_list:
        result.append(
            Movie(*item).to_dict()
        )
    return result

def top_10_movies(refactored_movies_list):
    '''
    refactored_movies_list: a refactored movies list - all the items in dict format

    To filter the 10 better rated movies, we can use the sort() function 
    passing a lambda function as 'key' and reverting the result due the original result
    is in crescent order
    '''
    result = [m for m in refactored_movies_list if m['certified_fresh']]
    top_10 = sorted(result, key=lambda m: m['rating'], reverse=True)    
    return top_10[0:TOP_MOVIES]

if __name__ == "__main__":
    movies_list = [[1, 9.0, 'Interstellar', True], [2, 8.5, 'Fast and the Furious', True]]
    
    refactored_movies_list = refactor_data(movies_list)
    print('Refactored data: ', refactored_movies_list)
    
    top_10 = top_10_movies(refactored_movies_list)
    print('Top 10 movies: ', top_10)
    sys.exit(0)
