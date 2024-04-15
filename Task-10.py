from selenium import webdriver
from selenium.webdriver.common.by import By

# Open a browser window
driver = webdriver.Chrome()

# Open Instagram URL
url = "https://www.instagram.com/guviofficial/"
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Find followers count
followers_element = driver.find_element(By.XPATH, "//a[@href='/{}/followers/']".format(driver.current_url.split('/')[-2]))
followers_count = followers_element.find_element(By.XPATH, ".//span").text

# Find following count
following_element = driver.find_element(By.XPATH, "//a[@href='/{}/following/']".format(driver.current_url.split('/')[-2]))
following_count = following_element.find_element(By.XPATH, ".//span").text

# Print the counts
print("Followers:", followers_count)
print("Following:", following_count)

# Close the browser
driver.quit()

