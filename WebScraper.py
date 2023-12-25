import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
import re
import time
import json
import urllib.robotparser

class WebScraper:
    def __init__(self, config):
        self.start_url = config["url"]
        self.match_pattern = config["match"]
        self.selector = config["selector"]
        self.max_pages = config["maxPagesToCrawl"]
        self.output_file = config["outputFileName"]
        self.visited = set()
        self.robot_parser = urllib.robotparser.RobotFileParser()
        self.fetch_robots_txt()

    async def fetch_url(self, url):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()
                return response.text
        except:
            pass

    def fetch_robots_txt(self):
        self.robot_parser.set_url(urljoin(self.start_url, "/robots.txt"))
        self.robot_parser.read()

    def can_fetch(self, url):
        return self.robot_parser.can_fetch("*", url)

    def respect_crawl_delay(self):
        crawl_delay = self.robot_parser.crawl_delay("*")
        if crawl_delay:
            time.sleep(crawl_delay)

    def normalize_url(self, url):
        parsed_url = urlparse(url)
        return urlunparse(parsed_url._replace(fragment=""))

    def parse_links(self, html, base_url):
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)
            normalized_url = self.normalize_url(full_url)
            if re.match(self.match_pattern, normalized_url) and normalized_url not in self.visited:
                yield normalized_url

    async def scrape(self):
        pages_to_visit = [self.normalize_url(self.start_url)]
        results = []

        while pages_to_visit and len(self.visited) < self.max_pages:
            url = pages_to_visit.pop(0)
            normalized_url = self.normalize_url(url)
            if normalized_url in self.visited or not self.can_fetch(normalized_url):
                continue

            self.respect_crawl_delay()

            print(f"Scraping {normalized_url}")
            self.visited.add(normalized_url)
            html = await self.fetch_url(normalized_url)

            if html:
                soup = BeautifulSoup(html, 'lxml')
                content = soup.select(self.selector)
                text_content = ' '.join([c.get_text(separator=' ', strip=True) for c in content])
                title = soup.title.string if soup.title else url

                results.append({
                    "title": title,
                    "url": url,
                    "text_content": text_content
                })

                links = self.parse_links(html, url)
                pages_to_visit.extend(links)
        output_path = '/app/data/' + self.output_file
        # output_path = self.output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        print(f"Scraping complete. Data written to {self.output_file}")
