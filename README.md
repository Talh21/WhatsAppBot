# WhatsAppBot
WhatAppBot is used to send automated messages through Whatsapp Web.

You can modify the "opening message" as you wish. The contact name will remain unique to each contact so it looks like a personal message.
The "main message" can be taken manually or randomly picked from an .Xlsx file(use the "Contacts and messages.xlsx" file).

## Features and instructions
- **Choose contacts through file** - enter the contacts(exactly as they are saved in your phone) in the "Contacts" column.
- **Enter contacts manually** - enter the contact name that you wish to send the message to, when you finish just type "Done".
- **Main message** - can be picked manually or from a file(fill in the "messages" column). You can make a "database" of messages, so that for every run of the program a different random message will be chosen. 
if you want to use the same message every time, just fill in the message only in the first cell. 
- **Opening message** - edit the opening message inside the code(line 52).

## Requirements
1. Make sure you install [ChromeDriver](http://chromedriver.chromium.org/downloads)
  >Note: Set ChromeDriver path(line 5). Change the path according to your ChromeDrive.exe installation path.
  ``` 
CHROME_PATH = 'D:\Program Files (x86)\chromedriver.exe'
  ```
2. - [openpyxl](https://pypi.org/project/openpyxl/)
   - [requests](https://pypi.org/project/requests/)
   - [selenium](https://pypi.org/project/selenium/)
   - [urllib3](https://pypi.org/project/urllib3/)

## QR code
Please note that as a default, selenium does not save cookies and that every run is a "fresh" session. Thus, a QR code login is required in the beginnig of every session. However, there is a way to bypass this scenario, explained in stepst 1-4 below:

1. Open a new profile path within you Chrome browser
2. get the path: 

    ![alt text](https://i.stack.imgur.com/BRDTM.png)
    ![alt text](https://i.stack.imgur.com/SWV0z.png)

3. In lines 147-148 edit according to your path and profile name(edit the *):
  ```
  #options.add_argument("user-data-dir=C:\\*\\*\\AppData\\Local\\Google\\Chrome\\User Data\\")
  #options.add_argument("profile-directory=*")
  ```
  
  4. Uncomment those lines(remove the character #) 
  
 ## Installation
 1. Clone or dowload the repository:
 
     `git clone https://github.com/Talh21/WhatsAppBot.git`
     
 2. Change directory to the folder of the dowloaded program:

     `cd <path>`
     
 3. Install all the requirements:

     `pip install -r requirements.txt`

      **or**

     `pip3 install -r requirements.txt`
     
 4. Run the program:

     `python WhatsAppBot.py`
