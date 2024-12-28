song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Checkpoint 1
tag_set = set(song_data['Retro Words'])

# Checkpoint 2
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)
print(tag_set)

# or tag_set.update([user_tag_1, user_tag_2, user_tag_3])

# Checkpoint 3
song_data = {'Retro Words': tag_set}
print(song_data)