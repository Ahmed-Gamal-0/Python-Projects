import webbrowser as wb

def webauto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        "google.com",
        "youtube.com",
        "gmail.com",
        "github.com"
    )  
    for url in URLS:
        print(f"Opening {url}")
        wb.get(chrome_path).open(url)
        
        
        
webauto()