# imports
import tkinter as tk
from tkinter import ttk
from datetime import date
import matplotlib
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import numpy as np
import webbrowser, re, random, time, pyperclip, export, smtplib

# global variables
global colour

# functions
##function that integrates the default setting into the code
def functionSettings():
    global colour
    f = open("dependencies/" + "Settings.txt", "rt")
    colour = f.readline()
    colViable = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    patHexa = re.compile(r"#[0-9a-fA-F]+")
    lstCol = colour.split(",")
    colour1 = lstCol[0].strip()
    colour2 = lstCol[1].strip()
    m = re.search(patHexa, colour1)
    n = re.search(patHexa, colour2)
    if ((colour1 in colViable) and (colour2 in colViable)) or ((m) and (n)):
        for wid in [lblCat, lblAll, lblSettings, lblAct, lblCatR]:
            wid.config(bg=colour1)
        for wid in [btnMov,btnAni,btnSho,btnBoo,btnSta,btnFin,btnExp,btnBar,btnQui,btnColor,btnAdd,btnRed,btnRan,lblDisplay,lblExtra,]:
            wid.config(bg=colour2)
    elif colour1 == "default" or colour2 == "default":
        for wid in [lblCat, lblAll, lblSettings, lblAct, lblCatR]:
            wid.config(bg="#A265CC")
        for wid in [btnMov,btnAni,btnSho,btnBoo,btnSta,btnFin,btnExp,btnBar,btnQui,btnColor,btnAdd,btnRed,btnRan,lblDisplay,lblExtra,]:
            wid.config(bg="#BC65CC")
    f.close()


##functions that choose the type of media you will be browsing
def functionChooseMovie(e = 1):
    widget = root.focus_get()
    if(widget != entEnter):
        lblCatR.config(text="Movies")
        for item in [btnAdd, btnRed, btnRem, btnRan]:
            item.config(state=tk.NORMAL)
        functionDisplay()
    else:
        print('Change active widget away from entry box by pressing the "Finished" main display')

##functions that choose the type of media you will be browsing
def functionChooseAnime(e = 1):
    widget = root.focus_get()
    if(widget != entEnter):
        lblCatR.config(text="Animes")
        for item in [btnAdd, btnRed, btnRem, btnRan]:
            item.config(state=tk.NORMAL)
        functionDisplay()
    else:
        print('Change active widget away from entry box by pressing the "Finished" main display')


##functions that choose the type of media you will be browsing
def functionChooseShow(e = 1):
    widget = root.focus_get()
    if(widget != entEnter):
        lblCatR.config(text="Shows")
        for item in [btnAdd, btnRed, btnRem, btnRan]:
            item.config(state=tk.NORMAL)
        functionDisplay()
    else:
        print('Change active widget away from entry box by pressing the "Finished" main display')


##functions that choose the type of media you will be browsing
def functionChooseBook(e = 1):
    widget = root.focus_get()
    if(widget != entEnter):
        lblCatR.config(text="Books")
        for item in [btnAdd, btnRed, btnRem, btnRan]:
            item.config(state=tk.NORMAL)
        functionDisplay()
    else:
        print('Change active widget away from entry box by pressing the "Finished" main display')


##function that displays the movies you currently would like to watch
def functionDisplay():
    fileName = lblCatR["text"]
    strOutput = ""
    strOutput += fileName + "\n"
    fileName = fileName.replace("s", "")
    fileName += ".txt"
    f = open("dependencies/" + fileName, "rt")
    lineC = 1
    lboDisplay.delete(0, tk.END)
    lblDisplay.pack_forget()
    lboDisplay.pack()
    for line in f:
        strOutput += str(lineC) + " " + line
        lineC += 1
        lboDisplay.insert(tk.END, line)
    f.close()


