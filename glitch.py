from pydub import AudioSegment
# must also install ffmpeg if you want to work with anything other than .wav
from random import randint



song = AudioSegment.from_mp3("allofthelights.mp3") # specify starting audio here
song = song[40000:80000] # take a section of that audio (in milliseconds if you choose

song_length = len(song) # length of song in milliseconds



def repeater(clip, n):  # repeats audio clip n times
    return clip * n

def slicer(audioClip, beginning, end):  # takes a begging number and an end milisecond and cuts audio between the two positions
    return audioClip[beginning:end]

def gluer(audio1, audio2): #appends together sliced audio
    return audio1 + audio2

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

















