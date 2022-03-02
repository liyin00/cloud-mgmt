# G6T4 - Learning Management System (LMS)
The LMS targets 3 different users and allows each user to do the stipulated actions as stated below.
| Employee Type       | Description                                                            |
| -----------         | -----------                                                            |
| Trainer             | Able to create assessments. Consist of senior engineer.                |
| Learner             | Able to enroll themselves into eligible courses and attend the classes online. Consist of both engineers and senior engineers.                                        |
| Human Resource      | Able to assign engineers to created classes.                           |

<br><br>

# 1. Getting Started
Please access our LMS's Login Page and follow the steps under **2. User Stories**. You can refer to the walkthrough under "recorded scenarios" folder.

<br><br>

## 2. Assumptions
- Trainer cannot create quiz after the class start date
- Trainer can only create chapter 2 if chapter 1 is already created
- Pre-assignment will be done manually, normally before the registration date [Piazza @136](https://piazza.com/class/kqq5xowd6cj3ov?cid=136)
- Trainers are assigned before the registration date.
- Trainers can to upload the course material before the registration start date.
- All classes have total registration slots of 50

<br><br>

# 3. User Stories
## 3.1 Human Resource (HR)
| Title                | User Story                                                                                                    |
| -----------          | -----------                                                                                                   |
| Assign Learners | As a HR, I want to be able to enroll and withdraw the trainers to classes based on their availability so that the trainers can start preparing their course materials.                                                                                   |
| Preassign Learners   | As a HR, I want to be able to preassign learners into prerequisite courses so that I can prioritise their enrollments into the course.     

<br><br>

<p align="center">
  <img src="frontend\static\img\markdown/hr_sitemap.png" width="700"/> <br>
  <i>HR's Sitemap</i>
</p>
<br>

<br>

#### Step 1: Log in
Log in to your account through the [Login Page](https://spm-lms-team4.s3.amazonaws.com/templates/login.html).
  - Click on "Log in as HR"

#### Step 2: View a course
  - Click on the "View Course" button for **BEM460** or **EM140**. These courses have classes that are within the registration period

#### Step 3: View a class
  - Click on "View Class" button

#### Step 4: Preassign/Assign/Withdraw Learner
Please click on the following tabs based on your decided action
| Preassign Learner                    | 
| -----------------                    |

**Successful Attempt**
  - Click on "PREASSIGN LEARNERS" tab
  - Press "Preassign" without any inputs. An unsuccessful alert will pop up
  - Input "22" as the Learner ID
    - A success alert will pop up
    - The number of slots left will be updated
    - The learner will appear under "ENROLLED LEARNERS" tab

**Unsuccessful Attempt**
  - Press "Preassign" again with 22 as the Learner ID
    - An unsuccessful alert will pop up
<br>

| Assign Learner                       | 
| -----------------                    |
- Click on "REGISTERED LEARNERS" tab
- Press "Approve" for any learner
  - The number of slots left will be updated
  - The learner will appear under "ENROLLED LEARNERS" tab

| Withdraw Learner                    | 
| -----------------                    |
- Click on "ENROLLED LEARNERS" tab
- Press "Approve" for any learner.
  - The number of slots left will be updated
  - The learner will no longer be enrolled in the course

<br><br><br>

## 3.2 Trainer
| Title                | User Story                                                          |
| -----------          | -----------                                                            |
| Create Ungraded Quiz | As a Trainer, I want to be able to set the format of each question for each quiz, so that I can choose the settings best suited for each individual question. online. Consist of both engineers and senior engineers.                                                 |
| Create Final Quiz    | As a Learner, I want to be able to take the final quiz for a course, so that I can successfully complete the course.                                                    |
| Auto Grade Quiz      | As a trainer, I want each quiz to be auto-graded, so that I save time from cross-checking through every question.                                                     |

<br>

<p align="center">
  <img src="frontend\static\img\markdown/tnr_sitemap.png" width="700"/> <br>
  <i>Trainer's Sitemap</i>
</p>
<br>

#### Step 1: Log in
Log in your account through the [Login Page](https://spm-lms-team4.s3.amazonaws.com/templates/login.html).
  - Trainer ID: TNR4 

#### Step 2: View a Class
- Click on the "View Class" button for BEM460 or EM140 (classes that you are currently teaching)

#### Step 3: View/Create Quiz
Please click on the following classes based on your decided action.
| View Quiz                            | 
| -----------------                    |
  - Click on EM140 Engineering Management Class 1
  - Click on "View Quiz" button. 
  - You will see the questions created for the selected chapter

| Create Quiz                          | 
| -----------------                    |

**Successful Attempt**
  - Click on the "View Course" button for BEM460 Basic Engineering Management Class 4
  - Click on the "Create Quiz" button for Chapter 1
  - Please fill the input fields as shown below
  <p align="center">
    <img src="frontend\static\img\markdown\quiz_success.png" width="700"/>
  </p>

  - After which, press "Save & Create Quiz"
    - A confirmation popup will appear
  - Press "Okay"
    - You will be redirected back to the previous page
    - You can view the quiz for Chapter 1

<br>

  **Unsuccessful Attempt**
  - Click on the "View Course" button for BEM460 Basic Engineering Management Class 4
  When "Save & Create Quiz" is clicked, any of the followings would trigger the alert message:
  - One or more input fields are empty
  - The duration of the quiz is 0
  - The quiz has 0 questions

<br><br><br>

## 3.3 Learner
| Title                | User Story                                                                                  |
| -----------          | -----------                                                                                 |
|Engineers can view all courses                             | As an engineer, I would want to view all available courses with descriptions, so I can decide which are the courses I am interested in.                                                  |
Engineers can register for interested courses|   As an engineer, I want to be able to register for the courses by entering the necessary registration details, so I can attend the courses.           |
| Engineers can view the status of the registered courses | As an engineer, I want to view the status of my registered courses, so I can register for other classes of the same course if my registration(s) is/are unsuccessful.                                            |  
| Engineers can withdraw from the classes they have registered for |     As an engineer, I want to be able to withdraw from the classes I have registered for previously, so I do not have to worry about signing up for the wrong class accidentally.                   |
| View Course Materials by different chapters             | As a Learner, I want to be able to access course details that I have enrolled under, in order to be able to track my personal progress.                                           |   
| Take Quizzes for Course Sections     |As a Learner, I want to be able to take the quizzes as many times as possible so that I can pass it.                                             |
| Take Final Quiz for Courses     |As a Learner, I want to be able to take the final quiz for a course, so that I can successfully complete the course.                         |

                                                                                                                               
<br>

#### Step 1:<br>
Log into your account through the [Login Page](https://spm-lms-team4.s3.amazonaws.com/templates/login.html). Please use LNR8, LNR9, LNR10, LNR11, LNR12 as the Learner ID for testing purposes.
<p align="center">
  <img src="frontend\static\img\markdown\login_page.png" width="700"/>
</p>

#### Step 2: <br>
You will be directed to the Browse Courses tab on the page. You will be able to see the courses that are currently available for registration. Click on  <b>Learn More</b> for any of the courses below to view the relevant course details as well as your eligibility to register for the course as a particular learner.

<p align="center">
  <img src="frontend\static\img\markdown\lnr_browse_courses.png" width="700"/>
</p>

#### Step 3a: <br>
If you are eligible to register for the course, a list of classes will be shown to you. You will be able to register for multiple classes of the same course as well. Simply click on the <b>Register</b> button to register.
<p align="center">
  <img src="frontend\static\img\markdown\lnr_register_class.png" width="700"/>
</p>
 
##### * If you have registered or if the class is already full, you will not be able to register.
<br>

#### Step 3b:<br>
There are some cases which may not allow you to register for a class. If you encounter any one of these, click on the <b>back button icon</b> on the screen and choose another course that you are eligible to register for.

Uncompleted Prerequisites | Already Enrolled | Already Completed |
:-------------------------:|:-------------------------:|:-------------------------:|
![](frontend\static\img\markdown\lnr_register_prereq.png)  |  ![](frontend\static\img\markdown\lnr_register_enrolled.png) |  ![](frontend\static\img\markdown\lnr_register_completed.png) |
|

#### Step 4:

In order to check the status of your registrations, click on the <b>View/Change Status</b> tab on the navigation bar. You can see your approved or pending registrations here.
<p align="center">
  <img src="frontend\static\img\markdown\lnr_viewstatus.png" width="700"/>
</p>

#### Step 5:

Next, you can also withdraw your registrations if you want to cancel them. Simply click on the <b>Withdraw</b> button beside any registration record you want to cancel. Click on <b>Withdraw</b> again to confirm.
<p align="center">
  <img src="frontend\static\img\markdown\lnr_withdraw_reg.png" width="700"/>
</p>


#### Step 6:

Moving on, we want to view the course materials of our successfully enrolled courses. Click on the <b>Enrolled Courses</b> tab on the navigation bar. Next, click on the <b>Select a Course</b> Dropdown Bar and select "BEM460 - Basic Engineering Management".
<p align="center">
  <img src="frontend\static\img\markdown\lnr_viewenrolledcourses.png" width="700"/>
</p>

There are multiple versions of this Course Materials page based on each Learner's course progress as shown below. 
Quizzes Not Attempted | Quizzes Attempted
:-------------------------:|:-------------------------:|
![](frontend\static\img\markdown\lnr_unattemptedChapters.png)  |  ![](frontend\static\img\markdown\lnr_attemptedAll.png)|
|   Click on <b>Learn</b> button to start learning (Have to attempt current quiz to unlock the next chapter)| Click on <b>View</b> to revise chapter materials| 
|       -   |    Click on <b>Practise</b> to reattempt chapter quizzes  |
|     

#### Step 7: View & Learn Course Materials

 When you click on <b>View</b> or <b>Learn</b> from the previous page, you will see a PDF containing the chapter materials.
<p align="center">
  <img src="frontend\static\img\markdown\lnr_viewmaterials.png" width="700"/>
</p>

#### Step 8: Attempt/Practise Quizzes (This applies to Final Quizzes as well)

If you clicked on <b>Learn</b> previously, scroll down all the way and click the <b>Take Quiz</b> button to attempt the quiz.
<p align="center">
  <img src="frontend\static\img\markdown\lnr_takequizbtn.png" width="700"/>
</p>
This is an example of what a quiz looks like. In order to submit the quiz, you have to attempt all the questions.
<p align="center">
  <img src="frontend\static\img\markdown\lnr_quiz.png" width="700"/>
</p>
Once you finish the quiz, scroll down all the way and click on the <b>Submit Quiz</b> button.
<p align="center">
  <img src="frontend\static\img\markdown\lnr_submitquiz.png" width="700"/>
</p>

<br><br><br>

# 4. Others

## 4.1 Testing on Local Host
Please follow these steps only if you want to review the code on your localhost.

### 4.1.1 Prerequisites 
Please ensure that you have the following installed on your machine.
- Python 3
- Visual Studio Code
- WAMP Server
- MySQL
- Google Chrome Extension Installed with [Allow CORS: Access-Control-Allow-Origin](https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf/related?hl=en)

### 4.1.2 Launch & Download
1. Please ensure that your WAMP Server is running, MySQL is running and your default port of MySQL is 8888. 
2. Please download and unzip **spm_lms_finaldb.sql** file.
3. Create a **.env file** and paste the following code inside the file
  ```
  dbURL=mysql+mysqlconnector://root:root@localhost:8888/spm_lms # database for our main application data
  testURLRDS =mysql+mysqlconnector://root:root@localhost:8888/testdb # database use for integration testing
  ```

4. Proceed to /backend folder and run ```python app.py```.

<br><br><br>
