import os
import filecmp
import shutil
import random
from win10toast import ToastNotifier
from tkinter import Tk, Label, Button, Entry, StringVar, Button, Grid, IntVar, Radiobutton, Message, messagebox
  
# create an object to ToastNotifier class
n = ToastNotifier()

allfolder=list()
selectfolder=list()
common=list()
match=list()
selected=list()



# def manually():
#     selected=[x for x in input("Enter the names of the file seperated by a space ").split()]
#     return selected


def comparison(all_folder, select_folder):
    files1=os.listdir(all_folder)
    files2=os.listdir(select_folder)
    # print("\nComparing files between the two directories...\n")
    for file in files1:
        allfolder.append(file)
    for file in files2:
        selectfolder.append(file)
    common=[x for x in set(allfolder) for y in set(selectfolder) if x.split('.')[0]==y.split('.')[0]]
    return common

def manualComp(all_folder, selected):
    file1=os.listdir(all_folder)
    # print("\nComparing files between the two directories...\n")
    for file in file1:
        allfolder.append(file)
    common=[x for x in set(allfolder) for y in set(selected) if x.split('.')[0]==y.split('.')[0]]
    return common


def getdirectory():
    with open ("records.txt", "a") as fh:
        fh.write("\n")
        fh.write(directory_folder_value.get())
        fh.write("\n")
        fh.write(fileplace_folder_value.get())
    messagebox.showinfo("File Directory", "This may take a few minutes.\n\nClick OK to Close this window.\n\nThe files will be copied to the folder soon.")
    master.destroy()


selected=list()
def getmanualdirectory():

    with open("directory.txt", "w") as f:
        f.write(folder_variable_value.get())
    root.destroy()


root=Tk()


def getvals():

    with open ("records.txt", "w") as f:
        f.write(all_file_value.get())
        f.write("\n")
        f.write(str(v.get()))

    root.destroy()

def getvalue():
    with open ("records.txt", "a") as f:
        f.write("\n")
        f.write(select_file_value.get())
    root.destroy()




root.geometry("644x344")
root.title("File Directory")
root.iconbitmap(r'F:\Subhra_Project\Python_icon.ico')
Label(root, text="Directory Entry", font="comicsans 13 bold", pady=15).grid(row=0, column=3)

all_file=Label(root,text=" All file Directory")
root_file=Label(root, text=" Do you wish to Input the file names manually (Y/N) ")

all_file.grid(row=1, column=2)
root_file.grid(row=2, column=2)

all_file_value=StringVar()
# select_file_value=StringVar()
v=IntVar()

all_file_entry=Entry(root, textvariable=all_file_value)
# select_file_entry=Entry(root, textvariable=select_file_value)

all_file_entry.grid(row=1, column=3)
# select_file_entry.grid(row=2, column=3)
Radiobutton(root, text='Yes', variable=v, value=1).grid(row=3, column=2)
Radiobutton(root, text='No', variable=v, value=2).grid(row=4, column=2)

Button(text="submit", command=getvals).grid(row=7, column=3)
root.mainloop()


# all_folder=input("Enter the all files directory ")
#ENTER COUNTER CASE IF USER WANTS TO MANUALLY ENTER THE FILENAME
# inp1=input("Do you wish to input the file names manually (Y/N) ")
ifile=open("records.txt", "r")
lines=ifile.readlines()

