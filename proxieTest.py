import requests


# targetUrl = "http://baidu.com"
#

# proxyHost = "58.243.28.38"
# proxyPort = "4270"
#
# proxyMeta = "http://%(host)s:%(port)s" % {
#
#     "host" : proxyHost,
#     "port" : proxyPort,
# }
#
# #pip install -U requests[socks]  socks5代理
# # proxyMeta = "socks5://%(host)s:%(port)s" % {
#
# #     "host" : proxyHost,
#
# #     "port" : proxyPort,
#
# # }
#
# proxies = {
#
#     "http"  : proxyMeta,
# }
resp = requests.get(url = 'http://webapi.http.zhimacangku.com/getip?num=20&type=1&pro=&city=0&yys=0&port=1&time=3&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=')
ip = resp.text.replace('/r/n', ' ').split()
print(ip)