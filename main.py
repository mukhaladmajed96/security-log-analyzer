from datetime import datetime

with open("login_logs.txt", "r") as file:
    logs = file.readlines()

failed_times = {}

for log in logs:
    parts = log.split()
    if len(parts) < 4:
        continue

    date = parts[0]
    time = parts[1]
    event = parts[2]
    ip = parts[3]

    if event == "LOGIN_FAILED":
        timestamp = datetime.strptime(
            date + " " + time,
            "%Y-%m-%d %H:%M:%S"
        )

        if ip not in failed_times:
            failed_times[ip] = []

        failed_times[ip].append(timestamp)

for ip, times in failed_times.items():

    times.sort()

    for i in range(len(times) - 2):

        difference = (
            times[i + 2] - times[i]
        ).total_seconds()

        if difference <= 30:
            print("ALERT:", ip)
            print("3 failed logins in", difference, "seconds")
            break