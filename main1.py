import sys,os
import datetime
from typing import Counter



import matplotlib.pyplot as plt

#date = datetime.datetime(int(year), int(month), 1)

# GLOBAL VALUES
data=[]
dates=[]
names=[]
attendance={}
attendees={}

def input_csv():
    with open("data.csv", "r") as file:
        for line in file.readlines():
            data.append(line.split(","))
        del data[0]

def to_get_dates():
    for each in data:
        if each[0] not in dates:
            dates.append(each[0])

def to_get_names():

    for each in data:
        if each[2] not in names:
            names.append(each[2])





def to_get_dict():
    
    
    for eachh in dates:
        legnth_of_data_set=len(data)
        names1=[]
        names2=[]
        temp=0
        while temp<legnth_of_data_set:
            if eachh==data[temp][0] and data[temp][1].startswith('11'):
                names1.append(data[temp][2])
                names1=list(set(names1))
            elif eachh==data[temp][0] and data[temp][1].startswith('15'):
                names2.append(data[temp][2])
                names2=list(set(names2))
            temp+=1
        attendance[f'{eachh}']=[names1,names2]      
    
    return(attendance)

def search_by_name(name):
    try:
        counter, total_counter = 0, len(dates*2)
        for each in dates:
            for eachh in attendance[f'{each}']:
                for eachhh in eachh:
                    if name in eachhh:
                        counter+=1
                
            
        
        return counter
    except Exception as error:
        print("Something went wrong")
        print("Error" + str(error))
def overall_attendance():
     
    try:
        for each in names:
            count=0
            count=search_by_name(each)
            attendees[f'{each}']=count
        return attendees
    except Exception as error:
        print("Something went wrong")

def weekly_attendance():
    current_date = datetime.datetime.today()
    week_dates = []
    dated = []
    temp = 0

    # to get object of dates of last 7 days
    while temp < 7:
        previous_date = current_date - datetime.timedelta(days=temp)
        week_dates.append(previous_date)
        temp+=1

    #to convert datetime object into the correct format as required
    for each in week_dates:
        day = each.strftime("%A")
        if day != "Sunday" and day != "Saturday":
            formatted_time = each.strftime("%m/%d/%y")
            dated.append(str(formatted_time))
    
    for each in dated:
        try:
            print(attendance[f'{each}'])
        except Exception as error:
            print("No data Found" + str(error))
    return dated

def yearly_attendance():
    current_date = datetime.datetime.today()
    week_dates = []
    dated = []
    temp = 0

    # to get object of dates of last 365 days
    while temp < 365:
        previous_date = current_date - datetime.timedelta(days=temp)
        week_dates.append(previous_date)
        temp+=1

    #to convert datetime object into the correct format as required
    for each in week_dates:
        day = each.strftime("%A")
        if day != "Sunday" and day != "Saturday":
            formatted_time = each.strftime("%m/%d/%y")
            dated.append(str(formatted_time))
    
    for each in dated:
        try:
            print(attendance[f'{each}'])
        except Exception as error:
            print("No data found" + str(error))
    return(dated)

def monthly_attendance():
    current_date = datetime.datetime.today()
    week_dates = []
    dated = []
    temp = 0

    # to get object of dates of last 7 days
    while temp < 30:
        previous_date = current_date - datetime.timedelta(days=temp)
        week_dates.append(previous_date)
        temp+=1

    #to convert datetime object into the correct format as required
    for each in week_dates:
        day = each.strftime("%A")
        if day != "Sunday" and day != "Saturday":
            formatted_time = each.strftime("%m/%d/%y")
            dated.append(str(formatted_time))
    
    for each in dated:
        try:
            print(attendance[f'{each}'])
        except Exception as error:
            print("No data Found" + str(error))
    return(dated)


def visualize_bar_overall_attendance():
    x=[]
    y=[]
    for each in names:
        count=search_by_name(each)
        y.append(count)
        x.append(each)
    y.append((len(dates)*2))
    x.append('Total shifts')
    plt.barh(x, y)
    plt.title('TOTAL ATTENDANCE')
    plt.show()

def visualize_pie_graph_search_by_name(name):
    count=search_by_name(name)
    print(count)
    y = [len(dates*2),count]
    mylabels = [f"{name} {count}",f"overall attendance {len(dates*2)}"]

    plt.pie(y, labels = mylabels,  startangle = 0)
    plt.title('TOTAL ATTENDANCE OF A SINGLE PERSON')
    plt.show() 

def weekly_bar():
    weekly_attendees={}
    weekly_name=[]

    dated=weekly_attendance()
    for date in dated:
        for each_attendance in attendance[f'{date}']:
            for each in each_attendance:
                weekly_name.append(each)

    for each in names:
        counter=0
        counter=weekly_name.count(each)
        weekly_attendees[f'{each}']=counter
    y =list(weekly_attendees.values())

    x =list(weekly_attendees.keys())

    y.append(10)
    x.append('Total attendance')
    plt.barh(x,y, color='brown')
    plt.title('Total Weekly Attendance')
    plt.show()

def monthly_bar():
    monthly_attendees={}
    
    dated=monthly_attendance()
    for each in dated:
        
        for name in names:
            counter=6
            for eachh in attendance[f'{each}']:
                
                for eachhh in eachh:
                    
                    if name in eachhh:
                        counter+=1
                monthly_attendees[f'{name}']=counter

    y =list(monthly_attendees.values())

    x =list(monthly_attendees.keys())
    

    plt.barh(x,y)
    plt.title('TOTAL ATTENDANCE')
    plt.show()


def cli_conversion():
    while True:
        print('Do you want to continue: Y/N')
        print("For Attendance by name press 1")
        print("For total attendance press 2")
        print("For weekly attendance press 3")
        print("For monthly attendance press 4")
        print('For yearly attendance press 5')
        print('For overall attenadce graph press 6')
        print('For pie graph for person press 7')
        print('For weekly bar graph of week press 8')

        choice=int(input('Enter:  '))

        if choice ==1:
            name=input('Enter name:   ')
            counter=search_by_name(name)
            print("Searched name: " + name ,", " + str(counter) + "/" + str(len(dates)*2))
        elif choice ==2:
            print(overall_attendance())
        elif choice ==3:
            weekly_attendance()
        elif choice ==4:
            monthly_attendance()
        elif choice ==5:
            yearly_attendance()
        elif choice ==6:
            visualize_bar_overall_attendance()
        elif choice ==7:
            visualize_pie_graph_search_by_name(input('Enter name:   '))
        elif choice ==8:
            weekly_bar()
        else:
            print('wrong input')

        print('Do you want to continue: Y/N')
        to_continue=input('Enter:   ').capitalize()
        if to_continue=='N':
            break



# Driver code
if __name__ == '__main__':
    input_csv()
    to_get_dates()
    to_get_names()
    to_get_dict()
    # search_by_name('Ritesh')
    # overall_attendance()
    # weekly_attendance()
    #visualize_bar_weekly_attendance()
    #monthly_attendance()
    #yearly_attendance()
    cli_conversion()
    visualize_bar_overall_attendance()
    # visualize_pie_graph_search_by_name('XHunter')
    weekly_bar()
    monthly_bar()


