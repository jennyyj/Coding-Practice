# p4_jacob_jenny.py

import csv
from typing import List, Tuple

def load_csv(filename: str, has_header: bool = True) -> List[dict]:
    
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            if not has_header:
                fieldnames = [f'Column{i}' for i in range(1, len(next(csvfile).split(',')) + 1)]
            else:
                fieldnames = None

            csvreader = csv.DictReader(csvfile, fieldnames=fieldnames)
            return list(csvreader)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        raise
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        raise

def display_top_collaborations(top_rated: List[dict], top_casts: List[dict]) -> None:
   
    try:
        director_actor_count = {}
        for movie in top_rated:
            title = movie.get('Title')  # Use .get() to handle missing keys
            year = movie.get('Year')
            director = None
            actors = []
            
            # Find the movie in the top_casts list
            for cast in top_casts:
                if cast.get('Title') == title and cast.get('Year') == year:
                    director = cast.get('Director')
                    actors = [cast[f'Actor {i}'] for i in range(1, 6) if cast.get(f'Actor {i}')]

            # Update director_actor_count dictionary
            if director and actors:
                key = (director, tuple(sorted(actors)))
                director_actor_count[key] = director_actor_count.get(key, 0) + 1

        # Sort and display the ranking
        sorted_director_actor_count = sorted(director_actor_count.items(), key=lambda x: x[1], reverse=True)
        print("Top Collaborations:")
        for i, (collaboration, count) in enumerate(sorted_director_actor_count[:10], start=1):
            director, actors = collaboration
            print(f"{i}. Director: {director}, Actors: {', '.join(actors)}, Movies: {count}")

    except Exception as e:
        print(f"Error displaying top collaborations: {e}")
        raise

def display_top_actors(top_grossing: List[dict]) -> None:
    
    try:
        actor_box_office = {}
        for movie in top_grossing:
            actors = [movie[f'Actor {i}'] for i in range(1, 6) if movie.get(f'Actor {i}')]
            box_office = float(movie.get('USA Box Office', '0').replace('$', '').replace(',', ''))

            # Update actor_box_office dictionary
            for actor in actors:
                actor_box_office[actor] = actor_box_office.get(actor, 0) + box_office

        # Sort and display the ranking
        sorted_actor_box_office = sorted(actor_box_office.items(), key=lambda x: x[1], reverse=True)
        print("Top Actors (by Box Office):")
        for i, (actor, box_office) in enumerate(sorted_actor_box_office[:10], start=1):
            print(f"{i}. Actor: {actor}, Total Box Office: ${box_office:,.2f}")

    except Exception as e:
        print(f"Error displaying top actors: {e}")
        raise

def main():
    try:
        # Load data from CSV files
        top_rated = load_csv('/Users/jennyjacob/Downloads/imdb-top-rated.csv')
        top_grossing = load_csv('/Users/jennyjacob/Downloads/imdb-top-grossing.csv')
        top_casts = load_csv('/Users/jennyjacob/Downloads/imdb-top-casts.csv', has_header=False)

        # a) Test display_top_collaborations function
        display_top_collaborations(top_rated, top_casts)

        # b) Test display_top_actors function
        display_top_actors(top_grossing)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

