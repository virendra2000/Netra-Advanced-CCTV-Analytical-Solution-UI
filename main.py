import customtkinter as ui
import os
import sys
import tkinter as tk
import cv2
import torch
import numpy as np
from torchvision import transforms
from PIL import Image,ImageTk
import cv2
import detection as dt
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
app = ui.CTk()
app.title("Netra")
app.geometry("500x250")
ui.set_appearance_mode("System")
app.iconbitmap(resource_path("favicon.ico"))
app.resizable(False,False)

# Flag to control camera capture
capture_flag = False
#firstframe
frame1 = ui.CTkFrame(master=app,width=500,height=250)
frame1.pack()
launcherimage = ui.CTkImage(Image.open(resource_path('images\\logo.png')),size=(100,100))
imagelbl = ui.CTkLabel(master=frame1,image=launcherimage,text="")
imagelbl.place(relx=0.5,rely=0.2,anchor=tk.CENTER)
mytitle = ui.CTkFont(family="Comic Sans MS",size=30,weight="bold")
mysubtitle = ui.CTkFont(family="sans-serif",size=18,weight="bold")
mytext = ui.CTkFont(family="sans-serif",size=15,weight="bold")
title = ui.CTkLabel(master=frame1,text="Netra",font=mytitle)
title.place(relx=0.5,rely=0.47,anchor=tk.CENTER)
subtitle = ui.CTkLabel(master=frame1,text="Ultimate Solution for all your Security",font=mysubtitle)
subtitle.place(relx=0.5,rely=0.6,anchor=tk.CENTER);
def launch():
    frame1.pack_forget()
    app.geometry("1080x600")
    tabview.pack()
launchbtn = ui.CTkButton(master=frame1,text="Get Started",corner_radius=50,height=40,font=mytext,cursor="hand2",command=launch)
launchbtn.place(relx=0.5,rely=0.8,anchor=tk.CENTER)

#tab for application
tabview = ui.CTkTabview(master=app,width=1080,height=600)
tabview.add("Home")
tabview.add("About")
tabview.add("Exit")

tabview.set("Home")
tabview.pack_forget()
    

# Define function to stop camera capture
# def stop_capture():
#     global capture_flag
#     capture_flag = False
#     stop_cap_btn.configure(state=tk.DISABLED)
#     start_cap_btn.configure(state=tk.NORMAL)

# def on_closing():
#     stop_capture()
#home frame
frame2 = ui.CTkFrame(tabview.tab("Home"),width=1120,height=600)
frame2.pack()

street_land_label = ui.CTkLabel(master=frame2,text="Street / Landmark",font=mysubtitle)
street_land_label.place(relx=0.33,rely=0.15,anchor=tk.CENTER);
street_land = ui.CTkTextbox(master=frame2,width=300,height=40,font=("Helvetica", 18),border_width=1,border_color="#ffffff",corner_radius=10)
street_land.place(relx=0.43,rely=0.1)

area_label = ui.CTkLabel(master=frame2,text="Area",font=mysubtitle)
area_label.place(relx=0.38,rely=0.25,anchor=tk.CENTER);
areatxt = ui.CTkTextbox(master=frame2,width=300,height=40,font=("Helvetica", 18),border_width=1,border_color="#ffffff",corner_radius=10)
areatxt.place(relx=0.43,rely=0.2)

city_label = ui.CTkLabel(master=frame2,text="City",font=mysubtitle)
city_label.place(relx=0.38,rely=0.35,anchor=tk.CENTER);
citytxt = ui.CTkTextbox(master=frame2,width=300,height=40,font=("Helvetica", 18),border_width=1,border_color="#ffffff",corner_radius=10)
citytxt.place(relx=0.43,rely=0.3)

states_list = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
state_label = ui.CTkLabel(master=frame2,text="State",font=mysubtitle)
state_label.place(relx=0.38,rely=0.45,anchor=tk.CENTER);
statetxt = ui.CTkComboBox(master=frame2,values=states_list,width=300,height=40,font=("Helvetica", 18),border_width=1,border_color="#ffffff",corner_radius=10)
statetxt.place(relx=0.43,rely=0.4)

