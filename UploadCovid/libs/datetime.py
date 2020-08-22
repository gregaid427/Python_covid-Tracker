import datetime



def getDate(number_of_days=1):
    today=datetime.datetime.today()
    yesterday=today-datetime.timedelta(days=number_of_days)
    return yesterday.strftime("%m-%d-%Y")
    
