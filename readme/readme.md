
# How to calculate age in present year using datetime library in python

## 1. Description of the program

Hello, in this lesson we will learn how to use the library and use one of its method to ***calculate age*** in present year using the Python programming language.  

Python has a library called datetime, which helps do operations on date and time.It makes the programmer's job easier without writing the actual code to calculate the age in present year.  

Using the datetime library, the age of a person can be easily found out with a few lines of code.  

## 2. Installation instructions

### 1. Python

#### 1. What is Python

+ Python is currently one of the most popular programming languages. 
+ It's easy to learn. Python supports object-oriented programming. 
+ It can be used in all the most common operating systems: Windows, Linux, macOS, Unix, etc.

#### 1. Installing Python on Windows 

In order to use Python, you need to install it on your machine.  

1. Download the Python installation package to your computer from <https://www.python.org/downloads/>
2. start installation
3. check installation by starting python

![python logo](/readme/screenshots/pythonlogo.png)

### 2. Git

#### 1. What is Git

+ Git is an open source distributed version control system (DVCS) that allows developers to work on the same project from anywhere and even if they’re offline. 
+ GitHub, GitLab and their alternatives are cloud services that provide remote hosting of Git repositories
+ Git is frequently used as a version control system for python projects.
+ Devops tool used for source code management
+ With Git, you can track the code changes you make over time and you can revert to specific versions.

#### 2. Installing Git on Windows
In order to use git version control, you need to install it on your machine.

1. Download the Git installation package to your computer from <https://git-scm.com/downloads/>
2. start installation
3. check installation by starting git bash

![git bash logo](/readme/screenshots/Gitbashlogo.PNG)

#### 3. Git bash startup

+ In git bash settings are done once.
+ create a folder in your computer where the version control system to be stored
+ right-click the desired folder and select Git Bash Here --> Git Bash command line opens so that the path is automatically in the desired folder.

![git bash setting](/readme/screenshots/gitbashsetting.png)

+ In order to use **git version control** on your computer , you first need to tell who you are once. This information is stored in Git's configuration information and is machine-specific.
+ configure git as follows

The steps are as follows:

1. open git bash 
2. enter the command to tell who you are
    git config --global user.name "firstname surname" 
3. enter the command to tell what is your email address
    git config --global user.email "your.email@example.com"

![git configuration](/readme/screenshots/gitconfiguration.PNG)

#### 3. Repository

1. A storage space where the project resides or a data warehouse
2. It may be in 
* folder
* Github or gitlab
* online host

##### what is remote repository ?

* A remote repository is a version of your project that is hosted remotely, so not on your own computer but on the internet or a network.

* This allows multiple developers to share the same work-flow, pushing and pulling to the same target.

* If you didn’t have remote repos it would be extremely inconvenient working on a single project as a team.

* Apart from this, a remote repository also serves as a backup for your code in case your laptop or computer suddenly fries. 
1. Github: A large remote host
2. gitlab: Small compare to github

* In order to create remote repository you should have signin credentials either in github or in gitlab.(using email you can create account in **github.com** or using office or college emails you can create account in gitlab)

##### Creating repository in Gitlab

1. Open gitlab and login with credentials
2. select new project and create a project and name the project eg: ABC123
3. Mark Initialize repository with a README
  This way the project will not be empty, but there will be something ready when we clone the project from the command line.
4. Press the green Create project function.
5. If required can give access to other developers for the same project by setting permission.
  check with the picture below

![gitlab repo](/readme/screenshots/gitlabrepo.png)  

continue repo cloning steps  

##### Repo cloning

* clone the repo from the gitlab server to your own computer
* It is done only once
**Authentication
  Using the HTTPS protocol
  SSH keys when using the SSH protocol 

**steps**

1. Select clone function use with HTTPS and copy the text of clone
2. In git bash installation and configuration, you created a folder in your computer on this folder right mouse button and choose Gitbash here
3. Gitbash command line window opens directly to the selected folder
4. clone the remote repo **git clone** command  
enter git clone and remote repo URL
5. Asks the gitlab credentials when cloning first time
6. eg. ABC123 should appear in the folder
7. check with **ls -a** in git bash to check the cloning was successful
8. git status to check the status of the project in gitbash command  
Adding a file to git version control  
9. Create a text file (eg. testi.txt)in the local repository folder with some text in it.
10. * Add the file to version control  
**git add testi.txt**  
* commit the file to your local repo as follows  
**git commit -m "new file added"**  
* finally we push the changes to the remote repo with the git push command  

In the same way new folder is added and commited, pushed to remote repository


### 1. Visual studio

#### 1. What is Visual studio

