from httpx import get

from bs4 import BeautifulSoup
from bs4.element import ResultSet

def extract_data_from_gupy(url: str ="https://gruposeb.gupy.io/") -> ResultSet:
    """
    Access the gupy website and extract the data from jobs list, return the data as a list.

    Keyword arguments:
        url (str): gupy website url (default=https://gruposeb.gupy.io/)
    returns:
        jobs (ResultSet): A filter set object from BeautifulSoup
    """
    page = get(url)

    if page.is_success:
        soup = BeautifulSoup(page.content, "html.parser")
        jobs = soup.find_all('li', attrs={"data-testid": "job-list__listitem"})

        return jobs
        
    return f"{page.status_code}"


def clean_data_from_gupy(data: ResultSet) -> list[dict]:
    """
    Keyword arguments:
        data (ResultSet): ResultSet object from BS4
    returns: 
        list: A list with the following pattern
        [
            {'function': 'job function description', 'location': 'job location', 'type': 'job type'},
            {'function': 'job function description', 'location': 'job location', 'type': 'job type'},
        ]
    """
    cleaned_data_objects = list()

    if data:
        for job in data:
            job_data = job.find_all("div")
            extracted_data = {
                "function": job_data[1].text,
                "location": job_data[2].text,
                "type": job_data[3].text
            }
            cleaned_data_objects.append(extracted_data)
    
        return cleaned_data_objects