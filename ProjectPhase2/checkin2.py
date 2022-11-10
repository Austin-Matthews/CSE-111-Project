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

    print("Adding sample data to cseatures_master...")
    try:
        cursor.execute('''
            INSERT INTO cseatures_master (cm_id, cm_name, cm_rarity, cm_value, cm_rate)
            VALUES
            ('01', 'Angelo Kyrilov', 'Common', '10', '0.17'),
            ('02', 'Santosh Chandrasekhar', 'Common', '10', '0.17'),
            ('03', 'Pengfei Su', 'Common', '10', '0.17'),
            ('04', 'Shawn Newsam', 'Common', '10', '0.17'),
            ('05', 'Florin Rusu', 'Common', '10', '0.17'),
            ('06', 'Judge Kyrilov', 'Rare', '350', '0.022'),
            ('07', 'Santosh Claus', 'Rare', '350', '0.022'),
            ('08', 'Pengfei Soup', 'Rare', '350', '0.022'),
            ('09', 'Shawn Oldsam', 'Rare', '350', '0.022'),
            ('10', 'Floral Rusu', 'Rare', '350', '0.022'),
            ('11', 'Angelo, The Last', 'Legendary', '20000', '0.004'),
            ('12', 'Punished Venom Santosh', 'Legendary', '20000', '0.008'),
            ('13', 'Pengflame Su', 'Legendary', '20000', '0.008'),
            ('14', 'Shawrannosaurus Rex', 'Legendary', '20000', '0.008'),
            ('15', 'R.U.S.U 9000', 'Legendary', '20000', '0.008')
            ''')
        print("Done!")
    except Error as error:
        print(error)
    print("----")

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
            ('10', '01'),
            ('10', '02'),
            ('10', '11'),
            ('11', ''),
            ('20', '04'),
            ('20', '07'),
            ('20', '03'),
            ('30', '03'),
            ('30', '11'),
            ('40', '08'),
            ('50', '01')
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
            ('10', '01'),
            ('10', '02'),
            ('11', ''),
            ('20', '07'),
            ('30', '03'),
            ('30', '11'),
            ('40', ''),
            ('50', '01')
            ''')
        print("Done!")
    except Error as error:
        print(error)
    print("++++++++++++++++++++++++++++++++++")

####################################################################
####################################################################

def SQL1(_conn):
    print("SQL1:")
    curr = _conn.cursor()
    curr.execute("""
            SELECT p_name, COUNT(i_ownedIDs) 
            FROM player, inventory 
            WHERE p_saveID == i_saveID
            GROUP BY p_name""")
    sql1 = curr.fetchall()
    for row in sql1:
        print("----")
        print("Username:", row[0])
        print("# of owned CSEatures:", row[1])
    print("++++++++++++++++++++++++++++++++++")

def SQL2(_conn):
    print("SQL2:")
    curr = _conn.cursor()
    curr.execute("""
        SELECT COUNT(p_saveID)
        FROM player
        WHERE p_saveID in (
            SELECT p_saveID
            FROM player, inventory
            WHERE p_region = "NA"
            AND p_saveID = i_saveID
        GROUP BY p_saveID
        HAVING COUNT(*) >= 3)
        """)
    sql2 = curr.fetchall()
    for row in sql2:
        print("Number of players with more than 2 CSEatures:", row[0])
    print("++++++++++++++++++++++++++++++++++")

def SQL3(_conn):
    print("SQL3:")
    curr = _conn.cursor()
    curr.execute('''SELECT p_name
        FROM player, inventory, cseatures_master
        WHERE p_saveID = i_saveID
            AND i_ownedIDs = cm_id
            AND cm_value = (
        SELECT MAX(cm_value)
        FROM cseatures_master
        )''')
    sql3 = curr.fetchall()
    print("(This query uses the tables player, inventory, and cseatures_master)")
    for row in sql3:
        print("This player owns a legendary CSEature:", row[0])
    print("++++++++++++++++++++++++++++++++++")

def SQL4(_conn):
    print("SQL4:")
    curr = _conn.cursor()
    curr.execute('''SELECT COUNT(p_saveID)
        FROM player
        WHERE p_saveID in (
            SELECT p_saveID
            FROM player, inventory, cseatures_master
            WHERE p_saveID = i_saveID
                AND i_ownedIDs = cm_id
                AND p_region = "AF"
            GROUP BY i_saveID
            HAVING COUNT(i_ownedIDs < 2))''')
    sql4 = curr.fetchall()
    for row in sql4:
        print("Number of players in Africa with less than 2 CSEatures:", row[0])
    print("++++++++++++++++++++++++++++++++++")

def SQL5(_conn):
    print("SQL5:")
    curr = _conn.cursor()
    curr.execute('''SELECT p_name
        FROM player
        WHERE p_catdollars = (
            SELECT MAX(p_catdollars)
            FROM player)''')
    sql5 = curr.fetchall()
    for row in sql5:
        print("The player with the most CatDollars is:", row[0])
    print("++++++++++++++++++++++++++++++++++")

def SQL6(_conn):
    print("SQL6:")
    curr = _conn.cursor()
    curr.execute('''SELECT p_name
        FROM player
        WHERE p_catdollars = (
            SELECT MIN(p_catdollars)
            FROM player)''')
    sql6 = curr.fetchall()
    for row in sql6:
        print("The player with the least CatDollars is:", row[0])

    print("++++++++++++++++++++++++++++++++++")

def SQL7(_conn):
    print("SQL7:")
    curr = _conn.cursor()
    curr.execute('''
        SELECT COUNT(DISTINCT p_saveID)
        FROM player
        WHERE p_region != "NA"
            AND p_region != "AF"''')
    sql7 = curr.fetchall()
    for row in sql7:
        print("Amount of players from neither North America nor Africa:", row[0])
    print("++++++++++++++++++++++++++++++++++")

def SQL8(_conn):
    print("SQL8:")
    curr = _conn.cursor()
    curr.execute('''SELECT p_name, p_region
        FROM player, inventory
        WHERE p_saveID = i_saveID
            AND i_ownedIDs = ''
            AND p_catdollars <= 10
        GROUP BY p_name''')
    sql8 = curr.fetchall()
    for row in sql8:
        print("Name and Region of players with no catdollars and no cseatures:", row[0], "|", row[1])
    
    print("++++++++++++++++++++++++++++++++++")

def SQL9(_conn):
    print("SQL9:")
    curr = _conn.cursor()
    curr.execute('''SELECT p_name, p_region
        FROM player, inventory, cseatures_master
        WHERE p_saveID = i_saveID
            AND i_ownedIDs = cm_id
        GROUP BY p_region
        ORDER BY p_region, MAX(cm_value)''')
    sql9 = curr.fetchall()
    print("These players own the highest value CSEature in their region:")
    for row in sql9:
        print(row[0], "from", row[1])
    print("++++++++++++++++++++++++++++++++++")

def SQL10(_conn):
    print("SQL10:")
    curr = _conn.cursor()
    curr.execute('''SELECT (p_name)
        FROM player
        WHERE p_region = "NA"''')
    sql10 = curr.fetchall()
    print("All North American players: ")
    for row in sql10:
        print(row[0])
    print("++++++++++++++++++++++++++++++++++")

def SQL11(_conn):
    print("SQL11:")
    curr = _conn.cursor()
    curr.execute('''SELECT cm_name
        FROM cseatures_master
        WHERE cm_rarity = "Legendary"
        GROUP BY cm_name''')
    sql11 = curr.fetchall()
    print("The legendary CSEatures are:")
    for row in sql11:
        print(row[0])
    print("++++++++++++++++++++++++++++++++++")

def SQL12(_conn):
    print("SQL12:")
    curr = _conn.cursor()
    curr.execute('''SELECT p_name
        FROM player, inventory, cseatures_master
        WHERE p_saveID = i_saveID
            AND i_ownedIDs = cm_id
        GROUP BY p_name HAVING (cm_value=10)''')
    sql12 = curr.fetchall()
    print("Players with a common CSEature:")
    for row in sql12:
        print(row[0])
    print("++++++++++++++++++++++++++++++++++")

def SQL13(_conn):
    print("SQL13:")
    print("Swapping the region of gamerboy's alt to EU...")
    curr = _conn.cursor()
    curr.execute('''UPDATE player
        SET p_region = 'EU'
        WHERE p_saveID = "11"''')
    print("Regionswapped gamerboy's alt to EU")
    print("++++++++++++++++++++++++++++++++++")

def SQL14(_conn):
    print("SQL14:")
    print("Changing ucmITofficial's password...")
    curr = _conn.cursor()
    curr.execute('''UPDATE login
        SET l_password = 'amuchsaferpassword'
        WHERE l_name = "ucmITofficial"''')
    print("Changed ucmITofficial's password to a much safer password")

    print("++++++++++++++++++++++++++++++++++")

def SQL15(_conn):
    print("SQL15:")
    curr = _conn.cursor()
    curr.execute('''SELECT p_name, cm_name
        FROM player, inventory, favorites, cseatures_master
        WHERE p_saveID = i_saveID
            AND i_saveID = f_saveID
            AND i_ownedIDs = f_favoriteIDs
            AND f_favoriteIDs = cm_id
            AND cm_value = (
                SELECT MAX(cm_value) FROM cseatures_master
            )
        GROUP BY p_name''')
    sql15 = curr.fetchall()
    for row in sql15:
        print("The player with the highest value *favorite* CSEature:", row[0])
        print(row[0],"'s favorite CSEature is:", row[1])
    print("++++++++++++++++++++++++++++++++++")

def SQL16(_conn):
    print("SQL16:")
    curr = _conn.cursor()
    curr.execute('''INSERT INTO cseatures_master (cm_id, cm_name, cm_rarity, cm_value, cm_rate)
        VALUES ('16', 'God-King Lord-Emperor Su', 'Legendary', '100000000', "0.001")''')
    print("Added new high value CSEature, 'God-King Lord-Emperor Su'! Go out and find him now!")
    print("++++++++++++++++++++++++++++++++++")

def SQL17(_conn):
    print("SQL17:")
    curr = _conn.cursor()
    curr.execute('''DELETE FROM favorites
        WHERE f_saveID = '10'
        AND f_favoriteIDs = "01"''')
    print("Removed CSEature of ID 01 from Player 1's 0'th save file.")
    print("++++++++++++++++++++++++++++++++++")

def SQL18(_conn):
    print("SQL18:")
    curr = _conn.cursor()
    curr.execute('''SELECT l_name, l_password
        FROM login''')
    print("All users' login information:")
    sql18 = curr.fetchall()
    for row in sql18:
        print("Username:", row[0], "and Password:", row[1])
    print("++++++++++++++++++++++++++++++++++")

def SQL19(_conn):
    print("SQL19:")
    curr = _conn.cursor()
    curr.execute('''SELECT cm_name, cm_rarity
        FROM cseatures_master''')
    print("All CSEatures and their rarity:")
    sql19 = curr.fetchall()
    for row in sql19:
        print("----")
        print("CSEature:", row[0])
        print("Rarity:", row[1])
    print("++++++++++++++++++++++++++++++++++")

def SQL20(_conn):
    print("SQL20:")
    curr = _conn.cursor()
    curr.execute('''SELECT cm_name
        FROM cseatures_master
        WHERE length(cm_name) = (
            SELECT min(length(cm_name))
            FROM cseatures_master
        )''')
    sql20 = curr.fetchall()
    for row in sql20:
        print("The CSEature with the shortest name is:", row[0])
    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"cseatures.sqlite"
    # create a database connection
    conn = openConnection(database)
    with conn:
        deleteContent(conn)
        addContent(conn)

        SQL1(conn)
        SQL2(conn)
        SQL3(conn)
        SQL4(conn)
        SQL5(conn)
        SQL6(conn)
        SQL7(conn)
        SQL8(conn)
        SQL9(conn)
        SQL10(conn)
        SQL11(conn)
        SQL12(conn)
        SQL13(conn)
        SQL14(conn)
        SQL15(conn)
        SQL16(conn)
        SQL17(conn)
        SQL18(conn)
        SQL19(conn)
        SQL20(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
