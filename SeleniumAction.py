from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumAction():
    """Wrapper to execute actions using Selenium"""

    def __init__(self, downloadDirectory=None, autoDownloadPDF=False):
        """Initialize SeleniumAction

        Parameters
        ----------
        download_directory : str, optional
            The directory to download files to, defaults to download directory

        Returns
        -------
        SeleniumAction
        """
        chromeOptions = webdriver.ChromeOptions()
        if downloadDirectory or autoDownloadPDF:
            options = {'download.prompt_for_download': not autoDownloadPDF}
            if downloadDirectory:
                options['download.default_directory'] = downloadDirectory
            if autoDownloadPDF:
                # From StackOverflow: https://stackoverflow.com/a/54427220
                options['download.prompt_for_download'] = False
                options['download.directory_upgrade'] = True,
                options['plugins.always_open_pdf_externally'] = True
            chromeOptions.add_experimental_option('prefs', options)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)

    def executeStepsUsingXPath(self, name, steps):
        """Execute a series of steps.

        Parameters
        ----------
        name : str
            The name of the step to execute
        steps : list
            A list of object with the following properties:
            action: "send_keys", "click"
                The action to execute for that step
            sendKeysData: str
                The data to send with the send_keys action
            xPath: str
                The xpath of the element to select on the current page
            sleepTime: int, optional
                The sleep time in seconds after executing the step, defaults to wait until next element is clickable

        Returns
        -------
        None
        """
        for index, step in enumerate(steps):
            try:
                element = self.driver.find_element_by_xpath(step["xPath"])
                if step["action"] == "send_keys":
                    element.send_keys(step["sendKeysData"])
                if step["action"] == "click":
                    element.click()
                if "sleepTime" in step:
                    sleep(step["sleepTime"])
                elif index < len(steps) - 1 and steps[index + 1]["action"] == "click":
                    wait = WebDriverWait(self.driver, 5)
                    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, steps[index + 1]["xPath"])))
            except Exception as exception:
                raise Exception("❌ %s failed on step #%d \"%s\" with error:\n%s" % (name, index, step["name"], repr(exception)))
        print("✅ Successfully executed \"%s\"" % name)

    def getURL(self, url, sleepTime=1):
        """Load url and sleep

        Parameters
        ----------
        url: str
            The url to load
        sleepTime: int, optional
            The sleep time in seconds after executing the URL load, defaults to 1s

        Returns
        -------
        None
        """
        self.driver.get(url)
        sleep(sleepTime)
