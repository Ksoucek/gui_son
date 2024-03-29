import json
import subprocess
import ctypes
import tkinter as Tk
from tkinter import ttk
from tkinter import scrolledtext
#Import modulů

#definice akcí
def OpenJson(Path):
    subprocess.call(['notepad.exe', Path])
    
def UnscheduleTask(command):
    result = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", "powershell", command, None, 0)
    if result <= 32:
        raise Exception("Failed to run as admin")
def RunTaskNow(command):
    result = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", "powershell", command, None, 0)
    if result <= 32:
        raise Exception("Failed to run as admin")


def ScheduleTask(command):
    result = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", "powershell", command, None, 0)
    if result <= 32:
        raise Exception("Failed to run as admin")

#Uložení dat do jsonu
def enter_data():
    Instance = Deployment_Instance_entry.get()
    TaskTime = task_time_entry.get()
    UserID = user_id_entry.get()
    TaskName = TaskName_entry.get()

    EmailBoolBeforestr = NewEmailBoolBefore.get() in ("true", "False")
    EmailBoolAfterstr = NewEmailBoolAfter.get() in ("true", "False")

    EmailFrom = Email_From_entry.get()
    EmailFromPW = AplicationPW_Entry.get()
    EmailTo = Email_to_Entry.get("1.0",'end-1c')
    SendEmailToMyself = NewSendEmailToMyself.get() in ("true", "False")


    Subject = Subject_entry.get()
    Body = Body_entry.get("1.0",'end')
    ReleasedFeatures = ReleasedFeatures_entry.get("1.0",'end-1c')

    if Instance and TaskTime:
        PATH_TO_JSON: str = r'C:\NTC\Settings.JSON'
        with open(PATH_TO_JSON, 'r', encoding='utf-8') as f:
         json_content = json.load(f)
         json_content['$DeploymentInstance'] = Instance
         json_content['$TaskTime'] = TaskTime
         json_content['$UserID'] = UserID
         json_content['$TaskName'] = TaskName

         json_content['$SentEmailBefore'] =  EmailBoolBeforestr
         json_content['$SentEmailAfter'] = EmailBoolAfterstr

         json_content['$EmailFrom'] = EmailFrom
         json_content['$EmailFromPW'] = EmailFromPW
         json_content['$EmailTo'] = EmailTo
         json_content['$SendEmailToMyself'] = SendEmailToMyself

         json_content['$Subject'] = Subject
         json_content['$Body'] = Body
         json_content['$ReleasedFeatures'] = ReleasedFeatures

        with open(PATH_TO_JSON, 'w') as f:
            json.dump(json_content, f, indent=4)

    else:
        Tk.messagebox.showwarning(title="Error", message="Instance a čas jsou povinné údaje.")



window = Tk.Tk()
window.title("Nastavení parametrů releasu")

#Načtení dat  do proměných z JSONu

PATH_TO_JSON: str = r'C:\NTC\Settings.JSON'
with open(PATH_TO_JSON, 'r', encoding='utf-8') as f:
    json_content = json.load(f)

    OldTaskName = json_content['$TaskName']
    OldTaskTime =   json_content['$TaskTime']
    OldReleasedFeatures =   json_content['$ReleasedFeatures']
    OldEmailFrom : str =   json_content['$EmailFrom']
    OldEmailFromPW : str =   json_content['$EmailFromPW']
    OldEmailTo : str =   json_content['$EmailTo']
    OldSubject : str =   json_content['$Subject']
    OldSubjectFinish : str =   json_content['$SubjectFinish']
    OldBody : str =   json_content['$Body']
    OldBodyFinish : str =   json_content['$BodyFinish']
    OldDeploymentInstance = json_content['$DeploymentInstance']
    OldEmailBoolBefore : str =   json_content['$SentEmailBefore'] 
    OldEmailBoolAfter : str =   json_content['$SentEmailAfter'] 
    OldUserID : str =   json_content['$UserID']
    OldSendEmailToMyself : str =   json_content['$SendEmailToMyself'] 


