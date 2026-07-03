# API Concept Explained in Detail

## What is an API?

**API (Application Programming Interface)** is a set of rules and protocols that allows two software applications to communicate with each other.

Think of an API as a **messenger** that takes requests from one application, sends them to another application, and returns the response.

### Real-Life Example: Restaurant

Imagine you visit a restaurant.

* **You (Client)** → Customer who wants food.
* **Waiter (API)** → Takes your order to the kitchen.
* **Kitchen (Server)** → Prepares the food.
* **Food** → Response sent back to you.

```
Customer
    │
    ▼
 Waiter (API)
    │
    ▼
 Kitchen (Server)
    │
    ▼
 Waiter
    │
    ▼
 Customer receives food
```

The customer never enters the kitchen. Similarly, applications don't directly access databases—they communicate through APIs.

---

# Why Do We Need APIs?

Without APIs:

* Every application would need direct database access.
* Security risks increase.
* Different applications become tightly coupled.
* Updating one system affects others.

With APIs:

* Secure communication.
* Easy integration.
* Faster development.
* Reusable functionality.
* Platform independence.

---

# Example from Daily Life

### Weather App

When you open a weather app:

```
Weather App
      │
      ▼
Weather API
      │
      ▼
Weather Database
      │
      ▼
Temperature Data
```

The app doesn't store weather information.

Instead, it asks the Weather API:

```
"What is today's weather in Hyderabad?"
```

The API replies:

```json
{
  "city":"Hyderabad",
  "temperature":"34°C",
  "condition":"Sunny"
}
```

---

# API in Web Development

Suppose you built an E-commerce website.

The frontend needs:

* Products
* User profile
* Orders
* Cart

Instead of accessing MySQL directly,

```
Frontend
     │
     ▼
Backend API
     │
     ▼
Database
```

The API acts as the middle layer.

---

# Components of an API

## 1. Client

The application making the request.

Examples:

* Website
* Mobile App
* React Application
* Flutter App

Example:

```
Amazon Mobile App
```

---

## 2. Server

Processes requests and sends responses.

Example:

```
Amazon Backend Server
```

---

## 3. Request

A message sent by the client.

Example:

```
Give me all products.
```

---

## 4. Response

Data returned by the server.

Example:

```json
[
   {
      "id":1,
      "name":"Laptop",
      "price":50000
   }
]
```

---

# API Request Flow

```
User clicks Login

       │

React Frontend

       │

HTTP Request

       │

Django API

       │

Checks Database

       │

Returns Result

       │

Frontend Displays Message
```

---

# Types of APIs

## 1. REST API (Most Popular)

Uses HTTP methods.

Example:

```
GET /products
```

Returns all products.

---

## 2. SOAP API

Older technology.

Uses XML.

Mostly used in:

* Banking
* Government
* Enterprise systems

---

## 3. GraphQL API

Instead of multiple endpoints,

Client asks exactly what data it needs.

Example:

```
Get only:

Product Name
Price
```

Instead of entire product details.

---

## 4. WebSocket API

Used for real-time communication.

Examples:

* WhatsApp
* Chat applications
* Live cricket scores
* Stock market updates

---

# HTTP Methods

These define the type of operation the client wants to perform.

---

## GET

Used to retrieve data.

Example:

```
GET /students
```

Returns:

```json
[
 {
   "id":1,
   "name":"John"
 }
]
```

---

## POST

Creates new data.

Example:

```
POST /students
```

Body:

```json
{
 "name":"Guru"
}
```

Response:

```
Student Created
```

---

## PUT

Updates the complete object.

Example:

```
PUT /students/5
```

---

## PATCH

Updates only selected fields.

Example:

```
PATCH /students/5
```

Only update:

```
Phone Number
```

---

## DELETE

Deletes data.

Example:

```
DELETE /students/5
```

---

# HTTP Status Codes

These tell the client whether the request was successful.

## 200

Success

```
OK
```

---

## 201

Created Successfully

```
Student Added
```

---

## 400

Bad Request

Client sent incorrect data.

---

## 401

Unauthorized