Visual Studio supports 36 different programming languages and allows the code editor and debugger to support (to varying degrees) nearly any programming language, provided a language-specific service exists. Built-in languages include C,[5] C++, C++/CLI, Visual Basic .NET, C#, F#,[6] JavaScript, TypeScript, XML, XSLT, HTML, and CSS. Support for other languages such as Python,[7] Ruby, Node.js, and M among others is available via plug-ins. Java (and J#) were supported in the past.

#### 1. Installing visual studio on Windows 

In order to use visual studio, you need to install it on your machine.  

1. Download the visual studio installation package to your computer from <https://code.visualstudio.com/Download/>
2. start installation
3. check installation by starting visual studio

![visualstudio](/readme/screenshots/visualstudiodownload.PNG)

4. In order to write program in Python language in visual studio you have  to install python extension in visual studio. check with the given picture below (1 step extension 2 step select python 3 step install)

![visualstudioextension](/readme/screenshots/visualstudioextensionpy.png)

After adding extension you can open the repository folder (eg.abc123) in the visual studio and start writing the programs in python language, name the files with extension .py(eg: agecalculator.py)

## 3. Our program

```
#Program to print current date and calculate the age of the user.
#Asking user to provide input name and year of birth
#import a datetime library to access current year
import datetime
#asking user input in console
full_name = str(input("Enter fullname:"))
birth_year = int(input("Enter year of birth:"))
#declaring a variable current_date and set date into it
current_date = datetime.datetime.now()
#declaring a variable current_year and set the current year
current_year = current_date.year

#Calculating the age of the user
age = current_year-birth_year

#Print the  current date and username with age
print("Todays date and time: ",current_date) 
print(f"Hello {full_name},you are {age} years")

```
Running the program we get the following output

![the image showing output of the program](/readme/screenshots/ageoutput.PNG)

## 4. Instructions to write program

step: 1 How to write Comments ?

* (#) Hashtag is used to write single line Comments that is to explain Python code.

* Comments can be used to make the code more readable.

* Comments can be used to prevent execution when testing code.
>#Program to print current date and calculate the age of the user.
>#Asking user to provide input name and year of birth
>#import a datetime library to access current year

step: 2 Declaring/ Intializing varaiables

* Variables are containers for storing data values.
* Python has no command for declaring a variable.
* A variable is created the moment you first assign a value to it.  

example:  
>x = 5  
>y = "John"  
>print(x)  
>print(y)  
>> output in console will be 
>> 5
>> John

Program variables  
> #declaring a variable current_date and set date into it  
> current_date = datetime.datetime.now()  
> #declaring a variable current_year and set the current year  
> current_year = current_date.year  


step: 3 How to import libraries  

* A date in Python is not a data type of its own, but we can import a library named datetime to work with dates as date objects.

> import datetime  
> current_date = datetime.datetime.now()  
> print("Todays date and time: ",current_date)   
>> output in console will be 
>> **Todays date and time:  2022-12-10 20:26:02.218399**  

* The date contains year, month, day, hour, minute, second, and microsecond.

step: 4 How to write user input  

* Python allows for user input.  
* That means we are able to ask the user for input.
* Python stops executing when it comes to the input() function, and continues when the user has given some input.
* user input is always in the form string datatype 
* To change the user entered str datatype number into numeric value always write int in the front of the user input variable value

Program user input    
> full_name = str(input("Enter fullname:"))  
> birth_year = int(input("Enter year of birth:"))
>> user input in the console and user entered details will be as follows
>> Enter fullname:Henna 
>> Enter year of birth:1991 


step: 5 How to write Python Operators  

* Operators are used to perform operations on variables and values.

example:
> x = 5    
> y = 3    
> z = x - y  
>print(z)
>> output in the console will be
>> 2

Program operators  
> #Calculating the age of the user  
> age = current_year - birth_year 

step: 6 How to write output variable ? 

* The Python print() function is often used to output variables.    
* The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:  
*f-strings make it incredibly easy to insert variables into your strings. By prefacing your string with an f (or F), you can include variables by name inside curly braces ({}).  

> #Print the  current date and username with age  
> print("Todays date and time: ",current_date)   
> print(f"Hei {full_name},olet {age} vuotta")  
>> output in the console will be  
>> Todays date and time:  2022-12-10 20:26:02.218399
>> Hello Henna,you are 31 years  

## 4. Summary

That's how you can create a program  age calculator in the visual studio editor using python extension and git add, git commit to the local repository and push the program code to remote repository (gitlab) in the Git bash command prompt or directly commit and push from visual studio editor. For detail information in the python language <https://www.w3schools.com/python/>
