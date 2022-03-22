# Potholes in Chicago (2011 - 2018)

## Introduction

Intuition tells us that potholes are simply due to wear and tear of roads through general use over time. However, what if other external factors influence potholes and overall road quality? In this analysis, we seek to uncover what influences, outside of general wear and tear, affect road quality. We focus our analysis on Chicago, IL and explore the potential effect that income, neighborhood, traffic, and arrests have on potholes in the city. 

## Data Collection
For this analysis, the main source of data contains potholes reported through 3-1-1 service requests in the city of Chicago, IL from 2010 through 2018. The data was made available by the City of Chicago, along with data on traffic crashes reported through the electronic crash reporting system under the jurisdiction of the Chicago Police Department. Additionally, income data by neighborhood was sourced from the U.S. Census Bureau to analyze the correlation between pothole repairs and surrounding household residential income, and arrest data from the Chicago Police Department was used to investigate geographic relationships between density of potholes and surrounding area criminal activity.

**Data Dictionaries:**
- [Potholes](data/potholes_data_dictionary.csv)
- [Traffic Crashes](data/crash_data_dictionary.csv)
- [Census](data/census_data_dictionary.csv )
- [Arrest](data/arrest_data_dictionary.csv)

## Analysis: Seasonality by Neighborhood 
Before considering external influences, we need to understand what kind of general wear and tear likely causes potholes in Chicago. This analysis can be found [here](code/potholes_by_month.ipynb). The first bar plot below shows the total number of potholes created in each month. We can see that the top three months with potholes created are February, March, and April. The second bar plot below shows the month with the highest number of potholes created for each community area. Once again, we can see across the community areas that February, March, and April are the most common months with the most potholes created. This tells us that Chicago pothole are mostly created in the spring, which makes sense when we consider the hard winters that Chicago experiences and the damage created by the freezing, thawing, and plowing of the roads. 

![Plot 1](artifacts/counts_by_month.png)

![Plot 2](artifacts/top_months.png)

Now that we understand the baseline seasonal cause of potholes in Chicago, we can explore how other factors may exacerbate this damage. 

## Analysis: Pothole Status by Neighborhood
To visualize pothole service request status geographically, a map was created plotting open versus completed pothole requests in the Chicago area. A basemap of Chicago neighborhoods was used to analyze any correlation and provide visual context to the income analysis explore below. As seen on the map, there do appear to be neighborhoods with a higher ratio of open to closed pothole service requests, although more rigorous analysis is needed to determine an exact relationship. For example, a neighborhood may appear to have a higher concentration of open requests, however, due to the sheer volume of completed requests over the time frame, it is difficult to visually determine the true ratio.
![Plot 3](artifacts/pothole_status_map.png)

Looking at just the open potholes, I subtracted todays date from `Creation Date` to create the column `Days_Open` to see which areas of Chicago had the longest ongoing unserviced potholes. The code for this part can be found [here](code/open_potholes_map.ipynb). Interestingly, the average time of these service requests have been open are much longer than the average completion time for the closed requests, and the longest unserviced areas are concentrated in the northwest Chicago area.

![Plot 4](artifacts/open_potholes.png)


## Analysis: Completion Time and Per Capita Income
The code for this part of the analysis can be found [here](code/census-pot.ipynb).
The idea was an exploration of the relationship between pothole completion times and income in Chicago's 77 community zones. First, the `Completion Time` variable was created by subtracting `Creation Date` from `Completion Date`. Then the `potholes` dataset was grouped by `Community Area`, where we calculated the total counts of potholes and the mean completion time of potholes by community area. This data frame was then merged with the `census_data` data frame into a final form `working_data`, which has each community area and community area name along with their per capita incomes, total counts of potholes over the years, and average completion time.

In the following two plots, the per capita income of the neighborhoods with the top 5 longest completion times and top 5 shortest completion times are shown. These metrics were calculated by viewing `working_data.head() ` and `working_data.tail()`. It seems that the incomes of neighborhoods with longer completion times are higher, but this analysis does not include other confounding variables, such as the population of each community area.
![Plot 5](artifacts/top_5.png)
![Plot 6](artifacts/bottom_5.png)

To further this analysis, a scatterplot was created with `Per Capita Income` on the x-axis and `Completion Time` on the y-axis: ![Plot 1](artifacts/income_scatter.png)
In the scatterplot, the color scale is by number of potholes, with the darkest points having the fewest number of potholes and the lighest points having the most potholes in that community zone. We see that in areas with the lowest incomes, even having a smaller number of potholes than in richer areas results in a slower average completion time.

