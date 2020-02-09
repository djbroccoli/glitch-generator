from pydub import AudioSegment
# must also install ffmpeg if you want to work with anything other than .wav
from random import randint



song = AudioSegment.from_mp3("allofthelights.mp3") # specify starting audio here
song = song[40000:80000] # take a section of that audio (in milliseconds if you choose

song_length = len(song) # length of song in milliseconds

# song_iterator = iter(list(range(song_length))) #creates a list with all values from song to be stepped through with .__next__

def repeater(clip, n):  # repeats audio clip n times
    return clip * n

def slicer(audioClip, beginning, end):  # takes a begging number and an end milisecond and cuts audio between the two positions
    return audioClip[beginning:end]

def gluer(audio1, audio2): #appends together sliced audio
    return audio1 + audio2

def x_second_looper(x, secondChunks): #takes x, how many times to repeat each chunk, and secondChunk, the size of the chunk in milliseconds
    t = song_length // (secondChunks)
    newClip = AudioSegment.empty()
    for n in range(t):
        if n == 0:
            n += 1
        else:
            ticker = n * (secondChunks)
            buffer = repeater(slicer(song, (ticker-(secondChunks)), ticker), x)
            newClip = newClip + buffer
    newClip.export("loopedMiley.mp3", format="mp3")

# x_second_looper(3, 50)

def glitch(): # a random glitch machine

    newSong = AudioSegment.empty() # creates blank audio file
    ticker = 1
    while ticker <= len(song):
        print(ticker)
        x = randint(1, 20)           # x is number of times section loops
        milliseconds = randint(1, 300) # defines the range of sizes for the slices taken in milliseconds
        buffer = repeater(slicer(song, ticker, (ticker + milliseconds)), x)
        newSong = newSong + buffer
        ticker = ticker + milliseconds
    title = input("what would you like to name your new song?  ")
    form = input("what format?  ")
    newSong.export((title + "." + form), format=form)

glitch()


#newClip = AudioSegment.empty()
# def two_seconds(place): #repeats every 2 seconds of song, init with 0
#     i = (place)
#
#     global newClip
#     if (i == 2000): # this is for the first pass through, grabs the first two seconds and adds to new clip, makes recursive call
#         firstAudioClip = repeater(slicer((i - 2000), i), 2)
#         newClip = firstAudioClip
#         n = next(song_iterator)
#         two_seconds(n)
#     elif i == 0:
#         next(song_iterator)
#     elif (i % 2000) == 0:
#         floatingAudio = repeater(slicer((i - 2000), i), 2)
#         newClip = newClip + floatingAudio
#         n = next(song_iterator)
#         two_seconds(n)
#     else:
#         n = next(song_iterator)
#         if n == StopIteration:
#             print("Done")
#             newClip.export("two_seconds.mp3", type="mp3")
#             return None
#         else:
#             two_seconds(n)
#
#
# two_seconds(1)
















