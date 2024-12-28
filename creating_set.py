genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Checkpoint 1
#We have a great idea for an application that allows users to share music that they create with others.
#One of the features of this application is the ability to tag songs with descriptive tags about the genre, mood, instruments, etc. Our team members have taken a survey of user’s favorite genres of music and provided us with a list of the results.
#Unfortunately, it seems like there are some duplicates in the collection. For the first step, find all of the genres of music that the users submitted without duplicates by creating a set from genre_results.
#Store the set in a variable called survey_genres. Finally, print survey_genres to see the new set!
survey_genres = set(genre_results)
print(survey_genres)

# Checkpoint 2
#You want to test if it is plausible to use abbreviated tags for describing music.
#For this step, use a set comprehension to create a new set called survey_abbreviated which stores the first three letters of each genre found in the survey results without duplication.
#Print survey_abbreviated to see the result!
survey_abbreviated = {genre[0:3] for genre in genre_results} # Example of a list comprehension
print(survey_abbreviated)