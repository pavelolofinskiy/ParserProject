import pymongo
from my_parser import bed_list, date_list, location_list, description_list, title_list, price_list, src_list


client = pymongo.MongoClient('mongodb+srv://testdb:5504717aA@cluster0.4cuo9vy.mongodb.net/?retryWrites=true&w=majority')
insert_method_db = client.get_database('parserdb2')
collection = insert_method_db.get_collection('parser_data')
data = []
for i in range(39):
    data.append({'bed': bed_list[i],
                 'date': date_list[i],
                 'location': location_list[i],
                 'description': description_list[i],
                 'title': title_list[i],
                 'price': price_list[i],
                 'image': src_list[i]})


collection.insert_many(data)


