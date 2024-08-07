# VIT Timetable to Calendar Converter

Converts the digital calendar given by the University in the student portal into the format (.ics) that can be imported by all calendar applications. This enables students to be able to keep their class timetable along with their other timetables, and to optionally receive notificaitions before class begings.

# Sample input:

![image](https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar/assets/74148176/d4c65a4d-d62e-43ec-91e4-4acdf1c60589)
![tt](https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar/assets/74148176/3328f086-7643-47ca-9623-c815225e6e69)

# Sample result:

<img src="https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar/assets/74148176/b1e672b3-45fb-4f33-97dd-c02c8a3bc4df" height = "700">

## Instructions:

1) Copy paste the full page's text from VTop (VIT's portal) into a .txt file
2) Run `Frontend/terminal_interface.py` and enter the required details
3) Upload the given .ics output file to any calendar service you like

### ⚠️ Important note for Google Calendar imports:

Create a new "calendar" and import this file into that, instead of importing directly to your default calendar in Google Calendar. Creating a new calendar for this will make it easy to delete it after the semester ends. Otherwise, you will have to delete each class of the week manually. 

Here is a video tutorial on how to import to Google Calendar: https://www.youtube.com/watch?v=gzahLrDPKv4

Do not forget to change the "calendar" that you are importing the .ics file too, even after creating the new calendar.
