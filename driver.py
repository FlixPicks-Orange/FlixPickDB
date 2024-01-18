import Database as db
import sqlite3 as sql
from faker import Faker
import random
from datetime import datetime, timedelta
dbname = "FlixPicksV1.db"
fake = Faker()
db.makeTables(dbname)
db.insert_genre(dbname, "Action")
db.showAll(dbname)

  