country_label = ui.CTkLabel(master=frame2,text="Country",font=mysubtitle)
country_label.place(relx=0.38,rely=0.55,anchor=tk.CENTER);
countrytxt = ui.CTkComboBox(master=frame2,values=["India"],width=300,height=40,font=("Helvetica", 18),border_width=1,border_color="#ffffff",corner_radius=10)
countrytxt.place(relx=0.43,rely=0.5)

zip_code_label = ui.CTkLabel(master=frame2,text="Pin Code",font=mysubtitle)
zip_code_label.place(relx=0.38,rely=0.65,anchor=tk.CENTER);
zipcodetxt = ui.CTkTextbox(master=frame2,width=300,height=40,font=("Helvetica", 18),border_width=1,border_color="#ffffff",corner_radius=10)
zipcodetxt.place(relx=0.43,rely=0.6)

camera_label = ui.CTkLabel(master=frame2,text="Camera Number / IP with PORT",font=mysubtitle)
camera_label.place(relx=0.29,rely=0.75,anchor=tk.CENTER);
cameratxt = ui.CTkTextbox(master=frame2,width=300,height=40,font=("Helvetica", 18),border_width=1,border_color="#ffffff",corner_radius=10)
cameratxt.place(relx=0.43,rely=0.7)

def get_location_details():
    street_landmark = street_land.get("0.0", "end").strip()
    area_value = areatxt.get("0.0", "end").strip()
    city_value = citytxt.get("0.0", "end").strip()
    state_value = statetxt.get()
    country_value = countrytxt.get()
    zipcode_value = zipcodetxt.get("0.0","end").strip()
    camera_value = cameratxt.get("0.0","end").strip()
    if camera_value == "0" or camera_value=="1" or camera_value=="2":
        camera_value = int(camera_value)
    dt.start_video(street_landmark,area_value,city_value,state_value,country_value,zipcode_value,camera_value)

start_cap_btn = ui.CTkButton(master=frame2,text="Start Monitoring",corner_radius=50,fg_color="white",text_color="blue",height=40,font=mytext,cursor="hand2",command=get_location_details)
start_cap_btn.place(relx=0.43,rely=0.8)

#about frame
frame3 = ui.CTkFrame(tabview.tab("About"),width=800,height=500)
frame3.pack()
abtimage = ui.CTkImage(Image.open(resource_path("images\\logo.png")),size=(100,100))
abtimagelbl = ui.CTkLabel(master=frame3,image=abtimage,text="")
abtimagelbl.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

abttextlbl = ui.CTkLabel(master=frame3,text="Netra",font=mytitle)
abttextlbl.place(relx=0.5,rely=0.35,anchor=tk.CENTER)

abtsubtextlbl = ui.CTkLabel(master=frame3,text="Ultimate Solution for all your Security",font=mysubtitle)
abtsubtextlbl.place(relx=0.5,rely=0.45,anchor=tk.CENTER)

abtinfotext = ui.CTkLabel(master=frame3,text="App Version 1.0.0\n\nDeveloped By\n\n Virendra Kalwar\n Chetana Bhoir\n Shruti Chavan \n Darshana Dahe",font=mytext)
abtinfotext.place(relx=0.5,rely=0.65,anchor=tk.CENTER)


#exit frame
frame5 = ui.CTkFrame(tabview.tab("Exit"),width=800,height=500)
frame5.pack()

exitimg = ui.CTkImage(Image.open(resource_path("images\\exit.png")),size=(100,100))
exitimglbl = ui.CTkLabel(master=frame5,text="",image=exitimg)
exitimglbl.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

exittextlbl = ui.CTkLabel(master=frame5,text="Are you want to close Netra's Eyes",font=mytitle)
exittextlbl.place(relx=0.5,rely=0.4,anchor=tk.CENTER)
def exitno():
    tabview.pack_forget()
    app.geometry("500x250")
    frame1.pack()
def exityes():
    app.destroy()
exitnobtn = ui.CTkButton(master=frame5,text="No",corner_radius=50,fg_color="white",text_color="blue",height=40,font=mytext,cursor="hand2",command=exitno)
exitnobtn.place(relx=0.3,rely=0.5)

exityesbtn = ui.CTkButton(master=frame5,text="Yes",corner_radius=50,fg_color="white",text_color="blue",height=40,font=mytext,cursor="hand2",command=exityes)
exityesbtn.place(relx=0.5,rely=0.5)

app.mainloop()
