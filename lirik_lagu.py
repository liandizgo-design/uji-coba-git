import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nUshinatte mo..", 0.10),
        ("ushinatte mo..",0.10),
        ("Ikite iku shika nai...", 0.19),
        ("Donna ni uchinomesarete mo...", 0.18),
        ("Mamoru mono ga aru.....", 0.12),
    ]
    
    delays = [0.3, 3.3, 6.3, 13.3, 20.0]  
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()