import sys
import datetime
sys.stdin = open('Tests data/test-input-01.txt', 'r')

time = '1995-10-13'
base_time = datetime.datetime.strptime(time, "%Y-%m-%d")
rule = ['.zip', '.rar', '.tgz']

def solution(S):
    # write your code in Python 3.6
    print(S)
    answer = 0
    Slist = S.split('\n')

    s_list = S.split()
    for i in Slist:
        s_list = i.split()
        nowtime = datetime.datetime.strptime(s_list[0], "%Y-%m-%d")
        isFlag = False
        for s in s_list:
            # 날짜 비교
            if nowtime.date() >= base_time.date():
                continue
            # 용량 비교
            if int(s_list[1]) >= 245760: # 240 * 2^10
                continue
            if s_list[2][-4:] not in rule:
                continue
            isFlag = True
        if isFlag:
            answer += 1
    print(answer)
    return answer

solution('1988-08-29        956 system.zip\n1976-09-16     126976 old-photos.tgz\n1987-02-03     118784 logs.rar\n1961-12-04  703594496 very-long-filename.rar\n1980-08-03          2 DELETE-THIS.TXT\n2014-08-23        138 important.rar\n2001-08-26     595968 MOONLIGHT-SONATA.FLAC\n1967-11-30     245760 archive.rar\n1995-10-13        731 file.tgz')
#
# while True:
#     try:
#         data = input()
#         solution(data)
#     except:
#         break