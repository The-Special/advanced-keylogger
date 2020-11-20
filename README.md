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

## Usage



## Explanation

### Libraries
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

**Email Libraries***

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


With these been said, let's get to the actual malware

### Exploits
