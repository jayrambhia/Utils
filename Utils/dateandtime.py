import time
import datetime

def change_date(num):
    """
    
    Returns new date as a tuple with number days changed.
    
    Today's date: March 14, 2012
    
    >>> new_date = change_date(3)
    >>> print new_date
    (2012, 3, 17)
    
    >>> new_date = change_date(-4)
    >>> print new_date
    (2012, 3, 10)
    
    
    """
    sec = num*24*3600
    sec = time.time()+sec
    t = time.ctime(sec)
    t_struct = time.strptime(t)
    new_date = t_struct[0:3]
    return new_date 

def get_date_string(date):
    """
    
    Enter a date tuple. It will return string
    
    Today's date: March 14, 2012
    
    >>> new_date = change_date(3)
    >>> print get_date_string(new_date)
    '3/17/2012'
    
    """
    year, mon, day = date
    string = str(mon)+'/'+str(day)+'/'+str(year)
    return string
  
def get_today():
    """
    
    Returns (year, month, day) tuple
    
    Today's date: March 14, 2012
    
    >>> today = get_today()
    (2012, 3, 14)
    """
    date_today = datetime.date.today().timetuple()[:3]
    return date_today
