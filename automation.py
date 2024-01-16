from datetime import datetime

from rpa_challenge.data_extraction import extract_data_from_gupy, clean_data_from_gupy
from rpa_challenge.data_post import post_data_to_form


start_data_extraction = datetime.now()
print(f"Data extraction started at: {start_data_extraction}")
data = extract_data_from_gupy("https://gruposeb.gupy.io/")
end_data_extraction = datetime.now()
print(f"Data extraction finished at: {end_data_extraction}")
total_time_extraction = end_data_extraction - start_data_extraction
print(f"Total time to data extraction: {total_time_extraction}")

start_data_cleaning = datetime.now()
print(f"Data cleaning started at: {start_data_cleaning}")
cleaned_data = clean_data_from_gupy(data)
end_data_cleaning = datetime.now()
print(f"Data cleaning finished at: {end_data_cleaning}")
total_time_data_cleaning = end_data_cleaning - start_data_cleaning
print(f"Total time to data cleaning: {total_time_data_cleaning}")

start_data_posting = datetime.now()
print(f"Data posting started at: {start_data_posting}")
print(
    post_data_to_form(
        cleaned_data,
        "https://forms.office.com/formapi/api/be041442-f3b6-4be1-8509-eca9c817528f/users/b50b72bb-53b3-439f-a149-94cf380b5e27/forms('QhQEvrbz4UuFCeypyBdSj7tyC7WzU59DoUmUzzgLXidUNllOQ0JYNjVMSDZSN1Q4MUFZWlVXQkw0UC4u')/responses",
        "r28823796bb8b461195112faa4376895e",
        "r62327b3de37b4158b46eb9bf1ff8b45d",
        "rb496f0bcd3a44b0baf03ea81caa84243"
    )
)
end_data_posting = datetime.now()
print(f"Data posting finished at: {end_data_posting}")
total_time_posting = end_data_posting - start_data_posting
print(f"Total time to data posting: {total_time_posting}")