#vytvoření okno prostředí
frame = Tk.Frame(window)
frame.pack()
#definice proměnných
OldString1 = Tk.StringVar()
Oldstring2 = Tk.StringVar()
OldString3 = Tk.StringVar()
OldString4 = Tk.StringVar()
OldString5 = Tk.StringVar()
OldString6 = Tk.StringVar()
OldString7 = Tk.StringVar()
OldString8 = Tk.StringVar()
OldString9 = Tk.StringVar()
OldString10 = Tk.StringVar()

# Nastavení releaseu
System_Frame =Tk.LabelFrame(frame, text="Release nastavení")
System_Frame.grid(row= 0, column=0, padx=20, pady=10)


OldString1.set(OldDeploymentInstance)
Deployment_Instance = Tk.Label(System_Frame, text="Deployment Instance")
Deployment_Instance.grid(row=0, column=0)
Deployment_Instance_entry = ttk.Entry(System_Frame,textvariable = OldString1)
Deployment_Instance_entry.grid(row=1, column=0)

Oldstring2.set(OldTaskTime)
TaskTimeLbl = Tk.Label(System_Frame, text="Čas spuštění")
TaskTimeLbl.grid(row=0, column=1)
task_time_entry = Tk.Entry(System_Frame,textvariable = Oldstring2)
task_time_entry.grid(row=1, column=1)

OldString3.set(OldUserID)
UserIDLbl = Tk.Label(System_Frame, text="USER ID")
UserIDLbl.grid(row=0, column=2)
user_id_entry = Tk.Entry(System_Frame,textvariable = OldString3)
user_id_entry.grid(row=1, column=2)

OldString6.set(OldTaskName)
TaskNameLbl = Tk.Label(System_Frame, text="Název tasku")
TaskNameLbl.grid(row=0, column=3)
TaskName_entry = Tk.Entry(System_Frame,textvariable = OldString6)
TaskName_entry.grid(row=1, column=3)


for widget in System_Frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# Nastavení Email
Email_Frame = Tk.LabelFrame(frame, text="Nastavení emailů k releasu")
Email_Frame.grid(row=2, column=0, padx=20, pady=15)

NewEmailBoolBefore = Tk.StringVar()
Sent_before_entry = Tk.Checkbutton(Email_Frame, text= "Odeslat email před nasazením.",
                                  variable=NewEmailBoolBefore, onvalue="true", offvalue="false")
Sent_before_entry.grid(row=0, column=0)

if OldEmailBoolBefore :
    Sent_before_entry.select()
else:
    Sent_before_entry.deselect()

NewEmailBoolAfter = Tk.StringVar()
Sent_After_entry = Tk.Checkbutton(Email_Frame, text= "Odeslat email po nasazení.",
                                  variable=NewEmailBoolAfter, onvalue="true", offvalue="false")
Sent_After_entry.grid(row=0, column=2)

if OldEmailBoolAfter :
    Sent_After_entry.select()
else:
    Sent_After_entry.deselect()


OldString4.set(OldEmailFrom)
EmailFromLbl = Tk.Label(Email_Frame, text="Odesilatel Mailu")
Email_From_entry = ttk.Combobox(Email_Frame, values=["jakub.soucek@navitec.cz", "daniel.barnet@navitec.cz"],textvariable = OldString4)
EmailFromLbl.grid(row=2, column=0)
Email_From_entry.grid(row=3, column=0)

OldString5.set(OldEmailFromPW)
AplicationPW = Tk.Label(Email_Frame, text="Aplikační heslo Mailu")
AplicationPW_Entry = Tk.Entry(Email_Frame, show="*", textvariable = OldString5)
AplicationPW.grid(row=2, column=1)
AplicationPW_Entry.grid(row=3, column=1)


