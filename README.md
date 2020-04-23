# Greendeck Data Science Intern Challenge
Project uses Flask and Python to build the backend. Postman was used for testing POST requests. App is hosted on
 Heroku. The url for the Heroku server is: https://enigmatic-mountain-99944.herokuapp.com/ <br>
 <b>NOTE: </b> Since there is no front end to the application, the user will get a Method Not Allowed response. Kindly use Postman 
 to check for responses to POST requests. 
<br><br>
It should also be noted that due to timeout error issues, I could not host the API with the test data on Heroku. I tried the template file given by Greendeck but it did not work. Then I tried zipping the file into 
my google drive, storing in my local machine, pushing to the heroku repo and then extracting it in the server. It still gave me timeout errors. A lot of effort was wasted trying to resolve this issue, therefore for demo purposes, I have 
stuck to the netaporter_gb_similar.json. However, I have tested this app with the test data on my local machine and it has worked throughout my testing.

Therefore, it would be appreciated if you run this repo on your local machine to get it running on test data.
<h2>Function Descriptions</h2>

<h3>QueryProcessing Class (queries.py)</h3>
These functions have been made such that most of the queries can be run even without a filter, which returns generic results on the entire dataset.
Additionally, multiple queries can be passed by adding a '|' after every query code in the POST request body. For eg. 
<b>{"query_type" : "discounted_products_list|avg_discount"}</b>. This would give 2 responses, a list of ids and an int for average discount. 
<br>
It is very <b>IMPORTANT</b> to note that if no filter is specified with the queries, an empty list should be passed along with the queries. For eg. 
<b>{"query_type" : "discounted_products_list|avg_discount", "filters":[ ]}</b>
<br><br>
 
<ul>

<li>
<b>discounted_product_list()<br></b>
parameters :<br>
<ul>
    <li>subset - json data as a list</li>   
</ul> 
>> returns a <b>list</b> of NAP product ids that are discounted. <br>
</li>

<li>
<b>discounted_product_count()<br></b>
parameters:<br>
<ul>
    <li>subset - json data as a list</li>   
</ul>
>> returns an <b>int</b> i.e. the number of NAP products that are discounted.
</li>

<li>
<b>avg_discount()<br></b>
parameters:<br>
<ul>
    <li>subset - json data as a list</li>   
</ul>
>> returns a <b>float</b> i.e. the average discount of all the products in the catalogue
</li>

<li>
<b>expensive_list()<br></b>
parameters:<br>
<ul>
    <li>subset - json data as a list</li>   
</ul>
>> returns a <b>list</b> of NAP products whose basket price is higher than any of the competing websites.
<b>NOTE: </b>The basket price of the competitor is taken form the 'min_price' section. This is because it is only logical
that a customer will buy the product with the minimum price first. Therefore, when comparing the 2 websites, the product
will compare minimum prices available. 
</li>

<li>
<b>competition_discount_diff_list()<br></b>
parameters:<br>
<ul>
    <li>subset - json data as a list</li> 
    <li>filters - the set of filters passed with the POST request</li>  
</ul>
>> returns a <b>list</b> of NAP product ids where the percentage difference between basket_prices of the NAP product and the competing product 
aligns with the discount_diff parameter ('>', '<', '==').<br>
This function depends on 2 filters (competition and discount_diff) that need to be present in the POST request. If not, will return error statement.<br>

</li>

</ul>


<h3>FilterProcessing Class (filters.py)</h3>
The functions in this class require the <b>operands</b> and the <b>operator</b> that is passed along
with the POST request.
<ul>

<li>
<b>discount()<br></b>
parameters:<br>
<ul>
<li>subset - json data as a list</li>
<li>op - either '==', '<' or '>'</li>
<li>op2 - an <b>int</b> that specifies the percentage discount of items</li>
</ul>
>> returns a <b>subset</b> of the data that contains only the products which match the discount criteria.
</li>

<li>
<b>brandname()<br></b>
parameters:<br>
<ul>
<li>subset - json data as a list</li>
<li>op2 - a <b>str</b> which specifies the brand name as found in the dataset.</li>
</ul>
>> returns a <b>subset</b> of the data that contains only the products which match the brandname criteria.
</li>

