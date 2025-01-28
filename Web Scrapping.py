import urllib
import urllib.request
from urllib.parse import urlparse # A library that I'm importing for fetching web pages


'''Main Program''' # In which we'll have a function for getting the name of the site.
def main():

    def get_site_name(url):
        domain = urlparse(url).netloc # retrieves the name of the site including the ".com"
        return domain.split('.')[0].capitalize() #therefore I use the split function on the domain variable
                                                    # at the "." and get the 0 index which would be the name of the site
                                                        # then we can capitalize the first word of the site.

        # User Input
    url1 = input("Enter a 'TECH' related URL \n"
                 "Eg: https://wired.com/ \n"
                 ": ").strip()
    url2 = input("Enter another 'TECH' related URL \n"
                 "Eg: https://techcrunch.com/ \n"
                 ": ").strip()

    site1_name = get_site_name(url1) # Getting the site name of the url(s) being input by the user
                            # stored in a variable that would be used in the display function
    site2_name = get_site_name(url2)

    # Fetching the HTML Content of the Url which would be extracted and placed in a separate container of its own.
    html1 = fetch_html(url1)
    html2 = fetch_html(url2)

    # Extract Relevant Content
    content1 = extract_content(html1, "body")  # Extract from <body> of the html which holds the url input by the users
    content2 = extract_content(html2, "body")

    # Keywords for Analysis
    keywords = ["Google", "Microsoft", "OpenAI"]
    normalized_keywords = [keyword.lower() for keyword in keywords]  # Converting evey keyword into lower case so that
                            # no matter if its upper or lower it would be counted.

    # Count Keywords
    counts1 = count_keywords(content1, normalized_keywords)
    counts2 = count_keywords(content2, normalized_keywords)

    # Display Results
    display_results([counts1, counts2], [site2_name,site1_name]) # passing two variables that are
                                #defined to be passed in the displaying of results.


'''Fetch HTML function'''
def fetch_html(url):
    # Creating a def function to fetch html and return it that would be used for variables
        # that will be passed by the user's website input
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # Google/Youtube help.
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        print("HTML content retrieved successfully.")  # Debug message
        return html
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return " Invalid Url input "


'''Extracting relevant HTML content ... headlines, body text'''
def extract_content(html_content, tag):
    start = html_content.find(f"<{tag}>") # Knowing how a WWW "tagline is set" we can extract key values from them in this case "tag" which is part of the query string
    end = html_content.find(f"</{tag}>", start)
    if start != -1 and end != -1:     # Conditional statement for the 2 variables that hold tagging info.
        return html_content[start + len(tag) + 2:end]
    return html_content
                 # (Extra help - Google)

'''Counting keyword frequencies'''
def count_keywords(text, keywords):
    counts = {key.lower(): 0 for key in keywords}
    words = text.lower().split()
    for word in words:
        if word in counts: # A logical statement of if words that holds information is found in counts which is another variable that hold info about keywords
            counts[word] += 1 # Irritating by 1 for every-variant of a key word found when scrapping both Urls'
    return counts


'''Displaying results in table format'''
def display_results(site_results, site_names):
    site1_name, site2_name = site_names

    print("\n Frequency Analysis Table")
    print(f"{'Keyword':<15} {site1_name:<10} {site2_name:<10} {'Total':<10}") # Tables' variable names.
    print("-" * 45)
    combined = {} # an empty dictionary, which would have a key and a value to said key.
    for key in site_results[0]:
        total = site_results[0][key] + site_results[1][key]
        combined[key] = total
        print(f"{key:<15} {site_results[0][key]:<10} {site_results[1][key]:<10} {total:<10}") # Tables' variable.
    most_referenced = str(max(combined, key=combined.get)) # Gets the information we want which is the keyword referenced the most
    if most_referenced == 0:
        print("Error, There are no reference detected") # Conditional statement for if the most referenced = 0 the following statement should be printed
    else:
        print("\nMost Referenced/Talked about Technology Topic in the News Today is:", most_referenced.capitalize())

main()
