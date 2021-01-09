'''
RAM_Usage : 0 Parameters. Displays RAM USAGE
Current_Processes : 1 integer Parameter(n). Shows n highest memory processes
Kill_Process : 1 integer Parameter(n). Kills the Process with Process ID = n
'''
from tabulate import tabulate
import psutil
import time
import sys


def RAM_Usage():
    a= psutil.virtual_memory()
    Mem_Columns = ["Total Memory (in GB)","Available Memory (in GB)","Percentage Usage","Used Memory (in GB)"]
    a = [[a[0]/1024**3,a[1]/1024**3,a[2],a[3]/1024**3]]
    print("\n\n")
    print(tabulate(a,headers=Mem_Columns,tablefmt='grid'))
    print("\n\n")
    

def Current_Processes(number):
    x = 0
    listOfProcess = []
    ProcessCols = ["Process ID","Process Name","Status","Memory Usage (in MBs)"]
    for i in psutil.process_iter():
        listOfProcess.append([i.pid,i.name(),i.status(),i.memory_info()[0]/1024**2])
        
    for i in range(len(listOfProcess)):
        listOfProcess[i] = listOfProcess[i][::-1]
    listOfProcess.sort(reverse=True)
    for i in range(len(listOfProcess)):
        listOfProcess[i] = listOfProcess[i][::-1]
    listOfProcess = listOfProcess[:number]
    
    print("\n\n")
    print("Top {} processes with Highest Memory Usage\n\n".format(number))
    print(tabulate(listOfProcess,headers=ProcessCols,tablefmt='grid'))
    print("\n\n")
    
def Kill_Process(PID):
    p = psutil.Process(PID)
    print("\n\n{} is closed\n\n".format(p.name()))
    p.terminate()

def Main():
    Codes = [[1,"Show RAM Usage"],[2,"Show Current Processes"],[3,"Kill Process by ProcessID"],[0,"Close Task Manager"]]
    while True:
        print("\n\n")
        print(tabulate(Codes,headers=["Code","Function"],tablefmt='grid'))
        print("\n\n")

        x = int(input("Enter the Code for desired operation\n\n"))
        if x==1:
            RAM_Usage()
        if x==2:
            n = int(input("\n\nEnter Number of Processes to See\n\n"))
            Current_Processes(n)
        if x==3:
            n = int(input("\n\nEnter Process ID of the Process to close\n\n"))
            Kill_Process(n)
        if x==0:
            break
            
Main()
