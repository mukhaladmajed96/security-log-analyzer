# Security Log Analyzer

A Python-based security log analyzer that detects possible brute-force attacks by tracking failed login attempts within a specific time window.

## Features

- Reads login events from a log file
- Identifies failed login attempts
- Extracts IP addresses and timestamps
- Tracks failed login attempts for each IP address
- Detects possible brute-force activity
- Ignores malformed log entries without crashing

## Detection Logic

The program raises an alert when the same IP address has 3 failed login attempts within 30 seconds.

Example:

17:30:01 LOGIN_FAILED 10.0.0.15  
17:30:10 LOGIN_FAILED 10.0.0.15  
17:30:20 LOGIN_FAILED 10.0.0.15

Output:

ALERT: 10.0.0.15  
3 failed logins in 19.0 seconds

## Technologies Used

- Python
- File I/O
- Dictionaries
- Lists
- Loops and conditional statements
- Python datetime module

## What I Learned

Through this project, I practiced reading and analyzing log files, extracting useful security information, tracking suspicious IP activity, and using timestamps to detect possible brute-force attacks.