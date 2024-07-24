<div style="padding: 15px 0px;"><h1 id="content-start" data-playwright-test-label="challenge-title">Demographic Data Analyzer</h1>
<p>In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database. Here is a sample of what the data looks like:</p>
<pre class="language-markdown" tabindex="0" role="region" aria-label=" code example"><code class="language-markdown">|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | &lt;=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | &lt;=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | &lt;=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | &lt;=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | &lt;=50K    |
</code></pre>
<p>You must use Pandas to answer the following questions:</p>
<ul>
<li>How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (<code>race</code> column)</li>
<li>What is the average age of men?</li>
<li>What is the percentage of people who have a Bachelor's degree?</li>
<li>What percentage of people with advanced education (<code>Bachelors</code>, <code>Masters</code>, or <code>Doctorate</code>) make more than 50K?</li>
<li>What percentage of people without advanced education make more than 50K?</li>
<li>What is the minimum number of hours a person works per week?</li>
<li>What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?</li>
<li>What country has the highest percentage of people that earn &gt;50K and what is that percentage?</li>
<li>Identify the most popular occupation for those who earn &gt;50K in India.</li>
</ul>
<h2>Dataset Source</h2>
<p>Dua, D. and Graff, C. (2019). <a href="http://archive.ics.uci.edu/ml" target="_blank" rel="noopener noreferrer nofollow">UCI Machine Learning Repository</a>. Irvine, CA: University of California, School of Information and Computer Science.</p>


<br>

---
[freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer)

