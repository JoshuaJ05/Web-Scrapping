# Web-Scrapping

Overview
    This program analyzes keyword frequencies from the body content of two user-provided, tech-related websites. By scraping HTML content from the URLs, it extracts relevant data, counts occurrences of predefined technology-related keywords, and outputs a frequency analysis table, while also identifying the most referenced tech topic across the two sites.

    Features
Website Integration
  Accepts two tech-related URLs as input.
  Extracts the domain name and dynamically processes the site's content.

HTML Content Fetching
  Retrieves the HTML content of the user-provided URLs.
  Extracts relevant sections (e.g., <body> tag) for analysis.

Keyword Analysis
  Analyzes the frequency of predefined keywords (e.g., "Google", "Microsoft", "OpenAI") in the extracted content.
  Normalizes text for case-insensitive matching.

Frequency Table
  Displays keyword frequencies from both sites side-by-side in a formatted table.
  Highlights the most referenced keyword across the two sites.


    How It Works
User Input
  The program prompts users to input two tech-related URLs (e.g., https://wired.com, https://techcrunch.com).

HTML Content Retrieval
  Fetches HTML content of both URLs using Python’s urllib library.
  Uses a custom function to locate and extract the content inside the <body> tag.

Keyword Frequency Analysis
  Predefined keywords are analyzed for frequency in the extracted text content.
  Frequencies are stored in a dictionary for easy aggregation and comparison.

Display Results
  Outputs a frequency analysis table comparing keyword occurrences on both sites.
  Highlights the most referenced keyword or indicates if no references are found.


    Dependencies
The program requires the following Python libraries:
  urllib: For making HTTP requests and fetching webpage content.
  urllib.parse: For parsing and extracting the domain name from URLs.

    How to Use
Ensure Python is installed on your system.
Run the program in your terminal or IDE.
Input two tech-related URLs when prompted.
View the frequency analysis table in the console output.

This code shows practical web scraping, keyword analysis, and data presentation techniques using Python. It’s a great foundation for building more complex web analytics tools.
