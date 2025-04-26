## Wildfire Detection and Monitoring System

This is a simple Python project me and my partner made for **CMPSC 132** that simulates a wildfire detection system. It uses sensors to read temperature and smoke levels and checks if those readings point to a possible wildfire. The program uses object-oriented programming and includes file handling, exceptions, and more.

---

## What This Project Does

- Simulates **temperature** and **smoke** sensors at different locations  
- Checks whether conditions are risky enough to trigger a **wildfire warning**  
- Logs all sensor activity and detection results into a `.txt` file  
- Uses object-oriented programming (OOP), exception handling, and randomness  
- Simple text-based menu to run the program  

---

## What I Used From CMPSC 132

This project shows a bunch of stuff we’ve learned in class:

- Classes and Inheritance  
- File writing and reading  
- Try/Except (custom error handling for faulty sensors)  
- Abstract base classes using `NotImplementedError`  
- Lists, loops, and conditional logic  
- Working with timestamps using the `datetime` module  
- Randomized values for simulating sensor activity  

---

## Interaction

When using this code, there will four options left for you to type and choose.

1. Run Diagnostics
→ Simulates a check-up of all sensors and prints their current readings (like temperature and smoke levels).
→ Also shows if any sensors failed to activate.

2. Detect Wildfire
→ Analyzes sensor data to see if there's a possible wildfire.
→ If the temperature is over 50°C and smoke level is 7 or higher, a warning is triggered.
→ The results are also stored in a log.

3. Save Logs
→ Writes all detection results and sensor info to a file called wildfire_logs.txt.
→ This is useful for record-keeping or reviewing past alerts.

4. Exit
→ Ends the program cleanly.

---

Created by James Macartney, Joseph Afflek
For CMPSC 132 – Spring 2025
