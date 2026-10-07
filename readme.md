# Flask Blog — README

 ## 📌 Project Overview

 This is a simple **Blog Management System** built using:

 - **Python**
- **Flask**
- **MySQL**
- **XAMPP**
- **SQLAlchemy**
- **HTML**
- **CSS**

 The application allows users to **create, view, edit, and delete blog posts**.

---

 ## 🚀 Features

 - Create a new blog post
- View all blog posts
- Edit existing posts
- Delete posts
- Store data in MySQL
- SQLAlchemy ORM for database operations
- Responsive and simple HTML/CSS interface

---

 ## 🛠️ Technologies Used

 | Technology | Purpose |
| --- | --- |
| Python | Backend programming |
| Flask | Web framework |
| MySQL | Database |
| XAMPP | MySQL server |
| SQLAlchemy | Database ORM |
| PyMySQL | MySQL connection |
| HTML | Web page structure |
| CSS | Web page styling |

---

 ## 📁 Project Structure

```
flask_blog/
│
├── app.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   └── edit.html
│
└── static/
    └── style.css
```

---

 ## ⚙️ Requirements

 Make sure you have installed:

 - Python 3
- XAMPP
- MySQL
- pip

 Install the Python packages:

```
pip install flask flask-sqlalchemy pymysql
```

---

 ## 🗄️ Database Setup

 ### 1\. Start XAMPP

 Open XAMPP Control Panel and start:

```
MySQL
```

 ### 2\. Open phpMyAdmin

 Go to:

```
http://localhost/phpmyadmin
```

 ### 3\. Create the database

 Run:

```
CREATE DATABASE flask_blog;

USE flask_blog;
```

 ### 4\. Create the table

```
CREATE TABLE post (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

 ## 🔗 MySQL Configuration

 The project uses the default XAMPP MySQL configuration:

```
Host: localhost
Port: 3306
Username: root
Password: empty
Database: flask_blog
```

 The connection in `app.py` is:

```
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:@localhost:3306/flask_blog"
)
```

 If your MySQL `root` user has a password, change the connection accordingly.

 For example:

```
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/flask_blog"
)
```

---

 ## ▶️ How to Run

 ### Step 1 — Start MySQL

 Open XAMPP and start:

```
MySQL
```

 ### Step 2 — Open the project

 Go to the project directory:

```
cd flask_blog
```

 ### Step 3 — Run Flask

```
python app.py
```

 ### Step 4 — Open the website

 Open your browser and visit:

```
http://127.0.0.1:5000
```

---

 ## 🔄 CRUD Operations

 ### Create

 Create a new blog post using:

```
/create
```

 ### Read

 View all posts on:

```
/
```

 ### Update

 Edit a post using:

```
/edit/<id>
```

 Example:

```
/edit/1
```

 ### Delete

 Delete a post using:

```
/delete/<id>
```

---

 ## 🗃️ Database Structure

 The `post` table contains:

```
post
│
├── id          INT
├── title       VARCHAR(200)
├── content     TEXT
└── timestamp   DATETIME
```

---

 ## 🧪 Testing

 You can add test data directly through phpMyAdmin:

```
INSERT INTO post (title, content)
VALUES
(
    'My First Blog',
    'This is my first blog post using Flask and MySQL.'
),
(
    'Learning Flask',
    'I am learning Flask, SQLAlchemy, HTML and CSS.'
);
```

 Then refresh:

```
http://127.0.0.1:5000
```

 The posts should appear on the website.

---

 ## 🔐 Database Flow

```
HTML/CSS
   ↓
Flask
   ↓
SQLAlchemy
   ↓
PyMySQL
   ↓
XAMPP MySQL
   ↓
flask_blog
   ↓
post table
```

---

 ## 👨‍💻 Author

 **Flask Blog Project**

 Built using **Flask, MySQL, SQLAlchemy, HTML and CSS**.