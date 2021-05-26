def solution(emails):
    toplevels = ['.com', '.net', '.org']
    answer = 0
    for email in emails:
        toplevel = email[-4:]
        if toplevel not in toplevels:
            continue
        before = email[:-4]
        if before.count('@') != 1:
            continue
        elif before.count('@') == 1:
            info_index = before.index('@')
            name = before[:info_index]
            domain = before[info_index+1:]
            isDomain = domain.islower()
            if isDomain == False:
                continue
            name = name.replace(".", "")
            if len(name) >= 1:
                isName = name.islower()
                if isName == False:
                    continue

            answer += 1


    return answer


print(solution(['...@a.com']))
