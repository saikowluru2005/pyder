import tkinter as tk
from tkinter import messagebox, filedialog, StringVar, OptionMenu
from pytube import YouTube

def Widgets():
    head_label = tk.Label(root, text="PY-DER",
                          padx=5,
                          pady=15,
                          font="Samarkan 24",
                          bg="#2e2824",
                          fg="white")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)

    link_label = tk.Label(root,
                          text="YouTube link :",
                          fg="white",
                          bg="#2e2824",
                          pady=5,
                          padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = tk.Entry(root,
                             width=35,
                             textvariable=video_Link,
                             font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    resolution_label = tk.Label(root,
                                text="Select Resolution:",
                                fg="white",
                                bg="#2e2824",
                                pady=5,
                                padx=5)
    resolution_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)

    resolution_options = ["Highest", "Lowest"]  # Add more options as needed
    root.resolutionVar = StringVar(root)
    root.resolutionVar.set(resolution_options[0])  # Default resolution option
    resolution_dropdown = OptionMenu(root, root.resolutionVar, *resolution_options)
    resolution_dropdown.config(bg="#cac6c0", width=10)
    resolution_dropdown.grid(row=3, column=1, pady=5, padx=5)

    destination_label = tk.Label(root,
                                  text="Destination :",
                                  fg="white",
                                  bg="#2e2824",
                                  pady=5,
                                  padx=9)
    destination_label.grid(row=4,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = tk.Entry(root,
                                    width=27,
                                    textvariable=download_Path,
                                    font="Arial 14")
    root.destinationText.grid(row=4,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = tk.Button(root,
                         text="Browse",
                         command=Browse,
                         width=10,
                         bg="#cac6c0",
                         relief=tk.GROOVE)
    browse_B.grid(row=4,
                  column=2,
                  pady=1,
                  padx=1)

    global Download_B
    Download_B = tk.Button(root,
                           text="Download Video",
                           command=Download,
                           width=20,
                           fg="white",
                           bg="#7e7366",
                           pady=10,
                           padx=15,
                           relief=tk.GROOVE,
                           font="Georgia, 13")
    Download_B.grid(row=5,
                     column=1,
                     pady=20,
                     padx=20)

def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="/", title="Save Video")
    download_Path.set(download_Directory)

def Download():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
    resolution = root.resolutionVar.get()
    if resolution == "Highest":
        videoStream = getVideo.streams.get_highest_resolution()
    elif resolution == "Lowest":
        videoStream = getVideo.streams.get_lowest_resolution()
    videoStream.download(download_Folder)
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)
root = tk.Tk()
root.geometry("520x320")
root.resizable(False, False)
root.title("PY-DER")
root.config(background="#2e2824")
video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()
