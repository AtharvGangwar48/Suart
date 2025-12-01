from bs4 import BeautifulSoup

class HTMLParser:
    def parse_html(self, html_content: str):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Extract text
        text = soup.get_text()
        
        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return {
            "text": text,
            "title": soup.title.string if soup.title else "",
            "meta_description": self._get_meta_description(soup)
        }
    
    def _get_meta_description(self, soup):
        meta = soup.find("meta", attrs={"name": "description"})
        return meta.get("content", "") if meta else ""