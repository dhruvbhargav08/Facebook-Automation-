# Importing required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import messagebox
import pyperclip
import pyautogui
import time
from tkinter import *
from tkinter import filedialog
# Defining variables
list_filename=[]
caption=''
USERNAME=''
PASSWORD=''
# Function to copy caption 
def Text_Input():
    global caption
    caption=text_caption.get("1.0","end-1c")
# Function to select file to upload
def File_Upload():
    global filename
    filename = filedialog.askopenfilename() 
    filename = filename.replace("/","\\")
    list_filename.append(filename)
    entry_browse.delete(0,END)
    entry_browse.insert(0,filename)
# Function that destroy the root window and run the driver
def Login():
    global USERNAME
    global PASSWORD
    Text_Input()
    USERNAME=entry_username.get()
    PASSWORD=entry_password.get() 
    root.destroy()
def next_entry(event):
    entry_password.focus_set()
# Main root window
root=Tk()
root.minsize(width=1000,height=400)
root.config(background="#FFD07F")
# Label inside root window
label=Label(root,background="#FF8243")
label.pack(pady=20)
# Label that contain run button to execute driver functionality
label_run=Label(label,background="#FF8243")
# Username and password label that takes username and password entries
label_username=Label(label,text="Email/Mobile Number:",font=("Times New Roman", 18),foreground="#ffffff",background="#FF8243")
entry_username=Entry(label,width=30,highlightthickness=0,background="#FDA65D")
label_password=Label(label,text="Password:",font=("Times New Roman", 18),foreground="#ffffff",background="#FF8243")
entry_username.bind('<Return>', next_entry)
entry_password=Entry(label,width=30,highlightthickness=0,background="#FDA65D")
# Caption label that contain caption text input 
label_caption=Label(label,background="#FF8243")
label_text_caption=Label(label_caption,text="Caption:",font=("Times New Roman", 18),background="#FF8243",foreground="#ffffff")
text_caption=Text(label_caption,width=50,height=10,background="#FDA65D")
# Label that contain browse file button and entry that shows the path of file to be upload
label_browse_file=Label(label,background="#FF8243")
button_browse=Button(label_browse_file,text="Attach File",command=File_Upload,font=("Times New Roman", 14),background="#E26A2C",foreground="#ffffff",activebackground="#FDA65D")
entry_browse=Entry(label_browse_file,width=40,background="#FDA65D")
# Button that execute main program
button_run=Button(label_run,text="Run",font=("Times New Roman", 18),background="#E26A2C",activebackground="#FDA65D",foreground="#ffffff",command=Login)
# Defining the position of all labels, entries and buttons on tkinter screen
# Username label position
label_username.grid(row=0,sticky=W,column=0,pady=20,padx=10)
# Username enrty position 
entry_username.grid(row=0,column=1,pady=20,padx=10)
# Password label position
label_password.grid(row=1,sticky=W,column=0,pady=20,padx=10)
# Password entry position
entry_password.grid(row=1,column=1,pady=20,padx=10)
# Caption label position
label_caption.grid(row=2,columnspan=2,pady=20,padx=10)
# Text field (that take caption as input) position
text_caption.grid(row=1,columnspan=2)
# File browse button position
button_browse.grid(row=0,column=1,padx=10)
# Browse entry (that shows the path of file to be uploaded) position
entry_browse.grid(row=0,column=0)
# Browse label (that contain browse button and browse entry) position
label_browse_file.grid(row=3,columnspan=2,pady=20,padx=10)
# Run label (that contain run button to execute main program) position
label_run.grid(row=4,columnspan=2,pady=20,padx=10)
# Label (a random label that show the text "Caption") position
label_text_caption.grid(row=0,sticky=W,pady=20,padx=10)
# Run button position
button_run.pack(pady=20)
root.mainloop()
# Main automation code
# Defining variables  
POST_TEXT=caption
chromedriverpath="./chromedriver.exe"
# Defining driver object 
driver=webdriver.Chrome(chromedriverpath)
driver.maximize_window()
# Driver redirecting to facebook.com
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
# Searching the username field and passing the username
user_input=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
for i in USERNAME:
    user_input.send_keys(i)
    time.sleep(0.1)
# Searching the password field and passing the password
password_input=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
for i in PASSWORD:
    password_input.send_keys(i)
    time.sleep(0.1)
# Loginprocess
password_input.send_keys(Keys.RETURN)
time.sleep(20)
loop=True
i=1
# While loop to search page and posting the content and terminate when content is posted on all the pages
while loop:
    try:
        # Searching for page
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]').click()
        time.sleep(1.2)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/div').click()
        time.sleep(0.8)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/a').click()
        driver.find_element(By.XPATH,f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[{i}]/a').click()
        time.sleep(2)
        try:
            # Searches create post button and paste the caption 
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div').click()
            time.sleep(2)
            pyperclip.copy(POST_TEXT)
            pyautogui.hotkey('ctrl', 'v')
            # Loop that takes file (to be posted) path and search for the upload file option. It then execute the loop untill all the files are uploaded.
            if len(list_filename)!=0:
                for j in range(len(list_filename)):
                    if j==0:
                        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/span/div').click()
                    else:
                        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/span/div').click()
                    time.sleep(3)
                    pyperclip.copy(list_filename[j])
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('enter')
                    time.sleep(5)
            time.sleep(5)
            # Post option 
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[4]/div').click()
            time.sleep(10)
            i=i+1
        except:
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[1]/div').click()
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div').click()
            # Searches create post button and paste the caption 
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div').click()
            time.sleep(2)
            pyperclip.copy(POST_TEXT)
            pyautogui.hotkey('ctrl', 'v')
            # Loop that takes file (to be posted) path and search for the upload file option. It then execute the loop untill all the files are uploaded.
            if len(list_filename)!=0:
                for j in range(len(list_filename)):
                    if j==0:
                        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/span/div').click()
                    else:
                        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/span/div').click()
                    time.sleep(3)
                    pyperclip.copy(list_filename[j])
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('enter')
                    time.sleep(5)
            time.sleep(5)
            # Post option 
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[4]/div').click()
            time.sleep(10)
            i=i+1
    except: 
        loop=False
        # Final driver.close() to terminate the program 
        # It is executed when we post the file on all the pages 
        # It will automatically generate an exception
        driver.close()
