#!/usr/bin/python3
import cgi, cgitb

cgitb.enable()
form = cgi.FieldStorage()

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def find_easter(y, dateformat):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    month = (h - m + r + 90) // 25
    day = (h - m + r + month + 19) % 32

    if dateformat == 1:
        return format_one(day, month, y)
    elif dateformat == 2:
        return format_two(day, month, y)
    elif dateformat == 3:
        return format_three(day, month, y)
    
def format_one(day, month, y):
    return '{:02}/0{}/{}'.format(day, month, y)
    
def format_two(day, month, y):
    return '{}{} {} {}'.format(day, date_ordinal(day), months[month - 1], y)

def format_three(day, month, y):
    return format_one(day, month, y) +' or '+ format_two(day, month, y)

def date_ordinal(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
        return "<sup>" + suffix + "</sup>"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
        return "<sup>" + suffix + "</sup>"    

    
print('Content-Type: text/html; charset=utf-8')
print("")
print('<!DOCTYPE html>')
print('<html>')
print('<head>' 
      '<meta charset="UTF-8">'
      '<link href="../style.css" type="text/css" rel="stylesheet">'
      '<title>Find Easter</title>'
      '</head>')
print("<body>")
if 'Year' in form and 'dateformat' in form:
    form_year = int(form.getvalue('Year'))
    form_month = int(form.getvalue('dateformat'))
    print('<p class="result">Easter falls on', find_easter(form_year, form_month), '</p>')
else:
    print('<p class="result">Easter: Some parameters are missing</p>')
print("</body>")
print("</html>")
