
                          Activity Grader

  What is it?
  -----------
   This application opens all activities in a given folder 
   in PT, extracts the grade and then outputs a CSV file with
   the filename, total percentage and sub component scores.


  System Requirements
  -------------------

   JRE:
     1.8 or above (https://java.com/getjava/)

   Packet Tracer 7.0 or above


  Upgrading Activity Grader
  -------------------------
  
   If there is a previous version of Activity Grader
   installed, remove it from the approved list and delete
   the "extensions\ActivityGrader" folder. Then follow the 
   "Installing Activity Grader" section.


  Installing Activity Grader
  --------------------------

   1) Unzip ActivityGrader.zip

   2) Copy the "ActivityGrader" folder to 
       "<Packet Tracer Installation Folder>\extensions"
       Typically: C:\Program Files\Packet Tracer\extensions

   3) Add ActivityGrader.pta using the IPC menu.
       a) Extensions Menu -> IPC -> Configure Apps
       b) Click on the Add button
       c) Select the folder "ActivityGrader"
       d) Select the ActivityGrader.pta file, then OK

       (See PT Help and Tutorials for additional information)




  Launching the Application
  -------------------------
  
   There are two ways to launch the application.
  
   A) Within Packet Tracer:
  	1) Extensions Menu -> IPC -> Configure Apps
	2) Select Activity Grader from App List
	3) Click on Launch button

   B) Standalone, execute "extensions\ActivityGraderx86.exe". This 
      method does not launch Packet Tracer automatically. Packet 
      Tracer must be already running and the IPC enabled at 
      port 39000. 

   For either method, Packet Tracer must allow this application
   to use the IPC. (See Step 3: Installing) 



  Using the Application
  ---------------------

   This application uses the activity filenames as the index. So,
   it would be best to have students append their name or student
   ID to the activity filename for submission.

   The location of the activity files should be in a single
   directory. This directory may be a local disk, network drive,
   or flash usb drive -- anywhere that Packet Tracer can access.

   1) Enter the location of the activities or browse
   2) Click Grade
  
   A Comma Separated Value (CSV) file will be created in the
   directory where the activity files are stored.




 




