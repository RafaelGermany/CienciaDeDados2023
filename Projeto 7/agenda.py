import sqlite3 as sql
from sqlite3 import Cursor

#Requisito RS2 - inserção de dados
def inserir (registro: list) -> sql.Cursor:
    conn = sql.connect("Agenda.db")
    conn.cursor()
    conn.execute("""
    INSERT INTO Contatos values registro;""")