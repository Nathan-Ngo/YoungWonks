#Social Media Application by Nathan Ngo
#Started on 19/9/21
#Finished on 22/9/21
##from tkinter import *
##import webbrowser
##root = Tk()
##root.title("Social Media Application")
##
##smd = {"Facebook":"None", "Snapchat":"None", "Instagram":"None", "Twitter":"Hyperonixus"}
##
##def showTagFacebook():
##    webbrowser.open_new_tab('www.facebook.com')
##
##def showTagSnapchat():
##    webbrowser.open_new_tab('www.snapchat.com')
##
##def showTagInstagram():
##    webbrowser.open_new_tab('www.instagram.com')
##
##def showTagTwitter():
##    webbrowser.open_new_tab('www.twitter.com')
##fB = Button(root, text = "Facebook", bg = "blue", fg = "white", command = showTagFacebook).grid(row=0, column=0)
##sB = Button(root, text = "Snapchat", bg = "yellow", fg = "black", command = showTagSnapchat).grid(row=0, column=1)
##iB = Button(root, text = "Instagram", bg = "orange", fg = "white", command = showTagInstagram).grid(row=1,column=0)
##tB = Button(root, text= "Twitter", bg = "#add8e6", fg = "black", command = showTagTwitter).grid(row=1, column=1)
##nL = Label(root, text = "test").grid(row=2, column = 0, columnspan=2)
##
##
##       
##root.mainloop()

from tkinter import *
import webbrowser

class SocialMediaApplication():
    def __init__(self, master):
        self.master = master

        self.smd = {"Facebook":"nathan1", "Snapchat":"nathan2", "Instagram":"nathan3", "Twitter":"nathan4", "Prawnhub":"totallynotathrowaway69420"}

        self.smdL = Label(self.master, text = "Social Media Application")
        self.smdL.grid(row=0, column=0, columnspan=2)

        self.fB = Button(self.master, text = "Facebook", bg = "#3b5998", fg = "white", command = self.showTagFacebook)
        self.fB.grid(row=1, column=0, sticky=NW, padx=2, pady=2)

        self.sB = Button(self.master, text = "Snapchat", bg = "#FFFC00", fg = "black", command = self.showTagSnapchat)
        self.sB.grid(row=1, column=1, sticky=NE, padx=2, pady=2)

        self.iB = Button(self.master, text = "Instagram", bg = "#E1306C", fg = "white", command = self.showTagInstagram)
        self.iB.grid(row=2, column=0, sticky=SW, padx=2, pady=2)

        self.tB = Button(self.master, text = "  Twitter  ", bg = "#55acee", fg = "black", command = self.showTagTwitter)
        self.tB.grid(row=2, column=1, sticky=SE, padx=2, pady=2)

        self.pL = Button(self.master, text = "Prawnhub", bg = "#ff748c", fg = "white", command = self.showTagPrawnhub)
        self.pL.grid(row=3, column=0, sticky=SW, padx=2, pady=2)

        self.nL = Label(self.master, text = "Please pick a button for the username!")
        self.nL.grid(row=4,column=0,columnspan=2)
 

        self.lM = None

    def showTagFacebook(self):
        webbrowser.open_new_tab('www.facebook.com')
        print("Facebook Username:", self.smd['Facebook'])
        self.lM = "Facebook Username: " + self.smd['Facebook']
        self.nL['text'] = self.lM
    def showTagSnapchat(self):
        webbrowser.open_new_tab('www.snapchat.com')
        print("Snapchat Username:", self.smd['Snapchat'])
        self.lM = "Snapchat Username: " + self.smd['Snapchat']
        self.nL['text'] = self.lM
    def showTagInstagram(self):
        webbrowser.open_new_tab('www.instagram.com')
        print("Instagram Username:", self.smd['Instagram'])
        self.lM = "Instagram Username: " + self.smd['Instagram']
        self.nL['text'] = self.lM
    def showTagTwitter(self):
        webbrowser.open_new_tab('www.twitter.com')
        print("Twitter Username:", self.smd['Twitter'])
        self.lM = "Twitter Username: " + self.smd['Twitter']
        self.nL['text'] = self.lM
    def showTagPrawnhub(self):
        webbrowser.open_new_tab('http://www.geocities.ws/travis/Prawnhub/Home.html')
        print("Prawnhub Username:", self.smd['Prawnhub'])
        self.lM = "Prawnhub Username: " + self.smd['Prawnhub']
        self.nL['text'] = self.lM
    

root = Tk()
GUI = SocialMediaApplication(root)
root.mainloop()
