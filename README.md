# Starter code for login system

## main.py 
This file will run server, communicate with browser and DB (sqlite)

This code will create an instance of the db and create a users table when the app runs
```
if __name__ == '__main__':
    db = database.Database()
    db.create_user_tbl()

    app.run(debug=True)
```

## database.py 

This file will handle CRUD commands.
 - Create users table
 - Update users table with data sent from Register page
 - Read data from users table when user trying to login
