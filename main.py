import pandas as pd



from utils.extracthtml import getHtml 


flipcarturl='https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptops&requestId=4d07eac9-3d28-46d6-bbf3-678c4593d8ef'

flipcartheader={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",

    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-full-version": "\"131.0.6778.110\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"131.0.6778.110\", \"Chromium\";v=\"131.0.6778.110\", \"Not_A Brand\";v=\"24.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "T=TI172192139846800123630733725711414117439322330234541628468814232935; K-ACTION=null; ud=8.icdr18KS5w96Lsef0YQs017tyR0Jeg1v5rvak7rYLIoFos2f_0NU1SSQgcaK9NqltoCc7R66dyBjQhHHPKcBeEDNCFqqW0CDkXF8Ylo_SBraouR1yREfAnqf7VV3DeoOQ21wMUnfsoYk8sy_Jly5_g; vh=633; vw=966; dpr=1; rt=null; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MzU2NjI2NTQsImlhdCI6MTczMzkzNDY1NCwiaXNzIjoia2V2bGFyIiwianRpIjoiMDkwNDcyMWMtNGI0Zi00NDZkLWJlMDYtYTc3NTliMWVkMzMyIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzIxOTIxMzk4NDY4MDAxMjM2MzA3MzM3MjU3MTE0MTQxMTc0MzkzMjIzMzAyMzQ1NDE2Mjg0Njg4MTQyMzI5MzUiLCJrZXZJZCI6IlZJQkEzMDJFOEMyRjg1NDcyMDlGQTMxRkRBOUIxRTcyODgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.3-LzA5O8PU2KnUld2eGIE4YJK_lljdVBjJ8AEsyOeGw; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20069%7CMCMID%7C77362217746442230322061457935204961284%7CMCAAMLH-1734539457%7C12%7CMCAAMB-1734539457%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1733941857s%7CNONE%7CMCAID%7CNONE; qH=c06ea84a1e3dc3c6; vd=VIBA302E8C2F8547209FA31FDA9B1E7288-1729133267864-4.1733997288.1733997288.154670937; Network-Type=4g; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Alaptops-store%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fsearch%25253Fq%25253Dlaptops%252526as%25253Don%252526as-show%25253Don%252526otracker%25253DAS_Query_TrendingAutoSuggest_1_0%2526ot%253DA; S=d1t11Wz8pP3QZPz8/dD8/Pz8/Ad4BQbb8r3HwEwx6MHhnkA+TnNpDSB0Bp3mDmZTacjfmBWB+y8OIvKHDa8FQjokVnw==; SN=VIBA302E8C2F8547209FA31FDA9B1E7288.TOK5D9A61C4EC3F44AFBA17FF43533344AE.1733997337158.LO"

}


if __name__=='__main__':



    flipdata= getHtml(websiteurl=flipcarturl,showbrowser=False,screenshotname='lp4')

    laptopdetails=[]

    for flip in flipdata.css('div[class="tUxRFH"]'):
        images=flip.css_first('[loading="eager"]')
        if images:
            allimages={
                'src':images.attrs.get('src',''),
                'alt':images.attrs.get('alt','')
            }
        else:
            allimages={'src':None,'alt':None}

        fliptitle=flip.css_first('div[class="KzDlHZ"]')    
        fliptitle=fliptitle.text() if fliptitle else None


        fliprating=flip.css_first('span > div[class*="XQDdHH"]')
        fliprating=fliprating.text() if fliprating else None

        Flipreview=flip.css_first('span[class*="Wphh3N"] ')
        Flipreview=Flipreview.text() if Flipreview else None

        laptopdetail=flip.css_first('ul[class*="G4BRas"]')
        laptopdetail=laptopdetail.text() if laptopdetail else None

        laptopprice=flip.css_first('div [class*="Nx9bqj"]')
        laptopprice=laptopprice.text().replace('₹','').replace(',','') if laptopprice else None


        discount=flip.css_first('div[class*="yRaY8j ZYYwLA"]')
        discount=discount.text().replace('₹','').replace(',','') if discount else None

        dispercentage=flip.css_first('div[class="UkUFwK"]')
        dispercentage=dispercentage.text() if dispercentage else None




        laptopdata={
            'Images':allimages,
            'Title':fliptitle,
            'Rating':fliprating,
            'Review':Flipreview,
            'Details':laptopdetail,
            'Price':laptopprice,
            'discount':discount,
            'percentdis':dispercentage

        }
        
        
        laptopdetails.append(laptopdata)

laptopdf=pd.DataFrame(laptopdetails)    
laptopdf.to_csv('flipdata2.csv',index=False)    

       
        



        
       

    
    
    