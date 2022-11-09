--Number of CSEatures from every Player
SELECT p_name, COUNT(i_ownedid)
FROM player, inventory
WHERE
    p_saveid == i_saveid
GROUP BY p_name