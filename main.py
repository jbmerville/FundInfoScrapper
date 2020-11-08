from SeleniumAction import SeleniumAction


def TravelToFundInfo(sa: SeleniumAction):
    URL = "https://www.fundinfo.com/fr/GB-prof"
    sa.getURL(URL)
    steps = [
        {
            "name": "clickButton1",
            "xPath": "/html/body/div[1]/div/div/div/div[2]/div/button[2]",
            "action": "click",
        },
        {
            "name": "clickItem1",
            "xPath": "/html/body/header/div/nav/ul/li[3]",
            "action": "click",
            "sleepTime": 2
        },
        {
            "name": "ChangeProfile",
            "xPath": "/html/body/header/div[2]/div[2]/div/div[1]/div/div[2]/label",
            "action": "click",
        },
        {
            "name": "clickItem2",
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
            "sleepTime": 4
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
        },
        {
            "name": "clickButton4",
            "xPath": "/html/body/header/form/div[2]/div/div[3]/button[2]",
            "action": "click",
            "sleepTime": 5
        },

    ]
    sa.executeStepsUsingXPath("TravelToFundInfo", steps)


def downloadPDFs(sa: SeleniumAction, firstX=10):
    for i in range(firstX):
        steps = [
            {
                "name": "downloadMR%d" % i,
                "xPath": "/html/body/div[2]/div/div[2]/div[1]/div/div[2]/ul/li[4]/div/div[1]/div[%d]/div/div[1]" % i,
                "action": "click",
                "sleepTime": 3
            },
        ]
        sa.executeStepsUsingXPath("Download PDF #%d" % i, steps)


if __name__ == '__main__':
    sa = SeleniumAction(autoDownloadPDF=True)
    TravelToFundInfo(sa)
    downloadPDFs(sa)
    print('✅ Done')
