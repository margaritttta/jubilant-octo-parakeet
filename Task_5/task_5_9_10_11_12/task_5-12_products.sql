-- 1. Выведите количество товаров в таблице products, сгруппировав результат по категориям
SELECT category, COUNT(*) AS product_count 
FROM products 
GROUP BY category;

-- 2. Выведите количество товаров в каждой категории, отсортировав по убыванию количества
SELECT category, COUNT(*) AS product_count 
FROM products 
GROUP BY category 
ORDER BY product_count DESC;