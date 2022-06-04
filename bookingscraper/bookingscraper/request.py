import requests


headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Cookie': '_pxhd=3TAk-RPVhxPScZ0hCHjCKycVtYuvhelps8R1dZh6d-DukdvBWfhHHia8%2FGkJ8BMBEir2BEiSbj4ssWi5UbvF4w%3D%3D%3AGP6VYWc2EvXmCfY5EU58e%2FbkjA2ZBzdPFF0S-n7xzYCFfMNjGCRAJJ%2FH7BYDuPpHdetIzYnECY96ZTRkiM6km97xdHRno03XXnPadzqOWD0%3D; cors_js=1; bkng_sso_session=e30; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1654259604363; BJS=-; _gid=GA1.2.1654469940.1654259608; _gat=1; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siYSI6MSwiaCI6IlZpcWN0Lzd6UmZKendvTlhReXdpUnhlYk81dzNEVFpCbjh1TzlWcThmbWsifV19; pxcts=f55e9fd5-e338-11ec-8499-444573415769; _pxvid=ef1700b8-e338-11ec-8f07-44496146687a; _pxff_ddtc=1; bkng_frontend_sese_exp=1; _px3=768b67bdab8068d3ad4d5028d4211f2766a356bb0ce075b376b8072af645705a:+rULh4x8oMpetdnXdCOw+AI7Jsl0msNTIGfpOA+Mp3ZB7NcdNrQws3dJSrEoS3QSOSdSNGgkMGn4gfS10Cvcmw==:1000:8o4ZgD/bBBBpgx7r1a1QBGoszC+fgZLXDjwHOSeB5A44QfA1JkyJZnhIckw2Zwo2ZhqL6rAH5ohQTXL/zFeTcC1K4fwf38l2DtVnMqU+6cVGY/K1A4E3FDEJNmtOIC6uSPquc2vGy1DucYdwbwlY5Io944M+sv6l10N1mnKsYIcmkJ/t3Zhrs1HBVeJgdo9vMzJSdanTzwA2nlNonBrqUQ==; _px_f394gi7Fvmc43dfg_user_id=NjA1MTNhZTAtZTMzOS0xMWVjLThmY2EtYjU0NGIxYjM1NTk2; _gcl_au=1.1.2084320253.1654259612; bkng_prue=1; _ga=GA1.1.1569637483.1654259608; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbXpFeYC4TUhDvvyKT5qqm2OjBIIv8pPkucqm9Jg2hsE1abzZDpOQiy%2FXpD%2FFQEOkMYBvTTyOpf48G4Gc2jlGja9AjiwAw1tGbQVxCjorCyPROqtCsrNizNVWBbRDk3JhbaEcxg2J8Sr%2BVrjip58lU%2FQy9%2BFwneQGqwPI8Tuax0bw%3D; _scid=36fa5d53-7382-4d7c-b9c8-fc226caa17d1; _uetsid=61d134e0e33911ecbfd4f1736ec5f2b0; _uetvid=61d1c760e33911ecb1dc1f6fece9372a; _pin_unauth=dWlkPU4yTTNaREJrWm1FdE1tSXdPQzAwTkRJMUxUazFNVEl0WlRJMFltSmtOR1poWW1RMQ; _sctr=1|1654185600000; has_preloaded=1; _pxde=ed906b9dbff68d7ab4e41818d604b4e0a91f3d01847edbe55598876c0a018ffb:eyJ0aW1lc3RhbXAiOjE2NTQyNTk0Njk5NzcsImZfa2IiOjAsImlwY19pZCI6W119; lastSeen=1654259654530; _ga_FPD6YLJCJ7=GS1.1.1654259612.1.0.1654259655.0',
	'Host': 'www.booking.com',
	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-User': '?1',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}


url = 'https://www.booking.com/searchresults.html?aid=304142&ss=United+Kingdom&nflt=ht_id%3D220'

response = requests.get(url, headers=headers)
print(response)