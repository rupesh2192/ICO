## Initial Coin Offering
The platform offers initial tokens that are avaialble for bidding. Users can place their bid during an active bidding session. After the the bidding session is complete, Admin can execute the token allocation algorithm.


This project has 3 main components:
* Token: This is the token that will be allocated to the users.
* Bid Session: Admin can create a Bid Session, bidding for the tokens is allowed only if there is an active  Bid Session.
* Bid: Users can bid for token with quantity and price of their choice.

#### The application is hosted on heroku [here](https://initial-coin-offering.herokuapp.com/)
### Flow
* By default, 5000 tokens are added to the database using the migrations.
* The admin needs to log in to the Admin UI and create a Bidding Session.
* Once the bidding session is active, users can start placing their bid.
* After the bidding session is complete, Admin can select the bidding session and allocate tokens for it.
* After the allocation is complete Admin can also view the report of token allocation.

### Setup
1. Create and activate python virtual environment.
2. Install dependencies:
   
    ```shell
    pip install -r requirements.txt
   ```
3. Migrate:
   ```shell
    python manage.py migrate
   ```
4. Create Users: 
    ```shell
    python manage.py create_users
    ```
5. Run Server:
   ```shell
   python manage.py runserver
   ```
   
### Usage
* After completing the above setup successfully, you will have the application running on http://127.0.0.1:8000/
* Three users are created with below credentials:
  * Admin User: `Username: admin Password: admin`
  * User 1: `Username: mike Password: admin`
  * User 2: `Username: john Password: admin`
  

* To start a Bidding Session:
  * Visit: [Bid Session](http://127.0.0.1:8000/admin/login/?next=/admin/coin_offering/bidsession/) page
  * Log in using admin user credentials
  * Click on `Add Bid Session`
  * Select Start and End time of your choice
  * Enter a title for reference
  * Click on `Save`
  

* To Place a bid:
  * Visit [Bid](http://127.0.0.1:8000/api-auth/login/?next=/bid/) API Page
  * Enter credentials of a User
  * Enter price and quantity of your choice and click on `POST`


* Allocate Tokens:
  * After the bidding session is complete, select the Bid Session from the list [here](http://127.0.0.1:8000/admin/coin_offering/bidsession/)
  * Click on the `Allocate Tokens` button in the Top right corner
  * After successful allocation, click on `Allocation Report` to check token allocation details
  