# Chromedrivers Scraper

This repository provides a Scrapy-based web scraper for extracting Chrome for Testing version information and downloadable assets across various platforms and release channels (Stable, Beta, Dev, Canary).

## 🚀 Features

- Extracts version, revision, binary type, platform, download URL, and HTTP status
- Supports Chrome, Chromedriver, and Headless Shell binaries
- Outputs structured data to a CSV file
- Compatible with GitHub Codespaces and VS Code Dev Containers

## 🐍 Tech Stack

- Python 3.8 (via Docker)
- Scrapy 2.5.1
- Pandas, Matplotlib (optional, for data analysis or visualization)
- VS Code Remote Containers / DevContainer setup

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chromedrivers.git
cd chromedrivers
```

### 2. Run in DevContainer (VS Code)

Make sure you have:
- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Then open the folder in VS Code and **reopen in container**.

### 3. Run the Spider

```bash
scrapy crawl drivers
```

This will produce a `chrome_testing_data.csv` file in the project root.

## 🧪 Sample Output

| channel | version       | revision  | binary        | platform  | url                                                   | http_status |
|---------|---------------|-----------|---------------|-----------|--------------------------------------------------------|-------------|
| stable  | 136.0.7103.49 | r1440670  | chrome        | win64     | https://.../chrome-win64.zip                          | 200         |
| beta    | 137.0.7151.6  | r1453031  | chromedriver  | mac-arm64 | https://.../chromedriver-mac-arm64.zip                | 200         |

## 🐳 Docker Setup

To rebuild the container:

```bash
docker-compose build
```

Or use the integrated DevContainer support in VS Code (`devcontainer.json`).

## 📄 License

MIT License. See `LICENSE` for details.

## 🙋‍♀️ Contributing

Pull requests welcome. Please submit issues for bugs, improvements, or suggestions.

## 🔗 References

- [Chrome for Testing Blog](https://developer.chrome.com/blog/chrome-for-testing/)
- [Chrome for Testing JSON API](https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints)
- [Scrapy Documentation](https://docs.scrapy.org/)