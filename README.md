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

### display (e.g., layout)

### grouped bars - created using d3

#### the information presented (e.g., explanatory text to facilitate the comprehension of the datasets presented)

- Used for wages data
  - A grouped bar chart showing average Indonesian monthly wage by year and gender. From 1999-2018, wages have increased for both females and males. The wage disparity between the two genders persists consistently throughout these years.

#### the charts (e.g., choice of form and visual encodings, axes, etc.) 

- If there are two or more sets of categories for which we want to show amounts, we can group or stack the bars (Chapter 6).
- Proportions can be visualized as pie charts, side-by-side bars, or stacked bars (Chapter 10).
- Grouped bars are used to visualize multiple sets of proportions. Grouped bars work well as long as the number of conditions compared is moderate (in this case two).

### line graph - created using Google Charts

#### the information presented (e.g., explanatory text to facilitate the comprehension of the datasets presented)

- Used for life expectancy data
  - Life Expectancy at Birth Year based on Country

#### the charts (e.g., choice of form and visual encodings, axes, etc.) 

- When the x axis represents time or a strictly increasing quantity such as a treatment dose, we commonly draw line graphs (Chapter 13). 
- We often have multiple time courses that we want to show at once.
- Figure 13-6 represents an acceptable visualization of the preprints dataset. However, the separate legend creates unnecessary cognitive load. We can reduce this cognitive load by labeling the lines directly (Figure 13-7). I have also eliminated the individual dots in this figure, for a result that is much more streamlined and easy to read than the original starting point, Figure 13-5.

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
