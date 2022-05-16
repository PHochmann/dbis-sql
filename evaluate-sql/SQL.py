import sqlite3
from IPython.display import display, Markdown
from tabulate import tabulate

def evaluate_sql(path_to_db, query):
    conn = sqlite3.connect(path_to_db)
    cursor = conn.execute(query)
    attributes = [description[0] for description in cursor.description]
    tuples = cursor.fetchall()
    table = tabulate(tuples, attributes, tablefmt="github")
    display(Markdown(table))
    conn.close()
    