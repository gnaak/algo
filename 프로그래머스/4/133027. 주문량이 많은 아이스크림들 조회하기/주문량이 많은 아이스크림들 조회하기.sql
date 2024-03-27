SELECT FLAVOR
FROM (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS total_orders
    FROM (
        SELECT FLAVOR, TOTAL_ORDER
        FROM FIRST_HALF
        UNION ALL
        SELECT FLAVOR, TOTAL_ORDER
        FROM JULY
    ) AS combined_orders
    GROUP BY FLAVOR
    ORDER BY total_orders DESC
    LIMIT 3
) AS top_flavors;
