from tkinter import *
import sqlite3


TABLETENNIS_DB="TableTennis.db"
FOREIGN_KEYS_ON="PRAGMA foreign_keys = ON"

def query(sql,data):
    with sqlite3.connect(TABLETENNIS_DB) as db:
        cursor = db.cursor()
        cursor.execute(FOREIGN_KEYS_ON)
        cursor.execute(sql,data)
        db.commit()


#def insert_graph():
    


def PointWon(matchId, shotName):
    sqltxt = 'update Shots set PointsWon=PointsWon + 1 where (MatchID=? and ShotName=?)'
    data = (matchId,shotName)
    query(sqltxt,data)

def PointLost(matchId, shotName):
    sqltxt = 'update Shots set PointsLost=PointsLost + 1 where (MatchID=? and ShotName=?)'
    data = (matchId,shotName)
    query(sqltxt,data)


def insert_match_details():
    popup = Tk()
    Label(popup, text="Opponent first name = ").grid(row=0)
    Label(popup, text="Opponent surname = ").grid(row=1)
    Label(popup, text="Tournament name = ").grid(row=2)
    Label(popup, text="Date of match with format DD/MM/YYYY = ").grid(row=3)
    Label(popup, text="Time of the match with format HH:MM = ").grid(row=4)
    first_name = Entry(popup)
    surname = Entry(popup)
    tournament = Entry(popup)
    date = Entry(popup)
    time = Entry(popup)
    first_name.grid(row=0,column=1)
    surname.grid(row=1,column=1)
    tournament.grid(row=2,column=1)
    date.grid(row=3,column=1)
    time.grid(row=4,column=1)
    Button(popup, text="Add", command=lambda: insert_new_match_details(first_name,surname,tournament,date,time), width=10).grid(row=5, column=0)
    Button(popup, text="Back", command=popup.destroy, width=10).grid(row=5, column=1)


def insert_new_match_details(first_name,surname,tournament,date,time):
    sql = "insert into MatchDetails (FirstName, Surname, TournamentName, Date, Time) values (?,?,?,?,?)"
    values = (first_name.get(),surname.get(),tournament.get(),date.get(),time.get())
    query(sql,values)
    match_id(first_name.get(),surname.get(),tournament.get(),date.get(),time.get())


def match_id(first_name,surname,tournament,date,time):
    with sqlite3.connect("TableTennis.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select MatchID from (MatchDetails) where (FirstName=? and Surname=? and TournamentName=? and Date=? and Time=?)",(first_name,surname,tournament,date,time))
        matchID = cursor.fetchone()
        for i in matchID:
            shot_names(i)

