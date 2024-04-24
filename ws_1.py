import requests
from bs4 import BeautifulSoup

def get_filmography(actor_name):
    # Construct the Wikipedia search URL
    search_url = f"https://en.wikipedia.org/wiki/{actor_name.replace(' ', '_')}"
    
    # Send a GET request to the Wikipedia page
    response = requests.get(search_url)
    
    # Parse the HTML content of the Wikipedia page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the filmography section
    filmography_section = soup.find("span", id="Filmography")
    
    # If the "Filmography" section is not found, return None
    if filmography_section is None:
        return None
    
    # Extract the filmography list
    filmography_list = filmography_section.find_next("ul")
    
    # Extract film titles and years
    filmography = []
    for film in filmography_list.find_all("li"):
        # Extract title
        title = film.get_text().strip()
        
        # Extract year if available
        year = film.find("span", class_="dtstart")
        if year:
            year = year.get_text().strip()
        else:
            year = "Year not available"
        
        filmography.append((title, year))
    
    # Sort the filmography by year in descending order
    filmography.sort(key=lambda x: x[1], reverse=True)
    
    return filmography

# Example usage
actor_name = input("Enter the name of the actor: ")
filmography = get_filmography(actor_name)
if filmography:
    print(f"\nFilmography of {actor_name} in descending order:")
    for film, year in filmography:
        print(f"{year}: {film}")
else:
    print(f"No filmography found for {actor_name} on Wikipedia.")
