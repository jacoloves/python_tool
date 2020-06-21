from tkinter import messagebox
import wave
import pyaudio

def play_wavfile(Filename = "./item/test.wav"):
    try:
        wf = wave.open(Filename, "r")
    except FileNotFoundError:
        print("[Error 404] No such file or directory:" + Filename)
        return 0

    # open Stream
    p = pyaudio.PyAudio()



def main():
    messagebox.showinfo("休憩終了", "10分休憩終わりだよ！")
    play_wavfile()


if __name__ == "__main__":
    main()
    
    
    
    
    