##function that lets you add a movie you want to watch
def functionAdd(e = 1):
    fileName = lblCatR["text"]
    strOutput = ""
    strOutput += fileName + "\n"
    fileName = fileName.replace("s", "")
    fileName += ".txt"
    f = open("dependencies/" + fileName, "rt")
    listItems = []
    for line in f:
        listItems.append(line)
    f.close()
    new = entEnter.get()
    entEnter.delete(0, tk.END)
    new += "\n"
    # adding
    if new not in listItems:
        listItems.append(new)
        # alphabet sort
        for i in range(len(listItems)):
            for x in range(len(listItems) - 1):
                if listItems[i] < listItems[x]:
                    storage = listItems[i]
                    listItems[i] = listItems[x]
                    listItems[x] = storage

        # display
        w = open("dependencies/" + fileName, "wt")
        lineC = 1
        for item in listItems:
            strOutput += str(lineC) + " " + item
            lineC += 1
            w.write(item)
        lblExtra.config(text="Total Items: " + str(lineC))
        lboDisplay.insert(tk.END, new)
        w.close()

        a = open("dependencies/Statistics.txt", "rt")
        line = a.read()
        lineList = line.split()
        lineList[0] = int(lineList[0]) + 1
        returnLine = str(lineList[0]) + " " + lineList[1]
        a.close()

        a = open("dependencies/Statistics.txt", "wt")
        a.write(returnLine)
        a.close()


##function that lets you "redeem" the movies you've watched
def functionRedeem():
    # file input
    fileName = lblCatR["text"]
    strOutput = ""
    strOutput += fileName + "\n"
    fileName = fileName.replace("s", "")
    fileName += ".txt"
    old = str((lboDisplay.get(tk.ACTIVE)))
    old = old.strip("\n")
    # old = entEnter.get()
    entEnter.delete(0, tk.END)
    old += "\n"
    f = open("dependencies/" + fileName, "rt")
    lboDisplay.pack()
    lblDisplay.pack_forget()
    listItems = []
    for line in f:
        listItems.append(line)
    f.close()
    if old in listItems:
        listItems.remove(old)
        lboDisplay.delete(tk.ANCHOR)
        itemC = 1
        w = open("dependencies/" + fileName, "wt")
        for item in listItems:
            w.write(item)
            itemC += 1
        lblExtra.config(text="Total Items: " + str(itemC))

        w = open("dependencies/" + "Statistics.txt", "rt")
        line = w.read()
        lineList = line.split()
        lineList[0] = int(lineList[0]) - 1
        lineList[1] = int(lineList[1]) + 1
        returnLine = str(lineList[0]) + " " + str(lineList[1])
        w.close()

        w = open("dependencies/" + "Statistics.txt", "wt")
        w.write(returnLine)
        w.close()
        oldedit = old.strip("\n")
        today = date.today()
        todaystr = str(today)
        f = open("dependencies/" + "Finished.txt", "at")
        temp = fileName[0] + "\t" + oldedit + "\t" + todaystr + "\n"
        f.write(temp)
        f.close()
    else:
        lblExtra.config(text="Item was not in list")


##function that allows the program to choose a random program and add it to your clipboard
def functionRandom():
    fileName = lblCatR["text"]
    fileName = fileName.replace("s", "")
    fileName += ".txt"
    f = open("dependencies/" + fileName, "rt")
    listItems = []
    for line in f:
        listItems.append(line)
    f.close()
    intRandom = random.randint(0, len(listItems) - 1)
    output = listItems[intRandom]
    pyperclip.copy(output)
    if "Show" in fileName or "Movie" in fileName:
        webbrowser.open("https://soap2day.ac/", new=1)
    elif "Anime" in fileName:
        webbrowser.open("https://9anime.se/", new=1)
    lblExtra.config(text=output)

##function that removes items from the associated list
def functionRemove():
    # file input
    fileName = lblCatR["text"]
    strOutput = ""
    strOutput += fileName + "\n"
    fileName = fileName.replace("s", "")
    fileName += ".txt"
    # old = entEnter.get()
    old = str((lboDisplay.get(tk.ACTIVE)))
    old = old.strip("\n")
    lboDisplay.delete(tk.ANCHOR)
    entEnter.delete(0, tk.END)
    old += "\n"
    f = open("dependencies/" + fileName, "rt")
    listItems = []
    for line in f:
        listItems.append(line)
    f.close()
    if old in listItems:
        listItems.remove(old)

        itemC = 1
        w = open("dependencies/" + fileName, "wt")
        for item in listItems:
            w.write(item)
            #     strOutput += str(itemC) + " "+item
            itemC += 1
        lblExtra.config(text="Total Items" + str(itemC))

        w = open("dependencies/" + "Statistics.txt", "rt")
        line = w.read()
        lineList = line.split()
        lineList[0] = int(lineList[0]) - 1
        returnLine = str(lineList[0]) + " " + str(lineList[1])
        w.close()

        w = open("dependencies/" + "Statistics.txt", "wt")
        w.write(returnLine)
        w.close()
    else:
        lblExtra.config(text="Item was not in list")


