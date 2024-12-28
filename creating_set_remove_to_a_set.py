song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Checkpoint 1
tag_set = set(song_data_users['Retro Words'])

# Checkpoint 2
tag_set.remove('onion')
tag_set.remove('helloworld')
tag_set.remove('spam')

# Checkpoint 3
song_data_users = {'Retro Words': tag_set}
print(song_data_users)