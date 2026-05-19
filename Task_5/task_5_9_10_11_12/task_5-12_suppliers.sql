-- 1. Выведите количество поставщиков для каждого товара из таблицы suppliers
SELECT product_id, COUNT(*) AS supplier_count 
FROM suppliers 
GROUP BY product_id;