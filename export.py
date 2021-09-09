import xlsxwriter
import webbrowser
import random

num=0

#functions
def functionExport(num):
    ##filling list
    f = open("Movie.txt", "rt")
    for line in f:
        string = f.read()
    f.close()
    listMovie = string.split('\n')    
    f = open("Anime.txt", "rt")
    for line in f:
        string = f.read()
    f.close()
    listAnime = string.split('\n')
    f = open("Book.txt", "rt")
    for line in f:
        string = f.read()
    f.close()
    listBook = string.split('\n')
    f = open("Show.txt", "rt")
    for line in f:
        string = f.read()
    f.close()
    listShow = string.split('\n')
    ##starting workbook
    workbook = xlsxwriter.Workbook('Export.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold':True})
    ##filling workbook
    ###media; list; total; random
    worksheet.write(0,0, "Movies", bold)
    row = 1
    for i in listMovie:
        worksheet.write(row, 0, i)
        row += 1
    string = "Total: " + str(len(listMovie)-1)
    worksheet.write(row, 0, string, bold)
    numberR = random.randint(2, len(listMovie))
    string = "Random: " + str(numberR)
    worksheet.write(row+1, 0, string, bold)
    worksheet.write(0,1, "Animes", bold)
    row = 1
    for i in listAnime:
        worksheet.write(row, 1, i)
        row += 1
    string = "Total: " + str(len(listAnime)-1)
    worksheet.write(row, 1, string, bold)
    numberR = random.randint(2, len(listAnime))
    string = "Random: " + str(numberR)
    worksheet.write(row+1, 1, string, bold)
    worksheet.write(0,2, "Books", bold)
    row = 1
    for i in listBook:
        worksheet.write(row, 2, i)
        row += 1
    string = "Total: " + str(len(listBook)-1)
    worksheet.write(row, 2, string, bold)
    numberR = random.randint(2, len(listBook))
    string = "Random: " + str(numberR)
    worksheet.write(row+1, 2, string, bold)
    worksheet.write(0,3, "Shows", bold)
    row = 1
    for i in listShow:
        worksheet.write(row, 3, i)
        row += 1
    string = "Total: " + str(len(listShow)-1)
    worksheet.write(row, 3, string, bold)
    numberR = random.randint(2, len(listShow))
    string = "Random: " + str(numberR)
    worksheet.write(row+1, 3, string, bold)
    ##statistics
    f = open("Statistics.txt", "rt")
    string = f.read()
    lineList = string.split()
    lineList[0] = int(lineList[0])
    lineList[1] = int(lineList[1])
    worksheet.write(0, 5, "Statistics", bold)
    string = "Active Items: " + str(lineList[0])
    worksheet.write(1, 5, string)
    string = "Redeemed Items: " + str(lineList[1])
    worksheet.write(2, 5, string)
    divisor = 1
    for i in range(lineList[0], 1, -1):
        if(lineList[1] % i == 0 and lineList[0] % i == 0):
            divisor = i
            break
    string = "Ratio: " + str(int(lineList[0]/divisor)) + ":" + str(int(lineList[1]/divisor))
    worksheet.write(3, 5, string)
    string = "Total: " + str(lineList[0]+ lineList[1]) 
    worksheet.write(4, 5, string)

    workbook.close()

    if(num == 5):
        webbrowser.open('Export.xlsx')
    
functionExport(8)
