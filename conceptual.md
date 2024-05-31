### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
An open source relational database managment system. 

- What is the difference between SQL and PostgreSQL?
SQL is the human-readable language for querying and modifying data and PostgreSQL is the database management system.

- In `psql`, how do you connect to a database?
\c DATABASE_NAME

- What is the difference between `HAVING` and `WHERE`?
Having: decide which groups to keep
Where: filter which rows are included

- What is the difference between an `INNER` and `OUTER` join?
Inner: only rows that match the condition in both tables
Outer: all rows from both tables (Full outer join)

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
Left outer: all rows from left/first table combined with matching rows from right/second table
Right outer: all rows from right table combined with matching rows from left table

- What is an ORM? What do they do?
Object relational mapping, trnaslation between OOP in server language and relational data in database, take SQL language and use in python apps

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  HTTP requests like AJAX is client-side, can be faster and doesnt involve flask. Server-sode requests easier for server to store or process data and need a password to access the API.

- What is CSRF? What is the purpose of the CSRF token?
Cross-site request forgery, generated when server form is shown and verifies user requests. All forms have a hidden CSRF field and we validate token when form submits.

- What is the purpose of `form.hidden_tag()`?
Hide CSRF token for security.
