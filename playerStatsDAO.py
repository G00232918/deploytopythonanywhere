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
        #values = (ID,Full_Name, Total_Prize_Money)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    


    # function to map column names to their values in a row
    def convertToDictionary(self, result):
        colnames=['ID', 'Full_Name', 'Total_Prize_Money']
        # iterating through rows creaing keyvalue pair
        playerStat = {colname: result[idx] for idx, colname in enumerate(colnames)}
        return playerStat
    
    
playerStatsDAO = PlayerStatsDAO()

# Reference
# Lecture Notes