
# sp22-cs411-team101-abduFormedTeam

# PanExpedia 
## The Ultimate Travel Web Application during COVID-19 Pandemic
`We are the best, don't listen to anyone else`

## Project Description 

For travelers in the world during COVID-19 pandemic, we designed a web application that assists travelers in searching for the rate of selected country's COVID-19 Cases, Hospitalization, Testing, and Vaccination. This project is intended to help people gain confidence in their trips as the pandemic goes on, giving them the power to decide for themselves whether or not to travel to a certain location. We used a [OWID COVID-19 Dataset](https://github.com/owid/covid-19-data/tree/master/public/data) for our project. We have preprocessed the CSV file This dataset is stored in a MySQL database, which was created from scratch for this project. The MySQL instance was set up via the Google Cloud Platform. Users can leave a new review and rating for each airport, read previous users' reviews, view aggregated values of COVID-19 data, and view the data visualization of the COVID-19 related data. 

## Built With
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Pandas](https://pandas.pydata.org/)
* [Plotly](https://plotly.com/)
* [SqlAlchemy](https://www.sqlalchemy.org/)
* [PyYaml](https://pyyaml.org/)
* [HTML](https://www.html.com/)
* [Javascript](https://www.javascript.com/)

## Getting Started
First, install relevant Python packages including Flask

```pip install flask flask_sqlalchemy pymysql pyyaml plotly pandas```

Run the app using Flask

For `Mac OS`, `Linux`
```
export FLASK_APP=app
flask run
```

For `Windows`
```
set FLASK_APP=app
flask run
```
## Demo Video Link
https://youtu.be/sP0EiD96zE0

## Credits
Project Contributer:


|   Info      |        Description     |
| ----------- | ---------------------- |
| TeamID      |         101      |
| TeamName    |     abduFormedTeam|
| Captain     |  Wonjong (Jeff) Shin |
| Captain     |      wonjong2@illinois.edu     |
| Member1     |  Tejal Bajaj |
| Member1     |      tejalb2@illinois.edu     |
| Member2     |   Steven James   |
| Member2     |      sjames34@illinois.edu     |
| Member3     |   Tarun Voruganti   |
| Member3     |      tvorug2@illinois.edu     |
