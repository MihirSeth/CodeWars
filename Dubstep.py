def song_decoder(song):
    song = song.split('WUB')
    orignal_song = []
    for i in song:
        if i != '':
         orignal_song += [i]

    return ' '.join(orignal_song)

# https://www.codewars.com/kata/551dc350bf4e526099000ae5