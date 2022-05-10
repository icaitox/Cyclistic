# Scenario :bike:

Cyclistic is a bike-sharing company in the city of Chicago (Illinois). For the sake of the company's survival, the marketing director wants to better understand how casual riders (those who pay full days or single passes) behave compared to members (this last group pays for a membership) in order to promote campaigns where the conversion towards "member" is a must for the company, as this group has been highlighted as the most profitable.

## Ask :question:

As a data analyst assigned to this task, the main problem I am trying to solve is to better **understand** how each group behaves and **indentify** patterns to propose creative data-drive decisions to increase the current number users paying for a membership. The principal stakeholder in this project is the Director of Marketing, as I will report directly to her and, besides, she is the one who will point out the route the company will take depending on the insights of my analysis. Besides this, it is important to note that the conclusions of my report will be based completely on the data recolected by the company, so it should clearly content positive business decisions that are hidden among millions of rows f data.

## Prepare  :man_factory_worker:

The data is located in the following [link](https://divvy-tripdata.s3.amazonaws.com/index.html) as a CSV file, thus we do not have any trust issues as it  was directly collected by the company and no other third party organizations participated in the data-collection process. As data was collected by the system itself, no trace of Bias was depicted. Data’s integrity was evaluated considering ownership, consent, currency, and privacy; as data was anonymous, most of these considerations are not relevant. Nevertheless, it is fundamental to let clear: (i) this data is not being sold and it is currently used exclusively by this organization and (ii) consent agreements are accepted by the client when using our bikes. Based on what has been previously stated, this data is reliable, current, comprehensive and original. This data will help me better understand the behavior of both groups by studying: (i) which are the more popular days, (ii) day period and (iii) year station for rentals for the company, (iv) where are most of the bikes being rented, (v) the average duration of trips and (vi) which type of bikes are mostly used. The only problem the data has is empty columns for critical information such as some start (and end, too) station ids, which will be treated during the cleaning stage.

## Process :broom:
Previous to the analysing step, it is important to clean the data. As most of the months have 100k+ entries, I decided to use python. For adding new columns, I defined two functions in the "/python/functions.py" directory. Here, I define them:

- tripnday: this function receives a dataFrame and adds the columns 'trip_length' (duration of the trip), 'week_day' (which day the bike was rented), and 'time_frame' (defines at which period of the day the trip started). 
- clean: this function receives a dataFrame and returns another dataframe which only contains trip lengths greater than 90 seconds but less than 1 day. It was established as it was considered that all rentals that took less than the minimum were "misrentals" (customer regrets about the rental) and those with a length of more than a day were considered "pollution", as target audience would not rent a bike for more than a day.

As monthly CSV were available at the download repository, another function was defined: **concatData**, which receives a list of dataframes and returns them all concatenated as an unique dataframe. Doubles were erased 

All of the empty values were at start or end station ID, and since this data was not taken into consideration for plotting -latitude and longitude were utilized for geolocating-, no further processing was needed.

## Analyze :microscope:
After cleaning, data was chronologically organized and the analyzing stage started (the twelve-month period between March 21 and March 22 was selected). Curiously, most of the users for this period (55.7%) were already paying for the membership, so previous campaigns have had a positive effect overall. Another highlight obtained from data was that the arrival of Summer pumped both casual and members rides, nevestheless the latter maintained steady numbers until October, where a negative trend is identified and associated with lower temperatures. Related to the most popular days for rentals, casuals were more common during weekends while members tend to rent the most over weekdays; similarly, the formers had an average of 27 minutes of ride compared to the 13 and a half minutes of the latter. For both groups, the afternoon was the preferred time block for the rentals, and the most popular bicycles among them was the classic one. With regard to the locations, a density map of Chicago will be shown, where hot spots will be observed. 

By understanding these facts, the company will be in a better position to suggest marketing proposals.
