def getOpenApplications(commands):
    applications = []
    for command in commands:
        if command == "clear":
            applications.clear()
            continue
        command, subject = command.split()
        if command == "open":
            applications.append(subject)
        elif command == "close":
            if int(subject) > len(applications):
                applications.clear()
                continue
            for _ in range(int(subject)):
                applications.pop()
    return applications
                
if __name__ == '__main__':
    commands_count = 5
    commands = ["clear", "open firefox", "close 4", "open firefox", "open curl", "close 1", "clear", "open ps"]
    result = getOpenApplications(commands)
    print(result)
