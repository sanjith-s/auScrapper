import time

from generateData.scrapData import ScrapData

try:
    with ScrapData() as bot:
        bot.land_first_page()
        bot.openEvents()
        bot.getNewsData()
        time.sleep(1000)
        print("Exiting")
except Exception as e:

    # To use the program in CLI

    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
