import pymongo
from my_parser import bed_list, date_list, location_list, description_list, title_list, price_list, source_list


client = pymongo.MongoClient('mongodb+srv://test_user:12345@cluster0.ie8qhwd.mongodb.net/?retryWrites=true&w=majority')
insert_method_db = client.get_database('my_database')
collection = insert_method_db.get_collection('my_collection')
data = []
for i in range(44):
    data.append({'bed': bed_list[i],
                 'date': date_list[i],
                 'location': location_list[i],
                 'description': description_list[i],
                 'title': title_list[i],
                 'price': price_list[i],
                 'image': source_list[i]})


collection.insert_many(data)


