from database.DB_connect import DBConnect
from model.countries import Country
from model.confini import Confine

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select * from country c order by c.StateAbb """
        cursor.execute(query, ())
        for row in cursor:
            result.append(Country(row['CCode'], row['StateAbb'], row['StateNme']))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCountriesAnno(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct (c.StateAbb), c.CCode ,StateNme from country c , contiguity c2 where  c2.year<=%s and c.CCode = c2.state1no  order by c.StateAbb """
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Country(row['CCode'], row['StateAbb'], row['StateNme']))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct(dyad),state1no , state2no  from contiguity c where c.conttype = '1' """
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Confine(row['dyad'], row['state1no'], row['state2no']))
        cursor.close()
        conn.close()
        return result
