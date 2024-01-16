# RPA Challenge

The project was developed following how an ETL proccess should work.

Firs the data was extracted from the gupy website, for this was used httpx to interact through the http protocol with the website and beautifulsoup4 to webscrap the content from the http response.

After this the raw data collected on previous step is treated and cleaned to a better data structure for the step of data insertion through the form. The data was mostly cleaned with python builtin functions.

After all data was cleaned the proccess to insert the data through the form was started. It was developed using httpx mostly and interacting with the API the form uses to insert the data sent.

The payload and endpoint for this insertion was collected analyzing the requests made by the browser when inserting the data manually through the form. The interaction directly through the api because the form when accessed by a web browser has components that changes their position and this could be a problem for a automation using selenium for example.


Once all the data is inserted on the forms the automation shows the time spent in every step of the whole proccess.