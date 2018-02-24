#!/usr/bin/env python 3
import fresh_tomatoes
import media

#create toy_story movie object 
toy_story = media.Movie("Toy story",  #movie_title
                        "A story of aboy and his toys that come to life",  #movie_storyline
                        "https://ca.movieposter.com/posters/archive/main/98/MPW-49385",#poster_image
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk" #trailer_youtube) 

#create avatar movie object
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/I/41vuODnDSuL.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#create school_of_rock movie object
school_of_rock = media.Movie("School of rock",
                             "using rock music to learn",
                             "http://img.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

#create ratatouille movie object
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in paris",
                          "http://www.pastposters.com/cw3/assets/product_full/R/ratatouille-cinema-quad-movie-poster-(teaser-1).jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

#createmidnight_in_paris  movie object
midnight_in_paris = media.Movie("Midnight in paris",
                                "Going back in time to meet authors",
                                "http://img.moviepostershop.com/midnight-in-paris-movie-poster-2011-1020695872.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

#create hunger_games movie object
hunger_games = media.Movie("Hunger games",
                           "Areally real reality show",
                           "https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

#Define movies variable as a list of objects
movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris ,hunger_games]

#calling open function to make the html file
fresh_tomatoes.open_movies_page(movies)




