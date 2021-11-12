#imports
import tkinter as tk
from datetime import date
import matplotlib
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import numpy as np
import webbrowser, re, random, time, pyperclip, export

#global variables
global colour

#functions
##function that integrates the default setting into the code
def functionSettings():
    global colour
    f = open('Settings.txt', 'rt')
    colour=f.readline()
    colViable = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    patHexa = re.compile(r"#[0-9a-fA-F]+")
    lstCol = colour.split(',')
    colour1 = lstCol[0].strip()
    colour2 = lstCol[1].strip()
    m = re.search(patHexa, colour1)
    n = re.search(patHexa, colour2)
    if ((colour1 in colViable) and  (colour2 in colViable)) or ((m)and(n)):
        for wid in [lblCat, lblAll, lblSettings, lblAct, lblCatR]:
            wid.config(bg = colour1)
        for wid in [btnMov, btnAni, btnSho, btnBoo, btnSta, btnFin, btnExp, btnBar, btnQui, btnColor, btnDis, btnAdd, btnRed, btnRan, lblDisplay, lblExtra]:
            wid.config(bg = colour2)
    elif(colour1 == 'default' or colour2 == 'default'):
        for wid in [lblCat, lblAll, lblSettings, lblAct, lblCatR]:
            wid.config(bg = '#A265CC')
        for wid in [btnMov, btnAni, btnSho, btnBoo, btnSta, btnFin, btnExp, btnBar, btnQui, btnColor, btnDis, btnAdd, btnRed, btnRan, lblDisplay, lblExtra]:
            wid.config(bg = '#BC65CC')
    f.close()

##functions that choose the type of media you will be browsing
def functionChooseMovie():
    lblCatR.config(text='Movies')
def functionChooseAnime():
    lblCatR.config(text='Animes')
def functionChooseShow():
    lblCatR.config(text='Shows')
def functionChooseBook():
    lblCatR.config(text='Books')

##function that displays the movies you currently would like to watch
def functionDisplay():
    fileName = lblCatR['text']
    strOutput = ''
    strOutput += fileName +'\n'
    fileName = fileName.replace('s', '')
    fileName += '.txt'
    f = open(fileName, "rt")
    lineC = 1
    for line in f:
        strOutput += str(lineC) + " "+line
        lineC += 1
    strOutput+="\nTotal: " + str(lineC-1) + '\n'
    lblDisplay.config(image='')
    lblDisplay.config(text = strOutput)
    lblDisplay.config(height = 25, width= 75)
    f.close()

##function that lets you add a movie you want to watch
def functionAdd():
    fileName = lblCatR['text']
    strOutput = ''
    strOutput += fileName +'\n'
    fileName = fileName.replace('s', '')
    fileName += '.txt'
    f = open(fileName, "rt")
    listItems = []
    for line in f:
        listItems.append(line)
    f.close()
    new = entEnter.get()
    entEnter.delete(0, tk.END)
    new += '\n'
    #adding
    if(new not in listItems):
        listItems.append(new)
        #alphabet sort
        for i in range(len(listItems)):
            for x in range(len(listItems)-1):
                if(listItems[i] < listItems[x]):
                    storage = listItems[i]
                    listItems[i] = listItems[x]
                    listItems[x] = storage
                
        #display
        w = open(fileName, "wt")
        lineC = 1
        for item in listItems:
            strOutput += str(lineC) + " "+item
            lineC += 1
            w.write(item)
        strOutput+="\nTotal: " + str(lineC-1) + '\n'
        lblDisplay.config(image='')
        lblDisplay.config(text = strOutput)
        lblDisplay.config(height = 25, width= 75)
        w.close()
        
        a = open("Statistics.txt", "rt")
        line = a.read()
        lineList = line.split()
        lineList[0] = int(lineList[0]) + 1
        returnLine = str(lineList[0]) + " " + lineList[1]
        a.close()
        
        a = open("Statistics.txt", "wt")
        a.write(returnLine)
        a.close()

