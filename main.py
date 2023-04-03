# # from scipy.stats import spearmanr
# # from pandas import read_csv
# # # create two lists of data
# #
# # file_data = read_csv("cardio_base.csv")
# # x = [2, 4, 6, 8, 10]
# # y = [1, 3, 5, 7, 9]
# #
# # # calculate the Spearman rank correlation coefficient and p-value
# # corr, pval = spearmanr(x, y)
# #
# # # print the result
# # print("Spearman rank correlation coefficient:", corr)
#
#
# import scrapy
#
# class JobSpider(scrapy.Spider):
#     name = 'job_spider'
#     start_urls = ['https://devitjobs.us/jobs/Python/remote/all']
#
#     def parse(self, response):
#         for job in response.css('div.job-box'):
#             yield {
#                 'title': job.css('a.job-link::text').get(),
#                 'company': job.css('div.job-company::text').get(),
#                 'location': job.css('div.job-location::text').get(),
#                 'description': job.css('div.job-description::text').get().strip()
#             }
#
#         next_page_url = response.css('div.pagination > a[rel="next"]::attr(href)').get()
#         if next_page_url:
#             yield response.follow(next_page_url, callback=self.parse)
import json

from linkedin_api import Linkedin
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Set up the LinkedIn API client
# client = Linkedin("kshitiz305@live.com","Rahuln97#",
#     refresh_cookies=True,
#     # max_connection_retries=10,
#     # request_timeout=30
# )
#
# # Set up the target profile ID and message
# target_profile_id = "shruthashivanna"
# message = "Hi, I would like to connect with you on LinkedIn."
#
# # Send the connection request
# # client.get_invitations(
# #     profile_id=target_profile_id,
# #     message=message
# # )
# res = client.search_people("skipp",current_company="skipp")
with open("connections_turing.json", "w") as f:
    # Write the list of dictionaries to the file
    json.dump(res, f)

with open("connections_turing.json", "r") as f:
    # Read the list of dictionaries from the file
    my_list = json.load(f)

# # Print the list of dictionaries
for i in my_list:
    # try:
    #     # a = client.add_connection(i["urn_id"])
    # except:
    #     print(i)
    print(f"https://www.linkedin.com/in/{i['public_id']}")
# Wait for a few seconds to avoid rate limiting
    time.sleep(2)


# Set up the driver and navigate to the target profile page
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/in/thomascherickal")

# Click the "Connect" button
connect_button = driver.find_element_by_css_selector("button[data-control-name='srp_profile_actions']")
driver.find_element(By.CSS_SELECTOR,"button[data-control-name='srp_profile_actions']")
connect_button.click()

# Wait for the "Connect" dialog to appear
time.sleep(2)

# Click the "Add a note" button
add_note_button = driver.find_element_by_css_selector("button[aria-label='Add a note']")
add_note_button.click()

# Wait for the note form to appear
time.sleep(2)

# Enter your connection message in the note field
note_field = driver.find_element_by_css_selector("textarea[name='message']")
note_field.send_keys("Hi, I would like to connect with you on LinkedIn.")

# Click the "Send" button to send the connection request
send_button = driver.find_element_by_css_selector("button[type='submit']")
send_button.click()

# Wait for a few seconds to avoid rate limiting
time.sleep(2)

# Close the driver
driver.quit()
