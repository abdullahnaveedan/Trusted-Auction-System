# Trusted Auction System

Trusted Auction System is a web application developed using Django, a Python web framework. The system allows users to participate in online auctions, where they can upload products for bidding, place bids on products, and close auctions based on their preferred time.

## Features

- User Registration and Authentication: Users can create accounts and log in to access the auction features.

- Product Listing: Registered users can list products for auction, providing details such as product name, description, starting price, and auction duration.

- Bidding: Users can place bids on listed products. Each bid must be higher than the previous bid.

- Auction Management: The user who listed the product can choose to close the auction manually when satisfied with the highest bid.

- Auto-Close: The system can automatically close auctions when the specified duration expires.

## Installation

1. Clone the repository: `git clone https://github.com/abdullahnaveedan/trusted-auction-system.git`

2. Navigate to the project directory: `cd trusted-auction-system`

3. Install dependencies (i.e. Install Django, Python, Pillows)

4. Set up the database: `python manage.py migrate`

5. Create a superuser for admin access: `python manage.py createsuperuser`

6. Start the development server: `python manage.py runserver`

7. Access the application in your web browser at `http://127.0.0.1:8000/`

## Usage

1. Register a new user account or log in with existing credentials.

2. Once logged in, navigate to the "Add Product" page to list a new product for auction. Provide product details and set the auction duration.

3. Other users can browse the listed products and place bids.

4. As the auction owner, you can manually close the auction when you decide. Alternatively, auctions will automatically close after the specified duration.

5. The highest bid wins the product, and the winner is notified.

## Future Enhancements

- Email Notifications: Send email notifications to users when they are outbid or when they win an auction.

- Payment Integration: Integrate a payment gateway for users to make secure payments for won auctions.

- Improved User Profiles: Enhance user profiles with additional information and a history of bids and auctions.

- Enhanced Security: Implement security measures to prevent fraudulent activity and ensure a trustworthy auction environment.

## Credits

This project was developed by Abdullah Naveed. Feel free to contribute by submitting pull requests or reporting issues.

## License

Feel free to use and modify the code according to your needs.

For any inquiries or support, please contact naveedabdullah00001@gmail.com  
Thanks

https://github.com/abdullahnaveedan/Trusted-Auction-System/assets/128359566/25b2ce23-5b7e-4b75-9eca-c68671f9a217

