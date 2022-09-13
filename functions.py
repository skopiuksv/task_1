from psycopg2 import connect
from config import credentials, engine
import pandas as pd


def conn():
    """
    create connection to db
    :return: connection object
    """
    con = connect(
        host=credentials['HOST'],
        user=credentials['USER'],
        password=credentials['PASSWORD'],
        database=credentials['DBNAME'],
        port=credentials['PORT']
    )
    con.autocommit = True
    return con


def disconnect():
    """
    closes connection to db
    :return: None
    """
    conn().cursor().close()
    conn().close()


def exec_query(query):
    """
    execute given query w/o fetchall
    :param query: sql query
    :return: None
    """
    cursor = conn().cursor()
    cursor.execute(query)
    disconnect()


def exec_query_f(query):
    """
    execute given query with fetchall
    :param query: sql query
    :return: result of query
    """
    cursor = conn().cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    disconnect()
    return res


def load_to_sql(table, dir_json_file):
    """
    load json to db
    :param table: db table
    :param dir_json_file: json file directory
    :return: None
    """
    df = pd.read_json(dir_json_file)
    df.to_sql(table, con=engine, index=False, if_exists='append')


def load_to_xml(query):
    """
    load results to xml file
    :param query: sql query
    :return: None
    """
    df = pd.DataFrame(exec_query_f(query), columns=[f'column_{i}' for i in range(len(exec_query_f(query)[0]))])
    df.to_xml('./results/pupa.xml')


def load_to_json(query):
    """
    load results to json file
    :param query: sql query
    :return: None
    """
    df = pd.DataFrame(exec_query_f(query), columns=[f'column_{i}' for i in range(len(exec_query_f(query)[0]))])
    df.to_json('./results/lupa.json')
