import json

headers = {
    'User‐Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome / 74.0.3729.169 Safari / 537.36'
}


def quote_get_demo():
    url = 'https://www.baidu.com/s?wd='
    url = url + urllib.parse.quote('小野')
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf‐8'))


def urlencode_get_demo():
    url = 'http://www.baidu.com/s?'
    data = {
        'name': '小刚',
        'sex': '男',
    }
    data = urllib.parse.urlencode(data)
    url = url + data
    print(url)
    request = urllib.request.Request(url=url, headers=headers)


# 1: get请求方式的参数必须编码,参数是拼接到url后面,编码之后不需要调用encode方法
# 2: post请求方式的参数必须编码,参数是放在请求对象定制的方法中,编码之后需要调用encode方法
def post_demo():
    url = 'https://fanyi.baidu.com/v2transapi'
    headers = {
    }
    data = {
        'from': 'en',
        'to': 'zh',
        'query': 'you',
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '269482.65435',
        'token': '2e0f1cb44414248f3a2b49fbad28bbd5',
    }
    # 参数的编码
    data = urllib.parse.urlencode(data).encode('utf‐8')
    # 请求对象的定制
    request = urllib.request.Request(url=url, headers=headers, data=data)
    response = urllib.request.urlopen(request)
    # 请求之后返回的所有的数据
    content = response.read().decode('utf‐8')

    # loads将字符串转换为python对象
    obj = json.loads(content)
    # python对象转换为json字符串 ensure_ascii=False 忽略字符集编码
    s = json.dumps(obj, ensure_ascii=False)
    print(s)


def proxy_demo():
    url = 'http://www.baidu.com/s?wd=ip'
    request = urllib.request.Request(url=url, headers=headers)
    proxies = {'http': '117.141.155.244:53281'}
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode('utf‐8')
    with open('daili.html', 'w', encoding='utf‐8') as fp:
        fp.write(content)
