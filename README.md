
# FoodOnline Django

A web app that allows users to browse menus, place orders, and track deliveries from a variety of restaurants, providing a convenient and efficient way to order food online and have it delivered to their doorstep.

## Tech Stack

**Client:** Html, CSS, Javascript

**Server:** Python, Django
## Run Locally

Clone the project

```bash
  git clone git@github.com:Kartik-soni-201900274/FoodOnline-Django.git
```

Go to the project directory

```bash
  cd FoodOnline-Clone
```

Start the server

```bash
  docker-compose -f docker-compose.yaml up
```

Run Migrations
```bash
  docker-compose exec django_app python manage.py migrate
```


## Flowchart

[FlowChart](https://drive.google.com/file/d/1UXT5hveHD8wOniKZA0a9r_tResseTca9/view?pli=1)


## Features

- Vendor Registration and Authentication: Allow restaurants to register and authenticate themselves on the platform.

- Token Verification & Email Configuration: Implement token-based verification for user authentication and configure email settings for notifications.

- Vendor Approval by Admin: Admin dashboard functionality to approve or reject vendor registrations.

- Restaurant Profile Forms & Custom Validators: Develop forms for restaurants to create and update their profiles with custom validation.

- Google Autocomplete Field: Implement Google Autocomplete to assist users in searching for locations and addresses.

- Menu Builder: Allow vendors to create, update, and delete food items and categories for their menus.

- Marketplace Implementation: Create a marketplace where users can browse and order from multiple restaurants.

- Cart Functionality with AJAX: Enable users to add items to their cart without refreshing the page using AJAX requests.

- Basic & Smart Search Functionalities: Implement search functionality for users to find specific restaurants or food items easily.

- Location-Based Search: Utilize geolocation to display nearby restaurants based on the user's current location.

- Dynamic Business Hours Module: Allow vendors to set and update their business hours dynamically, with AJAX support.

- Dynamic Tax Module: Implement dynamic tax calculations based on the user's location or other parameters.

- Customer App and Profile Building: Enable users to create profiles, manage orders, and track order history.

- Orders Model and Checkout Page: Develop a checkout page where users can review their orders and proceed with payment.

- Payment Gateways Integration: Integrate PayPal and Razorpay payment gateways to facilitate secure transactions.

- Vendor Dashboard: Provide vendors with a dashboard to monitor orders, revenue, and manage their menu items.

- Custom Middleware for Analytics: Implement custom middleware to track and analyze total revenue per vendor and monthly revenue.

- Email Templates Integration: Use customizable email templates for order confirmations, notifications, and other communication.

- Mobile-Friendly Design: Ensure the website is responsive and optimized for mobile devices to enhance user experience.


## Screenshots

 <img width="1440" alt="image" src="https://github.com/Kartik-soni-201900274/FoodOnline-Django/assets/91082323/579be862-00f9-4a30-9159-ee5385d30a62"> 

<img width="1440" alt="image" src="https://github.com/Kartik-soni-201900274/FoodOnline-Django/assets/91082323/12e67edd-0975-4a84-804b-f67d6d0563fb">

<img width="1437" alt="image" src="https://github.com/Kartik-soni-201900274/FoodOnline-Django/assets/91082323/8d70b6ef-fda2-4029-b726-535e7606b5b8">
<img width="1440" alt="image" src="https://github.com/Kartik-soni-201900274/FoodOnline-Django/assets/91082323/7465672f-1f7f-4410-9391-0d89379d151e">


