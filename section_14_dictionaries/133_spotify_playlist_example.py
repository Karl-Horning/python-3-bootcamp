playlist = {
   'title': 'Python Playlist', 
   'author': 'Karl Horning', 
   'songs': [
      {
         'title': 'Lazy Sunday',
         'artist': ['The Lonely Island', 'Chris Parnell'],
         'duration': 2.19
      },
      {
         'title': 'Song 2', 
         'artist': ['Blur'], 
         'duration': 2.02
      },
      {
         'title': '3 X 3',
         'artist': ['Bloc Party'],
         'duration': 2.39
      }
   ]
}

total_length = 0

for song in playlist['songs']:
   total_length += song['duration']

print(total_length)