##function that ljets you access the statistics of your consumption so far
def functionStatistics():
    f = open("dependencies/" + "Statistics.txt", "rt")
    line = f.read()
    lineList = line.split()
    lineList[0] = int(lineList[0])
    lineList[1] = int(lineList[1])
    f.close()
    strOutput = "Statistics\n"
    strOutput += "Active Items: " + str(lineList[0]) + "\n"
    strOutput += "Redeemed Items: " + str(lineList[1]) + "\n"
    divisor = 1
    for i in range(lineList[0], 1, -1):
        if lineList[1] % i == 0 and lineList[0] % i == 0:
            divisor = i
            break
    strOutput += (
        "Ratio: "
        + str(int(lineList[0] / divisor))
        + ":"
        + str(int(lineList[1] / divisor))
        + "\n"
    )
    strOutput += "Total: " + str(lineList[0] + lineList[1]) + "\n"
    lblCatR.config(text="All Categories")
    lblDisplay.pack()
    lboDisplay.pack_forget()
    lblDisplay.config(image="")
    lblDisplay.config(text=strOutput)
    lblDisplay.config(height=25, width=50)
    btnAdd.config(state=tk.DISABLED)
    btnRed.config(state=tk.DISABLED)
    btnRem.config(state=tk.DISABLED)
    btnRan.config(state=tk.DISABLED)


##function that displays to you the titles that you have completed thus far
def functionFinished(e = 1):
    f = open("dependencies/" + "Finished.txt", "rt")
    lboDisplay.pack()
    lblDisplay.pack_forget()
    lboDisplay.delete(0, tk.END)
    lblDisplay.pack_forget()
    lboDisplay.pack()
    for line in f:
        lstLine = line.split("\t")
        lboDisplay.insert(tk.END, lstLine[1])
    f.close()
    lblCatR.config(text="Finished")
    btnAdd.config(state=tk.DISABLED)
    btnRed.config(state=tk.DISABLED)
    btnRem.config(state=tk.DISABLED)
    btnRan.config(state=tk.DISABLED)


##function that exports an excel spreadsheet showing all the media that you still need to watch
def functionExport():
    export.functionExport(5)
    lblExtra.config(text="don't open more than one of the exports at a time!")
    btnAdd.config(state=tk.DISABLED)
    btnRed.config(state=tk.DISABLED)
    btnRem.config(state=tk.DISABLED)
    btnRan.config(state=tk.DISABLED)


##function that display a bar graph depicting the media types of your consumption
def functionBar():
    f = open("dependencies/" + "Finished.txt", "rt")
    strOutput = "Finished Items" + "\n"
    lstOptions = ["M", "A", "S", "B"]
    lstOptNum = [0, 0, 0, 0]
    for line in f:
        string = line
        for i in range(0, len(lstOptions)):
            if string[0] == lstOptions[i]:
                lstOptNum[i] = lstOptNum[i] + 1
    f.close()
    lstOptions = ["Movies", "Animes", "Shows", "Books"]
    plt.clf()
    x = np.array(lstOptions)
    y = np.array(lstOptNum)
    plt.bar(x, y, color="purple")
    plt.xlabel("Categories")
    plt.ylabel("Frequency")
    plt.title("Type of Media Watched")
    plt.savefig("figure.jpg")
    path = "figure.jpg"
    imagee = ImageTk.PhotoImage(Image.open(path))
    lblDisplay.pack()
    lboDisplay.pack_forget()
    lblDisplay.config(image=imagee)
    lblDisplay.config(width=600, height=500)
    lblDisplay.image = imagee
    lblExtra.config(text="might want to fullscreen it if you haven't already")
    btnAdd.config(state=tk.DISABLED)
    btnRed.config(state=tk.DISABLED)
    btnRem.config(state=tk.DISABLED)
    btnRan.config(state=tk.DISABLED)


