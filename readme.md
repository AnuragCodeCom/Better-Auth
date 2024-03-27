# **Better Auth** V1
### Made In Python By **[Anurag](https://anuragcode.com)**

> [!NOTE]
> Free to Use for Personal and Commercial Purposes

# About The Project:
A Simple Easy to Use Authentication Module Made In Python To Create, Verify and Store User Credentials in an Encrypted Form in SQLITE Databases.



> [!IMPORTANT]
> This Requires You To Have Basic Knowledge With Python Functions

# Required Packages:
Bcrypt: Use `pip install bcrypt` to Install  
OS: No External Installation Required  
Sqlite: No External Installation Required
            

# Setting Up The Module:
- Paste the ```auth``` folder in your Project Directory
- Go Into Your File: ```from auth import auth```
- Make A Variable: ```auth = auth.Auth(db_location='{location}', db_name ='{name}')```
    - Both The `db_location` and `db_name` are Two Optional Arguments that can be passed to customize the location of the database, please use proper directory paths for no issues.
    - Else, leave blank for default settings
> [!TIP]
> Don't Put a '/' Before your `db_location` or else it would move it to the root directory (which is not very nice)
- You Are Now all Set to Start Using The Module

# Usage
- Make A Variable Like: ```auth = auth.Auth(db_location='{location}', db_name ='{name}')```
- There are Three Options You Have: ``` create_user ; verify_user ; check_username```
- Lets Look at all of them in depth
- **create_user**
    - Used to Create A New User With a Username and password
    - Username and Passwords Are Case Sensitive
    - Usage: ```auth.create_user("username" , 'password')```
    - Outputs:  1. ```[ERROR] Invalid Characters In username``` -->User not Created
                2. ```[ERROR] Username Already Taken``` --> User not Created
                3. ```[SUCCESS] User Created Successfully``` --> User Created
- **check_username**
    - Used to verify wheather a username exists or not
    - Usage: ```auth.check_username(username='Username')```
    - Outputs:  1. ```True``` --> Username Exists
                2. ```False``` --> Username Does Not Exists
- **verify_user**
    - Used to Verify User Credentials
    - Usage: ```auth.verify_user(username="username" , password = 'password')```
    - Outputs:  1. ```True``` --> User Credentials Matched
                2. ```False``` --> User Credentials Not Matched
> [!TIP]
>### Share your projects and Ideas, Join my [Discord](https://anuragcode.com/discord)