Login required.

---

## 403

Forbidden

Permission denied.

---

## 404

Not Found

Requested resource doesn't exist.

---

## 500

Internal Server Error

Problem on the server.

---

# API Endpoint

An endpoint is a URL where the API can be accessed.

Example:

```
https://example.com/api/products
```

Here:

```
products
```

is the endpoint.

Examples:

```
GET /products

POST /products

GET /orders

DELETE /users/5
```

---

# Request Structure

A request consists of:

```
URL

Method

Headers

Body
```

Example:

```
POST

/api/login
```

Headers:

```
Content-Type: application/json
```

Body:

```json
{
 "email":"abc@gmail.com",
 "password":"123456"
}
```

---

# Response Structure

Example:

```json
{
   "status":"success",
   "message":"Login Successful",
   "token":"eyJhbGc..."
}
```

---

# What is JSON?

**JSON (JavaScript Object Notation)** is the standard format for exchanging data between applications.

Example:

```json
{
   "name":"Guru",
   "age":22,
   "city":"Vijayawada"
}
```

JSON is:

* Lightweight
* Human-readable
* Language-independent
* Easy for machines to parse

---

# Authentication in APIs

Authentication verifies the identity of the user.

Common methods include:

### API Key

A unique key provided with each request.

### Token Authentication

After login, the server returns a token.

```
Client Login

↓

Server verifies

↓

Returns Token

↓

Client sends Token in every request

↓

Server validates Token

↓

Access Granted
```

### JWT (JSON Web Token)

A popular token format containing encoded user information and an expiration time.

---

# CRUD Operations and HTTP Methods

| CRUD Operation | HTTP Method | Example           |
| -------------- | ----------- | ----------------- |
| Create         | POST        | Add a new student |
| Read           | GET         | View students     |
| Update         | PUT/PATCH   | Edit student      |
| Delete         | DELETE      | Remove student    |

---

# API Example Using Django

Imagine a student management system.

### API Endpoint

```
GET /api/students/
```

Response:

```json
[
 {
   "id":1,
   "name":"Guru",
   "course":"CSE"
 },
 {
   "id":2,
   "name":"Rahul",
   "course":"ECE"
 }
]
```

### Create Student

```
POST /api/students/
```

Request:

```json
{
 "name":"Anjali",
 "course":"IT"
}
```

Response:

```json
{
 "id":3,
 "name":"Anjali",
 "course":"IT"
}
```

---

# Complete API Flow

```
User clicks Login
        │
        ▼
Frontend (React/HTML)
        │
        ▼
HTTP POST Request
        │
        ▼
Django REST API
        │
        ▼
Authentication
        │
        ▼
Database (MySQL/PostgreSQL)
        │
        ▼
Data Retrieved
        │
        ▼
JSON Response
        │
        ▼
Frontend Updates UI
```

---

# Advantages of APIs

* Enables communication between different software systems.
* Separates the frontend and backend, making development easier.
* Promotes code reuse and modular design.
* Enhances security by restricting direct database access.
* Simplifies integration with third-party services (payment gateways, maps, email, etc.).
* Supports multiple client applications (web, mobile, desktop) using the same backend.
* Makes applications easier to maintain and scale.

---

# Real-World API Examples

| Application        | API Purpose                                |
| ------------------ | ------------------------------------------ |
| Payment Apps       | Process online payments securely           |
| Google Maps        | Display maps, routes, and locations        |
| Weather Apps       | Retrieve live weather data                 |
| WhatsApp           | Send and receive messages in real time     |
| Food Delivery Apps | Fetch restaurants, menus, and order status |
| E-commerce Sites   | Manage products, users, carts, and orders  |

---

# Key Takeaways

* An **API** is a bridge that enables communication between different software applications.
* **Clients** send requests, and **servers** process them and return responses.
* **REST APIs** commonly use **HTTP methods** like GET, POST, PUT, PATCH, and DELETE.
* Data is typically exchanged in **JSON** format.
* APIs improve **security, scalability, maintainability, and interoperability**, making them essential for modern web and mobile applications.
