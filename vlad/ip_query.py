# -*- coding: UTF-8 -*-
# 文件名：ip_query.py
# 使用网站接口 https://ipchaxun.com/


import requests
import socket

_EMO = ' Σ( ° △ °|||)︴'
_EMO1 = ' ヾ(￣O￣)Bye~Bye~ '


def _get_contents(text):
    ''' 
    内容按行切片
    '''
    lst = []
    if(type(text) == str):
        a = str.split(text, '>')
        for i in a:
            if (not str.startswith(i, '<')):
                lst.append(i[:-6])
    return lst


def _get_district(text):
    '''
    提取有用信息
    '''
    dct = {'my_ip': '妹', 'home': '找', 'inc': ('到' + _EMO)}
    if(type(text) == str):
        a = str.split(text, '\n')
        for i in a:
            if str.startswith(i, '<span class="name">归属地：'):
                s = ''
                k = _get_contents(i)
                for i in k:
                    s += i
                dct['home'] = s
            elif str.startswith(i, '<span class="name">iP地址：'):
                s = ''
                k = _get_contents(i)
                for i in k:
                    s += i
                dct['my_ip'] = s
            if str.startswith(i, '<label><span class="name">运营商：'):
                s = ''
                k = _get_contents(i)
                for i in k:
                    s += i
                dct['inc'] = s
    return dct


def get_url():
    '''
    创建 get 请求并将返回的信息输出到控制台
    '''
    ip = '222.222.222.222/'
    url = 'https://ipchaxun.com/'
    ip = input("请输入ip地址：\n")
    print('----------------------------')
    dct = {}
    try:
        r = requests.get(url + ip, headers={'user-agent': 'Chrome/10'})
        if (r.status_code == 200):
            dct = _get_district(r.text)
            for i in dct:
                print(dct[i], end=' ')
            print('\n----------------------------\n好耶！'+_EMO1)
        else:
            print('未知错误！')
            return get_url()
    except:
        # 如果出错请先尝试获得返回体的文本
        return get_url()


if (__name__ == '__main__'):
    get_url()

del(_EMO, _EMO1, _get_contents, _get_district)
