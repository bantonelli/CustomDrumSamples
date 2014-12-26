__author__ = 'brandonantonelli'

import urllib, urllib2

def post():
    username = 'humbertozayas'
    password = '123456'
    client_id = "aR!omYsELvz.Jihdlfk-xUdkPpZ2f7qc9L415fV2"
    url = 'http://127.0.0.1:8000/o/token/'
    if (client_id == "aR!omYsELvz.Jihdlfk-xUdkPpZ2f7qc9L415fV2"):
        client_secret = "U_qMHU-cWBD58vu5DOcp3U0RO79t5zEfIdoF1Xn.E:FT_ztn2WsdAxfV_V@V0Ji?Wb=IQl:1xM!X8WTb9kIH-!!uu1PUS0XVpYr6DxwXeEgJlUFBwpS7co8xtB9!5CAC"
    values = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    #Authentication step something like --> user = auth.authenticate(username=username, password=password)
    # Need to make this access the next value from Url and Redirect there if login was successful
    return req

urllib2.urlopen(post()).read()