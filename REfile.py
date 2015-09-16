from Tkinter import Tk, Text, BOTH, W, N, E, S, IntVar
from ttk import Frame, Button, Label, Style, Checkbutton
from ttk import Entry
import subprocess
import os
from subprocess import Popen, PIPE
from Tkinter import *
import os.path


class fileExplorer(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        #Determines which checkbox is active.
        self.option = 0
        
        #Setup window.
        self.parent.title("REA5PE")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
		
        #Create label
        lbl = Label(self, text="Select the format PE file.")
        lbl.grid(sticky=W)
		
        #Create checkbox 1
        self.var = IntVar()
        cb = Checkbutton(self, text="Show .txt",
        variable=self.var, command=self.onClick)
        cb.grid(row=1, column=0, sticky=W)
        
        #Create checkbox 2
        self.var2 = IntVar()
        cb2 = Checkbutton(self, text="Show Console",
        variable=self.var2, command=self.onClick2)
        cb2.grid(row=2, column=0, sticky=W)
        
        #Entry form
        self.e1 = Entry(self)
        self.e1.grid(row=3, column=0)
        self.e1.focus_set() #Currently owns focus
   
        #Submission
        abtn = Button(self, text="Disassemble", command=self.onClickDisassemble)
        abtn.grid(row=4, column=0, sticky=W+E)
        
        
     #checkbox1
    def onClick(self):
       
        if self.var.get() == 1:
            self.option+=1 
        else:
            self.option-=1
            
	#checkbox2		
    def onClick2(self):
       
        if self.var2.get() == 1:
            self.option+=2
        else:
            self.option-=2
                
   
    #Disassemble button
    def onClickDisassemble(self):
        #Grab the string from the entry field.
        print "Attempting to launch file: " + self.e1.get()
        decoded = self.e1.get()
        
        if(os.path.isfile(self.e1.get())==True):
            #Launch the process.
            process = Popen(["xed.exe", "-i", decoded], stdout=PIPE)
            (output, err) = process.communicate()
            exit_code = process.wait()
        else:
            print "File does not exist. Terminating application."
            sys.exit()
        
        #Save to file.
        print "Saving to file...."
        fx = open('xeddumptext.txt', 'w')
        fx.write(output)
        fx.close()
        fb = open('xeddumpbinary.txt', 'wb')
        fb.write(output)
        fb.close()
        print "done"
        
        if(self.option==0):
            print "No selection. Please choose a section."
        elif(self.option==1):
            print "Displaying text section only."
            self.extractText();
        elif(self.option==2):
            print "Displaying Console section only."
            self.extractConsole();
        elif(self.option==3):
            print "Displaying both sections."
            self.extractText();
            self.extractConsole();
        else:
            print "Unknown error."
            
    def extractText(self):
        # create child window
        win = Toplevel()
        # display message
        message = "Assembly Dump for .text section"
        Label(win, text=message).pack()
        self.scrollbar = Scrollbar(win)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.T = Text(win, height=20, width=100)
        self.T.pack()
        self.scrollbar.config(command=self.T.yview)
        
        #Fill out the window with the data.
        with open("xeddumpbinary.txt") as input_data:
            for line in input_data:
                if line.strip() == '# IA32 format':
                    break
                #Reads text until the end of the block.
            for line in input_data: #keep reading
                if line.strip() == '# end of text section.':
                    break
                self.T.insert(END, line)
        message2 = "Search:"
        Label(win,text=message2).pack()
        self.es = Entry(win)
        self.es.pack()
        self.es.focus_set()

        Button(win, text='OK', command=self.searchTerm).pack()
        
    def searchTerm(self):
        self.T.tag_remove('search', '1.0', END)
        s = self.es.get()
        if s:
            idx = '1.0'
            while 1:
                idx = self.T.search(s, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                self.T.tag_add('search', idx, lastidx)
                idx = lastidx
            self.T.tag_config("search", foreground="red")
        self.es.focus_set()       
        
    def extractConsole(self):
       # create child window
       win2 = Toplevel()
       # display message
       message = "Dump for Console"
       Label(win2, text=message).pack()
       self.scrollbarc = Scrollbar(win2)
       self.scrollbarc.pack(side=RIGHT, fill=Y)
       self.T2 = Text(win2, height=20, width=100, yscrollcommand=self.scrollbarc.set)
       self.T2.pack()
       
       self.scrollbarc.config(command=self.T2.yview)
       # quit child window and return to root window
       # the button is optional here, simply use the corner x of the child window
       with open('xeddumpbinary.txt') as input_datac:
            for line in input_datac:
                if line.strip() == '# end of text section.':
                    break
                #Reads text until the end of the block.
            for line in input_datac: #keep reading
                self.T2.insert(END, line)
       Button(win2, text='OK', command=win2.destroy).pack()
 
                     #Insert into window here.
    
 
              

def main():
  
    root = Tk()
    root.geometry("200x150+900+250")
    app = fileExplorer(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  