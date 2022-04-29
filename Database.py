import sqlite3
import datetime
import socket
import os
import sys

class SQDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('gameplay.db')
        self.cur = self.connection.cursor()

        self.cur.execute(
            '''CREATE TABLE IF NOT Exists GameStats (gno integer primary key autoincrement, time text, ip text, attempts integer, input text, wordle text, log text, foreignid integer, foreign key(foreignid) references game_main(gid))''')
        self.cur.execute(
            '''CREATE TABLE IF NOT Exists GameStatsInfo (gno integer primary key autoincrement, time text, Wins text, GamesNo integer, WinPercentage integer, Guesses text, foreignid integer, foreign key(foreignid) references game_main(gno))''')
        self.prev_id = 0

    def ip_data(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            soc.connect(('10.156.86.76', 1))
            IP = soc.getsockname()[0]
        except Exception:
            IP = 'Default IP: 127.0.0.1'
        finally:
            soc.close()
        return IP

    def GameDetails(self, attempts, input_word, wordle, log):
        current_time = datetime.datetime.now()
        socks = self.ip_data()
        self.cur.execute(
            "insert into GameStats values (null, ?, ?, ?, ?, ?, ?, ?)", ( current_time, socks, attempts, input_word, wordle, log, self.prev_id))

    def GameStatistics(self, win_status, number_of_games, win_percentage, guesses):
        current_time = datetime.datetime.now()
        self.cur.execute(
            "insert into GameStatsInfo values (null, ?, ?, ?, ?, ?, ?)", (current_time, win_status, number_of_games, win_percentage, guesses, self.prev_id))

    def DatabaseClose(self):
        self.connection.commit()
        print("Written Game records")
        self.connection.close()

    def analyze(self, startdate, enddate):
        if not os.path.exists("GameReport.txt"):
            f = open('GameReport.txt', 'w+')
        self.cur.execute(
            "SELECT * FROM 'GameStats' where time between :startdate and :enddate", {"startdate": startdate, "enddate": enddate})
        temp = self.cur.fetchall()
        with open('report.txt', 'w') as f:
            f.write(str(temp))
        print(
            f"\nReport generated successfully for date range entered between {startdate} and {enddate} \n")