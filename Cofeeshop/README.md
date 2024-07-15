# CoffeeShop Web Application

![CoffeeShop Main Page](chrome_B2DvHh4xGZ.png)

Welcome to the CoffeeShop web application! This project is a full-stack web application designed to manage and streamline operations for a coffee shop. The application includes features for managing products, orders, customers, and staff.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- *Product Management:* Add, update, and delete coffee products.
- *Order Management:* Create and manage customer orders.
- *Customer Management:* Maintain a customer database.
- *Staff Management:* Manage staff information and roles.
- *User Authentication:* Secure login and registration for customers and staff.
- *Responsive Design:* Accessible on both desktop and mobile devices.

## Technologies Used

- *Frontend:*
  - Django Templates
  - CSS
  - JavaScript
- *Backend:*
  - Django (MVC framework)
  - MySQL

## Installation

To run this application locally, follow these steps:

1. *Clone the repository:*
   ```bash
   git clone https://github.com/LiorLi1/Fullstack-Projects.git
   cd Fullstack-Projects/Cofeeshop
   ```
   
2. *Install backend dependencies:*
	```bash
	cd Fullstack-Projects/Cofeeshop
	pip install -r requirements.txt
	```

4. *Run database migration:*
	```bash
	cd Fullstack-Projects/Cofeeshop
	python manage.py migrate
	```
	
5. *Run the server:*
	```bash
	python manage.py runserver
	```
	
## Usage
1. *Access the application:*
	Open your web browser and navigate to `http://localhost:8000`.

2. *Register/Login:*
	Register a new account or login with an existing one.

3. *Manage products and orders:*
	Use the navigation menu to access the product and order management sections.

4. *Admin functionalities:*
	Admin users can manage customers and staff through the admin panel.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.

2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
   
3. Make your changes and commit them:
	```bash
	git commit -m 'Add some feature'
	```
	
4. Push to the branch:
	```bash
	git push origin feature-branch
	```
	
5. Create a pull request.

	