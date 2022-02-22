from pathlib import Path
import pathlib
import PySimpleGUI as sg
from tkinter import Tk, filedialog
import subprocess, os
import shutil

root = Tk() 
root.withdraw() 
root.attributes('-topmost', True)

layout = [ [sg.Text("NDS to CIA")], [sg.Button("Choose Folders")],[sg.Multiline(size=(30,5), key='textbox')] ]
window = sg.Window("NDS2CIA", layout,default_element_size=(12, 1),resizable=True,finalize=True)
while True:
    event, values = window.read()
    window['textbox'].update("Please select input and output folders!")
    if event == "Choose Folders":
        Source = filedialog.askdirectory()
        print(Source)
        Dest = filedialog.askdirectory()
        print(Dest)
        p=Path(Source)
        print(p)
        b=list(p.glob("**/*.nds"))
        print(b)
        p_d=Path(Dest)
        for i in b:
            RealPath=str(i)
            #print(RealPath)
            #print(str(p_d)+"\\"+i.stem+".cia")
            window['textbox'].update(window['textbox'].get()+"Converting "+i.name)
            print('--srl="'+RealPath+'" -o "'+str(p_d)+'\\'+i.stem+'.cia"')
            subprocess.run(['make_cia.exe', '--srl='+RealPath])
            print('"'+str(p)+'\\'+i.stem+'.cia"')
            try:
                os.remove(str(p)+'\\'+i.stem+'.cia')
            except OSError:
                pass
            else:    
                shutil.move(str(p)+'\\'+i.stem+'.cia', str(p_d))
            window['textbox'].update(window['textbox'].get()+i.name+" Done!")

    
    if event == sg.WIN_CLOSED:
        break


