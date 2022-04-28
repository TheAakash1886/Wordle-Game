import sqlite3

def main():
    connection = sqlite3.connect('gameplay.db')

    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
                (Guess TEXT,Logistics TIME, Year INT)''')




    cursor.commit()
    cursor.close()
    
if __name__ == "__main__":                                        #run the main function
    main()