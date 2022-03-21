# Chicago Potholes Data (2011 - 2017) or some better title
Requirements for reporting your analysis:

The goal of the analysis is must be clearly articulated
The report must include your methodology
The report must include a description of your project and its findings (or lack of findings)
Your findings (or non-findings) must be clearly documented
The limitations of the analysis must be clearly outlined
Extensions of your analysis or areas for more research must be included in your report
You should not include analysis, plots, discoveries, that aren’t directly related to your findings – you can put them as an appendix in another file if you like

## Analysis: Completion Time and Per Capita Income
In this part of the analysis, the goal was to explore the relationship between pothole completion times and income in Chicago's 77 community zones. First, the `Completion Time` variable was created by subtracting `Creation Date` from `Completion Date`, then averaging by community zone to find the average pothole completion time per community zone in days. Then, a scatterplot was created with `Per Capita Income` on the x-axis and `Completion Time` on the y-axis. In the plot below, the color scale is coded by `Hardship Index`, which is a scale from 1 - 100 from the City of Chicago's Department of Public Health indicating the level of "hardship" in living in a certain area. For more information, see [here](https://greatcities.uic.edu/2016/09/19/economic-hardship-index-shows-stark-inequality-across-chicago/#:~:text=Some%20of%20the%20highest%20index%20scores%20in%20Chicago,the%20highest%20hardship%20index%20scores%20in%20the%20city.?msclkid=dd0fdca1a95111ec950a83f104985331). We see from this plot that average completion time does not vary much between income levels at the lower range, but completion time significantly falls as per capita income increases. 

