-- Kiem tra co so du lieu co hay chua
DROP DATABASE IF EXISTS online_shop;

-- Tao database online_shop
CREATE DATABASE online_shop;

-- Su dung online_shop
USE online_shop;

-- Tao bang Catelogy
CREATE TABLE Catalog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    status BOOLEAN
);

-- Tao bang Product
CREATE TABLE Product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    status BOOLEAN,
    price FLOAT,
    sale_price FLOAT,
    created_date DATE,
    catalog_id INT,
    FOREIGN KEY (catalog_id) REFERENCES Catalog(id)
);

-- Tạo bảng Customer
CREATE TABLE Customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone VARCHAR(50) NOT NULL,
    address VARCHAR(255),
    create_date DATE,
    gender BOOLEAN,
    birthday DATE
);

-- Tao bang Orders
CREATE TABLE Orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    status BOOLEAN,
    order_date DATETIME,
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

-- Tao bang Order_Detail
CREATE TABLE Order_Detail (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price FLOAT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (product_id) REFERENCES Product(id)
);
-- them du lieu vao cac bang
-- Chen du lieu vao bang Category
INSERT INTO Catalog (name, status) VALUES
('Electronics', TRUE),
('Books', TRUE),
('Clothing', TRUE),
('Home & Kitchen', TRUE),
('Sports & Outdoors', TRUE);

-- Chen du lieu vao bang Product
INSERT INTO Product (name, status, price, sale_price, created_date, catalog_id) VALUES
('Laptop', TRUE, 1000, 900, '2023-01-01', 1),
('Smartphone', TRUE, 700, 650, '2023-02-01', 1),
('Tablet', TRUE, 400, 350, '2023-03-01', 1),
('Headphones', TRUE, 100, 80, '2023-04-01', 1),
('Smartwatch', TRUE, 200, 180, '2023-05-01', 1),
('Novel', TRUE, 20, 15, '2023-06-01', 2),
('Biography', TRUE, 25, 20, '2023-07-01', 2),
('Textbook', TRUE, 50, 45, '2023-08-01', 2),
('T-shirt', TRUE, 15, 10, '2023-09-01', 3),
('Jeans', TRUE, 40, 35, '2023-10-01', 3),
('Jacket', TRUE, 60, 50, '2023-11-01', 3),
('Blender', TRUE, 80, 70, '2023-12-01', 4),
('Toaster', TRUE, 30, 25, '2024-01-01', 4),
('Tent', TRUE, 100, 90, '2024-02-01', 5),
('Sleeping Bag', TRUE, 50, 45, '2024-03-01', 5);

-- Chen du lieu vao bang Customer
INSERT INTO Customer (name, email, phone, address, create_date, gender, birthday) VALUES
('John Doe', 'john@example.com', '1234567890', '123 Main St', '2023-01-01', TRUE, '1990-01-01'),
('Jane Smith', 'jane@example.com', '0987654321', '456 Elm St', '2023-02-01', FALSE, '1992-02-02'),
('Alice Johnson', 'alice@example.com', '5678901234', '789 Oak St', '2023-03-01', FALSE, '1994-03-03');

-- Chen du lieu vao bang Orders
INSERT INTO Orders (customer_id, status, order_date) VALUES
(1, TRUE, '2024-04-01 10:00:00'),
(2, TRUE, '2024-04-02 11:00:00'),
(3, TRUE, '2024-04-03 12:00:00');

-- Chen du lieu vao bang Order_Detail
INSERT INTO Order_Detail (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 900),
(1, 2, 2, 650),
(2, 3, 1, 350),
(2, 4, 3, 80),
(3, 5, 1, 180),
(3, 6, 2, 15);
-- query
-- 1. Lấy ra danh sách sản phẩm có sắp xếp giảm dần theo Price 
-- gồm các cột sau: Id,Name, Price, SalePrice, Status, CategoryName, CreatedDate
select p.id, p.name,price,sale_price,p.status, c.name, created_date 
from product p inner join `catalog` c on p.catalog_id =c.id 
order by price desc 
-- 2. Lấy ra danh sách Category gồm: Id, Name, TotalProduct, Status
select c.id, c.name ,c.status , count(p.id) TotalProduct 
from `catalog` c inner join product p on c.id = p.catalog_id 
group by c.id, c.name ,c.status

-- 3. Truy vấn danh sách Customer gồm: Id, Name, Email, Phone, Address,
-- CreatedDate, Gender, BirthDay, Age (Age là cột suy ra từ BirthDay, Gender nếu = 0
-- là Nam, 1 là Nữ ) ( Age = năm hiện tại - năm sinh của BirthDay)
select c.id, c.name ,c.email ,c.phone ,c.address ,c.create_date ,
	 CASE 
           WHEN c.gender = 0 THEN 'Nam'
           ELSE 'Nữ'
       END AS gender, 
       year(current_date()) - year(c.birthday) as Age
from customer  c 

-- 4. Truy vấn xóa các sản phẩm chưa được bán
delete 
from product p
where p.id not in (select d.product_id  from order_detail d)
-- 5. Cập nhật Cột SalePrice tăng thêm 10% cho tất cả các sản phẩm có SalePrice <=
-- 250000,
update product 
set sale_price =sale_price*1.1
where sale_price<=25000 