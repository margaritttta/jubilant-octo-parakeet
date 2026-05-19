-- 1. Выведите количество записей в таблице prices для каждого товара
SELECT product_id, COUNT(*) AS total_prices 
FROM prices 
GROUP BY product_id;

-- 2. Выведите среднюю цену товаров для каждого product_id
SELECT product_id, AVG(price) AS avg_price 
FROM prices 
GROUP BY product_id;

-- 3. Выведите минимальную цену для каждого товара
SELECT product_id, MIN(price) AS min_price 
FROM prices 
GROUP BY product_id;

-- 4. Выведите максимальную цену для каждого товара
SELECT product_id, MAX(price) AS max_price 
FROM prices 
GROUP BY product_id;