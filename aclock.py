from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("600x450")
clock_image= ImageTk.PhotoImage(Image.open ("clock.jpg"))
#-----------------India-----------------
india_label = Label(root,text="India")
india_label.place(relx=0.2,rely=0.05, anchor= CENTER)

india_clock=Label(root)
india_clock["image"]=clock_image
india_clock.place(relx=0.2,rely=0.35, anchor= CENTER)

india_time = Label(root)
india_time.place(relx=0.2,rely=0.65, anchor= CENTER)
#-------------------Canada---------------
canada_label = Label(root,text="Canada")
canada_label.place(relx=0.7,rely=0.05,anchor= CENTER)

canada_clock=Label(root)
canada_clock["image"]=clock_image
canada_clock.place(relx=0.7,rely=0.35, anchor= CENTER)

canada_time = Label(root)
canada_time.place(relx=0.7,rely=0.55, anchor= CENTER)
#-------------------Australia-----------------
australia_label = Label(root,text="Australia")
australia_label.place(relx=0.25,rely=0.15,anchor= CENTER)

australia_clock=Label(root)
australia_clock["image"]=clock_image
australia_clock.place(relx=0.25,rely=0.45, anchor= CENTER)

australia_time = Label(root)
australia_time.place(relx=0.25,rely=0.75, anchor= CENTER)


class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time :"+ current_time
        india_time.after(200,self.times)
class Canada():
      def times(self):
          home=pytz.timezone('Canada/Eastern')
          local_time=datetime.now(home)
          current_time=local_time.strftime("%H:%M:%S")
          canada_time["text"]="Time :"+ current_time
          canada_time.after(200,self.times)
class Australia():
      def times(self):
          home=pytz.timezone('Australia/ACT')
          local_time=datetime.now(home)
          current_time=local_time.strftime("%H:%M:%S")
          australia_time["text"]="Time :"+ current_time
          australia_time.after(200,self.times)
          
obj_india=India()
obj_usa=USA()
india_btn=Button(root,text="Show Time",command=obj_india.times)
india_btn.place(relx=0.2,rely=0.8, anchor= CENTER)
canada_btn=Button(root,text="Show Time",command=obj_usa.times)
canada_btn.place(relx=0.7,rely=0.8, anchor= CENTER)
australia_btn=Button(root,text="Show Time",command=obj_usa.times)
australia.place(relx=0.25,rely=0.92, anchor= CENTER)
root.mainloop()