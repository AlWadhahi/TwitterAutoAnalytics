from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import codecs
import csv



options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=D:\Python\Memory\TwitterAutoAnalytics")

driver = webdriver.Chrome(
executable_path=r"TYPE_CHROME_DRIVER_PATH_HERE", chrome_options=options)


file = open('tweets.txt', 'r')
URLs = file.readlines()

i = 1

with open('Tweets.csv', mode='w', encoding='utf-8', newline='\n') as TweetsFile:
    File_writer = csv.writer(TweetsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    File_writer.writerow(
        ['Impressions', 'Engagements', 'Likes', 'Retweets', 'Media Engagements', 'Profile Clicks', 'Hashtag Clicks', 'Replies', 'Detail expands', 'URL'])
    for url in URLs:
        driver.get(url + "/analytics")

        print("Getting details of Tweet #" + str(i))
        wait = WebDriverWait(driver, 10)

        #Analytics_button = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//button')))

        #Analytics_button.click()

        analytics_div = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div/iframe')))

        driver.switch_to.frame(analytics_div)
        view_more_button = driver.find_element_by_xpath('//button[contains(text(),"View all engagements")]')

        view_more_button.click()

        impressions = 0
        engagements = 0
        media_views = 0
        media_engagements = 0
        likes = 0
        retweets = 0
        profileClicks = 0
        hashtagClicks = 0
        replies = 0
        detail = 0

        try:
            impressions_span = driver.find_element_by_xpath('//div[@data-metric-type="Impressions"]/span')
            impressions = int(impressions_span.text.replace(',', ''))
        except NoSuchElementException:
            pass

        try:
            engagements_span = driver.find_element_by_xpath('//div[@data-metric-type="Engagements"]/span')
            engagements = int(engagements_span.text.replace(',', ''))
        except NoSuchElementException:
            pass
        '''
        try:
            media_views_span = driver.find_element_by_xpath('//div[@data-metric-type="MediaViews"]/span')
            media_views = int(media_views_span.text.replace(',', ''))
        except NoSuchElementException:
            pass
        '''
        try:
            media_engagements_span = driver.find_element_by_xpath('//div[@data-metric-type="MediaEngagements"]/span')
            media_engagements = int(media_engagements_span.text.replace(',', ''))
        except NoSuchElementException:
            pass


        try:
            likes_span = driver.find_element_by_xpath('//div[@data-metric-type="Favorites"]/span')
            likes = int(likes_span.text.replace(',', ''))
        except NoSuchElementException:
            pass

        try:
            retweets_span = driver.find_element_by_xpath('//div[@data-metric-type="Retweets"]/span')
            retweets = int(retweets_span.text.replace(',', ''))
        except NoSuchElementException:
            pass

        try:
            profileClicks_span = driver.find_element_by_xpath('//div[@data-metric-type="UserProfileClicks"]/span')
            profileClicks = int(profileClicks_span.text.replace(',', ''))
        except NoSuchElementException:
            pass

        try:
            hashtagClicks_span = driver.find_element_by_xpath('//div[@data-metric-type="HashtagClicks"]/span')
            hashtagClicks = int(hashtagClicks_span.text.replace(',', ''))
        except NoSuchElementException:
            pass

        try:
            replies_span = driver.find_element_by_xpath('//div[@data-metric-type="Replies"]/span')
            replies = int(replies_span.text.replace(',', ''))
        except NoSuchElementException:
            pass

        try:
            detail_span = driver.find_element_by_xpath('//div[@data-metric-type="DetailExpands"]/span')
            detail = int(detail_span.text.replace(',', ''))
        except NoSuchElementException:
            pass

        print("impressions: " + str(impressions))
        print("engagements: " + str(engagements))
        print("media engagements: " + str(media_engagements))
        print("likes: " + str(likes))
        print("retweets: " + str(retweets))
        print("profile clicks: " + str(profileClicks))
        print("hashtag clicks: " + str(hashtagClicks))
        print("replies: " + str(replies))
        print("detail expands: " + str(detail))

        i+=1

        File_writer.writerow([impressions, engagements, likes, retweets, \
                              media_engagements, profileClicks, hashtagClicks, \
                              replies, detail, url])


print('Finished!')

