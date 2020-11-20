# ADVANCED KEYLOGGER MADE BY USING PYTHON

## **I do not take any responsibility, use at your own risk.**

Keep in mind, this is not just a basic keylogger, it has other features have been done and more features to be added.

## Usage and Explanation 
First of all, you have to specify some of values by *yourself*. Here's what are them


Line 95

![Startup](https://i.hizliresim.com/1koCaR.png)


From line 224 to 232

![Email](https://i.hizliresim.com/YoHqPC.png)



After you have done them, you can check the usage and explanation now

# Usage

## How to Run?

First of all if you want to run this malware, you need to open the script as administrator mode, otherwise some functions won't work and you'll get an error.

The best way to run this script as administrator is turning into an exe file. See the instructions down below:

[Download Pyinstaller](https://pypi.org/project/pyinstaller/)

- [How To Use Pyinstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html)
- [How To Use Pyinstaller](https://realpython.com/pyinstaller-python/)

## WARNING

This program is really dangerous. There are functions that disables windows' features such as **Task Manager** and **CMD**, I do not recommend to run this file before reading the the explanation. 


# Explanation

## Libraries
Some of imports are commented because they seemed useless and at the same time, seemed like could be useful so they have just got commented instead of taken out. Keep in mind

Some libraries are custom libraries so you might need to download them before using the program, I will create a requirements.txt to help you out

**Relative Paths**

![Path](https://i.hizliresim.com/DSRSX4.png)

As you see, we use **os** and **sys** modules. We use **os** module for some functions and methods. For example *expanduser, listdir* and more. These functions and methods are helping us to get relative paths and control them as how we want.

*sys* module is never used in this program, we have just imported in advance updating the program. So keep in mind, you can take it out as you like

----------------------------------------------------------

**Interacting With Shell and Doing Basic Windows Operations**

![Shell](https://i.hizliresim.com/dVl9vx.png)

This part is little bit complicated so I will explain one by one

**ctypes** library is used for interacting with windows. It helps us to do basic windows operations with Python. For an example, we used **ctypes** library in this program for hiding our file that we will store our data

**platform** library is used for getting the operation system's name so we can determine what we want to do when we face with different operation system types. Keep in mind, this is the first release of this program so there is nothing designed other than dealing with windows, I have just seperated them because I will update this program and make it work for other operation systems as well

**getpass** library is used for getting current user's name, it helps us to adding our program to startup without facing any problem

----------------------------------------------------------

**Sleep function**

![Time](https://i.hizliresim.com/hSTur0.png)

In this part, actually we aren't getting the process time because I haven't coded that yet, it's easy and I will add that feature after I fix basic problems and add features

**sleep** method is used for stopping our thread functions for a certain time, so in that way our **infinite while loops** don't crash our program

----------------------------------------------------------

**Getting ipv6 Address**

![Ipv6](https://i.hizliresim.com/CoXHpM.png)

We are getting requests from an api page that gives us only the ipv6 address

----------------------------------------------------------

**Email Libraries**

![Email](https://i.hizliresim.com/Ew6yJR.png)

These our SMTP libraries used for sending emails after we get the keylogs and the screenshots, I don't know this library that much so you can check by yourself if you are wondering how they work

[SMTP Documentary](https://docs.python.org/3/library/smtplib.html)

----------------------------------------------------------

**Keylogger Libraries**

![Keyloggers](https://i.hizliresim.com/55YSGj.png)

These are the libraries that helps us to get keylogs

**logging** library is used for formatting how we want to get the keys

----------------------------------------------------------

**Threading**

![Threading](https://i.hizliresim.com/V9tpJP.png)

We use **threading** library to multiprocess our functions and methods. So in that way we can do more than one thing at the same time and make our program work like a real malware

----------------------------------------------------------

**Backdoor Libraries (Haven't added yet)**

![Backdoor](https://i.hizliresim.com/1kS1pj.png)

This version of this program doesn't have the keylogger yet, after I code the server side this file will be the client and you'll be able to use it as a backdoor. These libraries are useless for now

----------------------------------------------------------

**Pyautogui**

![Screenshot](https://i.hizliresim.com/4Usoze.png)

We use **pyautogui**'s **screenshot** function to attach screenshots to our emails

----------------------------------------------------------

### Checks
Checks are used for disabling windows features and include other features than the actual parts. Now let's get to the explanation about how they work

**Adding To Startup**

![Startup](https://i.hizliresim.com/jTxC84.png)

This function is used for adding our program to startup. When the victim opens his pc, he won't recognize that this program will run automaticly so in that way we will be always active

----------------------------------------------------------

**Disable Features**

![Disable](https://i.hizliresim.com/Ihnbbe.png)

In this part, we are disabling windows features to oppress the victim and restrict him from doing actions such as trying to disable this program

----------------------------------------------------------

**Taking Screenshots**

![Screenshot](https://i.hizliresim.com/njpORD.png)

We are taking screenshot of the whole screen every five seconds and saving them to specified path. Remember that we defined **sleep** function as **s**

----------------------------------------------------------

**Returning ipv6 Address**

![ipv6](https://i.hizliresim.com/Ah7so1.png)

With this function, we are returning the victim's ipv6 address

----------------------------------------------------------

## Exploits

Keep in mind, again and again. These are the classes and the functions where we only **define**. We don't run them in here yet, we run them after we find the specified operation system.

### Keylogger

**Keylogger Class**

![Keylog1](https://i.hizliresim.com/gmrcHc.png)

This is our keylogger class which is saves the keyboard inputs into a list and then after some ammount of keys, saves into a file and so on. Let's explain how these methods work.

**Saving Keys**

![Keylog2](https://i.hizliresim.com/5llCAX.png)

Our method that where we listen to inputs and save them to a list (or array you can say). In this method, we have another functions included inside

**Saving to a file**

![Keylog3](https://i.hizliresim.com/0Nijz1.png)

This is the function and the if statement included in that method. **savefile** function simply does save the keys in a file and that **if** statement decides when to save the keys in a file. You can change the number of keys as you like, I was using 20 keys for testing it

![Keylog4](https://i.hizliresim.com/nl6W7h.png)

**logger** method is where we call the **on_press** method. **on_press** method is determines how the listener should work, so **logger** method depends on how **on_press** method has designed.

**Running Thread Methods**

![Keylog5](https://i.hizliresim.com/ccvPm8.png)

In this part, we can finally run our keylogger with this method as thread methods (functions).


### Sending Email

**Email Class** 

![Mail1](https://i.hizliresim.com/cbHEpX.png)

This is our email class, we are planning to send emails after we get the keylogs and the screenshots

With this constructor we define email's header and body.

1. **Don't forget to put your informations in empty strings**
2. **If you encounter with some problems, there are possible solutions I have for it**
     - If you are using gmail, make sure that you have opened the **Less secure app access**, otherwise you can't send emails with it
     - If you are using an another mail system, you need to change the **address** on **line 251**. You don't need to change the port
     
**Adding Attachments to Emails**

![Mail2](https://i.hizliresim.com/D4ObE2.png)

In here, we add attachments to our email based on the files in the directory we are iterating in.

I have just specified two types of files because this malware doesn't save any other type of files.

Keylogs are saved as `.txt`, images are saved as `.png`

**Sending the Email and Starting the Threads**

![Mail3](https://i.hizliresim.com/meWptc.png)

Our **send** method is used for sending the email when everything is done (Specifying header and the body, attaching the certain files).

And our **run** method is used for running these methods as **thread** methods to multiprocess our program like in the **keylogger** class

### Running The Malware (WINDOWS)

**Determining the Operation System's Name**

![Run1](https://i.hizliresim.com/rwrjyB.png)

First of all, we need to learn what operation system does our victim use. We find out with the **getsystem** function and then deciding what to do based on the operation system.

Like I said, this is the first version of this program, so it just works on windows for now.

**Creating Our Directory**

![Run2](https://i.hizliresim.com/44k9vw.png)

We are getting the **desktop** and **system32**'s path. We are creating a file in **system32** to store our keylogs and screenshots. If the file is already exists (which is nearly impossible) we just skip it and use the exist file

in **line 285**, **ctypes** helps us to hide our directory.

**Applying the Checks**

![Run3](https://i.hizliresim.com/nfGnhn.png)

In here, we run the methods that where we disable **Group Policy**, **Regedit**, **Task Manager** and **CMD**.

**AddToRegistry** function is for adding our program to startup, so we run it here

**Running the Threads**

![Run4](https://i.hizliresim.com/n6KzOC.png)

Finally we have finished our program.

1. First of all, we are creating objects for our classes.
2. After we create our objects, we start to run thread methods
3. While the thread methods are running, we create an function to send our email after certain steps are done
4. In our **sendmail** function, we check if the keylog files ammount is more than 5 every 5 seconds
5. If our keylog files ammount more than 5, we call the **run** method of email to send our email. 
6. While we are sending our email, files in the directory that we created are getting attached to that email
7. After we send our email, we delete the files in that directory to not attach the same files and not to spend memory, otherwise victim's pc could get crashed
8. That's all, after we delete the files we repeat the same thing