##function that lets you "redeem" the movies you've watched 
def functionRedeem():
    #file input
    fileName = lblCatR['text']
    strOutput = ''
    strOutput += fileName +'\n'
    fileName = fileName.replace('s', '')
    fileName += '.txt'
    old = entEnter.get()
    entEnter.delete(0, tk.END)
    old += "\n"
    f = open(fileName, "rt")
    listItems = []
    for line in f:
        listItems.append(line)
    f.close()
    if(old in listItems):
        listItems.remove(old)
        
        itemC = 1
        w = open(fileName, "wt")
        for item in listItems:
            w.write(item)
            strOutput += str(itemC) + " "+item
            itemC += 1
        strOutput+="\nTotal: " + str(itemC-1) + '\n'
        lblDisplay.config(image='')
        lblDisplay.config(text = strOutput)
        lblDisplay.config(height = 25, width= 75)
        
        w = open("Statistics.txt", "rt")
        line = w.read()
        lineList = line.split()
        lineList[0] = int(lineList[0]) - 1
        lineList[1] = int(lineList[1]) + 1
        returnLine = str(lineList[0]) + " " + str(lineList[1])
        w.close()

        w = open("Statistics.txt", "wt")
        w.write(returnLine)
        w.close()
        oldedit = old.strip('\n')
        today = date.today()
        todaystr = str(today)
        f = open("Finished.txt", "at")
        temp = fileName[0] + "\t" + oldedit + "\t" + todaystr + "\n"
        f.write(temp)
        f.close()
    else:
        print("Item was not in list")

##function that allows the program to choose a random program and add it to your clipboard
def functionRandom():
    fileName = lblCatR['text']
    fileName = fileName.replace('s', '')
    fileName += '.txt'
    f = open(fileName, "rt")
    listItems = []
    for line in f:
        listItems.append(line)
    f.close()
    intRandom = random.randint(0, len(listItems)-1)
    output = listItems[intRandom]
    pyperclip.copy(output)
    if("Show" in fileName or "Movie" in fileName):
        webbrowser.open('https://lookmovie.io/', new=1)
    elif("Anime" in fileName):
        webbrowser.open("https://9anime.ru/", new=1)
    lblExtra.config(text=output)

##function that lets you access the statistics of your consumption so far
def functionStatistics():
    f = open('Statistics.txt', "rt")
    line = f.read()
    lineList = line.split()
    lineList[0] = int(lineList[0])
    lineList[1] = int(lineList[1])
    f.close()
    strOutput = "Statistics\n"
    strOutput += "Active Items: " + str(lineList[0]) + "\n"
    strOutput += "Redeemed Items: " + str(lineList[1]) + '\n'
    divisor = 1
    for i in range(lineList[0], 1, -1):
        if(lineList[1] % i == 0 and lineList[0] % i == 0):
            divisor = i
            break
    strOutput += "Ratio: " + str(int(lineList[0]/divisor)) + ":" + str(int(lineList[1]/divisor)) + '\n'
    strOutput += "Total: " + str(lineList[0] + lineList[1]) +"\n"
    lblCatR.config(text="All Categories")
    lblDisplay.config(image='')
    lblDisplay.config(text=strOutput)
    lblDisplay.config(height = 25, width= 75)

##function that displays to you the titles that you have completed thus far
def functionFinished():
    f = open("Finished.txt", "rt")
    strOutput = "Finished Items" + '\n'
    for line in f:
        string = line
        string.replace("\t", " ")
        strOutput += string
    f.close()
    lblDisplay.config(image='')
    lblDisplay.config(text=strOutput)
    lblDisplay.config(height = 25, width= 75)

##function that exports an excel spreadsheet showing all the media that you still need to watch    
def functionExport():
    export.functionExport(5)
    lblExtra.config(text='don\'t open more than one of the exports at a time!')

##function that display a bar graph depicting the media types of your consumption
def functionBar():
    f = open("Finished.txt", "rt")
    strOutput = "Finished Items" + '\n'
    lstOptions = ['M', 'A', 'S', 'B']
    lstOptNum = [0,0,0,0]
    for line in f:
        string = line
        for i in range(0, len(lstOptions)):
            if(string[0] == lstOptions[i]):
                lstOptNum[i] = lstOptNum[i] + 1
    f.close()
    lstOptions = ['Movies', 'Animes', 'Shows', 'Books']
    plt.clf()
    x = np.array(lstOptions)
    y = np.array(lstOptNum)
    plt.bar(x,y, color = "purple")
    plt.xlabel("Categories")
    plt.ylabel("Frequency")
    plt.title("Type of Media Watched")
    plt.savefig('figure.jpg')
    path = 'figure.jpg'
    imagee = ImageTk.PhotoImage(Image.open(path))
    lblDisplay.config(image = imagee)
    lblDisplay.config(width=600, height=500)
    lblDisplay.image = imagee
    lblExtra.config(text="might want to fullscreen it if you haven't already")

