# This python file contains basic beautifulSoup problems that I covered through Youtube videos and on my own

from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h5') # searches for the first tag satisfying this criteria
    tags_all = soup.find_all('h5')

    for courses in tags_all:
        print(courses.text)

    course_cards_all = soup.find_all('div', class_='card')
    for course in course_cards_all:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print("{} costs {}".format(course_name, course_price))


