import requests

def request_with_data():
    url = "https://app.qr-code-generator.com/create/handlecodesubmit"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://app.qr-code-generator.com",
        "priority": "u=0, i",
        "referer": "https://app.qr-code-generator.com/create/getform/add/url",
        "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "cookie": "optimizelyEndUserId=oeu1723918626845r0.543833931537252; OptanonAlertBoxClosed=2024-08-17T18:17:12.548Z; _gcl_au=1.1.2039956685.1723918633; _fbp=fb.1.1723918633411.262095937949773802; _pin_unauth=dWlkPU5URTNNakV6WVdJdE0ySmhaQzAwWkRVM0xXSmtaVEV0T0RGbVkyTXhPV013Tm1GaA; _hjSessionUser_1256611=eyJpZCI6ImNlNWUwZTU2LWJhMDYtNTc0ZC05YTczLWQ0MjY1MGZjYjVhYyIsImNyZWF0ZWQiOjE3MjM5MTg2MzMyOTUsImV4aXN0aW5nIjp0cnVlfQ==; sp=a3d28c26-87db-4efa-b80a-acc457636ee9; intercom-device-id-u4ys98rc=df9a9464-7381-4017-b82e-d6da0fd2e5ea; _hjSessionUser_1177107=eyJpZCI6IjMxNzJiNGVhLTQ5OWMtNTA0Mi05ZjQyLTljNjdiNmEzMTdmZCIsImNyZWF0ZWQiOjE3MjU3Mzk3NDM5MjUsImV4aXN0aW5nIjp0cnVlfQ==; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Sep+10+2024+01%3A02%3A56+GMT%2B0700+(Western+Indonesia+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=c0c17099-dc4b-4cb1-98c8-f640d6013cf5&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1&geolocation=ID%3BJT&AwaitingReconsent=false; _uetvid=ecf905205cc411ef9207139ab4309d48; _clck=1g97t3o%7C2%7Cfp2%7C0%7C1690; YII_CSRF_TOKEN=a0c76c77da8c3edb6450a3b443c41fa159777422s%3A40%3A%2200340cfc1147c5697cf4e3ab626d8114c3c065ff%22%3B; _gid=GA1.2.1772912544.1726928638; show_news_till=1b8eec6c9098a3a9bc7f98f65862db0ce47e155di%3A1%3B; mp_270c28de5852901160a9df5f882c6b7d_mixpanel=%7B%22distinct_id%22%3A%20%2237829098%22%2C%22%24device_id%22%3A%20%22191618fa7fe1021-050de0922fb29a-26001e51-190140-191618fa7fe1021%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Flogin.qr-code-generator.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22login.qr-code-generator.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Flogin.qr-code-generator.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22login.qr-code-generator.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%2237829098%22%7D; intercom-session-u4ys98rc=bHZHdnFBME5zTzNwWXVWWW1OMnpFRjVlaG5TU25pU0NhNWZhNlh0K2RmOS9UZzBZb0lXZVlGdmgvdDdUMGQ4ci0tbXo1c2pWcVVTaWErL3ZpeDc1U3FwUT09--0dcfe46069ee0140af40bacdc3fc30b7824faad8; _sp_ses.c4d1=*; CognitoIdentityServiceProvider.48n928qm6dfudrvb8r21j27tip.lljpt753868%40mailnesia.com.idToken=eyJraWQiOiJLZGI3dW9PXC92RzZtR3NGVE5MUCtkTjFOUExDN29NRGphVmRwYjlqK004dz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIwZmU3ZGRhZS02MDk2LTQxYTktYTA5NS05YjA2Yzg4NzA3MTgiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtd2VzdC0xLmFtYXpvbmF3cy5jb21cL2V1LXdlc3QtMV82Z0RmZjBlVnciLCJjb2duaXRvOnVzZXJuYW1lIjoiMGZlN2RkYWUtNjA5Ni00MWE5LWEwOTUtOWIwNmM4ODcwNzE4IiwiY3VzdG9tOmxhbmd1YWdlX2NvZGUiOiJlbiIsImF1ZCI6IjQ4bjkyOHFtNmRmdWRydmI4cjIxajI3dGlwIiwiZXZlbnRfaWQiOiI5NWMzZjcyOC1iYzM4LTRkM2YtYjBiZC1lZDYyOGRkZWM1ZWIiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTcyNzAyOTIxMiwiY3VzdG9tOnNpZ251cF9jb3VudHJ5IjoiSUQiLCJleHAiOjE3MjcwMzI4MTIsImlhdCI6MTcyNzAyOTIxMiwiZW1haWwiOiJsbGpwdDc1Mzg2OEBtYWlsbmVzaWEuY29tIn0.Um2Myu9KSp7obQIImHs5Jj6AKf-BJeDPGBrfmXHmyuajfM5gvsLE4JP_0Ub902Fvid2o3ads5q1m6lJd3Ixxu5xzRSTI_la_JRbXLRNJhOWfp8B3ImJH_7LOfIsBh4kRYsuw8I9kBZ10bC5AaZzQ4FL-5o5Zlaixk7CArpjfp2UfqlfoEe51TCwIQ97UCXgjxPf4wUoU4UaeWEx4xlB6mlT6MV5aSBehhbfFor2fD-02nKSi3lJGUBCmgfBKSbqWlZp21CckfOYfeKGh-6WwiSP00JWBqbzUa6-dVVB20j-MltLGCM0B9ap_VarC9QxXlT7A-EA9RERsfjo8jEJDKQ; CognitoIdentityServiceProvider.48n928qm6dfudrvb8r21j27tip.lljpt753868%40mailnesia.com.accessToken=eyJraWQiOiJscVVyc2d2elhaTkpCZ01VNzZiWEVzUmlmQzBxT0dkRUxOV1VcL2xDUFJrUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIwZmU3ZGRhZS02MDk2LTQxYTktYTA5NS05YjA2Yzg4NzA3MTgiLCJldmVudF9pZCI6Ijk1YzNmNzI4LWJjMzgtNGQzZi1iMGJkLWVkNjI4ZGRlYzVlYiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3MjcwMjkyMTIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5ldS13ZXN0LTEuYW1hem9uYXdzLmNvbVwvZXUtd2VzdC0xXzZnRGZmMGVWdyIsImV4cCI6MTcyNzAzMjgxMiwiaWF0IjoxNzI3MDI5MjEyLCJqdGkiOiJhMGExZjI3My1kMDk4LTRhZDctYmM0ZS1mZDBkMWJlYTU0YmMiLCJjbGllbnRfaWQiOiI0OG45MjhxbTZkZnVkcnZiOHIyMWoyN3RpcCIsInVzZXJuYW1lIjoiMGZlN2RkYWUtNjA5Ni00MWE5LWEwOTUtOWIwNmM4ODcwNzE4In0.aUL5aj2CzdYcKrQhXcQetuLciLSlUjFb24aByPbIre2WOnfdlwQNDNnda5L7frzu8DnSEW9zelFGcTCaZn9Ir7A6TsJZ-O6Sc2EwAEebrw8ONkwbfbWf5UdL6EWtF-NbIIWTgJp-2oBZ3KthAaRmKtMy9isGKY5jdD95f1d8_WXtU2haVIE-3SmxeKFjHyiFP8wD8-0aHO5Yx222DaEwqDcQSMGh7R7nl5WHnhw7-GRoMv7g1dKg_B5PLmEjNhOZ00MW4iqRSbk53Wv3tetOizBpNbGANLIEcRjTIQb0XVc-bat1icEOxmYOmzGygq7rfkQEhait1jHMcG1UCeY5Kw; CognitoIdentityServiceProvider.48n928qm6dfudrvb8r21j27tip.lljpt753868%40mailnesia.com.refreshToken=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.E9tYV6-yxazryJL_9OggORHC5ho902UUEZlllUSCgd_0EzGjqb7bfagqVbWKFoTTgulH8SeqdBZkCWnmfV4diy6yxwmYX4IiTfgTYiegqHXIDd6MZ0aUBU-4xv_L4_bGHxfJzB8nnLDui4E1vsu-6_oW-8bCjPGVG0DFpUBLrwb2saXewZIcG-bj5DuHYBqxWfV8Kt_kXIzN7ZdKL8PCaxoeh4JFU9JOX3ekqd830bwMwJMtVQIeUObxmLTzF6Q0nfYtPkWAQGKVsVORjhxULOdMKfe_AmqdH-IGw4VuzfjSg6MGIW1BIcPLZOGDH_fKME8AVU9GRh2z79ZEZju5cw.pfz42wF0BfV0IsAk.a41Zsymz7vAsO7fWYYLQi0mqPKzunmKtRXpKVCy8n0Zs--tozObzTeU1fqXPvfmua8R7bhOvlOxyBurUA8CBRrhwlVNvflqJ5yVEe4B2Jjgg8w--DS9FovzWs-JJcL3izj-_BnMn1lzen9DqZDAAM9JFacBbqQb5SDoC46biRjDFrhxjZLLGLvRRvDwFw1wvtnxsztXetFEzvSRVLYa5LldHDmRoyARjWaSi6ioHd21yowL5jTcmyCr8NSot6impFo8L8hy4b3fd5WrUBtp5lX0Zse_uPT6zHHyL-zn6wv8_AsEmu5jdRrhQC2oZVnGrfmJcjFjsTPJH-9TuUuTQ5NcZ28-EFYdCLCUdeMM2IaB2-VkV4RXx4cbHl2kHREpE4xSzimnqlTl3QB8A7n27Z6Kba4J-kLzqpQ2zaTHBgjp4wN_M4o_iqvDrThigf4lUZFju0XlYxy3sF14p1yLMtQ7sW_1eRTtZ-mc3QRglonv8eA6ytpYM76C7-H0BiFc94sadvFHMRlbSGnsS9VWfj9oJsuRyiF2ZXxyOmVgIGoHGZApOAkVyGBhAIt7khw8zpVcSxdCF8BbCfWFE_aMT6fC5SDtHzn9qw9Pq1J9oEc_HYAVIZIxjhXDZkHbHJp9TgqAbQeRLt70ZpHprWHx1eeVHeHxI2l2RbOTzhD3ZsyiszwAH92SjU09lO6G7lDGdKefNjeOHU0Bp-hxQXHoNKXnAvQhp8cXQO0qAYAaf-3a5nETAenoLGSgNo-49odrAZDv8xHlaYzFEaSoadPp-y0HDhl3AkbIczeyUWlgLXVrL6exROpJBFl0r4aXpuYvCdWlWBQgpxAhuf29lzpyFziWIfYECBCtEBxDc_TT1KC84u-wS7gwg1WwQJjHd020bMBwkZhSRXsfPxbTSUIXTM8znZb3n7l5uVX9dZVCiycxPZv1iApYsKZ2rhaq5uIx3xiImp51nwpFNaFFMlO9hg3Bz9H46bbi7gwl6rCiCgeqGKBnpEjWtJcwQXsUloZ92lfZwaPJQem-7nmVbwV7SDDstgMhtL0ywVq79q62I5aqsrbpMocJ9dLekekh-NexhZInnR4AyFyZCxrI1_tEUe6FJ-2iU-_ZJVePZ4ZbjYkCNInyEwGSWWAivHt57AEQ9ONByPqP5k5Yn5kFgM292x2LArgkWKRhLFMui_P-S6ZZCXGNpMWm8vKvVb10J9WmPVTzq12WXCIVAiGAhKaw7yV8wSkHRRgrF-d3e5axzKJigsstszAbSopOZoGDYPLvzVo3h3UBk5y9G1XFSI_H_AsgYce2p60Zj2RgOxSyvlim9Depg2W2MQxzhcg.vofNceZxo2nRE-6RE7f5uA; CognitoIdentityServiceProvider.48n928qm6dfudrvb8r21j27tip.lljpt753868%40mailnesia.com.clockDrift=0; CognitoIdentityServiceProvider.48n928qm6dfudrvb8r21j27tip.LastAuthUser=lljpt753868@mailnesia.com; CognitoIdentityServiceProvider.48n928qm6dfudrvb8r21j27tip.lljpt753868%40mailnesia.com.userData={%22UserAttributes%22:[{%22Name%22:%22sub%22%2C%22Value%22:%220fe7ddae-6096-41a9-a095-9b06c8870718%22}%2C{%22Name%22:%22custom:signup_country%22%2C%22Value%22:%22ID%22}%2C{%22Name%22:%22custom:language_code%22%2C%22Value%22:%22en%22}%2C{%22Name%22:%22email%22%2C%22Value%22:%22lljpt753868@mailnesia.com%22}]%2C%22Username%22:%220fe7ddae-6096-41a9-a095-9b06c8870718%22}; amplify-signin-with-hostedUI=false; language=6b0d41ab40b8c4a7ce9631cfa7e1fef4a2a42406s%3A2%3A%22en%22%3B; SiteSession=70550253d16c7c2ca8f8d9715f5ee5e8; 36dec7038009863fa18feb5363eb8728=1191fe64357ce9b61ee4ff56eb8b47626eef7127s%3A126%3A%22af1daa104dd468c0a0306368eb0aa08e61dc1b92a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2237865529%22%3Bi%3A1%3Bs%3A25%3A%22lljpt753868%40mailnesia.com%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D%22%3B; AWSALB=dOS0dXYnmN+4mun4syyBGcoxPa2hl3D7vciZWutOR9L6u3+CwUjtZV+7CasBcqOzI8xMHlIH/l7nAZe66HB1B3WTMGqStg3aDc9nZBWEseP/rV1DMEL8x5Xhn/TN; AWSALBCORS=dOS0dXYnmN+4mun4syyBGcoxPa2hl3D7vciZWutOR9L6u3+CwUjtZV+7CasBcqOzI8xMHlIH/l7nAZe66HB1B3WTMGqStg3aDc9nZBWEseP/rV1DMEL8x5Xhn/TN; vue_app_access_token=yCqMeZOoAq708oDFH8-lPS3N8wA2yuGVdFfZgphs7Sx7a6Y0oNCn0JO5C-lipibI; _sp_id.c4d1=89be636f-18ed-4e0b-bc4c-fcaac43381d9.1723918627.37.1727029216.1726959389.63139559-15c0-4335-877a-4c4dee443303.c540d55b-65d5-4609-9931-b8e9a9984100.92603f2b-a3be-4810-8021-73017e114f5b.1727029216069.1; _ga_8YZ6XFRQHW=GS1.1.1727029199.39.1.1727029216.43.0.0; _ga=GA1.2.1855462778.1723918633; _gat_UA-4909985-36=1; _hjSession_1177107=eyJpZCI6IjZiYTgxMGI5LTI5ZWUtNDliNC1iODRkLWFiZjdiMWRiYmIxMiIsImMiOjE3MjcwMjkyMTY1NDMsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    
    loop_count = int(input("Masukkan jumlah looping yang diinginkan: "))
    url_input = input("Masukkan URL yang ingin dibuat shortlink: ")
    
    for i in range(1, loop_count + 1):
        data = {
            "YII_CSRF_TOKEN": "00340cfc1147c5697cf4e3ab626d8114c3c065ff",
            "codeValue": "%21",
            "oldCodeId": "0",
            "UrlBarcode[qrcode_type_id]": "1",
            "UrlBarcode[folder_id]": "1",
            "UrlBarcode[industry_id]": "",
            "UrlBarcode[qr_demo_id]": "",
            "UrlBarcode[designer_templates_id]": "0",
            "UrlBarcode[app_templates_id]": "0",
            "UrlBarcode[trackable]": "1",
            "UrlBarcode[user_id]": "",
            "UrlBarcode[active]": "1",
            "UrlBarcode[trash]": "0",
            "UrlBarcode[filename]": "",
            "UrlBarcode[total_scans]": "0",
            "UrlBarcode[unique_scans]": "0",
            "UrlBarcode[_record_id]": "0",
            "UrlBarcode[json_data]": "{}",
            "downloadIndicatorName": "no",
            "UrlBarcode[back_color]": "ffffff",
            "UrlBarcode[front_color]": "000000",
            "UrlBarcode[error_correction]": "M",
            "UrlBarcode[title]": f"{i}",  # Menggunakan nomor urutan dari loop
            "UrlBarcode[geolocation]": "0",
            "UrlBarcode[url]": url_input
        }

        response = requests.post(url, headers=headers, data=data)
        
        if response.status_code == 200:
            if "Code added successfully" in response.text:
                print("Short Berhasil Dibuat")
            else:
                print("Gagal memuat shortlink")
                print(response.text)
        else:
            print("Failed to access the desired page.")

# contoh penggunaan
request_with_data()
