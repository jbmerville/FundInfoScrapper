from SeleniumAction import SeleniumAction


def TravelToFundInfo(sa: SeleniumAction):
    URL = "https://www.fundinfo.com/fr/GB-prof"
    sa.getURL(URL)
    steps = [
        {
            "name": "acceptTermsOfServices",
            "xPath": "/html/body/div[1]/div/div/div/div[2]/div/button[2]",
            "action": "click",
        },
        {
            "name": "selectCountry",
            "xPath": "/html/body/header/div/nav/ul/li[3]",
            "action": "click",
        },
        {
            "name": "ChangeProfile",
            "xPath": "/html/body/header/div[2]/div[2]/div/div[1]/div/div[2]/label",
            "action": "click",
            "sleepTime": 1,
        },
        {
            "name": "chooseUKFundMarket",
            "xPath": "/html/body/header/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div[5]",
            "action": "click",
        },
        {
            "name": "clickItem3",
            "xPath": "/html/body/header/div[2]/div[2]/div/div[1]/div/div[1]/div[1]",
            "action": "click",
        },
        {
            "name": "clickItem4",
            "xPath": "/html/body/header/div[2]/div[2]/div/div[1]/div/div[4]/div/label/span",
            "action": "click",
        },
        {
            "name": "clickButton2",
            "xPath": "/html/body/header/div[2]/div[2]/div/div[1]/div/div[5]/button[2]",
            "action": "click",
        },
        {
            "name": "clickButton3",
            "xPath": "/html/body/header/form/div/div/div[2]/button",
            "action": "click",
        },
        {
            "name": "chooseCategory",
            "xPath": "/html/body/header/form/div[2]/div/div[1]/div[1]/div/ul/li[6]/a",
            "action": "click",
        },
        {
            "name": "chooseRegion",
            "xPath": "/html/body/header/form/div[2]/div/div[1]/div[1]/div/div/div[12]/div[7]/label/span[2]",
            "action": "click",
            "sleepTime": 1,
        },
        {
            "name": "clickButton4",
            "xPath": "/html/body/header/form/div[2]/div/div[3]/button[2]",
            "action": "click",
            "sleepTime": 2,
        },

    ]
    sa.executeStepsUsingXPath("TravelToFundInfo", steps)


def downloadPDFs(sa: SeleniumAction, firstX=10):
    steps = []
    for i in range(firstX):
        steps.append({
            "name": "downloadMR%d" % i,
            "xPath": "/html/body/div[2]/div/div[2]/div[1]/div/div[2]/ul/li[%d]/div/div[1]/div[5]/div/div[1]" % (i + 2),
            "action": "click",
        }),
        steps.append({
            "name": "clickOffDownloadPopUp",
            "xPath": "/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]",
            "action": "click",
        })
    sa.executeStepsUsingXPath("Download PDF", steps)


if __name__ == '__main__':
    sa = SeleniumAction(autoDownloadPDF=True)
    TravelToFundInfo(sa)
    downloadPDFs(sa)
    print('✅ Done')
