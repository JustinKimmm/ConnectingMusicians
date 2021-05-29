import sqlite3
conn = sqlite3.connect('C:\\Users\\15164\\Downloads\\music_db.sqlite')
cursor = conn.cursor()
x = "Saxophone"


class MatchingClass:
    def __init__(self):
        finalInput = cursor.execute("SELECT ID FROM Musician WHERE ID=(SELECT max(ID) FROM Musician);")
        print(type(finalInput));
        print(finalInput)
        select_query = f"""SELECT * FROM Musician
        WHERE instrument LIKE '{x}' AND NOT ID = '{finalInput}' ;
        """

        cursor.execute(select_query)
        print(cursor.fetchall())



MatchingClass()
