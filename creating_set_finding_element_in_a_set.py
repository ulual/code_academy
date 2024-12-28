allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])

# Create an empty list to store bad tags
bad_tags = []

# Iterate through each tag in tag_set
for tag in tag_set:
    # Check if the tag is not in allowed_tags
    if tag not in allowed_tags:
        # Add the tag to bad_tags
        bad_tags.append(tag)

print(bad_tags)
print(tag_set)

for tag in bad_tags:
    # Check if the tag is not in allowed_tags
    if tag in tag_set:
        # Add the tag to bad_tags
        tag_set.remove(tag)

print(tag_set)

song_data_users = {'Retro Words': tag_set}

print(song_data_users)