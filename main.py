from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.title("Text Editor")

def openDoc():

    def openDoc_():
        placeHolder.delete(0, tk.END)
        textEntry.delete("1.0", tk.END)
        fileNameEntry.delete(0, tk.END)
        
        filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("Text Files","*.txt"),("all files","*.*")))

        with open(filename, "r") as f:
            data = f.read()

        filelist = filename.split("/")
        filename2 = filelist[-1]
        filename2 = filename2[:-4]
        
        fileNameEntry.insert(0, filename2)

        textEntry.insert("1.0", data)

        placeHolder.insert(0, filename)

    if textEntry.get("1.0", "end-1c") != "":
        def noSave():
            saveAsk.destroy()
            openDoc_()

        def yesSave():
            saveAsk.destroy()
            saveDoc()
            openDoc_()
        
        saveAsk = tk.Tk()
        saveAsk.title("Save?")
        tk.Label(saveAsk, text="Do you want to save?").grid(row=0, column=0, columnspan=2)
        tk.Button(saveAsk, text='Yes', command=yesSave).grid(row=1, column=0)
        tk.Button(saveAsk, text="No", command=noSave).grid(row=1, column=1)
        saveAsk.mainloop()
    else:
        openDoc_()

def saveDoc():
    if placeHolder.get() != "":
        filename = placeHolder.get()

        fs =  open(filename, "w")
        fs.write(textEntry.get("1.0", "end-1c"))
        fs.close()
    else:
        fs = filedialog.asksaveasfile(mode='w', title="Save File", initialfile=fileNameEntry.get(), defaultextension=".txt", filetypes = (("Text Files","*.txt"),("all files","*.*")))
        fs.write(textEntry.get("1.0", "end-1c"))
        fs.close()
        
        placeHolder.delete(0, tk.END)
        placeHolder.insert(0, fs.name)

        filelist = fs.name.split("/")
        filename2 = filelist[-1]
        filename2 = filename2[:-4]
        
        fileNameEntry.delete(0, tk.END)
        fileNameEntry.insert(0, filename2)

def on_closing():
    def closer():
            def saveClose():
                closePrompt.destroy()
                saveDoc()
                root.destroy()
            
            def noSaveClose():
                closePrompt.destroy()
                root.destroy()

            closePrompt = tk.Tk()
            closePrompt.title("Close")
            tk.Label(closePrompt, text="Do you want to save?").grid(row=0, column=0, columnspan=2)
            tk.Button(closePrompt, text="Yes", command=saveClose).grid(row=1, column=0)
            tk.Button(closePrompt, text="No", command=noSaveClose).grid(row=1, column=1)
            closePrompt.mainloop()

    if placeHolder.get() != "":
        try:
            with open(placeHolder.get(), "r") as fsc:
                data_c = fsc.read()
        except:
            pass

        if textEntry.get("1.0", "end-1c") != data_c:
            closer()
        else:
            root.destroy()
    elif textEntry.get("1.0", "end-1c") != "":
            closer()
    else:
        root.destroy()

fileNameEntry = tk.Entry(root)
textEntry = tk.Text(root)
openButton = tk.Button(root, text="Open", command=openDoc)
saveButton = tk.Button(root, text="Save", command=saveDoc)
placeHolder = tk.Entry(root)

fileNameEntry.grid(row=0, column=2, pady=5)
openButton.grid(row=0, column=1)
saveButton.grid(row=0, column=3)
textEntry.grid(row=1, column=0, columnspan=5)

fileNameEntry.insert(0, "New Text Document")

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()