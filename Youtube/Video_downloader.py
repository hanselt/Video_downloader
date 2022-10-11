from msilib.schema import Icon
from sre_parse import expand_template
from tkinter import *
#from tkinter.ttk import *
#pip install pytube
from pytube import YouTube
#Functions
def descargar():
    global url_video, obj_filter
    
        #url = YouTube( str(url_video.get()) ).streams.first().download()        
    if obj_filter != None:
        obj_filter.first().download()
        label_warning.config(text="The video/audio has been successfully downloaded.")
        url_video.set("")
        label_warning.config(fg="black")
    
def getVideo():
    global url_video, obj_filter
    try:
        video_list = YouTube( str(url_video.get()) )
        filter = video_list.streams.filter(mime_type="video/mp4", progressive=True)
        if len(filter.fmt_streams) > 0:
            obj_filter = filter
            btn_downloader.config(state="normal")
            label_warning.config(text="This video is ready for donwloading.")
            label_warning.config(fg="black")
    except:
        getUrlError()
def getAudio():
    global url_video, obj_filter
    try:
        audio_list = YouTube( str(url_video.get()) )
        filter = audio_list.streams.filter(only_audio=True)
        print(filter)
        if len(filter.fmt_streams) > 0:
            obj_filter = filter
            btn_downloader.config(state="normal")
            label_warning.config(text="This audio is ready for donwloading.")
            label_warning.config(fg="black")
    except:
        getUrlError()
def getUrlError():
    global url_video
    url_video.set("")
    label_warning.config(text="The URL is incorrect, enter a new URL correctly.")
#Tk root 
root = Tk()
root.title("Download from Youtube")
root.iconbitmap("youtube.ico")
root.config(bd=10)
root.resizable(1,0)
root.minsize(400,100)

obj_filter = None

first_frame = Frame(root)
first_frame.pack(fill='both', expand=1)
first_frame.grid_columnconfigure(1, weight=1)
#start_1st
label = Label(first_frame, text="URL")
label.grid(row=0, column=0, padx=5, pady=5)
url_video = StringVar()
url_video.set("")
entry = Entry(first_frame, textvariable=url_video)
entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
label_info = Label(first_frame, text="Example:    https://www.youtube.com/watch?v=X791IzOwt3Q")
label_info.grid(row=1, column=1, padx=5, pady=1)
entry.config(justify="left")
#end_1st
#start_2nd
second_frame = Frame(root)
second_frame.pack()
#If u use ttk and want to change styles u have to use this !!
#style = Style()
#style.configure("BW.TLabel", background="Blue")
#second_frame.config(style="BW.TLabel")
#With tk just bg in config
#second_frame.config(bg="blue")
second_frame.grid_columnconfigure(1, weight=2)


btn_video =  Button(second_frame)
btn_video.config(command=getVideo, text="Get Video!")
btn_video.grid(row=0, column=0, padx=5, pady=5)

btn_audio =  Button(second_frame)
btn_audio.config(command=getAudio, text="Get Audio!")
btn_audio.grid(row=0, column=1, padx=5, pady=5)

second_frame.pack(fill='both', expand=1)
#end_2nd
#start_3rd
third_frame = Frame(root)
third_frame.pack(fill='both', expand=1)

label_warning = Label(third_frame)
label_warning.pack(side="top")
label_warning.config(fg="red")

btn_downloader = Button(third_frame, text="DOWNLOAD!")
btn_downloader.config(command=descargar, state="disabled")
btn_downloader.pack(side="bottom")
#end_3rd

root.mainloop()