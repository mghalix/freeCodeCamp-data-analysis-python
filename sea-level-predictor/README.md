<div style="padding: 15px 0px;"><h1 id="content-start" data-playwright-test-label="challenge-title">Sea Level Predictor</h1></div>
<p>You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.</p>
<p>Use the data to complete the following tasks:</p>
<ul>
<li>Use Pandas to import the data from <code>epa-sea-level.csv</code>.</li>
<li>Use matplotlib to create a scatter plot using the <code>Year</code> column as the x-axis and the <code>CSIRO Adjusted Sea Level</code> column as the y-axis.</li>
<li>Use the <code>linregress</code> function from <code>scipy.stats</code> to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.</li>
<li>Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.</li>
<li>The x label should be <code>Year</code>, the y label should be <code>Sea Level (inches)</code>, and the title should be <code>Rise in Sea Level</code>.</li>
</ul>
<p>The boilerplate also includes commands to save and return the image.</p>

<h2>Data Source</h2>
<p><a href="https://datahub.io/core/sea-level-rise" target="_blank" rel="noopener noreferrer nofollow">Global Average Absolute Sea Level Change</a>, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.</p>

<br>

---
[freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor)