NewSendEmailToMyself = Tk.StringVar()
SendEmailToMyself_entry = Tk.Checkbutton(Email_Frame, text= "Odeslat emaily jen sobě",
                                  variable=NewSendEmailToMyself, onvalue="true", offvalue="false")
SendEmailToMyself_entry.grid(row=3, column=2)

if OldSendEmailToMyself  :
    SendEmailToMyself_entry.select()
else:
    SendEmailToMyself_entry.deselect()

OldString7.set(OldEmailTo)
OldEmailTo = Tk.Label(Email_Frame, text="Seznam příjemců")
OldEmailTo.grid(row=6, column=1, sticky='we')
Email_to_Entry = scrolledtext.ScrolledText(Email_Frame,
                                      wrap = Tk.WORD,
                                      width = 170,
                                      height = 1,
                                      font = ("Times New Roman",
                                              10))
Email_to_Entry.insert(Tk.INSERT,OldString7.get())
Email_to_Entry.grid(column = 0, pady = 10, padx = 10, sticky='w',columnspan=3)


OldString8.set(OldSubject)
SubjectLbl = Tk.Label(Email_Frame, text="Předmět mailu")
SubjectLbl.grid(row=4, column=0, sticky='nsew', padx = 10, pady=10, columnspan= 170)
Subject_entry = Tk.Entry(Email_Frame,textvariable = OldString8)
Subject_entry.grid(row=5, column=0,sticky='nsew', padx = 10, pady=10, columnspan= 170)

OldString9.set(OldBody)
OldBody = Tk.Label(Email_Frame, text="Tělo Mailu")
OldBody.grid(row=8, column=1, sticky='we')
Body_entry = scrolledtext.ScrolledText(Email_Frame,
                                      wrap = Tk.WORD,
                                      width = 170,
                                      height = 1,
                                      font = ("Times New Roman",
                                              10))
Body_entry.insert(Tk.INSERT,OldString9.get())
Body_entry.grid(column = 0, pady = 10, padx = 10, sticky='w',columnspan=3)

OldString10.set(OldReleasedFeatures)
OldReleasedFeatures = Tk.Label(Email_Frame, text="Seznam Požadavků")
OldReleasedFeatures.grid(row=10, column=1, sticky='we',rowspan=5)
ReleasedFeatures_entry = scrolledtext.ScrolledText(Email_Frame,
                                      wrap = Tk.WORD,
                                      width = 170,
                                      height = 1,
                                      font = ("Times New Roman",
                                              10))
ReleasedFeatures_entry.insert(Tk.INSERT,OldString10.get())
ReleasedFeatures_entry.grid(column = 0, pady = 10, padx = 10, sticky='w',columnspan=3,rowspan=5)

# tlačítka a akce
button1 = Tk.Button(frame, text="Uložit JSON", command= enter_data)
button1.grid(row=16, column=0, sticky="news", padx=20, pady=10)

button4 = Tk.Button(frame, text="Otevři JSON", command=  lambda : OpenJson("C:\\NTC\\Settings.json"))
button4.grid(row=18, column=0, sticky="news", padx=20, pady=10)

button2 = Tk.Button(frame, text="Spustit timer ", command= lambda : ScheduleTask("C:\\NTC\\ScheduledTaskRealease.ps1"))
button2.grid(row=20, column=0, sticky="news", padx=20, pady=10)

button3 = Tk.Button(frame, text="Zrušit timer ", command=  lambda : UnscheduleTask("C:\\NTC\\UnscheduleTask.ps1"))
button3.grid(row=22, column=0, sticky="news", padx=20, pady=10)

button5 = Tk.Button(frame, text="Spustit release hned ", command=  lambda : RunTaskNow("C:\\NTC\\ReleaseAndNotificationNow.ps1"))
button5.grid(row=24, column=0, sticky="news", padx=20, pady=10)


window.mainloop()