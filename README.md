# Greendeck-intern-challenge
The project was <br>

##Function Descriptions

####QueryProcessing Class
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


####FilterProcessing Class
The functions in this class require the <b>operands</b> and the <b>operator</b> that is passed along
with the POST request.
<ul>

<li>
<b>discount()<br></b>
parameters:<br>
<ul>
<li>subset - </li>
<li>op - </li>
<li>op2 - </li>
</ul>
returns 
</li>

<li>
<b>brandname()<br></b>
parameters:<br>
<ul>
<li>subset - </li>
<li>op2 - </li>
</ul>
returns 
</li>

<li>
<b>discount_diff()<br></b>
parameters:<br>
<ul>
<li>subset_from_competition - </li>
<li>op - </li>
<li>op2 - </li>
<li>competing_id - </li>
</ul>
returns 
</li>

<li>
<b>competition()<br></b>
parameters:<br>
<ul>
<li>subset - </li>
<li>op2 - </li>
</ul>
returns 
</li>


</ul>

####API processing
  
  
 First filter the data to obtain a subset of the data<br>
 Take the subset and apply the queries to return result<br>
  
