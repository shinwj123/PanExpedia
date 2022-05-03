# Project Reflection Report

### 1. Please list out changes in directions of your project if the final project is different from your original proposal (based on your stage 1 proposal submission)
       
- In the stage 1 proposal, we wanted to have COVID data based on the user’s destination city. However, the data we found on hospitalizations, testing, vaccinations, and testing was country-based, not city-based. Hence, we decided to make all our data based on the user’s destination country instead. Other than that, we were able to maintain the original intent and direction of our project. In general, the goals we outlined in our original proposal were all met in our final project.  

### 2. Discuss what you think your application achieved or failed to achieve regarding its usefulness.
       
- In general, we feel that our application achieved all the goals that it had to in order to prove its usefulness. We are properly using the data we have stored in our database, and through advanced database programs, users of our application have all the information they need to come to a decision about traveling to a certain website. Aside from the advanced database programs, we also have easy-to-understand graphs that users can use to come to an informed decision.   
      
### 3. Discuss if you change the schema or source of the data for your application
       
- While our current schema is very similar to the original schema that we created, one change we made was the specific attributes we put in some of the tables. For CovidCases, Testings, etc, we wanted to have separate attributes for both daily numbers and overall numbers. However, this wasn’t ideal because overall numbers are simply an aggregation. We instead changed it to store data using both dates and country as a key and removed the overall numbers attribute. Other than this small change we made during Stage 2, our schema and source of data remained the same.
     
### 4. Discuss what you change to your ER diagram and/or your table implementations. What are some differences between the original design and the final design? Why? What do you think is a more suitable design?
       
- We had a lot of modifications throughout the UML design. Our initial UML design had the UserProfile, Ratings, CountryData, CovidCases, Vaccination, Hospitalization, and Testing tables connected to the AirportData table with a foreign key constraint. Since the primary key in the tables of the CovidCases, Vaccination, Hospitalization, and the Testing were set as a country, we made the modification to connect them to the CountryData instead of AirportData with a foreign key. Furthermore, we made a modification of connecting the UserProfile and Ratings back to the AirportData since the users are leaving the review and ratings of the airport, not the country. Finally, since we had trouble letting users have many destination cities set up in their account, we had to let the user only select one destination city when giving the ratings, but they can switch their destination city in the user profile if they want to leave the rating for the different airport.    
     
### 5. Discuss what functionalities you added or removed. Why?
       
- We removed the ability to have multiple destination cities because we couldn’t store lists in SQL. We also added classifications for vaccination rate and death per covid case rate as part of our stored procedure. We never added links to websites to buy plane tickets as we said in our proposal but we ran out of time and it wasn’t as important of a feature.
     
### 6. Explain how you think your advanced database programs complement your application.
       
- For our trigger, when dealing with user input and databases, we have to be very careful of the values we are using in our queries, or else errors will pop up and things will break without the user knowing what happened. By checking the existence of the desired destination city, we can alert the user that their destination city is invalid rather than just breaking the page without them knowing what went wrong.
   
- Our stored procedure calculates some advanced metrics and displays them in a user-friendly way. The vaccination rate is important when traveling. The other rate we calculate is the death rate of people who get the virus. This shows how well people in a country recover from the virus. We display them in a way so that it’s classified as poor, below average, average, above average, or great so the user knows if the location they are going to is actually safe. Just displaying the rates themselves can be confusing because you do not have the context of other countries.
   
### 7. Each team member should describe one technical challenge that the team encountered. This should be sufficiently detailed such that another future team could use this as helpful advice if they were to start a similar project or where to maintain your project.
      
- Tejal: Since all of us were working on the project, we had a lot of branches that we were committing to. For our final demo, unfortunately, we faced the situation were in one branch, our trigger didn’t work, but in the other branch where the trigger did work, our delete didn’t work. We could have prevented this by merging our codes as soon as possible and working on the merged code, rather than our personal codebase.
   
- Steven: We had a lot of problems connecting the frontend and backend. A lot of buttons and features weren’t working when clicked but we could run queries in the background easily. Our current design is pretty much the same as our original design and has all the features we originally wanted.
   
- Tarun: Testing was very difficult and we used lots of print commands and alerts. There was no really good way to test or debug our code and many times we had to have the database running to see if our changes were actually occurring. I was brand new to using Flask so it took some time to figure out how everything worked together which meant lots of debugging. 
    
- Jeff: The main technical challenge that I have encountered was hosting the app on GCP and connecting to a MySQL database hosted on GCP. I have worked on the GCP application deployed, but couldn’t solve the problem on .yaml file to properly deploy on the cloud application.
      
### 8. Are there other things that changed comparing the final application with the original proposal?
       
- 	There weren't other things that changed comparing the final application with the original proposal.
     
### 9. Describe future work that you think, other than the interface, that the application can improve on
     
- We would like for users to be able to have multiple destination cities in their profile. This is difficult since you cannot save lists so we would probably have to create a new table to store the information. 
    
### 10. Describe the final division of labor and how well you managed teamwork. 
     
- Tejal: Frontend. Worked with HTML and Python to create the interactive graphs and UI elements.
- Steven: Full stack. Mainly worked with Flask and JavaScript to connect frontend components to functions that manipulate the database.
- Tarun: Backend. Took care of database connections and wrote many of the queries including the stored procedure and returned the results to the frontend.
- Jeff: Frontend and data science. Worked with HTML and CSS to create the UI elements, worked with Python to preprocess the CSV dataset, and worked on data architecture of the database.
    
We did the bulk of our coding in working sessions on Zoom, which allowed for real-time collaboration and division of labor. It also allowed us to solve conflicts as they came up instead of letting emotions simmer. For debugging purposes, we used pair programming (as opposed to doing it individually), which worked out with our overlapping roles as well. Overall, our teamwork was pretty good.
