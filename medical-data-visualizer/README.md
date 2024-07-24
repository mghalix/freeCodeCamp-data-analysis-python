<div spacer" style="padding: 15px 0px;"></div><h1 id="content-start" data-playwright-test-label="challenge-title">Medical Data Visualizer</h1><section id="description">
<p>In this project, you will visualize and make calculations from medical examination data using <code>matplotlib</code>, <code>seaborn</code>, and <code>pandas</code>. The dataset values were collected during medical examinations.</p>
<h2>Data description</h2>
<p>The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.</p>
<p>File name: medical_examination.csv</p>
<table>
<thead>
<tr>
<th align="center">Feature</th>
<th align="center">Variable Type</th>
<th align="center">Variable</th>
<th align="center">Value Type</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Age</td>
<td align="center">Objective Feature</td>
<td align="center"><code>age</code></td>
<td align="center">int (days)</td>
</tr>
<tr>
<td align="center">Height</td>
<td align="center">Objective Feature</td>
<td align="center"><code>height</code></td>
<td align="center">int (cm)</td>
</tr>
<tr>
<td align="center">Weight</td>
<td align="center">Objective Feature</td>
<td align="center"><code>weight</code></td>
<td align="center">float (kg)</td>
</tr>
<tr>
<td align="center">Gender</td>
<td align="center">Objective Feature</td>
<td align="center"><code>gender</code></td>
<td align="center">categorical code</td>
</tr>
<tr>
<td align="center">Systolic blood pressure</td>
<td align="center">Examination Feature</td>
<td align="center"><code>ap_hi</code></td>
<td align="center">int</td>
</tr>
<tr>
<td align="center">Diastolic blood pressure</td>
<td align="center">Examination Feature</td>
<td align="center"><code>ap_lo</code></td>
<td align="center">int</td>
</tr>
<tr>
<td align="center">Cholesterol</td>
<td align="center">Examination Feature</td>
<td align="center"><code>cholesterol</code></td>
<td align="center">1: normal, 2: above normal, 3: well above normal</td>
</tr>
<tr>
<td align="center">Glucose</td>
<td align="center">Examination Feature</td>
<td align="center"><code>gluc</code></td>
<td align="center">1: normal, 2: above normal, 3: well above normal</td>
</tr>
<tr>
<td align="center">Smoking</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>smoke</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Alcohol intake</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>alco</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Physical activity</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>active</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Presence or absence of cardiovascular disease</td>
<td align="center">Target Variable</td>
<td align="center"><code>cardio</code></td>
<td align="center">binary</td>
</tr>
</tbody>
</table>
<h2>Tasks</h2>
<p>Create a chart similar to
<figure>
    <center> <img src="./examples/Figure_1.png" width="1000"> </center>
</figure>
where we show the counts of good and bad outcomes for the <code>cholesterol</code>, <code>gluc</code>, <code>alco</code>, <code>active</code>, and <code>smoke</code> variables for patients with <code>cardio=1</code> and <code>cardio=0</code> in different panels.</p>
<p>Use the data to complete the following tasks in <code>medical_data_visualizer.py</code>:</p>
<ul>
<li>Add an <code>overweight</code> column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is &gt; 25 then the person is overweight. Use the value <code>0</code> for NOT overweight and the value <code>1</code> for overweight.</li>
<li>Normalize the data by making <code>0</code> always good and <code>1</code> always bad. If the value of <code>cholesterol</code> or <code>gluc</code> is <code>1</code>, make the value <code>0</code>. If the value is more than <code>1</code>, make the value <code>1</code>.</li>
<li>Convert the data into long format and create a chart that shows the value counts of the categorical features using <code>seaborn</code>'s <code>catplot()</code>. The dataset should be split by <code>Cardio</code> so there is one chart for each <code>cardio</code> value. The chart should look like <code>examples/Figure_1.png</code>.</li>
<li>Clean the data. Filter out the following patient segments that represent incorrect data:
<ul>
<li>diastolic pressure is higher than systolic (Keep the correct data with <code>(df['ap_lo'] &lt;= df['ap_hi'])</code>)</li>
<li>height is less than the 2.5th percentile (Keep the correct data with <code>(df['height'] &gt;= df['height'].quantile(0.025))</code>)</li>
<li>height is more than the 97.5th percentile</li>
<li>weight is less than the 2.5th percentile</li>
<li>weight is more than the 97.5th percentile</li>
</ul>
</li>
<li>Create a correlation matrix using the dataset. Plot the correlation matrix using <code>seaborn</code>'s <code>heatmap()</code>. Mask the upper triangle. The chart should look like this
<figure>
    <center> <img src="./examples/Figure_2.png" width=800> <center>
</figure>
<img
</ul>

<br>

---
[freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer)
