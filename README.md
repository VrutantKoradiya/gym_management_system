# 🏋️‍♂️ Gym Management System (Frappe App)

A complete Gym Management System built using the **Frappe Framework**, designed to handle memberships, trainers, classes, workouts, and reports.



Doctypes ::::::::::::::::::::::::::::

1. Gym Member ( Standard ) - done
role: 
1. gym admin - full
2. gym member - Read / Edit own profile only 
3. Gym Trainer - read only

 
2. Gym Membership ( Submittable DocType ) - done
role:
1. Gym Admin - Full
2. Gym Member - Read only


3. Gym Trainer ( Standard ) - done
role:
1. Gym Admin - Full
2. Gym Trainer - Read / Edit own profile only


4. Gym Trainer Subscription ( Submittable doctype ) - done
role:
1. Gym Admin - Full
2. Gym Member - Create / Read
3. Gym Trainer - Read only (to see assigned members)


5. Gym Locker Booking ( Standard ) - done

role:
1. Gym Admin - Full
2. Gym Member - Create / Read (book own locker)



6. Gym Class Booking ( Standard )
role:
1. Gym Member - Create / Read
2. Gym Admin - Full



7. Gym Workout Plan ( Standard )
role:
1. Gym Trainer - Create / Edit / Read
2. Gym Member - Read only
3. Gym Admin - Full



8. Gym Workout Plan Exercise (Child Table)
role:
1. Gym Trainer - Create / Edit / Read



9. Gym Settings ( Single )
role:
1. Gym Admin - Full (Single Doctype)

other :

1. Gym Progress Tracker ( created for report)
functionality ->
  Client:
   1. calculate BMI based on weight enterd or height which one is fetch from Gym Member Dcotype
   2. add today date

##########################################################################################


Core Functionality ::::::::::::::::::::::::::::::::;;;

1. Member Registration – Admin registers new member (e.g., Riya) in Gym Member.
2. Membership Plan – Admin creates Gym Membership and assigns plan (Monthly/Yearly).
3. Locker Booking – Member books a locker through Gym Locker Booking.
4. Trainer Subscription – Member subscribes to a trainer via Gym Trainer Subscription.
5. Workout Plan – Trainer creates Gym Workout Plan with exercises for the members.
6. Group Class Booking – Member books group classes (Zumba, Boxing, etc.).
7. Progress Tracking – Trainer records member’s progress (weight, calories, BMI).
8. Weekly Summary – System emails member weekly class summary automatically.
9. Profile Page – Member views active plan, remaining days, trainer info, and progress.
10. Reports – Admin reviews revenue, popular classes, and members’ fitness journey.


##########################################################################################

coding functionality for each doctye ::::::::::::::::::::::::::

1. Gym Member ----
Client :
1. calculate BMI

python:
1. duplicate email ? or duplicate mobile no ? throw error

----------------------------------------------------------------------------------------------------

2. Gym Membership ----
Cleint:
1. auto set price based on plan type
2. calculate end date
3. get member details if memebership is already exists

python :
1. setting memebrship , activeplan , status field in Mmber Doctype
2. check member ship is already exists -> if yes then throw error.

other :
1. expire as scheduler events

----------------------------------------------------------------------------------------------------

3. Gym Locker Booking
Client : 
1. calculate expiry date

Python:
1. Checking  if locker already booked and still active

other :
1. expire as scheduler events

----------------------------------------------------------------------------------------------------

4. Gym Trainer
Client:
1. rating should from 0 - 5


Python : 
1. auto-update trainer's average rating from all subscriptions ( added in api.py or use frappe.call)

----------------------------------------------------------------------------------------------------

5. Gym Trainer Subscription
Client:
1. set end date

Python :
1. set trainer field of member doctype when subdcription is created.. (assign trainer to member)
2. checking member has active membership 
3. checking member has already trainer subscription

other:
1.  expire as scheduler events

----------------------------------------------------------------------------------------------------

6. Gym Class Booking
Python:
1. check member is active
2. check weekly booking limit from Gym Settings
3. prevent double booking same time slot and date 

other:
1. mark old classes 'Missed' if not attended


----------------------------------------------------------------------------------------------------

7. Gym Workout Plan
Client:
1. check at least one exercise is added

Python:
1. ensure trainer + level combination is unique
2. if published but no exercises, throw error

----------------------------------------------------------------------------------------------------

8. Gym Workout Plan Exercise
Client:
1. cehck sets & reps has atleast 1 if not the set 1
2. check duration should not negative
3. trigger message a new row is added

----------------------------------------------------------------------------------------------------

9. Gym Settings
Client:
1. Validate positive numbers

##########################################################################################


Custom page :::::::::
1. for page practical use user rames means its email to create member ... 

##########################################################################################

Reports ::::::::
1. Fitness Journey Report

- report that shows the fitness journey of a customer.
- Show tracked weight, calories, etc in a report and also show a chart. 
The report  have a filter to select a customer.

2. Popular Classes Report
- showing average group classes for all classes or single trainer

##########################################################################################

apprach for implementation ::::::::

30-40 % - AI use
useage:
1. understand workflow of gym management system
2. for creating reports, Pages...


70-70% - Self implementation







