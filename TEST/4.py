def solution(program, flag_rules, commands):
    answer = []
    alias = []
    rule_dict = {}
    for flag_rule in flag_rules:
        rule = flag_rule.split()
        if 'ALIAS' in rule:
            alias.append(rule)
        else:
            # flag_name과 argument type을 Dictionary 형태로 저장
            key = rule[0]
            value = rule[1]
            if rule[0] not in rule_dict.keys():
                rule_dict[key] = value
    alias_dict = {}
    for ali in alias:
        key = ali[2]
        value = rule_dict[key]
        rule_dict[ali[0]] = value
        alias_dict[ali[0]] = 0
        alias_dict[ali[2]] = 0
    # 각 command를 띄어쓰기 단위로 구분
    for command in commands:
        # 마지막 단위 점검 위한 -end 삽입
        command += ' -endendend'
        isCorrect = True
        arr = command.split()

        for ali in alias:
            a = arr.count(ali[0])
            b = arr.count(ali[2])
            if (a+b) >= 2:
                isCorrect = False
                continue

        # 첫번째 인자가 program과 일치하는지 여부 확인, 일치하지 않을 경우 False
        if arr[0] != program:
            isCorrect = False
            answer.append(isCorrect)
            continue
        # 두번째 인자부터 인자에 '-'가 있는 경우 key 경우 없는 경우 type
        arr_name = ''
        arr_type = []
        for idx in range(1, len(arr)):
            if '-' in arr[idx]:
                isFlag = True
                for tp in arr_type:
                    if rule_dict[arr_name] == 'NUMBERS':
                        if type(tp) != type(1):
                            isFlag = False
                            break
                    elif rule_dict[arr_name] == 'NUMBER':
                        if len(arr_type) >= 2:
                            isFlag = False
                            break
                        if type(tp) != type(1):
                            isFlag = False
                            break
                    elif rule_dict[arr_name] == 'STRINGS':
                        if type(tp) != type('string'):
                            isFlag = False
                            break
                    elif rule_dict[arr_name] == 'STRING':
                        if len(arr_type) >= 2:
                            isFlag = False
                            break
                        if type(tp) != type('string'):
                            isFlag = False
                            break
                    elif rule_dict[arr_name] == 'NULL':
                        if len(arr_type) != 0:
                            isFlag = False
                            break
                if isFlag == False:
                    isCorrect =False
                    break

                # 판단 후 초기화
                arr_name = arr[idx]
                arr_type = []
            else:
                if arr_name == '':
                    isCorrect = False
                    break
                # 여러 개 들어올 경우 숫자는 int 전환, 문자는 그대로 하여 리스트삽입
                try:
                    arr[idx] = int(arr[idx])
                except:
                    arr[idx] = arr[idx]
                arr_type.append(arr[idx])

        answer.append(isCorrect)
    print(answer)
    return answer


# solution('line', 	["-s STRINGS", "-n NUMBERS", "-e NULL"],["line -n 100 102 -s hi -e", "line -n id pwd -n 100"])
# solution('trip', 	["-days NUMBERS", "-dest STRING"],["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"])
# solution('bank', 	["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"])
solution("line", 	["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"], ["line -n 100 -s hi -e", "line -n 100 -e -num 150"])
