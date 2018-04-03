# CrawlerUtility

Simplify the development of your webcrawler

# Usage

## Common Utility

You can use this module without installing any third-part packages.

### ChromeHeaders2Dict

```
from CrawlerUtility import ChromeHeaders2Dict

chrome_headers = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Connection: keep-alive
    Cookie: BAIDUID=E40AF2FAEC8CB0F382A3A8F5F59AC44D:FG=1; BIDUPSID=E40AF2FAEC8CB0F382A3A8F5F59AC44D; PSTM=1513916193; BDRCVFR[C0-VKBuJmg_]=mk3SLVN4HKm; BD_CK_SAM=1; pgv_pvi=8525405184; pgv_si=s3529928704; FP_UID=5eea85cb6e65c4d7a9f0f7b9d23ff3cb; BDRCVFR[w2jhEs_Zudc]=I67x6TjHwwYf0; BD_UPN=123253; shifen[62291884541_98248]=1520672084; BCLID=11171094791344044520; BDSFRCVID=LNCsJeC62ZBf13rACvOD-ViSJHNR0mTTH6aoKULoKvtI-AUyiIRrEG0PqU8g0Ku-sN62ogKK0mOTHvbP; H_BDCLCKID_SF=tbKq_DLXf-bSK4b1-4QD2DCShUFsWU6m-2Q-5KL-yqothDO4Lfb-XU3D3xrgBfvwLJRL-UbdJJjoOU5shUR-5McDLJo8axcN-eTxoUJhQCnJhhvGqJbFj6DebPRiJPr9Qgbq3ftLK-oj-D-mD55P; PSINO=7; MCITY=-131%3A; BDUSS=Vdic1Z6WHhEaGhvSW1KflhWUVYwcFRhemI0RjhDdjVmcGF1bktaVkNWQnppZDVhQUFBQUFBJCQAAAAAAAAAAAEAAACoVyMi1MLC5F-zpLCyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHP8tlpz~LZac; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1993_1436_21094_18560_22157; sugstore=1; BDSVRTM=0
    DNT: 1
    Host: www.baidu.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
    '''
    headers_dict = ChromeHeaders2Dict(chrome_headers)
    headers_dict
```

## Scrapy Utility

If you want to use this module, you must install `Scrapy` first.

### AbuyunProxyMiddleware


Modify `settings.py` of your Scrapy project:

```
DOWNLOADER_MIDDLEWARES = {
   'ChromeHeaders2Dict.scrapy_utility.ScrapyUtility.AbuyunProxyMiddleware': 548,
}

ABUYUN_PROXY_SERVER = 'http://http-dyn.abuyun.com:9020' # must be set
ABUYUN_PROXY_USER = 'DWE2341LFOWQC4' # must be set
ABUYUN_PROXY_PASSWORD = '94SLIC1304C' # must be set
SPIDER_BEHIND_PROXY = ['BaiduSpider', 'QQSpider'] # list of spider name. if not set, all spider will be behind the proxy
SKIP_PROXY_KEYWORD = ['http://google.com', 'safeurl.com/aaa'] # the urls will not use proxy if they satisfy these pattern in the list,
```
