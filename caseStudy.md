# Scenario :bike:

Cyclistic is a bike-sharing company in the city of Chicago (Illinois). For the sake of the company's survival, the marketing director wants to better understand how casual riders (those who pay full days or single passes) behave compared to members (this last group pays for a membership) in order to promote campaigns where the conversion towards "member" is a must for the company, as this group has been highlighted as the most profitable.

## Ask :question:

As a data analyst assigned to this task, the main problem I am trying to solve is to better **understand** how each group behaves and **indentify** patterns to propose creative data-drive decisions to increase the current number users paying for a membership. The principal stakeholder in this project is the Director of Marketing, as I will report directly to her and, besides, she is the one who will point out the route the company will take depending on the insights of my analysis. Besides this, it is important to note that the conclusions of my report will be based completely on the data recolected by the company, so it should clearly content positive business decisions that are hidden among millions of rows f data.

## Prepare  :man_factory_worker:

The data is located in the following [link](https://divvy-tripdata.s3.amazonaws.com/index.html) as a CSV file, thus we do not have any trust issues as it  was directly collected by the company and no other third party organizations participated in the data-collection process. As data was collected by the system itself, no trace of Bias was depicted. Data’s integrity was evaluated considering ownership, consent, currency, and privacy; as data was anonymous, most of these considerations are not relevant. Nevertheless, it is fundamental to let clear: (i) this data is not being sold and it is currently used exclusively by this organization and (ii) consent agreements are accepted by the client when using our bikes. Based on what has been previously stated, this data is reliable, current, comprehensive and original. This data will help me better understand the behavior of both groups by studying: (i) which are the more popular days, (ii) day period and (iii) year station for rentals for the company, (iv) where are most of the bikes being rented, (v) the average duration of trips and (vi) which type of bikes are mostly used. The only problem the data has is empty columns for critical information such as some start (and end, too) station ids, which will be treated during the cleaning stage.

## Process :broom:
Previous to the analysing step, it is important to clean the data. As most of the months have 100k+ entries, I decided to use python. I will upload all the functions I utilized to process the data in a folder called "python" later.


## Analyze :microscope:
