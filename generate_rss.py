import json
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def generate_rss_feed():
    """Generate RSS feed from scraped data"""
    
    # Load scraped data
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            items = json.load(f)
    except FileNotFoundError:
        items = []
    
    # Create RSS structure
    rss = Element('rss', version='2.0')
    rss.set('xmlns:atom', 'http://www.w3.org/2005/Atom')
    
    channel = SubElement(rss, 'channel')
    
    # Channel information
    SubElement(channel, 'title').text = 'CDSCO SEC Notifications'
    SubElement(channel, 'link').text = 'https://cdsco.gov.in/opencms/opencms/en/Committees/SEC/'
    SubElement(channel, 'description').text = 'Automated RSS feed for CDSCO Subject Expert Committee (SEC) notifications and drug approval updates'
    SubElement(channel, 'language').text = 'en-IN'
    SubElement(channel, 'lastBuildDate').text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0530')
    
    # Self-reference link
    atom_link = SubElement(channel, '{http://www.w3.org/2005/Atom}link')
    atom_link.set('href', 'https://simpleman181.github.io/cdsco-sec-rss-feed/feed.xml')
    atom_link.set('rel', 'self')
    atom_link.set('type', 'application/rss+xml')
    
    # Add items (limit to latest 50)
    for item_data in items[:50]:
        item = SubElement(channel, 'item')
        SubElement(item, 'title').text = item_data['title']
        SubElement(item, 'link').text = item_data['link']
        SubElement(item, 'description').text = item_data['description']
        SubElement(item, 'pubDate').text = item_data['pubDate']
        SubElement(item, 'category').text = item_data['category']
        SubElement(item, 'guid', isPermaLink='false').text = item_data['guid']
    
    # Pretty print XML
    xml_string = minidom.parseString(tostring(rss)).toprettyxml(indent="  ")
    
    # Save to file
    with open('feed.xml', 'w', encoding='utf-8') as f:
        f.write(xml_string)
    
    print(f"RSS feed generated with {len(items[:50])} items")

if __name__ == "__main__":
    generate_rss_feed()
