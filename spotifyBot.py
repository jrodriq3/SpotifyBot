from SeleniumUtils import SeleniumUtils
from configparser import ConfigParser
import sys

# using arguments passed to determine which chromedriver to use
if len(sys.argv) != 2:
    print("Usage: python spotifyBot.py arg1")
    print("Argument: 1= mac or windows for if you are running the program on mac or windows")
    sys.exit(1)
operating_system = sys.argv[1]

# setting up and initializing config parser
config = ConfigParser()
config.read("spotifyConfig.ini")

# setting up variables from config file
url_target = config["URL"]["urltarget"]
chrmDriverPath = None
if operating_system == "mac":
    chrmDriverPath = config["MAC"]["chromedriverpath"]
elif operating_system == "windows":
    chrmDriverPath = config["WINDOWS"]["chromedriverpath"]
else:
    print("Unknown operating system")
    sys.exit(1)
email = config["Jason"]["email"]
password = config["Jason"]["password"]


# Setting up selenium and running spotify bot
su = SeleniumUtils()
su.set_url_target(url_target)
su.set_chrome_options(True)
su.set_chrome_driver_path(chrmDriverPath)
su.set_service()
su.start_service()
su.set_driver()
su.access_url()
su.wait_for_presence("id", 30, "login-username")
target_element = su.get_element("id", "login-username")
su.send_text(target_element, email)
target_element = su.get_element("id", "login-password")
su.send_text(target_element, password)
target_element = su.get_element("id", "login-button")
target_element.click()
su.wait_for_presence("class-name", 30, "svelte-1gcdbl9")
target_element = su.get_element("class-name", "svelte-1gcdbl9")
target_element.click()
su.wait_for_presence("css-selector", 30, 'button[aria-labelledby="listrow-title-spotify:playlist:1lSGJCSyXhlp8APbKnqmUo listrow-subtitle-spotify:playlist:1lSGJCSyXhlp8APbKnqmUo"]')
target_element = su.get_element("css-selector", 'button[aria-labelledby="listrow-title-spotify:playlist:1lSGJCSyXhlp8APbKnqmUo listrow-subtitle-spotify:playlist:1lSGJCSyXhlp8APbKnqmUo"]')
target_element.click()
su.wait_for_presence("css-selector", 30, 'button[aria-label="Play My Playlist #1"]')
target_element = su.get_element("css-selector", 'button[aria-label="Play My Playlist #1"]')
target_element.click()