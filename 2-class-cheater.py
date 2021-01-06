from json import dumps, loads
from urllib.request import Request, urlopen

raise Exception('请把COOKIE改成自己的，然后删掉这句话')
COOKIE = ''

##switcher = {
##        '0' : 'A',
##        '1' : 'B',
##        '2' : 'C',
##        '3' : 'D'
##}
##def main_func1():
##    cid = input('请输入考试ID: ')
##    num = 0
##    test_paper = get_test_paper(cid)
##    for question in test_paper['data']['testPaperList']:
##        answer = question['answer']
##        if question['examType'] == 'single':
##            print("题目%d: %s" % (num, switch(answer)))
##        elif question['examType'] == 'multiselect':
##            answers = answer.split(',')
##            print("题目%d: " % num, end = '')
##            for a in answers:
##                print(switch(a), end = '')
##            print()
##        num += 1

def main_func2():
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Cookie': COOKIE
    }
    for cid in range(1,600):
        try:
            req = Request('https://www.2-class.com/api/exam/getTestPaperList?courseId=%s' % cid, headers = headers)
            test_paper = loads(urlopen(req).read().decode())
            num = 0
            data = []
            for question in test_paper['data']['testPaperList']:
                data.append({
                        'examId': num + 1,
                        'answer': question['answer']
                })
                num +=1
            req_data = {
                'courseId': cid,
                'exam': 'course',
                'examCommitReqDataList': data,
                'reqtoken': '00000000-0000-0000-0000-000000000000'
            }
            req = Request('https://www.2-class.com/api/exam/commit', data = dumps(req_data).encode(), headers = headers)
            res = urlopen(req).read().decode()
            print("考试ID %s: 成功" % cid)
        except Exception as e:
            print("考试ID %s: 失败" % cid)

def get_cookie():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    req = Request('https://2-class.com', headers = headers)
    res = urlopen(req).headers['set-cookie'].split(';')
    return res

##def login(un, pw):
##    headers = {
##        'Content-Type': 'application/json; charset=utf-8'
##    }
##    req_data = {
##        'account': un,
##        'password': pw,
##        'checkCode': '',
##        'codeKey': '',
##        'reqtoken': '00000000-0000-0000-0000-000000000000'
##    }
##    req = Request('https://www.2-class.com/api/user/login', data = dumps(req_data).encode(), headers = headers)
##    cookies = urlopen(req).headers['set-cookie'].split(';')
##    return cookies[0]
    

##def switch_1(answer_id):
##    return switcher_1.get(answer_id, '答案无效')

if __name__ == '__main__':
    main_func2()
##    while(1):
##        try:
##            main_func1()
##        except Exception as e:
##            print(e)
