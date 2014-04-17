#ScriptName : 160by2.py
#---------------------

from selenium import webdriver
import time
############ to hide firefox
# from pyvirtualdisplay import Display

# display = Display(visible=0, size=(800, 600))
# display.start()

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "http://www.160by2.com/Index"
username = "7405598718"
password = "5922"

xpaths = { 'usernameTxtBox' : "/html/body/form/div/div/div[2]/div/p[3]/input[@id='username']",
           'passwordTxtBox' : "/html/body/form/div/div/div[2]/div/p[5]/input[@id='password']",
           'submitButton' 	: "/html/body/form/div/div/div[2]/div/p[6]/button",
           'skipveri'       : '/html/body/div/section/div[2]/div[3]/div[3]',
         }

#
# Block images,css,flash
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

## get the Firefox profile object
firefoxProfile = FirefoxProfile()
## Disable CSS
firefoxProfile.set_preference('permissions.default.stylesheet', 2)
## Disable images
firefoxProfile.set_preference('permissions.default.image', 2)
## Disable Flash
firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
## Set the modified profile while creating the browser object 
mydriver = webdriver.Firefox(firefoxProfile)
print "Connecting...."
##################
##################
mydriver.get(baseurl)
print "Loggin in..."
#Clear Username TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
#Clear Password TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
#Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

##############################################
################# LOGGED IN ##################
##############################################
print "Successfully logged in"
########################
# On CONFIRM MAIL page #
########################

num = raw_input("Send to: ")
message21 = raw_input("Enter Message to be sent: ")
a = mydriver.find_elements_by_tag_name('div')
for t in a:
  c = t.get_attribute('class')
asd = mydriver.find_element_by_xpath(xpaths['skipveri'])
asd.click()

#####################
# On DASHBOARD page #
#####################
#
# Redirect to send sms using **SCRIPT1**
# 
script1 = """var x = document.getElementById("by2Frame");
console.log(x.id);
var y = document.getElementById("aSMS");
var z = String(y.onclick);
console.log(z.substring(36,z.length-34));
x.src=z.substring(35,z.length-34);"""
mydriver.execute_script(script1)

###################
# On SENDSMS page #
###################

time.sleep(1)     # for Loading...
mydriver.switch_to_frame(mydriver.find_element_by_name("by2Frame"))

#
# Mobile number and message entered using **SCRIPT2**
#
script2 = """
var y = document.getElementsByTagName("input");
document.getElementById("sendSMSMsg").innerHTML = '%s';
for(var i=0;i<19;i++){
  if(y[i].id == y[i].id.toUpperCase() && y[i].id.length == 6){
    var my_id = y[i].id;
    console.log();
    y[i].value = %s;
  }
};
""" % (message21,num)
mydriver.execute_script(script2)

#
# Submit the Send sms form using **SCRIPT3**
#
script3="""
document.getElementById("hid_exists").value="no";
  setCookie("adCookie",1,1);
  exCookie("shiftpro","axisproapril8th",1);    
  $("#maxwellapps").val(mySessionVal);                    
  $("#UgadHieXampp").val("ugadicome");
  $("#aprilfoolc").val("HoliWed27");
  $('#btnsendsms').val("Sending...");
  $('#btnsendsms').attr("disabled", true);
  $('#sendlater').attr("disabled", true); 
  window.parent.rampingStyle(true);
  document.frm_sendsms.action=$("#fkapps").val();
  setTimeout(function(){document.frm_sendsms.submit();},500);
"""
mydriver.execute_script(script3)

####################
# On MSG SENT page #
####################
time.sleep(2) # for Loading...

#
#  Checking if sending successful using **SCRIPT4**
#
script4="""
var s = document.getElementsByTagName("iframe");
console.log(s.length);
if(document.getElementById("showLate").innerHTML=="<span>Your message has been sent !!!</span> "){
  return 1;
}
else {
  return 0;
}
"""
if mydriver.execute_script(script4):
  print "success"
else:
  print 'failed'

for handle in mydriver.window_handles:
  mydriver.switch_to_window(handle)
  mydriver.close()