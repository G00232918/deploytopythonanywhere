import mysql.connector
import dbconfig as cfg

class PlayerStatsDAO:

    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    def getCursor(self): 
        # Using the existing database connection details
        self.connection = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    # get cumulative prize for each player based on 3 years
    def find_cumulative_prize_by_year(self):
        cursor = self.db.cursor()

        # SQL query to join both tables to get total prize money
        sql = """
            SELECT p.ID, p.Full_Name, p.Age, p.Nationality,
                   SUM(ps.Prize_Money) AS Total_Prize_Money
            FROM players p
            JOIN playerstats ps ON p.Full_Name = ps.Full_Name
            group by p.ID, p.Full_Name, p.Age, p.Nationality
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    
    
playerStatsDAO = PlayerStatsDAO()

# Reference
# Lecture Notes