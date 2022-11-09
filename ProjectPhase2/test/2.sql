--Find number of players that have at least 3 CSEatures from NA region
SELECT COUNT(p_saveid)
FROM (
    SELECT p_saveid
    FROM player, CSEatures, inventory
    WHERE p_region = "NA"
        AND p_saveid = i_saveid
    GROUP BY p_saveid
    HAVING COUNT(i_ownedids >= 3)
) AS result