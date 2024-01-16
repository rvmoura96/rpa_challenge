from datetime import datetime

from httpx import post


def post_data_to_form(
        cleaned_data: list =[],
        url: str ="https://forms.office.com/formapi/api/be041442-f3b6-4be1-8509-eca9c817528f/users/b50b72bb-53b3-439f-a149-94cf380b5e27/forms('QhQEvrbz4UuFCeypyBdSj7tyC7WzU59DoUmUzzgLXidUNllOQ0JYNjVMSDZSN1Q4MUFZWlVXQkw0UC4u')/responses",
        function_key_id: str ="r28823796bb8b461195112faa4376895e",
        city_key_id: str ="r62327b3de37b4158b46eb9bf1ff8b45d",
        job_type_id: str ="rb496f0bcd3a44b0baf03ea81caa84243"
        ) -> str:
    """
    Submit the data extracted from extract_data_from_gupy to forms from office.

    In case of success return a message that all data was successufully posted otherwise an error message.

    expected cleaned_data pattern:
    [
        {'function': 'job function description', 'location': 'job location', 'type': 'job type'},
        {'function': 'job function description', 'location': 'job location', 'type': 'job type'},
    ]

    Keyword arguments:
        cleaned_data (list): a list of objects get on extract_data_from_gupy function (default=[])
        url (str): url for forms office (default=https://forms.office.com/formapi/api/be041442-f3b6-4be1-8509-eca9c817528f/users/b50b72bb-53b3-439f-a149-94cf380b5e27/forms('QhQEvrbz4UuFCeypyBdSj7tyC7WzU59DoUmUzzgLXidUNllOQ0JYNjVMSDZSN1Q4MUFZWlVXQkw0UC4u')/responses)
        function_key_id (str): id sent on post linking function to the form (default=r28823796bb8b461195112faa4376895e)
        city_key_id (str): id sent on post linking to the city to the form (default=r62327b3de37b4158b46eb9bf1ff8b45d),
        job_type_id (str): id sent on post linkint to job type flag(default=rb496f0bcd3a44b0baf03ea81caa84243)
    returns:
        str: A message with the execution success or failure
    """


    status_codes = list()
    if cleaned_data:
        for data in cleaned_data:
            payload = create_post_payload(data, function_key_id, city_key_id, job_type_id)
            response = post(url,json=payload)
            
            if response.status_code == 201:
                status_codes.append(response.status_code)
        
        if len(status_codes) == len(cleaned_data):
            return "All data successfully posted."
    
        return "Error submiting some entries."
    return "No entries provided."


def create_post_payload(
        input_data: dict = {},
        function_key_id: str = "r28823796bb8b461195112faa4376895e",
        city_key_id: str = "r62327b3de37b4158b46eb9bf1ff8b45d",
        job_type_id: str = "rb496f0bcd3a44b0baf03ea81caa84243"
        ) -> dict:
        """
        Create a payload used on the post request on post_data_to_form function.

        Keyword arguments:
            input_data (dict): A dict containing the data used to fill the post request.
            function_key_id (str): id sent on post linking function to the form (default=r28823796bb8b461195112faa4376895e)
            city_key_id (str): id sent on post linking to the city to the form (default=r62327b3de37b4158b46eb9bf1ff8b45d),
            job_type_id (str): id sent on post linkint to job type flag(default=rb496f0bcd3a44b0baf03ea81caa84243)

        returns:
            dict: A dict with the following pattern
            {
              'startDate': 'isoformatdatetime',
              'submitDate': 'isoformatdatetime',
              'answers': [
                {'questionId': function_key_id, answer1: function},
                {'questionId': city_key_id, answer1: city},
                {'questionId': job_type_id, answer1: job_type},
               ]

            }
        """
        function = input_data["function"]
        city = input_data["location"]
        job_type = "Não" if input_data["type"] != "Efetivo" else "Sim"
        
        function_key = {"questionId": function_key_id, "answer1": function}
        city_key = {"questionId": city_key_id, "answer1": city}
        job_key = {"questionId": job_type_id, "answer1": job_type}
        
        payload = {
            'startDate': f"{datetime.now().isoformat()}Z",
            'submitDate': f"{datetime.now().isoformat()}Z",
            'answers': f'[{function_key},{city_key},{job_key}]'
        }
        return payload