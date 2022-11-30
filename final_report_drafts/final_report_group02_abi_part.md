# Exploratory Data Analysis

## Research Questions
In this project, I set out to answer 3 main research questions:

1. Which countries produce the highest percentage of their energy via coal when compared to that country's overall energy mix? Which countries produce the lowest percentage of their energy via coal when compared to that country's overall energy mix?
2. Which country has made the largest reduction in their usage of coal to produce energy between 1990 and 2018?
3. Has the same country dominated coal energy production from 1990 to 2018?
    
Whilst exploring the dataset, nothing jumped out at me since this dataset was from a very reputable source and was created professionally. I kept only the relevant columns through the data wrangling and cleaning process. Below, I will show some of the graphs I created during the exploratory data analysis which will not be used to answer the research questions listed above.

![Percentage of Electricity Generation via Coal in 2017](images/ad_elec_share_2017.png)

This graph displays the percentage of energy a country produced via coal in 2017 when compared to its' overall energy share mix.

![Change in Coal Consumption](images/ad_coal_change_cons.png)

This graph shows the annual change in coal consumption for each country as a sum for all the years of the dataset.

![Change in Coal Production](images/ad_coal_change_prod.png)

This graph is similiar to the one above, but show the anual change in coal production as a sum for all the years of the dataset.


# Which countries produce the highest and lowest percentage of their energy via coal when compared to that country's overall energy mix? 

In this section, I discovered which countries used coal to produce the most and least amount of their energy. In doing so, I created a graph to show which countries produced the most amount of energy via coal in 1990.

![Percentage of Electricity Generation via Coal in 1990](images/ad_elec_generation_1990.png)

This bar plot shows that, in 1990, Poland, South Africa, and Australia were among the countries which used coal to produce most of their energy. It can be seen that Poland and South Africa produced roughly 90% of their electricity through coal, while Australia's percentage was around 80%. On the other hand, the countries which used the least amount of coal to produce to their energy were Norway, Iran, and Sweden. All of whom which used coal to produce nearly none of their energy.

Alongside this graph, I also created a graph to show the countries and their percentages of electricy generation through coal in 2018.

![Percentage of Electricity Generation via Coal in 2018](images/ad_elec_generation_2018.png)

This bar plot shows that, although they have swapped positions, South Africa and Poland remain the countries which produced the most of their energy by coal in 2018. In third place is now India, with roughly 75% of their energy being generated via coal and Australia has significantly reduced their coal share to around 55%. The countries with the least percentage of their energy generated by coal in 2018 are Venezuela, Brazil, and New Zealand.

The results from this section show that, in 2018, the countries that use coal to produce most of their energy are South Africa and Poland and the countries using coal to produce the least of their energy are Venezuela and Brazil.

# Which country has made the largest reduction in their usage of coal to produce energy between 1990 and 2018?

This section aims to uncover which country has made the largest reduction in their usage of coal to produce energy between 1990 and 2018. I created a graph which shows the net change in a country's coal production between 1990 and 2018.

![The Change in a Country's Coal Production from 1990 to 2018](images/ad_change_coal_prod.png)

This graph shows that there are only a few countries that have decreased their coal production between 1990 and 2018, the largest reduction seems to have been made by the United States. To roughly quantify how much, we can see the production of coal by the United States in terawatt-hours in 1990 through this visualization below.

![A Country's Coal Production in 1990](images/ad_coal_prod_1990.png)

From this visualization, we can see that the United States was the second leading coal producer, with exactly 6260.927 terawatt-hours. Now to see how many Terawatt-hours of coal the United States produced in 2018, let us look at this visualization below.

![A Country's Coal Production in 2018](images/ad_coal_prod_2018.png)

We can see that the United States is well below the 5000 terawatt-hour mark, with exactly 4277.451 terawatt-hours of coal produced in 2018.

Throughout this section, we discovered that the country that made the largest reduction in coal production was the United States, with a 2033.476 terawatt-hour reduction from 1990 to 2018.

# Has the same country dominated coal energy production from 1990 to 2018?

This last section aims to uncover which country has dominated coal production over the span of 28 years, from 1990 to 2018. In order to anwer this question, I have created a map of the top coal producers from 1990.

![A Map of Global Coal Production in 1990](images/ad_coal_prod_map_1990.png)

This map is a representation of the largest coal producers in 1990, with the shade depicting the amount of coal production. The darker a country, the more coal it has produced. In this map, China and the United States are almost tied in their production of coal, with the difference being only 18.593 terawatt-hours. Now let us compare this map to the 2018 version.

![A Map of Global Coal Production in 2018](images/ad_coal_prod_map_2018.png)

It is very clear that China has clearly become the top coal producer by a great amount. We can see that the United States still remains in second place, but other than that it seems the other countries produced around the same amount of coal. To quantify how much China has increased its' coal production by, I have created a table.

A table of the top coal producing countries in 1990 and 2018:

| Country        | Coal Production (TWh) | Coal Production (TWh) | 
| :---           | :---:                 | :---:                 | 
| China          | 6279.520              | 21352.949             | 
| United States  | 6260.927              | 4277.451              | 
| Russia         | 2158.076              | 2562.787              | 
| Indonesia      | 73.534                | 3822.470              | 

This section has determined that the same country has dominated coal energy production from 1990 to 2018, that country being China. China has increased its' coal production by nearly 3.5 times and produces nearly 5 times as much coal as the United States which is in second in terms of coal production.