Expanding on our analysis of income, we take a further look into how total potholes compares to per capita income in this [file](code/potholes_by_income.ipynb). While we have uncovered some of the relationship between pothole completion time and income, it is important to consider if total number of potholes in each area is correlated with income. After grouping the data by `Community Area`, we can total the number of potholes and compare that to the per capita income of the area.  From the bar plot below, we can see that as per capita income decreases, there is a subtle upward trend in number of potholes. This provides some visual evidence of a potential relationship between per capita income and potholes. 

![Plot 7](artifacts/counts_by_income.png)

## Analysis: Potholes vs. Traffic Crashes
In this analysis, we attempt to visualize the density of potholes and traffic crashes due to road defects. The traffic crash data was obtained from the City of Chicago and the Chicago Police Department and was filtered to only include crashes during the 2010 - 2018 timeframe that were caused by rut or hole road defects. These were then plotted alongside potholes (both open and completed) over the neighborhood map. From the plot below, we can see that certain neighborhoods, particularly in the Northwest and Southwest regions, have a high percentage of both potholes and traffic crashes, ostensibly a significant portion of which were directly caused by potholes. Further rigorous analysis including linkage of crashes to potholes through latitude and longitude and time stamps would provide a clearer methodology to investigate how potholes affect public health across neighborhoods.  
![Plot 9](artifacts/dualmap.png)

## Analysis: Potholes vs. Arrests in the Chicago Area
The code used for the analysis can be found [here](code/arrestdata.ipynb).
The motivation was that for each police district, there might be more intense activities where the arrests happen more which might lead to increased numbers of potholes. As the arrest data was available for 2014-2017, I focused on the years of 2014-2017 in the potholes data. I grouped the data and counted all the arrests and created potholes in those years and plotted them by police districts.
![Plot 10](artifacts/arrests_and_potholes.png)
Unfortunately, it does not seem they are closely correlated.

## Analysis: OLS Regression
To better understand the relation between our pothole data and other social factors, a regression analysis was used. Data wrangling on our main data set, census data, and crime statistics allowed to produce the necessary variables. The dependent variable in the first regression was total pothole density (count/km^2), and for the second it was average pothole service request completion time; both separated by community area. The regressors were average income, percentage of people below the poverty line, yearly crime expected rate, and population density (people/km^2); all by community area.
The results for the first regression clearly indicate significant effects for crime rate, population density, and population below the poverty line. The latter, notably, is negative; this is possibly due to car ownership among empoverished people. The R-squared is fairly high at around 0.69 .
![Table 3](artifacts/reg1.png)
The results for the second regression indicate only a significant effect for population density, and a fairly low R-squared of about 0.16, indicating that contrarily to our intuition, the factors chose were not very relevant predictors of pothole servicing time.
![Table 4](artifacts/reg2.png)

## Conclusion

Through our analysis we have explored the factors that generally influence road quality in the Chicago area from 2010 to 2018. We pick some potentially relevant predictors of potholes such as crime and traffic crashes to support our analysis. We, unsurprisingly find that months coming from winter see most potholes created as compared to other months throghout the year. We also find that certain neighborhoods within the Chicago Area had more potholes than others. However, this may be due to more pothole services being requested in those specific neighborhoods. Further, we look into the time it takes for potholes to be services,  and find that it takes much longer for the Northwest of Chicago poholes to be fixed than for other areas of Chicago. Our analysis shows that neighborhoods with higher income have longer completion time, which is counterintuitive to what we would expect. We attribute this finding to potential confounding factors such as population in that area. We also look at any potential correlation between potholes and traffic crashes and observe a positive correlation between the two for the Northwest and Southwest regions but not other areas. Further, looking at arrests we do not find any statistically significant correlation between the number of arrests and the number of potholes. Lastly, we run a regression analysis to show the relation between potholes with other social factors and we do not find any relevant predictors for pothole servicing time. 


## Data Limitations and extensions
We could not find recent data for the potholes in the Chicago area; 
The were a lot of missing data in the Pothole dataset; 
We could not find data on Chicago Area arrests for years 2010-2013 and 2018. So, we focused our pothole-arrest analysis on years 2014-2017; 
Linkage of crashes to potholes through latitude and longitude and time stamps would be needed to provide a clearer methodology; 
