import scrapy  # Importing the Scrapy library, which is a powerful framework for extracting data from websites.

# Define a new Scrapy Spider class named 'DriversSpider'.
# This spider is responsible for scraping information related to Chrome drivers from a specific website.
class DriversSpider(scrapy.Spider):
    name = 'drivers'  # This sets the name of the spider, which is used when running the Scrapy crawler.
    
    # Define the allowed domains that this spider can scrape data from.
    # This prevents the spider from navigating to other domains unintentionally.
    allowed_domains = ['googlechromelabs.github.io']
    
    # List of start URLs where the spider begins scraping.
    # In this case, it starts from the "chrome-for-testing" page.
    start_urls = ['https://googlechromelabs.github.io/chrome-for-testing/']

    # The 'parse' method is the main method for processing the response from the website.
    # It extracts relevant data from the HTML structure.
    def parse(self, response):
        # Loop through all sections that contain the "status-ok" class, which indicates available Chrome drivers.
        for section in response.xpath('//section[contains(@class, "status-ok")]'):
            # Extract the unique identifier for the section, representing different Chrome channels (e.g., Stable, Beta, Dev).
            channel = section.xpath('./@id').get()
            
            # Extract the version number of the Chrome driver listed in this section.
            version = section.xpath('./p/code[1]/text()').get()
            
            # Extract the revision number, which provides additional details about the version.
            revision = section.xpath('./p/code[2]/text()').get()

            # Loop through all rows inside the table within this section.
            # Each row represents an available Chrome driver binary for a specific platform.
            for row in section.xpath('.//table//tr[contains(@class, "status-ok")]'):
                # Extract the name of the binary file, such as 'chromedriver' or 'chrome'.
                binary = row.xpath('.//th[1]/code/text()').get()
                
                # Extract the platform for which this binary is available (e.g., "Linux", "Mac", "Windows").
                platform = row.xpath('.//th[2]/code/text()').get()
                
                # Extract the direct download URL for the Chrome driver binary.
                url = row.xpath('.//td[1]/code/text()').get()
                
                # Extract the HTTP status of the download link to ensure it's valid.
                http_status = row.xpath('.//td[2]/code/text()').get()

                # Yield a dictionary containing all extracted data.
                # This sends the scraped data to Scrapy's output pipeline for further processing or storage.
                yield {
                    "channel": channel,       # Chrome release channel (Stable, Beta, etc.)
                    "version": version,       # Chrome driver version
                    "revision": revision,     # Revision number
                    "binary": binary,         # Binary file name
                    "platform": platform,     # Platform type (Windows, Linux, etc.)
                    "url": url,               # Direct download URL
                    "http_status": http_status,  # HTTP status of the download link
                }