##function that displays a line graph depicting your watch times starting from the first entry
def functionLine():
    strRaw = ''
    lstFinishedProc = []
    f = open('Finished.txt', 'rt')
    for line in f:
        strRaw+=line
    f.close()

    lstFinishedProc = re.findall(r'\d\d\d\d-\d\d\-\d\d', strRaw)
    lstDaysE = []
    lstStor = lstFinishedProc[0].split('-')
    
    dayI = date(int(lstStor[0]), int(lstStor[1]), int(lstStor[2]))
    for days in lstFinishedProc:
        lstStor = days.split('-')
        dayF = date(int(lstStor[0]), int(lstStor[1]), int(lstStor[2]))
        deltaTime = dayF - dayI
        lstDaysE.append(deltaTime.days)

    intStor = 1
    lstUnique = []
    lstUniqueInt = []
    boolFirst = True
    for i in range(0, lstDaysE[-1]):
        lstUnique.append(i/30)
        lstUniqueInt.append(lstDaysE.count(i))

        
    
    # print(lstDaysE)
    # print(lstUnique, len(lstUnique))
    # print(lstUniqueInt, len(lstUniqueInt))
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
    plt.savefig('figure.jpg')
    path = 'figure.jpg'
    imagee = ImageTk.PhotoImage(Image.open(path))
    lblDisplay.config(image = imagee)
    lblDisplay.config(width=600, height=500)
    lblDisplay.image = imagee

##function that lets you change the default colour of your program
def functionColour():
    global colour
    colViable = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    patHexa = re.compile(r"#[0-9a-fA-F]+")
    colour = entEnter.get()
    lstCol = colour.split(',')
    colour1 = lstCol[0].strip()
    colour2 = lstCol[1].strip()
    m = re.search(patHexa, colour1)
    n = re.search(patHexa, colour2)
    lblDisplay.config(text = colour)
    lblDisplay.config(height = 25, width= 75)
    if ((colour1 in colViable) and  (colour2 in colViable)) or ((m)and(n)):
        for wid in [lblCat, lblAll, lblSettings, lblAct, lblCatR]:
            wid.config(bg = colour1)
        for wid in [btnMov, btnAni, btnSho, btnBoo, btnSta, btnFin, btnExp, btnBar, btnQui, btnColor, btnDis, btnAdd, btnRed, btnRan, lblDisplay, lblExtra]:
            wid.config(bg = colour2)
    elif(colour1 == 'default' or colour2 == 'default'):
        for wid in [lblCat, lblAll, lblSettings, lblAct, lblCatR]:
            wid.config(bg = '#A265CC')
        for wid in [btnMov, btnAni, btnSho, btnBoo, btnSta, btnFin, btnExp, btnBar, btnQui, btnColor, btnDis, btnAdd, btnRed, btnRan, lblDisplay, lblExtra]:
            wid.config(bg = '#BC65CC')
    f = open('Settings.txt', 'wt')
    f.write(colour)
    root.destroy
    f.close()    

#main code
##GUI creation
root = tk.Tk()
root.title("Entertaiment Library")

