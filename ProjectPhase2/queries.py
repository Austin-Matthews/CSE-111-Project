import sqlite3
from sqlite3 import Error

def openConnection(_dbFile):
    print("Open database: ", _dbFile)
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("Done!")
    except Error as error:
        print(error)
    print("++++++++++++++++++++++++++++++++++")
    return conn

####################################################################
####################################################################

def closeConnection(_conn, _dbFile):
    print("Close database: ", _dbFile)
    try:
        _conn.close()
        print("Done!")
    except Error as error:
        print(error)
    print("++++++++++++++++++++++++++++++++++")

####################################################################
####################################################################

def deleteContent(_conn):
    cursor = _conn.cursor()

    print("Deleting content from cseatures_master...")
    try:
        cursor.execute(f'''DELETE FROM cseatures_master''')
        print("Done!")
    except Error as error:
        print(error)

    print("----")

    print("Deleting content from data...")
    try:
        cursor.execute(f'''DELETE FROM data''')
        print("Done!")
    except Error as error:
        print(error)

    print("----")
    
    print("Deleting content from favorites...")
    try:
        cursor.execute(f'''DELETE FROM favorites''')
        print("Done!")
    except Error as error:
        print(error)

    print("----")

    print("Deleting content from inventory...")
    try:
        cursor.execute(f'''DELETE FROM inventory''')
        print("Done!")
    except Error as error:
        print(error)
    
    print("----")

    print("Deleting content from login...")
    try:
        cursor.execute(f'''DELETE FROM login''')
        print("Done!")
    except Error as error:
        print(error)

    print("----")

    print("Deleting content from player...")
    try:
        cursor.execute(f'''DELETE FROM player''')
        print("Done!")
    except Error as error:
        print(error)
    print("++++++++++++++++++++++++++++++++++")

####################################################################
####################################################################

def addContent(_conn):
    cursor = _conn.cursor()
    
    print("Adding sample data to login...")
    try:
        cursor.execute('''
            INSERT INTO login (l_id, l_name, l_password)
            VALUES
            ('1', 'gamerboy', 'password1'),
            ('2', 'gamergirl', 'qwertyuiop'),
            ('3', 'gamerdad', 'christiandadrock12'),
            ('4', 'angelokyrilov1', 'd3m0cr4cY2323'),
            ('5', 'ucmITofficial', 'rufusluvr90210')
            ''')
        print("Done!")
    except Error as error:
        print(error)
    print("----")

    print("Adding sample data to data...")
    try:
        cursor.execute('''
            INSERT INTO data (d_id, d_saveID)
            VALUES
            ('1', '10'),
            ('1', '11'),
            ('2', '20'),
            ('3', '30'),
            ('4', '40'),
            ('5', '50')
            ''')
        print("Done!")
    except Error as error:
        print(error)
    print("----")

    print("Adding sample data to player...")
    try:
        cursor.execute('''
            INSERT INTO player (p_saveID, p_catdollars, p_name, p_region)
            VALUES
            ('10', '10100', 'gamerboy4ever', 'NA'),
            ('11', '0', 'GamerBoyAltHero', 'NA'),
            ('20', '250', 'StarKiller1337', 'NA'),
            ('30', '10', 'TeaTimeGTG', 'EU'),
            ('40', '25', 'GoogleDotCom', 'AF'),
            ('50', '999999999999', 'ucmITofficial', 'NA')
            ''')
        print("Done!")
    except Error as error:
        print(error)
    print("----")

    print("Adding sample data to inventory...")
    try:
        cursor.execute('''
            INSERT INTO inventory (i_saveID, i_ownedIDs)
            VALUES
            ('10', '015|021|033|043|051|061|081|092|101|124|132|141|152'),
            ('11', ''),
            ('20', '041|072|101|151'),
            ('30', '031|111|121'),
            ('40', '081'),
            ('50', '015|025|035|045|055|065|075|085|095|105|115|125|135|145|155')
            ''')
        print("Done!")
    except Error as error:
        print(error)
    print("----")

    print("Adding sample data to favorites...")
    try:
        cursor.execute('''
            INSERT INTO favorites (f_saveID, f_favoriteIDs)
            VALUES
            ('10', '015|124'),
            ('11', ''),
            ('20', '072'),
            ('30', '031|111|121'),
            ('40', ''),
            ('50', '015|025|035')
            ''')
        print("Done!")
    except Error as error:
        print(error)
    print("++++++++++++++++++++++++++++++++++")

def Q1(_conn):
    print("Q1")
    curr = _conn.cursor()
    curr.execute("""
        SELECT p_name, COUNT(i_ownedid) 
        FROM player, inventory 
        WHERE p_saveid == i_saveid 
        GROUP BY p_name""")
    
    q1 = curr.fetchall()
    print(q1)        

    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("Q2")
    curr = _conn.cursor()
    curr.execute("""
        SELECT COUNT(p_saveID)
        FROM (
            SELECT p_saveID
            FROM player, CSEatures, inventory
            WHERE p_region = "NA"
            AND p_saveID = i_saveID
        GROUP BY p_saveID
        HAVING COUNT(i_ownedIDs >= 3))
        AS result""")
    
    q1 = curr.fetchall()
    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("Q3")

    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("Q4")

    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("Q5")

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"cseatures.sqlite"
    # create a database connection
    conn = openConnection(database)
    with conn:
        deleteContent(conn)
        addContent(conn)

        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()