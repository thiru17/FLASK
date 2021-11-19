from flask import Flask, render_template ,request,send_file
import os
import xml.etree.ElementTree as ET
import pandas as pd
from subprocess import Popen,PIPE
app = Flask(__name__)

@app.route("/")
def mainMenu():
    return '''
        <html><body>
        <form action="/scan" method="get">
                ENTER IP ADDRESS: <input type="text" name="ip">  <br />
                <input type="submit" value="Submit" />
                </form>
        </body></html>
        '''    

@app.route("/scan")
def Host_DisCov():
    ip= request.args.get("ip") 
          
    a= Popen(
        ['nmap', '-v','-oX','hostlist.xml',`] , shell=True ,stdout= PIPE,stderr= PIPE ,universal_newlines=True)
    s=a.wait()
    out,err=a.communicate()
   #xml parsing 
    tree=ET.parse('hostlist.xml')
    root=tree.getroot()
    port=[]
    for i in root.iter('port'):
       port.append(i.attrib)
    state=[]
    for i in root.iter('state'):
       state.append(i.attrib)
    address=[]
    for i in root.iter('address'):
       address.append(i.attrib)
    lit1=pd.DataFrame(port)
    lit2=pd.DataFrame(state)
    lit3=pd.DataFrame(address)
    lit4=pd.merge(lit1,lit2,right_index=True,left_index=True)
    result=pd.merge(lit4,lit3,right_index=True,left_index=True)
    result.to_html("templates/new2.html")
    result.to_csv("templates/newcs1.csv")
    f=open('templates/new2.html','a')
    message="""<html>
    <br><br><a href='/download'><button>DOWNLOAD</button></a>
    </html>"""
    f.write(message)
    f.close()
    return render_template('new2.html')

@app.route('/download')
def download():
   return send_file('templates/newcs1.csv', as_attachment=True)

  
   
def merge(port,state,address):
      merge_list=tuple(zip(port,state,address))
      return merge_list

    
if __name__ == '__main__':
	app.run(debug=True)  
