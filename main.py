from functions import *
from queries import *

#creating tables
exec_query(create_tables)

#loading data to tables
load_to_sql('rooms', './data/rooms.json')
load_to_sql('students', './data/students.json')

#queries mentioned in the task
print(exec_query_f(query_1))
print(exec_query_f(query_2))
print(exec_query_f(query_3))
print(exec_query_f(query_4))

#loading results to xml/json
load_to_json(query_2)
load_to_xml(query_3)
