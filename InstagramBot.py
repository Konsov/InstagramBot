from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from random import randint

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        profile = webdriver.FirefoxProfile()
        #options = Options()
        #options.add_argument('--headless')
        
        
        profile.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16")
        self.driver = webdriver.Firefox(profile)#,options=options)

    def closeBrowser(self):
        self.driver.close()

    def login(self):
       driver = self.driver
       driver.get("https://www.instagram.com/") #andare sulla homepage
       time.sleep(2)
       login_button = driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]')   #andare sulla schermata di log
       login_button.click()
       time.sleep(2)
       user_name_space = driver.find_element_by_name("username")  #impostare nome e password 
       user_name_space.clear()
       user_name_space.send_keys(self.username)
       time.sleep(2)
       password_space = driver.find_element_by_name("password")
       password_space.clear()
       password_space.send_keys(self.password)
       time.sleep(2)
       password_space.send_keys(Keys.RETURN)
       time.sleep(5)
       try:
         driver.find_element_by_xpath('//a[@class="_3m3RQ _7XMpj"]').click()   #saltare richiesta download app e richiesta notifiche
       except:
          print("nessuna richiesta di download app")
       time.sleep(5)
       try:
         driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
       except:
          print("nessuna richiesta di notifiche")
       time.sleep(2)

    def bot_by_hashtag(self, hashtag, secLike, probFollow):                                     
        driver = self.driver                                                                      #cerco by hashtag
        driver.get("https://www.instagram.com/explore/tags/" + hashtag +"/")                      
        print("Start looking for photos by #" + hashtag +  " at: " + str(time.strftime("%H:%M:%S")))         #stampo ora inizio bot per hashtag
        time.sleep(2)
    
        for _ in range(2):                                                                      #scrollo 2 volte la pagina
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        hrefs = driver.find_elements_by_tag_name('a')                                            #metto tutte le foto che ho caricato in un array,
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]                               #di cui tolgo le prime 14 perchè di pagine famose e non di utenti
        pic_hrefs = [href for href in pic_hrefs if "/p/" in href]
        print("#"+hashtag + " all photos: " + str(len(pic_hrefs)))
        
        if len(pic_hrefs) > 14:
           for _ in range(14):
               pic_hrefs.pop(0)
        print("#" + hashtag + " user photos: " + str(len(pic_hrefs)))
                
        follows = 0                                                                                      #metto like e follow alle foto nell'array
        likes = 0
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            try:
               driver.find_element_by_xpath('//button[@class="dCJp8 afkep _0mzm-"]').click()
               likes = likes + 1
               print("Like on photo: "+ pic_href + " at: " + str(time.strftime("%H:%M:%S")))
               time.sleep(secLike)
            except:
                print("Photo not available")
                time.sleep(2)

            prob = randint(1, probFollow)
            
            if (prob == 1):
               try:
                following =  driver.find_element_by_xpath('//a[@class="FPmhX notranslate nJAzx"]').text
                print("Start to follow: " + str(following) + " at: " + str(time.strftime("%H:%M:%S")))
                time.sleep(2)    
               except:
                print("Error: Can't print the following")
                time.sleep(2)
             
               try:
                  driver.find_element_by_xpath('//button[@class="oW_lN _0mzm- sqdOP yWX7d        "]').click()                  
                  follows = follows + 1
                  time.sleep(2)
               except:
                print("Already Follower")
                time.sleep(2)

        print("Bot on hashtag #" + hashtag +  " ends at: " + str(time.strftime("%H:%M:%S")))   
        nLikesFollows = [likes, follows]
        return nLikesFollows

    def goToFollowing(self,username):
        driver = self.driver                                                                      
        driver.get("https://www.instagram.com/" + username)
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//a[@href="/dailymicio/following/"]').click()      
        except:
            print("Error: unable to view following")
        time.sleep(5)

    def unFollow(self,nUnfollow):
        driver = self.driver
        try:
            if(nUnfollow > 24):         
                nScrolls = (nUnfollow - 24) // 12 + 1
            else:
                nScrolls = 0
            print(str(nScrolls))  
            scr1 =  driver.find_element_by_xpath('//div[@class="isgrP"]')
            for _ in range(nScrolls):                
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                time.sleep(3)
            followers =  driver.find_elements_by_xpath('//a[@class="FPmhX notranslate _0imsa "]')
            print(str(len(followers)))
            time.sleep(2)    
        except:
            print("Error: Can't take the unfollowers list")
            time.sleep(2)
        for _ in range(nUnfollow):
            time.sleep(15)
            try:
                driver.find_element_by_xpath('//button[@class="_0mzm- sqdOP  L3NKy   _8A5w5    "]').click()                  
            except:
                print("Error: unable to unfollow")
            time.sleep(2)
            try:
                driver.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]').click()      
                print("Unfollow: " + str(followers[0].get_attribute('title')) + " at: " + str(time.strftime("%H:%M:%S")))
                del followers[0]
            except:
                print("Error: unable to confirm unfollow")
            time.sleep(2)
       




