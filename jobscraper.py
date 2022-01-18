from operator import index
from traceback import print_tb
from bs4 import BeautifulSoup
import requests

def find_job():
    html_text = requests.get("https://www.reed.co.uk/jobs/retail-assistant-jobs-in-leicester").text
    soup = BeautifulSoup(html_text, "lxml")

    jobs = soup.find_all("article", class_="job-result")

    for job in jobs:
        job_working_times = job.find_all("li", class_="time")
        job_position = job.find("h3", class_="title").text.split("-")[0]
        job_salary = job.find("li", class_="salary").text

        for job_working_time in job_working_times:
        
            working_time = job_working_time.text
            job_link = job.header.h3.a["href"]
            print(f"Job Title: {job_position.strip()}")
            print(f"Job Salary: {job_salary.strip()}")
            print(f"Job Working Time: {working_time.strip()}")
            print(f"Click here for more info: https://www.reed.co.uk{job_link}")
            
            print("")
    
if __name__ == "__main__":
    find_job()
else:
    print("Sorry you can only call this function when in main file")
