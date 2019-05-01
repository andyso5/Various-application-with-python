#-*- encoding: utf-8 -*-#
import requests,bs4,time,os

def daily_bing_img(path):
    url = 'http://cn.bing.com/'
    try:
        res  = requests.get(url)
        res.raise_for_status()
        # if res.status_code == requests.codes.ok:
        bs = bs4.BeautifulSoup(res.content,features='html.parser')
        bg = bs.select('#bgLink,head > [href*="1980×1080"]')
        #理论上bg只有一个元素:Logically,just one element in variable bg
        img_href = bg[0].attrs['href']
        if not img_href:
            print('Wrong selector!')
            return False
        img_url = url + img_href
        img = requests.get(img_url)
        img.raise_for_status()
        img_name = time.strftime('%Y-%m-%d',time.localtime()) + '.jpg'
        abs_dir = os.path.join(path,img_name)
        if os.path.exists(abs_dir):
            abs_dir = abs_dir[:-4] + '(1)' + abs_dir[-4:]
        f_img = open(abs_dir,'wb')
        f_img.write(img.content)
        f_img.close()
    except Exception as exc:
        print('There is a problem:%s' % exc)
    else:
        return True

if __name__ == '__main__':
    path = r'C:\Users\Administrator\Desktop\test\bing'
    print(daily_bing_img(path))
    

