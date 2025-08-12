#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "requests",
#   "beautifulsoup4",
# ]
# ///

"""
Web scraping demonstration using requests and BeautifulSoup.
This script shows how to fetch and parse web content responsibly.
"""

import requests
from bs4 import BeautifulSoup
import time
import json
from urllib.parse import urljoin, urlparse

def get_page_content(url, timeout=10):
    """Fetch page content with error handling."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print(f"🌐 Fetching: {url}")
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.text
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return None

def extract_page_info(html_content, base_url):
    """Extract basic information from HTML content."""
    if not html_content:
        return None
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract basic page info
    page_info = {
        'title': '',
        'description': '',
        'headings': {'h1': [], 'h2': [], 'h3': []},
        'links': [],
        'images': [],
        'meta_info': {}
    }
    
    # Title
    title_tag = soup.find('title')
    if title_tag:
        page_info['title'] = title_tag.get_text().strip()
    
    # Description
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if desc_tag and desc_tag.get('content'):
        page_info['description'] = desc_tag.get('content').strip()
    
    # Headings
    for level in ['h1', 'h2', 'h3']:
        headings = soup.find_all(level)
        page_info['headings'][level] = [h.get_text().strip() for h in headings[:5]]  # Limit to 5
    
    # Links (internal and external)
    links = soup.find_all('a', href=True)
    for link in links[:10]:  # Limit to 10
        href = link.get('href')
        full_url = urljoin(base_url, href)
        text = link.get_text().strip()
        if text and href:
            page_info['links'].append({
                'text': text[:50],  # Limit text length
                'url': full_url
            })
    
    # Images
    images = soup.find_all('img', src=True)
    for img in images[:5]:  # Limit to 5
        src = img.get('src')
        alt = img.get('alt', '')
        full_url = urljoin(base_url, src)
        page_info['images'].append({
            'alt': alt[:30],  # Limit alt text
            'src': full_url
        })
    
    # Meta information
    meta_tags = soup.find_all('meta')
    for meta in meta_tags:
        name = meta.get('name') or meta.get('property')
        content = meta.get('content')
        if name and content and len(page_info['meta_info']) < 10:  # Limit meta tags
            page_info['meta_info'][name] = content[:100]  # Limit content length
    
    return page_info

def analyze_website(url):
    """Analyze a website and extract information."""
    print(f"🔍 Analyzing website: {url}")
    print("=" * 50)
    
    # Get page content
    html_content = get_page_content(url)
    if not html_content:
        return None
    
    # Extract information
    page_info = extract_page_info(html_content, url)
    if not page_info:
        return None
    
    # Display results
    print(f"📄 Title: {page_info['title']}")
    print(f"📝 Description: {page_info['description'][:100]}...\" if page_info['description'] else 'No description found'}")
    
    # Headings
    print(\"\\n📋 Page Structure:\")
    for level, headings in page_info['headings'].items():
        if headings:
            print(f\"  {level.upper()}: {len(headings)} found\")
            for i, heading in enumerate(headings[:3], 1):
                print(f\"    {i}. {heading[:60]}...\")
    
    # Links
    if page_info['links']:
        print(f\"\\n🔗 Links: {len(page_info['links'])} found (showing first 3)\")
        for i, link in enumerate(page_info['links'][:3], 1):
            print(f\"  {i}. {link['text']} -> {link['url']}\")
    
    # Images
    if page_info['images']:
        print(f\"\\n🖼️  Images: {len(page_info['images'])} found (showing first 3)\")
        for i, img in enumerate(page_info['images'][:3], 1):
            print(f\"  {i}. {img['alt']} -> {img['src']}\")
    
    return page_info

def save_analysis(data, url):
    \"\"\"Save analysis results to JSON file.\"\"\"
    if data:
        # Create filename from URL
        domain = urlparse(url).netloc.replace('.', '_')
        filename = f\"website_analysis_{domain}.json\"
        
        # Add metadata
        analysis_result = {
            'url': url,
            'analyzed_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'data': data
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(analysis_result, f, indent=2, ensure_ascii=False)
        
        print(f\"\\n💾 Analysis saved to {filename}\")
        return filename
    return None

def main():
    \"\"\"Main function for web scraping demo.\"\"\"
    print(\"🕷️  Web Scraping Demo\")
    print(\"=\" * 30)
    print(\"⚠️  Remember: Always respect robots.txt and rate limits!\")
    print(\"⚠️  This demo is for educational purposes only.\")
    
    # Default URLs to try (public, scraping-friendly sites)
    default_urls = [
        \"https://httpbin.org/html\",
        \"https://example.com\",
        \"https://httpbin.org/\"
    ]
    
    # Get URL from user or use default
    url = input(f\"\\nEnter a URL to analyze (or press Enter for examples): \").strip()
    
    if not url:
        print(\"\\n📝 Using example URLs for demonstration:\")
        for test_url in default_urls:
            print(f\"\\n{'='*50}\")
            result = analyze_website(test_url)
            if result:
                save_analysis(result, test_url)
            
            # Be respectful - add delay between requests
            time.sleep(1)
    else:
        # Analyze user-provided URL
        result = analyze_website(url)
        if result:
            save_analysis(result, url)
    
    print(\"\\n✅ Web scraping demo completed!\")
    print(\"📚 Remember to always:\")
    print(\"  - Check robots.txt\")
    print(\"  - Respect rate limits\")
    print(\"  - Be ethical and legal\")

if __name__ == \"__main__\":
    main()