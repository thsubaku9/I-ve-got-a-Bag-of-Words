import tkinter
import _pickle as cp

#datatypes and variables

fl=[];lvalue=[];llc=[];lll=[];seachq=''
fileList = [] #refresh continuously
CollectionTerms = {}
stopWords = cp.load(open('stopWords.p', "rb"))
#
class File:    
    def parsecontent(self, file):
        with open(file) as f:
            for line in f:
                temp1 = line.split()
                for i in temp1:
                    if i not in stopWords:
                        self.content.append(i.strip('!?.,—:;"').lower())


    def createlist(self):
        for j in self.content:
            try:
                self.postingLists[j].append(self.distance)
            except KeyError:
                self.postingLists[j] = [self.distance]
            self.distance += 1

    
    def __init__(self, file):
        self.distance = int(0)  # Distance from the first word. Index starts at zero.
        self.content = []  # List of all words.
        self.postingLists = {}  # Dictionary of all posting lists
        self.parsecontent(file)
        self.createlist()


#the function part
def selectfile():
    global fl
    global lvalue
    global llc
    global lll
    fl=tkinter.filedialog.askopenfilenames()
    for x in range(0,len(fl)):
        a=fl[x].split('/')
        a=a[-1]
        var=tkinter.IntVar()
        ttemp=tkinter.Label(root,text=a)
        tch=tkinter.Checkbutton(root,variable=var)
        ttemp.grid(column=0,row=x)
        tch.grid(column=2,row=x)
        lll+=[ttemp]
        lvalue+=[var]
        llc+=[tch]
def boolandsearch():
    txt.grid(column=10,row=int(len(fl)/2))
def ultii():
    global lvalue
    global fl
    global fileList        
    root2=tkinter.Tk()
    root2.geometry("400x400")
    scr=tkinter.Scrollbar(root2)
    scr.pack( side = 'right', fill = 'y' )
    mylist = tkinter.Listbox(root2, yscrollcommand = scr.set,width=400 )
    mylist.pack( side = 'left', fill = 'both' )
    #displaying the result from selected files
    for x in range(0,len(lvalue)):        
        fileList=[]
        if (lvalue[x]==1):
            fileList.append(fl[x])  #have taken in values for reading
    for item in fileList:
        fileName=item.split('/')
        fileName=fileName[-1]
        fileName = item.strip('.txt')                                                        
        inObj = File(item)
        for i in inObj.postingLists:
            try:
                CollectionTerms[i].append((fileName, inObj.postingLists[i]))
            except KeyError:
                CollectionTerms[i] = []
                CollectionTerms[i].append((fileName, inObj.postingLists[i]))
    for term in CollectionTerms:
        aghh='';aghh+=term;aghh+=" ";aghh+=CollectionTerms.get(term)
        mylist.insert('end',aghh)
    #
    
    scr.config( command = mylist.yview )
    
###
root=tkinter.Tk();root.geometry("500x500");root.resizable(width=False,height=False)
root.title("Boolean Retrieval Model")
Mmenu=tkinter.Menu(root);root.config(menu=Mmenu)
subm=tkinter.Menu(Mmenu)
Mmenu.add_cascade(label="Select files",menu=subm)
subm.add_command(label="Open",command=selectfile)
subm.add_separator()
subm.add_command(label="AND operation",command=boolandsearch)
#b1 command needs to be checked
b1=tkinter.Button(root,text='inverted index result',command=ultii)
b1.grid(column=0,row=10,columnspan=10)
#b2=tkinter.Button(root,text="AND result",command=andresult)
#b2.pack(fill='both')
txt=tkinter.Text(root,height=1,width=20)
'''
#use this for search and operation
searchq=txt.get('1.0','end-1c')
qlist=searchq.split(' ')
'''
root.mainloop()

        
    
