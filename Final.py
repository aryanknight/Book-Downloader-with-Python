from bs4 import BeautifulSoup as bb
import requests, os
from tkinter import *
import threading, popup, webbrowser as wb, io
aryan = Tk()
aryan.wm_title('Arabian Knights :- Book Downloader')
backdir = os.getcwd()
fullp3 = backdir + '\\Images\\s1.ico'
aryan.iconbitmap(fullp3)
fullp1 = backdir + '\\Images\\B1.png'
fullp2 = backdir + '\\Images\\S1.png'
fullp4 = backdir + '\\Images\\S2.png'
aryan.minsize(700, 467)
aryan.resizable(0, 0)
back = PhotoImage(file=fullp1)
BU = PhotoImage(file=fullp2)
BU2 = PhotoImage(file=fullp4)
label = Label(aryan, image=back)
label.place(x=0, y=0, relwidth=1, relheight=1)

def site1():
    j = ''
    e = {}
    p = []
    t = 0
    s = 1
    q = ''
    backdir9 = os.getcwd()
    fine = backdir9 + '\\Data\\name.txt'
    fine1 = backdir9 + '\\Data\\count.txt'
    with open(fine, 'r+') as (f):
        f.truncate()
    with open(fine1, 'r+') as (f):
        f.truncate()
    popup.lead2()
    with open(fine, 'r+') as (f):
        j = f.read()
        f.seek(0)
        f.truncate()
    web = 'http://gen.lib.rus.ec/search.php?req='
    web1 = 'http://gen.lib.rus.ec/'
    web2 = 'http://93.174.95.29'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    book = j
    name = book.replace(' ', '+')
    r = requests.get((web + name), headers=headers)
    soup = bb(r.text, 'lxml')
    match = soup.findAll('td', width='500')
    x = 1
    for d in match:
        g = d.a.text
        o = d.a['href']
        e[g] = o

    with io.open(fine, 'r+', encoding='utf-8') as (f):
        for a in e.keys():
            m = str(x)
            f.write(m + '.  ' + a + '\n\n')
            x += 1

    os.startfile(fine)
    popup.lead3()
    with open(fine1, 'r+') as (f):
        t = int(f.readline())
        f.truncate()
    for d in e.keys():
        if s == t:
            q = d
        s += 1

    new = e[q]
    new2 = web1 + new
    new3 = requests.get(new2, headers=headers)
    soup1 = bb(new3.text, 'lxml')
    match1 = soup1.find('a', {'title': 'Gen.lib.rus.ec'})['href']
    new4 = requests.get(match1, headers=headers)
    soup2 = bb(new4.text, 'lxml')
    latest = web2 + soup2.h2.a['href']
    wb.open_new(latest)


def site2():
    s = 1
    q = ''
    e = {}
    j = ''
    t = 0
    test = 9
    backdir9 = os.getcwd()
    fine = backdir9 + '\\Data\\name.txt'
    fine1 = backdir9 + '\\Data\\count.txt'
    with open(fine, 'r+') as (f):
        f.truncate()
    with open(fine1, 'r+') as (f):
        f.truncate()
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    popup.lead2()
    with open(fine, 'r+') as (f):
        j = f.read()
        f.seek(0)
        f.truncate()
    book = j
    name = book.replace(' ', '+')
    web = 'http://www.ebook777.com'
    r = requests.get(('http://www.ebook777.com/?s=' + name), headers=headers)
    soup = bb(r.text, 'lxml')
    match = soup.findAll('div', class_='content')
    x = 1
    for a in match:
        g = a.find('a', {'class': 'title'}).text
        o = a.find('a', {'class': 'title'})['href']
        e[g] = o

    with open(fine, 'r+') as (f):
        for a in e.keys():
            m = str(x)
            f.write(m + '.  ' + a + '\n\n')
            x += 1

    os.startfile(fine)
    popup.lead3()
    with open(fine1, 'r+') as (f):
        t = int(f.readline())
        f.truncate()
    for d in e.keys():
        if s == t:
            q = d
            test = 10
        s += 1

    if test == 10:
        new = e[q]
        newr = requests.get(new, headers)
        soup1 = bb(newr.text, 'lxml')
        match1 = soup1.find('span', class_='download-links')
        match2 = match1.find('a')['href']
        wb.open_new(match2)


B1 = Button(aryan, command=(lambda : threading.Thread(target=site1).start()), image=BU, highlightthickness=0, bd=0)
B1.place(x=50, y=60)
B2 = Button(aryan, command=(lambda : threading.Thread(target=site2).start()), image=BU2, highlightthickness=0, bd=0)
B2.place(x=50, y=117)
aryan.mainloop()