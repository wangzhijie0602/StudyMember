import requests
import json

def undone(dict):
        return None


def get_image():        #获取验证码图片
        global cookie,header
        cookie = {
                "NOCC_TOKEN": "EFUxN0lQiHKRED3acnLkK0bm0Cl29en4",
                "NOCC_SIGN": "bea518bdd869ad8519d12b342ea2667c8db9e552",
                "NOCC_T": "2110201737",
                "security_session_verify":"55bb5ddba9e734221d2aa64d8f8b61a9",
                "PHPSESSID":"0c51ff689d3ff6a533a29ef33e2232f1"
                }
        header = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                "referer": "https://bghb.54heb.com/",
                "origin": "https://bghb.54heb.com",

                }
        url = "https://bgapi.54heb.com/login/verify"
        r = requests.get(url,cookies= cookie,headers= header)
        r.encoding = "utf-8"
        return r.content
        

def get_token(verify):
        url = "https://bgapi.54heb.com/admin/login"
        data = {
                "account": "18003233003",
                "pass": "7176ce",
                "verify": verify,
                "is_quick": "0"
                }
        token = requests.post(url,headers = header,data = data,cookies = cookie)
        return token


def get_member(token,page,r):

        url = "https://bgapi.54heb.com/" + r
        header = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                "referer": "https://bghb.54heb.com/",
                "origin": "https://bghb.54heb.com",
                "token":token
                }
        param = {
                "page": page,
                "rows": "20",
                "keyword": "",
                "oid": "100518991",
                "leagueStatus": "",
                "goHomeStatus": "",
                "memberCardStatus": "", 
                "isPartyMember": "",
                "age_type": "",
                "ageOption": "",
                "isAll": ""
                }

        a = requests.get(url,params = param,headers = header,cookies = cookie)
        userDict = json.loads(a.text)
        return userDict


def main():
        global header,cookie
        cookie = {
                "NOCC_TOKEN": "EFUxN0lQiHKRED3acnLkK0bm0Cl29en4",
                "NOCC_SIGN": "bea518bdd869ad8519d12b342ea2667c8db9e552",
                "NOCC_T": "2110201737",
                "security_session_verify":"55bb5ddba9e734221d2aa64d8f8b61a9"
                }
        header = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                "referer": "https://bghb.54heb.com/",
                "origin": "https://bghb.54heb.com",
                }

if __name__ == "__main__":
    main()
