---
layout: page
title: FAQ
description: Frequently asked questions about the course.
nav_order: 4
---

# Frequently Asked Questions 🙋
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Enrollment

### I am on the waitlist, so how can I keep up with the course?

You can (and should) still submit assignments if you are on the waitlist. Waitlisted students should have access to Datahub to work on assignments. You may need to add yourself to some course tools; see the [Getting Started](../syllabus#getting-started) section of the syllabus.

### What are my chances of getting off the waitlist?

The instructional staff is not equipped to answer this question. Many questions about enrollment are [answered here](http://datascience.ucsd.edu/academics/undergraduate/faq/). Please direct your questions about enrollment to DSC advising. You can send an email to [dscstudent@ucsd.edu](mailto:dscstudent@ucsd.edu), send a message through the Virtual Advising Center, or stop by drop-in advising hours. In short, seats in the class open up when students drop the class, which can be hard to predict.

### Will another section be added? Will more seats open up?

Unfortunately, no. Despite not having the limitation of physical classroom space, we are still constrained by the staff’s ability to support you. We are not able to add more staff to the course and therefore we are not able to accept more students in the course.

### I have been added to Gradescope, Canvas, Campuswire, and other course tools. Does this mean I am off the waitlist?

No. Students on the waitlist were also added to all course tools, so they can complete assignments while they are on the waitlist. Check [Webreg](https://act.ucsd.edu/webreg2) if you are not sure of your enrollment status.

## Course
 
### How do I submit assignments?

Follow the instructions with the Jupyter Notebook to download your notebook and upload it to Gradescope. If you are working with a partner, use the “Add Group Member” feature on Gradescope to tag your partner. Only one of the two partners should submit.
 
### How do I submit a regrade request?

If you think there is a problem with the autograder, please post in the #autograder chatroom on Campuswire. If you think there is a problem with how your written question was graded, submit a regrade request through Gradescope. Submit regrade requests within one week of getting your score back. After that, grades will not be changed.

### What should I do if a correction to an assignment is announced?

You must first log into [datahub.ucsd.edu](https://datahub.ucsd.edu), then click the assignment link from the course homepage. This will download a corrected version of the assignment. You won’t lose your work by doing this.

### Which version of my assignment will be graded?

By default, the most recent version of your assignment will be graded. If you are working with a partner, the last submission from either one of you will be graded by default.
 
### How are assignments graded?

Written questions are graded manually on Gradescope. Python questions are graded automatically by executing all the cells in your notebook, then checking that the variables pass certain correctness checks. It is important that you run all the cells in the notebook in order so that you have an accurate impression of what will be graded. It is also important not to change the names of any variables, otherwise the correctness checks may fail. For homework assignments, these correctness checks that determine your grade are different than the in-notebook formatting tests, so just because you pass all the tests in the notebook does not mean you will get a perfect grade on the homework. The in-notebook tests check things like whether the variable is an integer, whereas the correctness test used for grading would check whether the variable is equal to the correct value. The formatting tests basically just prevent you from getting too far off track. For labs, we do not run additional correctness tests outside of the tests within the notebook. Your grade is simply the proportion of the in-notebook tests that your code passes. In addition, all submissions will be automatically checked for similarity with other submissions to detect academic integrity violations.

### What should I ask and not ask in tutor hours?

Tutor hours are your chance to ask for general help, clarification on assignments, and to review previous assignments.  They will not tell you if your answer is correct, and it is inappropriate to ask. The tutors have previously taken the class, done well, and been trained in how to help you. Here are some really good questions to ask:
- I got confused about a concept in class.  Can you explain it?
- When the assignment says X, does it mean A or B?
- My code is giving a weird error - can you help me understand why?
- I can’t get this test to pass, so I must be doing something wrong.  Can you help me figure it out?
- My code is doing something different than what I expected. Can you explain what is happening?

Questions that you should never ask a tutor:

- Is this the right answer?
- Can you check my code and make sure it is right?
- What is the answer?
- What’s going to be on the exam?

Your primary motivation when interacting with course staff should be learning.
 
### Is discussion section mandatory?

No. Discussion section is supplemental, and will be especially useful for those students who are new to programming.
 
### Do I have to attend the lecture and discussion I am enrolled in?

You must attend the lecture you're enrolled in (email us if you have any concerns), but you can attend any discussion section.

## Tech Support

### Why can’t I log in to Datahub?

Log out of all Google accounts or open an incognito window. When prompted, enter your full UCSD email, "username@ucsd.edu", as your credentials.

### How can Extension Students access Datahub?

Extension students may receive separate accounts for the purpose of accessing Datahub.  To look up your account information and reset any additional account passwords, visit [https://sdacs.ucsd.edu/~icc/index.php](https://sdacs.ucsd.edu/~icc/index.php) and enter your AX account in the username field and your UID in the Student ID field (e.g. "axNNNN", "cs120sp20aa", etc.)

### My notebook won't load. Is Datahub down?

Sometimes Datahub does have availability issues. Usually it is back up and running again within an hour. In other instances, there are some things you can do to get the notebook running again: Make sure your internet connection is working. If you can, restart your server by clicking the button at the top right labeled "Control Panel", then select "Stop My Server", followed by "Start My Server".  If that doesn't work, try restarting your computer and using a different browser. Whenever you resume working on a notebook, run all cells you've previously completed. If your problem persists after trying all these steps, please notify us.

### Why does running a particular cell cause my kernel to die?

If one particular cell seems to cause your kernel to die, your code is probably incorrect in a way that is causing the computer to use more memory than it has available. For instance: your code is trying to create a gigantic array. To prevent from crashing the entire server, the kernel will "die". This is an indication that there is a mistake in your code that you need to fix.

### How do I quickly run all the cells in a notebook?

Go to the Cell menu in the top toolbar, then “Run All.” You can also select a certain cell and run all cells before this point, or run all cells after this point. You should run all the cells in your notebook before submitting to confirm that you pass all the tests.

### I clicked the assignment link, but why can’t I find my assignment in Datahub?

You must first log [datahub.ucsd.edu](https://datahub.ucsd.edu), then click the assignment link. Click the link again AFTER logging in.

### Why does `grader.check_all()` fail, if all previous tests passed?

This can happen if you "overwrite" a variable that is used in a question. For instance, if Question 1 asks you to store your answer in a variable named foo, and later on in the notebook you change the value of foo, you'll see the test after Question 1 pass, but the test at the end of the notebook fail. Make sure to rename later instances of that variable so you're not overwriting it.


### Why does a notebook test fail now, when it passed before and I didn’t change my code?

You probably ran your notebook out of order.  Re-run previous cells.

### Why did a Gradescope test fail, when all the notebook's tests passed?

This can happen if you're running your notebook's cells out-of-order. The autograder runs your notebook top-to-bottom. If you're defining a variable at the bottom of your notebook and using it at the top, the Gradescope autograder will fail because it doesn't recognize the variable when it encounters it.

This is why we recommend running Kernel -> Restart and Run All: it "forgets" all of the variables and runs the notebook from top-to-bottom, just like the Gradescope autograder will. It will highlight any issues. Find the first cell that raises an error. Make sure that all of the variables used in that cell have been defined above that cell, and not below.

### Why do I get an error saying grader is not defined?

If it has been a while since you've worked on an assignment, the kernel will shut itself down to preserve memory. When this happens, all of your variables are forgotten, including the grader. That's OK: you'll just need to re-run all of the cells. The easiest way to do this is by using Kernel -> Restart and Run All.

### I’m positive I have the right answer, but the test fails. Is there a mistake in the test?

While you might see the correct answer displayed as the result of the cell, chances are it isn't being stored in the answer variable. Make sure you are assigning the result to the answer variable. Make sure there are no typos in the variable name. 

### What does it mean when I see an error like `isinstance(..., numbers.Integral)`?

This error is telling you that the answer should be an integer, but your answer is not. This often happens when you've done some intermediate work towards the answer and saved an intermediate result in the answer variable instead of the final result.

Sometimes instead of `isinstance(..., numbers.Integral)`, you'll see something like `isinstance(..., bpd.DataFrame)`. This is saying that the answer should be a DataFrame, but yours was something else. The rest of the above still applies.

Check the type of your answer variable with `type()`. Is it what you expected?

### What does this Python error message mean?

It can be difficult to decipher the meaning of error messages in Python. [Here is a useful guide](https://swcarpentry.github.io/python-novice-inflammation/07-errors/index.html). You can also ask in tutor hours, or on Campuswire, provided you are not posting your code publicly or otherwise giving away the answer in your post. Understanding cryptic error messages is a skill that comes with experience.