##function that displays a line graph depicting your watch times starting from the first entry
def functionLine():
    strRaw = ""
    lstFinishedProc = []
    f = open("dependencies/" + "Finished.txt", "rt")
    for line in f:
        strRaw += line
    f.close()

    lstFinishedProc = re.findall(r"\d\d\d\d-\d\d\-\d\d", strRaw)
    lstDaysE = []
    lstStor = lstFinishedProc[0].split("-")

    dayI = date(int(lstStor[0]), int(lstStor[1]), int(lstStor[2]))
    for days in lstFinishedProc:
        lstStor = days.split("-")
        dayF = date(int(lstStor[0]), int(lstStor[1]), int(lstStor[2]))
        deltaTime = dayF - dayI
        lstDaysE.append(deltaTime.days)

    intStor = 1
    lstUnique = []
    lstUniqueInt = []
    boolFirst = True
    for i in range(0, lstDaysE[-1]):
        lstUnique.append(i / 30)
        lstUniqueInt.append(lstDaysE.count(i))

    lstStor = []
    for item in lstDaysE:
        lstStor.append(1)

    plt.clf()

    lstUniqueNp = np.array(lstUnique)
    lstUniqueIntNp = np.array(lstUniqueInt)

    plt.plot(lstUniqueNp, lstUniqueIntNp)
    plt.ylabel("# Media Consumed")
    plt.xlabel("Months Since " + lstFinishedProc[0])
    plt.title("# Media Consumed Over Time")
    plt.savefig("figure.jpg")
    path = "figure.jpg"
    imagee = ImageTk.PhotoImage(Image.open(path))
    lblDisplay.pack()
    lboDisplay.pack_forget()
    lblDisplay.config(image=imagee)
    lblDisplay.config(width=600, height=500)
    lblDisplay.image = imagee
    btnAdd.config(state=tk.DISABLED)
    btnRed.config(state=tk.DISABLED)
    btnRem.config(state=tk.DISABLED)
    btnRan.config(state=tk.DISABLED)


##function that lets you change the default colour of your program
def functionColour():
    global colour
    colViable = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    patHexa = re.compile(r"#[0-9a-fA-F]+")
    colour = entEnter.get()
    lstCol = colour.split(",")
    colour1 = lstCol[0].strip()
    colour2 = lstCol[1].strip()
    m = re.search(patHexa, colour1)
    n = re.search(patHexa, colour2)
    lblDisplay.config(text=colour)
    lblDisplay.config(height=25, width=75)
    if ((colour1 in colViable) and (colour2 in colViable)) or ((m) and (n)):
        for wid in [lblCat, lblAll, lblSettings, lblAct, lblCatR]:
            wid.config(bg=colour1)
        for wid in [btnMov,btnAni,btnSho,btnBoo,btnSta,btnFin,btnExp,btnBar,btnQui,btnColor,btnAdd,btnRed,btnRan,lblDisplay,lblExtra]:
            wid.config(bg=colour2)
    elif colour1 == "default" or colour2 == "default":
        for wid in [lblCat, lblAll, lblSettings, lblAct, lblCatR]:
            wid.config(bg="#A265CC")
        for wid in [btnMov,btnAni,btnSho,btnBoo,btnSta,btnFin,btnExp,btnBar,btnQui,btnColor,btnAdd,btnRed,btnRan,lblDisplay,lblExtra]:
            wid.config(bg="#BC65CC")
    f = open("dependencies/" + "dependencies/" + "Settings.txt", "wt")
    f.write(colour)
    root.destroy
    f.close()


##function that emails your Entertainment Library to yourself
def functionEmail():
    strSend = "Subject: Entertainment Library List\n\n"
    ###getting email and password from entry
    strEntry = entEnter.get()
    entEnter.delete(0, tk.END)
    lstEntry = strEntry.split()
    email, password = lstEntry[0], lstEntry[1]
    lblExtra.config(text="Emailed Entertainment Library List to and from %s" % email)
    ###getting textfile information
    for file in ["Movie", "Anime", "Show", "Book"]:
        strSend += "~~" + file + "~~\n"
        f = open("dependencies/" + file + ".txt", "rt")
        for line in f:
            strSend += line
        strSend += "\n"
    ###sending email
    conn = smtplib.SMTP("smtp-mail.outlook.com", 587)
    conn.ehlo()
    conn.starttls()
    conn.login(email, password)
    conn.sendmail(email, email, strSend)
    conn.quit()