if lines[1]=="1":
    
    root = Tk()
    root.geometry("644x344")
    root.iconbitmap(r'F:\Subhra_Project\Python_icon.ico')
    folder_variable=Label(root, text="Enter names of the File seperated by a Space")
    folder_variable.grid(row=1, column=2)
    folder_variable_value=StringVar()
    folder_variable_entry=Entry(root, textvariable=folder_variable_value)
    folder_variable_entry.grid(row=1, column=16)
    Button(text="submit", command=getmanualdirectory).grid(row=2, column=5)
    root.mainloop()

    with open("directory.txt") as fh:
        lines=fh.read()
        selected=[i for i in lines.split()]

    
    ifile=open("records.txt", "r")
    line=ifile.readlines()
    all_folder=line[0].strip()
    # selected=manually()
    match=manualComp(all_folder, selected)
    # folderDirectory(match)
    master=Tk()
    master.geometry("644x344")
    master.iconbitmap(r'F:\Subhra_Project\Python_icon.ico')
    master.title("File Directory")
    Label(master, text="Directory Entry", font="comicsans 13 bold", pady=15).grid(row=0, column=3)

    directory_folder=Label(master,text=" Enter the Directory of your new folder")
    fileplace_folder=Label(master, text="Enter the name of your new folder")
    directory_folder.grid(row=1, column=2)
    fileplace_folder.grid(row=2, column=2)

    directory_folder_value=StringVar()
    fileplace_folder_value=StringVar()

    directory_folder_entry=Entry(master, textvariable=directory_folder_value)
    fileplace_folder_entry=Entry(master, textvariable=fileplace_folder_value)

    directory_folder_entry.grid(row=1, column=3)
    fileplace_folder_entry.grid(row=2, column=3)
    
    Button(text="submit", command=getdirectory).grid(row=7, column=3)
    master.mainloop()

    
    ifile=open("records.txt", "r")
    lines=ifile.readlines()

    directory=lines[2].strip()
    fileplace=lines[3].strip()
    filedirec=directory+"\\"+fileplace
    # print(filedirec)
    try:
        os.mkdir(filedirec)
    except:
        filedirec=directory+"\\"+fileplace+str(random.randint(1,15))
        os.mkdir(filedirec)

    ifile=open("records.txt", "r")
    lines=ifile.readlines()
    all_folder=lines[0].strip()
    for i in range(len(match)):
        file1=all_folder+"\\"+match[i]
        # print(file1)
        shutil.copy(file1, filedirec)




elif lines[1]=="2":

    root=Tk()
    root.geometry("644x344")
    root.iconbitmap(r'F:\Subhra_Project\Python_icon.ico')
    root.title("File Directory")
    Label(root, text="Directory Entry", font="comicsans 13 bold", pady=15).grid(row=0, column=3)

    select_file=Label(root,text=" Enter Client file directory")
    select_file.grid(row=1, column=2)

    select_file_value=StringVar()
    select_file_entry=Entry(root, textvariable=select_file_value)

    select_file_entry.grid(row=1, column=3)
    Button(text="submit", command=getvalue).grid(row=7, column=3)
    root.mainloop()

    ifile=open("records.txt", "r")
    line=ifile.readlines()
    all_folder=line[0].strip()
    select_folder=line[2].strip()
    
    match=comparison(all_folder, select_folder)
    # folderDirectory(match)

    master=Tk()
    master.geometry("644x344")
    master.title("File Directory")
    master.iconbitmap(r'F:\Subhra_Project\Python_icon.ico')
    Label(master, text="Directory Entry", font="comicsans 13 bold", pady=15).grid(row=0, column=3)

    directory_folder=Label(master,text=" Enter the Directory of your new folder")
    fileplace_folder=Label(master, text="Enter the name of your new folder")
    directory_folder.grid(row=1, column=2)
    fileplace_folder.grid(row=2, column=2)

    directory_folder_value=StringVar()
    fileplace_folder_value=StringVar()

    directory_folder_entry=Entry(master, textvariable=directory_folder_value)
    fileplace_folder_entry=Entry(master, textvariable=fileplace_folder_value)

    directory_folder_entry.grid(row=1, column=3)
    fileplace_folder_entry.grid(row=2, column=3)
    
    Button(text="submit", command=getdirectory).grid(row=7, column=3)
    master.mainloop()

    
    ifile=open("records.txt", "r")
    lines=ifile.readlines()

    directory=lines[3].strip()
    fileplace=lines[4].strip()
    filedirec=directory+"\\"+fileplace
    # print(filedirec)
    try:
        os.mkdir(filedirec)
    except:
        filedirec=directory+"\\"+fileplace+str(random.randint(1,15))
        os.mkdir(filedirec)

    ifile=open("records.txt", "r")
    lines=ifile.readlines()
    all_folder=lines[0].strip()
    for i in range(len(match)):
        file1=all_folder+"\\"+match[i]
        # print(file1)
        shutil.copy(file1, filedirec)


n.show_toast("File Directory", "Your files have been copied successfully", icon_path=None, duration = 30, threaded=False)

    
#F:\Subhra_Project\proj
#H:\My Photo Album\Dadabhai wedding\Babai\Portrait 2
#H:\My Photo Album\Dadabhai wedding\Babai Biyer Album
#C:\Users\USER\Desktop