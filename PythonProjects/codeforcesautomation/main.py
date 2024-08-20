from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


cf =  {
    "executablePath" : r"/usr/bin/chromedriver",
    "userDataDir" : r"/home/window/.config/browserautocache",
}



class CodeforcesAutomation:
    def __init__(self, user_data_dir, executable_path):
        # Instantiate ChromeOptions
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={user_data_dir}")

        # Instantiate Service
        service = Service(executable_path)

        # Initialize the Chrome WebDriver with options and service
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://codeforces.com/enter")
        


if __name__ == "__main__":
    automation = CodeforcesAutomation(cf["userDataDir"], cf["executablePath"])

    try:
        while True:
            pass  # Infinite loop to keep the script running
    except KeyboardInterrupt:
        print("Stopping script...")

    automation.driver.quit()  # Close the browser when script is terminated
