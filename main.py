import webapp2
import cgi

form = """ 
<script>
var day = document.getElementsByName('name').value;
if(day<0 || day>31){
window.alert(enter valid date!!);
}

</script>
<form method="post">
Please enter your Name and birthday:</br>
Name:<input type="text" name="name" value="%(name)s"></br>
Day:<input type="text" name="day" value="%(day)s" >
Month:<input  type="text" name="month" value="%(month)s">
Year:<input type="text"  name="year" value="%(year)s">
<input type="submit">
<div style="color:red">%(error)s </div>
</form>
"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def escapeHTML(s):
    return cgi.escape(s, quote=True)


def validMonth(month):
    for a in months:
        if a.lower()==month.lower():
            return a;


def validDay(day):
    if day and day.isdigit():
        day=int(day)
        if (day<=31 and day>0):
            return day;


def validYear(year):
    if(len(year)==4):
        return year

class MainHandler(webapp2.RequestHandler):
    def writeForm(self,error="",name="",day="",month="",year=""):
        self.response.out.write(form %{"error":error,"name":escapeHTML(name),"day":escapeHTML(day),"month":escapeHTML(month),"year":escapeHTML(year)})
    def get(self):
        self.writeForm()
    def post(self):
        Vday = validDay(self.request.get('day'))
        Vmonth = validMonth(self.request.get('month'))
        Vyear = validYear(self.request.get('year'))
        Vname = self.request.get('name')
        data=(Vname, Vday, Vmonth, Vyear)
        if not (Vday and Vmonth and Vyear and Vname):
            self.writeForm("oops! please enter valid date of Birth",self.request.get('name'),self.request.get('day'),self.request.get('month'),self.request.get('year'))
        else:
            s="Thanks! %s, your date of birth is %s,%s,%s." %data
            self.response.out.write(s)
            
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks")	

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/thanks',ThanksHandler)
], debug=True)