def shot_names(matchID):
    with sqlite3.connect("TableTennis.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        serve = ("Serve")
        push = ("Push")
        flick = ("Flick")
        normaltopspin = ("Normal topspin")
        smash = ("Smash")
        topspinagainstbackspin = ("Topspin against backspin")
        countertopspin = ("Counter topspin")
        block = ("Block")
        lefthanded = ("Left handed")

        pointwon = 0
        pointlost = 0

        sql = "insert into Shots (MatchID,ShotName,PointsWon,PointsLost) values (?,?,?,?)"
        data = [(matchID,serve,pointwon,pointlost),(matchID,push,pointwon,pointlost),(matchID,flick,pointwon,pointlost),(matchID,normaltopspin,pointwon,pointlost),(matchID,smash,pointwon,pointlost),(matchID,topspinagainstbackspin,pointwon,pointlost),(matchID,countertopspin,pointwon,pointlost),(matchID,block,pointwon,pointlost),(matchID,lefthanded,pointwon,pointlost)]
        for i in data:
            query(sql,i)

        insert_shot_details(matchID)


def insert_shot_details(matchID):
    popup = Tk()
    Label(popup, text="Serve: ").grid(row=0, column=0)
    Label(popup, text="Push: ").grid(row=1, column=0)
    Label(popup, text="Flick: ").grid(row=2, column=0)
    Label(popup, text="Normal topspin: ").grid(row=3, column=0)
    Label(popup, text="Smash: ").grid(row=4, column=0)
    Label(popup, text="Topsin against backspin: ").grid(row=5, column=0)
    Label(popup, text="Counter topspin: ").grid(row=6, column=0)
    Label(popup, text="Block: ").grid(row=7, column=0)
    Label(popup, text="Left handed: ").grid(row=8, column=0)

    Button(popup, text="Point won", command=lambda:PointWon(matchID,"Serve"), width=10).grid(row=0, column=1)
    Button(popup, text="Point won", command=lambda:PointWon(matchID,"Push"), width=10).grid(row=1, column=1)
    Button(popup, text="Point won", command=lambda:PointWon(matchID,"Flick"), width=10).grid(row=2, column=1)
    Button(popup, text="Point won", command=lambda:PointWon(matchID,"Normal topspin"), width=10).grid(row=3, column=1)
    Button(popup, text="Point won", command=lambda:PointWon(matchID,"Smash"), width=10).grid(row=4, column=1)
    Button(popup, text="Point won", command=lambda:PointWon(matchID,"Topspin against backspin"), width=10).grid(row=5, column=1)
    Button(popup, text="Point won", command=lambda:PointWon(matchID,"Counter topspin"), width=10).grid(row=6, column=1)
    Button(popup, text="Point won", command=lambda:PointWon(matchID,"Block"), width=10).grid(row=7, column=1)
    Button(popup, text="Point won", command=lambda:PointWon(matchID,"Left handed"), width=10).grid(row=8, column=1)

    Button(popup, text="Point lost", command=lambda:PointLost(matchID,"Serve"), width=10).grid(row=0, column=2)
    Button(popup, text="Point lost", command=lambda:PointLost(matchID,"Push"), width=10).grid(row=1, column=2)
    Button(popup, text="Point lost", command=lambda:PointLost(matchID,"Flick"), width=10).grid(row=2, column=2)
    Button(popup, text="Point lost", command=lambda:PointLost(matchID,"Normal topspin"), width=10).grid(row=3, column=2)
    Button(popup, text="Point lost", command=lambda:PointLost(matchID,"Smash"), width=10).grid(row=4, column=2)
    Button(popup, text="Point lost", command=lambda:PointLost(matchID,"Topspin against backspin"), width=10).grid(row=5, column=2)
    Button(popup, text="Point lost", command=lambda:PointLost(matchID,"Counter topspin"), width=10).grid(row=6, column=2)
    Button(popup, text="Point lost", command=lambda:PointLost(matchID,"Block"), width=10).grid(row=7, column=2)
    Button(popup, text="Point lost", command=lambda:PointLost(matchID,"Left handed"), width=10).grid(row=8, column=2)

    Button(popup, text="Back", command=popup.destroy, width=10).grid(row=9, column=1)
    #Button(popup, text="Finished", command=insert_graph, width=10).grid(row=10, column=1)




def match_details():
    with sqlite3.connect("TableTennis.db") as db:
        cursor = db.cursor()
        sql = """create table MatchDetails
                 (MatchID integer,
                 FirstName text,
                 Surname text,
                 TournamentName text,
                 Date text,
                 Time text,
                 primary key(MatchID))"""
        cursor.execute(sql)
        db.commit()
    

def shot_details():
    with sqlite3.connect("TableTennis.db") as db:
        cursor = db.cursor()
        sql = """create table Shots
                 (MatchID integer,
                 ShotID integer,
                 ShotName text,
                 PointsWon integer,
                 PointsLost integer,
                 primary key(ShotID)
                 foreign key(MatchID) references MatchDetails(MatchID))"""
        cursor.execute(sql)
        db.commit()






window = Tk()
#Button(window, text="Create a new match details table", command=match_details, width=30).grid(row=1, column=0, sticky=W, pady=4)
#Button(window, text="Create a new shot details table", command=shot_details, width=30).grid(row=1, column=1, sticky=W, pady=4)
Button(window, text="Add a new match", command=insert_match_details, width=30).grid(row=0, column=0, sticky=W, pady=4)
Button(window, text="Exit", command=quit, width=30).grid(row=1, column=0, sticky=W, pady=4)
window.mainloop()


