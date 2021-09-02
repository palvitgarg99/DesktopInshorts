import json
import requests
import time as tt
from tkinter import *
from tkinter import ttk

api_url = "https://inshortsv2.vercel.app/news?type="


def check_api():
    response = requests.get((api_url + "trending"))
    return response.status_code


def request_data():
    response = requests.get(api_url + "trending")
    return json.loads(response.text)


def update_data(category):
    global data
    response = requests.get(api_url + str(category))
    data = json.loads(response.text)
    print(data['total'], "pp")


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Inshorts News")
        self.minsize(1000, 1000)

    def quit(self):
        self.destroy()


lst = []


def OnButtonClick(id):
    update_data(id)
    print(data['total'])
    for i in lst:
        i.destroy()
    lst.clear()
    for i in range(data['total']):
        label1 = Label(fram2, text=data['articles'][i]['title'])
        label2 = Label(fram2, text=data['articles'][i]['description'], anchor=CENTER, relief="solid", width=100,
                       wraplength=700)
        label1.pack()
        label2.pack()
        lst.append(label1)
        lst.append(label2)
        if i == 8:
            break


if __name__ == '__main__':
    # print(check_api())
    data = request_data()
    root = Root()
    frame = Frame(root)
    frame.pack()

    var = StringVar()
    var.set(data['articles'][0]['title'])

    panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)
    fram1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
    fram2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)
    panedwindow.add(fram1, weight=1)
    panedwindow.add(fram2, weight=4)

    for i in range(data['total']):
        label1 = Label(fram2, text=data['articles'][i]['title'])
        label2 = Label(fram2, text=data['articles'][i]['description'], anchor=CENTER, relief="solid", width=100,
                       wraplength=700)
        label1.pack()
        label2.pack()
        lst.append(label1)
        lst.append(label2)
        if i == 8:
            break
    button = Button(fram1, text="trending", command=lambda: OnButtonClick("trending"), height=2, width=20)
    button.pack(side=TOP)
    button = Button(fram1, text="top_stories", command=lambda: OnButtonClick("top_stories"), height=2, width=20)
    button.pack(side=TOP)
    button = Button(fram1, text="national", command=lambda: OnButtonClick("national"), height=2, width=20)
    button.pack(side=TOP)
    button = Button(fram1, text="business", command=lambda: OnButtonClick("business"), height=2, width=20)
    button.pack(side=TOP)
    button = Button(fram1, text="sports", command=lambda: OnButtonClick("sports"), height=2, width=20)
    button.pack(side=TOP)
    root.mainloop()
