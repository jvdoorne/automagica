"""Copyright 2020 Oakwood Technologies BVBA"""
from automagica.activities import Excel, Chrome


def test_excel_activities():
    """
    Test scenario for testing Excel activities (requires Microsoft Excel)
    """
    # Open Excel
    excel = Excel()

    # Write cell activity
    excel.write_cell(1, 1, "Testing")

    # Read the result
    result = excel.read_cell(1, 1)

    # Quit Excel
    excel.quit()

    assert result == "Testing"


def test_chrome_activities():
    """
    Test scenario for testing Chrome browser activities (requires Google Chrome)
    """
    # Open Chrome
    chrome = Chrome(auto_update_chromedriver=True)

    # Browse to Google
    chrome.browse_to("https://google.com")

    # Save the page source
    source = chrome.page_source

    # Quit the browser
    chrome.quit()

    assert "Google" in source
