def ChromeHeaders2Dict(chrome_headers_str: str) -> dict:
    """

    :param chrome_headers_str:
    :return: dict
    """
    if not chrome_headers_str:
        return {}

    headers = {}
    item_list = chrome_headers_str.splitlines(keepends=False)
    for item in item_list:
        item_str = item.strip()
        if not item_str:
            continue
        if item_str.startswith(':'):
            continue
        key_value_pair = item_str.split(':')
        if len(key_value_pair) < 2:
            continue
        key = key_value_pair[0]
        value = ':'.join(key_value_pair[1:])
        headers[key] = value.strip()
    return headers


if __name__ == '__main__':
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
    h = ChromeHeaders2Dict(chrome_headers)
    print(h)
