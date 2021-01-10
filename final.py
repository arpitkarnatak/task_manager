from tabulate import tabulate
import psutil
import speedtest 

def RAM_Usage():
    a= psutil.virtual_memory()
    Mem_Columns = ["Total Memory (in GB)","Available Memory (in GB)","Percentage Usage","Used Memory (in GB)"]
    
    ### psutil.virtual_memory() gives disk usage in bytes, so convert it to Gigabytes
    a = [[a[0]/1024**3,a[1]/1024**3,a[2],a[3]/1024**3]]
    print("\n\n")
    
    ## tabulate function to display data in a tabular format
    print(tabulate(a,headers=Mem_Columns,tablefmt='grid'))
    print("\n\n")
    

def Current_Processes(number):
    x = 0
    listOfProcess = []
    ProcessCols = ["Process ID","Process Name","Status","Memory Usage (in MBs)"]
    
    ### psutil.process_iter() gives the list of all processes
    for i in psutil.process_iter():
        listOfProcess.append([i.pid,i.name(),i.status(),i.memory_info()[0]/1024**2])
        
    for i in range(len(listOfProcess)):
        listOfProcess[i] = listOfProcess[i][::-1]
    ## Sorting the processes by Memory Usage
    listOfProcess.sort(reverse=True)
    for i in range(len(listOfProcess)):
        listOfProcess[i] = listOfProcess[i][::-1]
        
    ## Displaying only the given number of processes
    listOfProcess = listOfProcess[:number]
    
    print("\n\n")
    print("Top {} processes with Highest Memory Usage\n\n".format(number))
    print(tabulate(listOfProcess,headers=ProcessCols,tablefmt='grid'))
    print("\n\n")
    
    
def Kill_Process(PID):
    p = psutil.Process(PID)
    p.terminate()

    
def WiFi():
    st = speedtest.Speedtest() 
    data = [["Download Speed (in MBps)",st.download()/1024**2],["Upload Speed (in MBps)",st.upload()/1024**2]]
    print("\n\n")
    print("Internet Speed")
    print("\n\n")
    print(tabulate(data,tablefmt='grid'))
    print("\n\n")

def Main():
    Codes = [[1,"Show RAM Usage"],[2,"Show Current Processes"],[3,"Kill Process by ProcessID"],[4,"Connection Details"],[0,"Close Task Manager"]]
    while True:
        print("\n\n")
        print(tabulate(Codes,headers=["Code","Function"],tablefmt='grid'))
        print("\n\n")

        x = int(input())
        if x==1:
            RAM_Usage()
        if x==2:
            n = int(input("\n\nEnter Number of Processes to See\n\n"))
            Current_Processes(n)
        if x==3:
            n = int(input("\n\nEnter Process ID of the Process to close\n\n"))
            Kill_Process(n)
        if x==4:
            WiFi()
        if x==0:
            break
            
Main()