##left frame creation
frmLeft = tk.Frame(master = root, relief = "raised", borderwidth = 5,bg = '#B298C4')
frmLeft.pack(fill=tk.BOTH, side=tk.LEFT)
##categories
lblCat = tk.Label(frmLeft, text = 'Categories', bg = '#A265CC', fg = 'white', font=("Helvetica",12,"bold"))
lblCat.grid(row=0, column = 0, pady = 5, padx = 5, sticky = 'nesw', ipady = 10)
###button for selecting movies
btnMov = tk.Button(frmLeft, text = 'Movie', bg = '#BC65CC', fg = 'white', command = functionChooseMovie)
btnMov.grid(row=1, column = 0, pady = 5, padx = 5, sticky = 'nesw')
###button for selecting animes
btnAni = tk.Button(frmLeft, text = 'Anime', bg = '#BC65CC', fg = 'white', command = functionChooseAnime)
btnAni.grid(row=2, column = 0, pady = 5, padx = 5, sticky = 'nesw')
###button for selecting shows
btnSho = tk.Button(frmLeft, text = 'Show', bg = '#BC65CC', fg = 'white', command = functionChooseShow)
btnSho.grid(row=3, column = 0, pady = 5, padx = 5, sticky = 'nesw')
###button for selecting books
btnBoo = tk.Button(frmLeft, text = 'Book', bg = '#BC65CC', fg = 'white', command = functionChooseBook)
btnBoo.grid(row=4, column = 0, pady = 5, padx = 5, sticky = 'nesw')
##for all
lblAll = tk.Label(frmLeft, text = 'For All', bg = '#A265CC', fg = 'white', font=("Helvetica",12,"bold"))
lblAll.grid(row=5, column = 0, pady = 5, padx = 5, sticky = 'nesw', ipady = 10)
btnSta = tk.Button(frmLeft, text = 'Statistics', bg = '#BC65CC', fg = 'white', command = functionStatistics)
btnSta.grid(row=6, column = 0, pady = 5, padx = 5, sticky = 'nesw')
btnFin = tk.Button(frmLeft, text = 'Finished', bg = '#BC65CC', fg = 'white', command = functionFinished)
btnFin.grid(row=7, column = 0, pady = 5, padx = 5, sticky = 'nesw')
btnExp = tk.Button(frmLeft, text = 'Export Excel', bg = '#BC65CC', fg = 'white', command=functionExport)
btnExp.grid(row=8, column = 0, pady = 5, padx = 5, sticky = 'nesw')
btnBar = tk.Button(frmLeft, text = 'Figure - Bar', bg = '#BC65CC', fg = 'white', command=functionBar)
btnBar.grid(row=9, column = 0, pady = 5, padx = 5, sticky = 'nsew')
btnLine = tk.Button(frmLeft, text = 'Figure - Line', bg = '#BC65CC', fg = 'white', command=functionLine)
btnLine.grid(row=10, column = 0, pady = 5, padx = 5, sticky = 'nsew')
btnQui = tk.Button(frmLeft, text = 'Quit', bg = '#BC65CC', fg = 'white', command=root.destroy)
btnQui.grid(row=11, column = 0, pady = 5, padx = 5, sticky = 'nesw')
##settings
lblSettings = tk.Label(frmLeft, text = 'Settings', bg = '#A265CC', fg = 'white', font=("Helvetica",12,"bold"))
lblSettings.grid(row=12, column = 0, pady=5, padx=5, sticky= 'nesw', ipady = 10)
btnColor = tk.Button(frmLeft, text = 'Change Colour', bg = '#BC65CC', fg = 'white', command = functionColour)
btnColor.grid(row=13, column = 0, pady = 5, padx = 5, sticky = 'nesw', ipady = 10)

##middle frame creation
frmMiddle = tk.Frame(master = root, relief = "raised", borderwidth = 5,bg = '#B298C4')
frmMiddle.pack(fill=tk.BOTH, side=tk.LEFT)
###labels for actions
lblAct = tk.Label(frmMiddle, text = 'Actions', bg = '#A265CC', fg = 'white', font=("Helvetica",12,"bold"))
lblAct.grid(row=0, column = 0, pady = 5, padx = 5, sticky = 'nesw', ipady = 10)
###button to display media
btnDis = tk.Button(frmMiddle, text = 'Display', bg = '#BC65CC', fg = 'white', command = functionDisplay)
btnDis.grid(row=1, column=0, pady = 5, padx = 5, sticky = 'nesw')
###button to add media
btnAdd = tk.Button(frmMiddle, text = 'Add', bg = '#BC65CC', fg = 'white', command = functionAdd)
btnAdd.grid(row=2, column=0, pady = 5, padx = 5, sticky = 'nesw')
###button to redeem media
btnRed = tk.Button(frmMiddle, text = 'Redeem', bg = '#BC65CC', fg = 'white', command = functionRedeem)
btnRed.grid(row=3, column=0, pady = 5, padx = 5, sticky = 'nesw')
###button to randomize media
btnRan = tk.Button(frmMiddle, text = 'Random', bg = '#BC65CC', fg = 'white', command = functionRandom)
btnRan.grid(row=4, column=0, pady = 5, padx = 5, sticky = 'nesw')


##right frame creation
frmRight = tk.Frame(root, relief = 'raised', borderwidth = 5,bg = '#B298C4')
frmRight.pack(fill=tk.BOTH, side=tk.LEFT, expand = True)
###label showing type of media
lblCatR = tk.Label(frmRight, text = "Movies", bg = '#A265CC', fg = 'white', font=("Helvetica",14,"bold"))
lblCatR.pack(fill=tk.X, side = tk.TOP)
###label for main displaying
lblDisplay = tk.Label(frmRight, text = 'There is nothing to display', height = 25, width= 75)
lblDisplay.pack(fill=tk.BOTH, expand = True, side = tk.TOP)
###entry for entries
entEnter = tk.Entry(frmRight)
entEnter.pack(fill=tk.X, side = tk.TOP)
###lable for extra test
lblExtra = tk.Label(frmRight, text= "hewwo uwu", bg = '#BD98C4', fg = 'white', height = 3)
lblExtra.pack(fill=tk.X, side = tk.TOP)

##settings
functionSettings()

#required mainloop
root.mainloop()