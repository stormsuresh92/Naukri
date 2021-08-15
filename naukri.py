from requests_html import HTMLSession
import os
import pandas as pd


s = HTMLSession()

data = []

def page(x):
    url = f'https://www.naukri.com/{search}-jobs-in-india-{x}?k={search}&l=india'
    response = s.get(url)
    response.html.render(sleep=3, timeout=300, keep_page=True)
    contents = response.html.find('article.jobTuple.bgWhite.br4.mb-8')
    for job in contents:
        try:
            Job_Title = job.find('div.info.fleft a', first=True).text
        except:
            Job_Title = ''
        try:    
            Company = job.find('div.mt-7.companyInfo.subheading.lh16 a', first=True).text
        except:
            Company = ''
        try:    
            Experience = job.find('li.fleft.grey-text.br2.placeHolderLi.experience', first=True).text
        except:
            Experience = ''
        try:    
            Salary = job.find('li.fleft.grey-text.br2.placeHolderLi.salary', first=True).text
        except:
            Salary = ''
        try:
            Rating = job.find('span.starRating.fleft.dot', first=True).text
        except:
            Rating = ''
        try:
            Reviews = job.find('a.reviewsCount.ml-5.fleft.blue-text', first=True).text.replace('Reviews', '').replace('(', '').replace(')', '')
        except:
            Reviews = ''
        try:    
            Location = job.find('li.fleft.grey-text.br2.placeHolderLi.location', first=True).text
        except:
            Location = ''
        try:
            Job_description = job.find('div.job-description.fs12.grey-text', first=True).text
        except:
            Job_description = ''
        try:
            Skills = job.find('ul.tags.has-description', first=True).text
        except:
            Skills = ''
        try:
            Posted = job.find('div.type.br2.fleft.green', first=True).text
        except:
            Posted = ''
        
        dic = {
            'Company':Company,
            'Job_Title':Job_Title,
            'Experience':Experience,
            'Salary':Salary,
            'Rating':Rating,
            'Reviews':Reviews,
            'Job_description':Job_description,
            'Skills':Skills,
            'Posted':Posted,
            'Location':Location
            
        }
        
        data.append(dic)
    return data

search = input('Enter keyword: ')       
for x in range(1, 6):
    page(x)
    
df = pd.DataFrame(data)
df.to_csv(f'{search}.csv', index=False)
print('File downloaded')
    
      