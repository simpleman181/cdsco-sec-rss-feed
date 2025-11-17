import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os

def scrape_cdsco_sec():
    """Scrape CDSCO SEC page for latest notifications"""
    url = "https://cdsco.gov.in/opencms/opencms/en/Committees/SEC/"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table with SEC data
        table = soup.find('table')
        items = []
        
        if table:
            rows = table.find_all('tr')[1:]  # Skip header row
            
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 4:
                    # Extract data
                    serial_no = cols[0].get_text(strip=True)
                    title = cols[1].get_text(strip=True)
                    date_str = cols[2].get_text(strip=True)
                    category = cols[3].get_text(strip=True)
                    
                    # Find PDF link
                    pdf_link = ""
                    link_tag = cols[4].find('a') if len(cols) > 4 else None
                    if link_tag and link_tag.get('href'):
                        pdf_link = link_tag['href']
                        if not pdf_link.startswith('http'):
                            pdf_link = f"https://cdsco.gov.in{pdf_link}"
                    
                    # Parse date
                    try:
                        pub_date = datetime.strptime(date_str, '%d-%b-%Y')
                    except:
                        pub_date = datetime.now()
                    
                    item = {
                        'title': title,
                        'link': pdf_link,
                        'description': f"{category} - {title}",
                        'pubDate': pub_date.strftime('%a, %d %b %Y %H:%M:%S +0530'),
                        'category': category,
                        'guid': f"cdsco-sec-{serial_no}-{pub_date.strftime('%Y%m%d')}"
                    }
                    items.append(item)
        
        # Save to JSON file
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully scraped {len(items)} items")
        return items
        
    except Exception as e:
        print(f"Error scraping: {e}")
        return []

if __name__ == "__main__":
    scrape_cdsco_sec()
