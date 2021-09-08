## Initial Coin Offering
This project has 3 main components:
* Token: This is the token that will be allocated to the users.
* Bid Session: Admin can create a Bid Session, bidding for the tokens is allowed only if there is an active  Bid Session.
* Bid: Users can bid for token with quantity and price of their choice.

### Flow
* By default, 5000 tokens are added to the database using the migrations.
* The admin needs to log in to the Admin UI and create a Bidding Session.
* Once the bidding session is active, users can start place their bid.
* After the bidding session is complete, Admin can select the bidding session and allocate tokens for it.
* After the allocation is complete Admin can also view the report of token allocation.