<li>
<b>discount_diff()<br></b>
parameters:<br>
<ul>
<li>subset_from_competition - <b>json data</b> got after using the competition filter</li>
<li>op - either '==', '<' or '>' </li>
<li>op2 - an <b>int</b> that specifies the difference of percentage discount between 
basket_prices of the NAP product and the competing product.</li>
<li>competing_id - <b>str</b> id of the competing website.</li>
</ul>
>> returns returns a <b>subset</b> of the data that contains only the products which match the discount_diff criteria.
<b>NOTE: </b> The discount_diff filter is only valid when there is a competition filter used as well. Otherwise, it will return an error statement.
</li>

<li>
<b>competition()<br></b>
parameters:<br>
<ul>
<li>subset - json data as a list</li>
<li>op2 - a <b>str</b> id of the competing website.</li>
</ul>
>> returns a <b>subset</b> of the data that contains only the products which match the competition criteria.
</li>


</ul>

<h3>API Processing</h3>
The API works in 2 steps. First the "filters" dictionary is grabbed from the request body and data is filtered accordingly. Since each filter function returns a subset of the data, that subset can then be used for another filter and so on. 
This way there is no confusion of different return values for filters and can be scaled or modified for further use.<br>
Once the filters are run, it will return a subset of the data that complies with all constraints. This can then be passed through the query functions which return their respective 
results, either a list of ids,  a float etc.<br>

This processing is handled by the <b>request_processing</b> function in the <b>data_processing.py</b> file.<br>
<br>
Additionally, there is a need to explain the API entry point, i.e the <b>api.py</b> file.
This is where the app is loaded.<br>
There are 2 optional functions defined in this file, namely <b>init_files()</b> and the <b>extract_zip()</b>.
The first function is used to download the data from a google drive link. The file_path is the parameter. The file itself is not restricted to json, but can also 
be a zip file.<br>
The second function is used only if a zipped dataset is downloaded. In that case, this method needs 
to be used before sending the data into the prepare_dataset method for further processing. 

<h3>Demo Request and Response and Steps to run on Heroku or localhost</h3>
<h4>Steps to run on localhost</h4>
<ol>
<li>Make sure you have installed flask, flask_cors, gdown and zipfile along with python3 to get everything running.</li>
<li>Depending upon the type of test file you want to test on, either download the data or use the demo data(which is the default data used). Check the 
api.py file and uncomment the both or the init_files() function call displayed by the arrow in the file.</li>
<li>In a terminal, type <code>python api.py</code></li>
<li>Should open the app on the default location <code>localhost:5000</code>. Still, check the terminal to see where the app is hosted. Go to that url.</li>
<li>Open Postman. Open a new tab in it. Change request type to <b>POST</b>. By default it is at <b>GET</b>.
Type the app URL in the bar beside the request type.
</li>
<li>
Select <b>Body</b> from the menu bar below and then select <b>raw</b> from the menu bar above the blank space.</li>
<li>Type request in this format: <br>
<code>{ "query_type": "discounted_products_list|avg_discount|discounted_product_count", 
  "filters": [{ "operand1": "discount", "operator": ">", "operand2": 30 }] } </code></li>
<li>Check the output in the response space below.</li>
</ol>

<h4>Steps to run on Heroku</h4>
As mentioned earlier, the URL is : https://enigmatic-mountain-99944.herokuapp.com/
<ol>
<li>Since the server is already running , there is no need to go the url.</li>
<li>Simply copy the URL and paste in the URL bar as was done for localhost in the earlier steps.</li>
<li>Give the request in the same way, and get the output.</li>
</ol>

This is a screenshot of Postman after the POST request is processed on the Heroku server.
![postman_screenshot](https://drive.google.com/uc?export=view&id=1-E4R2Kn-sL6z8HEILrVtjhfUiyA339_a)

Check out the <b>sample.jpg</b> in the root directory to see the screenshot if the picture is not being displayed in the pdf file.