# main code
##GUI creation
root = tk.Tk()
root.title("Entertainment Library")
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file="dependencies/icon.png"))


"""
left frame creation, contains
- Categories, subheading text for all the different media types
- Movie, button to select movies
- Anime, button to select animes
- Show, button to select shows
- Book, button to select books
- For All, subheading text for buttons that apply to all media types
- Statistics, shows numerical statistics
- Finished, shows finished media
- Email, emails to be watched media
- Export Excel, exports list to excel
- Figure - Bar, exports bar graph of finished media
- Figure - Line, exports line graph of finished media
- Quit - quits
"""
frmLeft = tk.Frame(master=root, relief="raised", borderwidth=5, bg="#B298C4")
frmLeft.pack(fill=tk.BOTH, side=tk.LEFT)
##categories
lblCat = tk.Label(frmLeft, text="Categories", bg="#A265CC", fg="white", font=("Helvetica", 12, "bold"))
lblCat.grid(row=0, column=0, pady=5, padx=5, sticky="nesw", ipady=10)
###button for selecting movies
btnMov = tk.Button(frmLeft, text="Movie", bg="#BC65CC", fg="white", command=functionChooseMovie)
btnMov.grid(row=1, column=0, pady=5, padx=5, sticky="nesw")
root.bind('<space>m', functionChooseMovie)
###button for selecting animes
btnAni = tk.Button(frmLeft, text="Anime", bg="#BC65CC", fg="white", command=functionChooseAnime)
btnAni.grid(row=2, column=0, pady=5, padx=5, sticky="nesw")
root.bind("<space>a", functionChooseAnime)
###button for selecting shows
btnSho = tk.Button(frmLeft, text="Show", bg="#BC65CC", fg="white", command=functionChooseShow)
btnSho.grid(row=3, column=0, pady=5, padx=5, sticky="nesw")
root.bind("<space>s", functionChooseShow)
###button for selecting books
btnBoo = tk.Button(frmLeft, text="Book", bg="#BC65CC", fg="white", command=functionChooseBook)
btnBoo.grid(row=4, column=0, pady=5, padx=5, sticky="nesw")
root.bind("<space>b", functionChooseBook)

##for all
lblAll = tk.Label(frmLeft, text="For All", bg="#A265CC", fg="white", font=("Helvetica", 12, "bold"))
lblAll.grid(row=5, column=0, pady=5, padx=5, sticky="nesw", ipady=10)
###button for numerical statistics
btnSta = tk.Button(frmLeft, text="Statistics", bg="#BC65CC", fg="white", command=functionStatistics)
btnSta.grid(row=6, column=0, pady=5, padx=5, sticky="nesw")
###button to display finished media
btnFin = tk.Button(frmLeft, text="Finished", bg="#BC65CC", fg="white", command=functionFinished)
btnFin.grid(row=7, column=0, pady=5, padx=5, sticky="nesw")
root.bind("<f>", functionFinished)
###button to email Entertainment List to self provided with email password
btnEma = tk.Button(frmLeft, text="Email", bg="#BC65CC", fg="white", command=functionEmail)
btnEma.grid(row=8, column=0, pady=5, padx=5, sticky="nesw")
###button to export Entertainment List into excel
btnExp = tk.Button(frmLeft, text="Export Excel", bg="#BC65CC", fg="white", command=functionExport)
btnExp.grid(row=9, column=0, pady=5, padx=5, sticky="nesw")
###button to display bar graph of finished media
btnBar = tk.Button(frmLeft, text="Figure - Bar", bg="#BC65CC", fg="white", command=functionBar)
btnBar.grid(row=10, column=0, pady=5, padx=5, sticky="nsew")
###button to display line graph of finished media
btnLine = tk.Button(frmLeft, text="Figure - Line", bg="#BC65CC", fg="white", command=functionLine)
btnLine.grid(row=11, column=0, pady=5, padx=5, sticky="nsew")
###button to exit program
btnQui = tk.Button(frmLeft, text="Quit", bg="#BC65CC", fg="white", command=root.destroy)
btnQui.grid(row=12, column=0, pady=5, padx=5, sticky="nesw")


