# for people in peopleList:
#     if people["Place"] == place and people["Music Type"] == musicType:
#         print(people["Name"] + " matches your description.")

#Connects to the sqlite datatable
import sqlite3
conn = sqlite3.connect('C:\\Users\\15164\\Downloads\\music_db.sqlite')
cursor = conn.cursor()

#Asks for the user's information
name = input("Please enter your name:")
country = input("Please enter your country:")
#If statement to only show up if the country is USA
state = ""
if country == "USA":
    state = input("Please enter your state or type BLANK:")
instrument = input("Please enter your Instrument:")
music_type = input("Please enter your Music Type:")
zipcode = input("Please enter your zipcode or type BLANK:")
bio = input("Please enter your bio or type BLANK:")

#Asks the user for specifications to match a person.

country = input("Please enter the countries you can travel to:")
#If statement to only show up if the country is USA
state = ""
if country == "USA":
    state = input("Please enter the states you can travel to or type BLANK for any:")
instrument = input("Please enter the instrument you would like to play with:")
music_type = input("Please enter the music genre you play:")
zipcode = input("Please enter your zipcode or type BLANK:")
bio = input("Please enter your bio or type BLANK:")

#Takes the values of the user input and inputs it into the datatable.
insert_query = f"""INSERT INTO Musician (NAME, Country, State, Instrument, MusicType, Zipcode, Biography)
VALUES ('{name}', '{country}', '{state}', '{instrument}', '{music_type}', {zipcode}, '{bio}');
"""
cursor.execute(insert_query)
conn.commit()

#Retrieves the ID of the last row in the datatable.
select_last_row_ID = """SELECT last_insert_rowid()"""
cursor.execute(select_last_row_ID)
current_user_id = (cursor.fetchone()[0])


#Shows musicians that have the specified country and isn't the user.
select_query = f"""SELECT * FROM Musician
WHERE country LIKE '{country}' AND NOT ID = {current_user_id} ;
"""

cursor.execute(select_query)
print(cursor.fetchall())
cursor.close()
conn.close()