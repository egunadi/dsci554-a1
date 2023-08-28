[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/heHvgCiq)
# DSCI 554 Assignment 1

- [ASSIGNMENT.md](ASSIGNMENT.md) contains the Rubric

## Landing page instructions

"index.html" is the landing page. It can be served on a browser via hot-reload:

```bash
npm install    #install js libraries
npm run serve  #starts server on port 2000
```
Alternately, this page can be viewed in GitHub at <https://egunadi.github.io/dsci554-a1/>.

## Design choices 

The landing page showcases two visualizations, laid out side-by-side with thumbnails and a brief description. 

### Average Indonesian Monthly Wage by Year and Gender

This is a d3 grouped bar chart showing average Indonesian monthly wage by year and gender. From 1999-2018, wages have increased for both females and males. The wage disparity between the two genders persists consistently throughout these years.

A grouped bar chart was chosen since it both shows amounts (in this case, monthly wage) and proportions (in this case, comparing wages between men and women).

### Life Expectancy at Birth Year based on Country

This is a Google Charts line graph projecting life expectancy at birth from 1950-2100 for Indonesia and USA. Over time, the disparity between the two countries seem to converge at the 80-90 year age-range.

A line graph was chosen since we are interested in how life expectancy changes over time (the x axis). Having grown up in both Indonesia and USA, I was interested in comparing time courses for these two countries.

## Running the project

Processed data used for visualization are available in "d3_plot/subset_data" and "googlecharts_plot/subset_data". 

For details on how the raw data was processed, see scripts:

- "d3_plot/subset_code/wages.py"
- "googlecharts_plot/subset_code/life_expectancy.py" 

(The environment.yml file included can be used to recreate the Python environment used.)

Raw data is stored in the "data/pixstory" folder. The data on wages can be redownloaded here:

<http://data.un.org/Data.aspx?q=indonesia&d=LABORSTA&f=tableCode%3a5A%3bcountryCode%3aID&c=2,3,5,7,9,11,13,15,17,18&s=country_nameEnglish:asc,yr:desc,sexCode:asc&v=1>

(Note that a fresh download includes a footnote section that must be removed before the file can be processed.)

As for the data on life expectancy, it can be redownloaded here:

<http://data.un.org/Data.aspx?q=indonesia&d=PopDiv&f=variableID%3a68%3bcrID%3a360%2c840&c=2,4,6,7&s=_crEngNameOrderBy:asc,_timeEngNameOrderBy:desc,_varEngNameOrderBy:asc&v=1>