"""
middle frame creation, contains:
- Actions, subheading text for actions specific to different medias
- Add, adds a new movie/anime/show/book to the media type
- Redeem, redeems a recently finished title
- Random, randomly selects a to-be-watched title, and goes to the affiliated site
- Remove, removes the title
- Settings, subheading text for settings
- Change Colour, changes default colour given two arguments: a foreground colour and a background colour
"""
frmMiddle = tk.Frame(master=root, relief="raised", borderwidth=5, bg="#B298C4")
frmMiddle.pack(fill=tk.BOTH, side=tk.LEFT)
###labels for actions
lblAct = tk.Label(frmMiddle, text="Actions", bg="#A265CC", fg="white", font=("Helvetica", 12, "bold"))
lblAct.grid(row=0, column=0, pady=5, padx=5, sticky="nesw", ipady=10)
###button to add media
btnAdd = tk.Button(frmMiddle, text="Add", bg="#BC65CC", fg="white", command=functionAdd)
btnAdd.grid(row=1, column=0, pady=5, padx=5, sticky="nesw")
root.bind('<Return>', functionAdd)
###button to redeem media
btnRed = tk.Button(frmMiddle, text="Redeem", bg="#BC65CC", fg="white", command=functionRedeem)
btnRed.grid(row=2, column=0, pady=5, padx=5, sticky="nesw")
###button to randomize media
btnRan = tk.Button(frmMiddle, text="Random", bg="#BC65CC", fg="white", command=functionRandom)
btnRan.grid(row=3, column=0, pady=5, padx=5, sticky="nesw")
btnRem = tk.Button(frmMiddle, text="Remove", bg="#BC65CC", fg="white", command=functionRemove)
btnRem.grid(row=4, column=0, pady=5, padx=5, sticky="news")
##title for the settings
lblSettings = tk.Label(frmMiddle, text="Settings", bg="#A265CC", fg="white", font=("Helvetica", 12, "bold"))
lblSettings.grid(row=5, column=0, pady=5, padx=5, sticky="nesw", ipady=10)
###button to change teh default colours of the program when passed either basic colour strings or hexadecimal colours
btnColor = tk.Button(frmMiddle, text="Change Colour", bg="#BC65CC", fg="white", command=functionColour)
btnColor.grid(row=6, column=0, pady=5, padx=5, sticky="nesw", ipady=10)


"""right frame creation, contains:
- Media Type, subheading text that displays whichever media group you have selected
- Huge Display, the main display for the program
- Entry Box, all-purpose entry box
- Text Box, text box for messages to be communicated with the user
"""
frmRight = tk.Frame(root, relief="raised", borderwidth=5, bg="#B298C4")
frmRight.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
###label showing type of media
lblCatR = tk.Label(frmRight, text="Movies", bg="#A265CC", fg="white", font=("Helvetica", 14, "bold"))
lblCatR.pack(fill=tk.X, side=tk.TOP)
###label for main displaying
frmDisplay = tk.Label(frmRight, relief="sunken", borderwidth=5, bg="#B298C4")
frmDisplay.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
###main label for display
lblDisplay = tk.Label(frmDisplay, text="There is nothing to display", height=25, width=50)
lblDisplay.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, pady=10, padx=10)
lblDisplay.pack_forget()
###vertical scrollbar for display
scrDisplay = tk.Scrollbar(frmDisplay)
scrDisplay.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
###multi-item list box for display
lboDisplay = tk.Listbox(frmDisplay, yscrollcommand=scrDisplay.set, height=25, width=50)
scrDisplay.config(command=lboDisplay.yview)
lboDisplay.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
###entry for entries
entEnter = tk.Entry(frmRight)
entEnter.pack(fill=tk.X, side=tk.TOP)
###lable for extra test
lblExtra = tk.Label(frmRight, text="hewwo uwu", bg="#BD98C4", fg="white", height=3)
lblExtra.pack(fill=tk.X, side=tk.TOP)

##settings
functionSettings()
functionChooseMovie()

# required mainloop
root.mainloop()
