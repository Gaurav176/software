import os
import random
import pygame
from tkinter import Tk, Button, Label

songs_dir = "/home/gaurav/assign1"

song_list = os.listdir(songs_dir)

pygame.mixer.init()

current_index=0
current_path=""

def play_random_song():
    global current_index,current_path
    current_index=random.randint(0,len(song_list)-1)
    current_path = os.path.join(songs_dir, song_list[current_index])
    pygame.mixer.music.load(current_path)
    pygame.mixer.music.play()
   
def play_next_song():
    global current_index, current_path
    current_index = (current_index + 1) % len(song_list)
    current_path = os.path.join(songs_dir, song_list[current_index])
    pygame.mixer.music.load(current_path)
    pygame.mixer.music.play()
 
def pause_song():
    pygame.mixer.music.pause()

def continue_song():
    pygame.mixer.music.unpause()
    
interface=Tk()
interface.title("ASSIGNMENT SONG_PLAYER")

option=Label(interface,text="click on the options to use it!!!")
option.pack()

button_play_random=Button(interface, text="start songs", command=play_random_song)
button_play_random.pack() 

button_play_next = Button(interface, text="Play Next Song", command=play_next_song)
button_play_next.pack()

button_pause = Button(interface, text="Pause", command=pause_song)
button_pause.pack()

button_continue = Button(interface, text="Continue,if paused", command=continue_song)
button_continue.pack()
interface.mainloop()      
