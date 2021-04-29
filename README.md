<img src="media/banner-text.png">

Welcome to my full-stack development milestone project. For this project I chose to create [Bella Ciao](https://cafe-bella-ciao.herokuapp.com/), an online store for a barista based in Limerick, Ireland.

The owners have a commercial kitchen facility that specialises in corporate event catering, but during lockdown decided that they wanted to diversify their business towards delivery orders. The business contains a number of highly-trained staff who wished to display their own skills beyond the corporate catering environment, so the owners and employees collectively decided to convert a vacant storehouse within their premises into an area where they can host a range of exclusive events for repeat customers and corporate team-building events once public health restrictions are eased. 

I based the project idea on a number of businesses I had used in Irish cities during lockdown, who had embraced delivery sales by purchasing industrial units purely as a food production site, instead of having a physical shop that customers could visit.


## User Experience

### Colour Selection

<img src="media/palette.png">

I wanted to portray that the staff at the store have an authentic connection to both Italy, where many of the staff trained, and Ireland. To achieve this I used the a uniform palette of hex colours, selected using [Pixlr](https://www.pixlr.com/), and all colour selections are stored in their own [CSS file](static/css/palette.css). To create a strong theme, the navbar uses these colours in a vertical fade, while the landing page header is of the ornate Sarsfield Bridge, familiar to any Limerick resident, stylised using the palette to emphasise the strong connection between the city and this business.

- #008763 - The natural place to start was the colour green, present on both national flags. Officially called [Golf Green](https://www.pantone.com/color-finder/18-5642-TCX), this green was used on the [flag of Italy](https://en.wikipedia.org/wiki/Flag_of_Italy#Description) before a constitutional change in 2006. This is the first shade used in the background of the navigation element on larger devices, and the only shade used on smaller device navigation elements;
- #f0eee9 - officially called [Cloud Dancer](https://www.pantone.com/color-finder/11-4201-TCX), before 2006 this was the official colour of the central band of the Italian flag. The [new colour](https://www.pantone.com/color-finder/11-0601-TCX) is much brighter and tended to stand out too much when used as a background, so I defaulted to the older version;
- #3b0022 - Rather than use the official red, I used Color Hex to identify a red shade that best complemented the greens already selected. This red jumped out as providing a dark contrast against items with a white background, or vice versa;
- #e64757 - For a red that needs to indicate danger or warning, I used a tint close to the default Bootstrap colour for such elements (including their default 'danger' buttons), but made it slightly paler;
- #ceca03 - This is a gold that is slightly paler again than Bootstrap's default caution colour, and overrides the btn-warning elements accordingly. It is also used to highlight the cart total once an item is placed there;
- #100f10 - Lastly this is the default colour of any text on the site that is not within a header element or a button tag.

### Fonts and Icons

- [Arvo](https://fonts.google.com/specimen/Arvo) - I wanted a blocky font that would not look out of place on a screen-printed or stamped design, and Arvo fulfils that requirement, especially in upper case.
- [Montserrat](https://fonts.google.com/specimen/Montserrat) - luckily Google Fonts contains a handy tool which shows commonly-selected fonts against each other, so once I had selected Arvo I decided to pick out Montserrat as a lightweight font to display non-header elements or larger blocks of text.

The icons I used within this project are all sourced from [Font Awesome](https://fontawesome.com/)'s free package.

### Wireframes and Responsive Design

- A [Balsamiq](https://www.balsamiq.com/) wireframe for this project is included in the repository, with [desktop/tablet](planning/wireframes/desktop-index.pdf) and [mobile](planning/wireframes/mobile-index.pdf) versions.

In terms of look and feel, the site is similar across all browsers. The tablet and desktop views are almost identical but for a few alignment changes, while mobile devices always drop into col-12 formatting. Google recently added the Galaxy Fold into their dev tools responsiveness tests which presented some challenges as this device has a very narrow 280px screen, but Bootstrap has done the bulk of the work here, and I've added some media queries where neceassary. In my last project I overused the jQuery html class to replace text in buttons with icons, I've pulled back on that a little this time, and I've used Bootstrap responsive classes, which takes away a lot of the requirements in writing custom CSS and even some basic jQuery. A full responsiveness testing procedure can be found within the [testing log](planning/testing/TESTING.md).

### User Stories

Testing for each of the below user stories is included within the [testing log](planning/testing/TESTING.md).

As a user I want to...

  1. ... view the products available in the shop;
  2. ... read more information about a product;
  3. ... order an item from the store;
  4. ... modify the size or quantity of product I order;
  5. ... view my current cart;
  6. ... edit or delete an item in my cart;
  7. ... checkout my order;
  8. ... create an account;
  9. ... sign in to my account;
  10. ... reset my password;
  11. ... edit my profile information;
  12. ... view upcoming events.
  13. ... sign up to an in-store event;
  14. ... view events I have signed up to;
  15. ... remove an event from my events list;
  16. ... view my order history;
  17. ... view a particular previous order;
  18. ... save my address for future use;
  19. ... sign out of my account;

As an admin, I want to...
  1. ... add a new product;
  2. ... update a product;
  3. ... delete a product;
  4. ... view all orders;
  5. ... view a specific order;
  6. ... add an event;
  7. ... edit an event;
  8. ... delete an event;
  9. ... see a list of event attendees;
  10. ... delete a user from an event;


## Features

### Existing Features

- All users can access the Store page and make a purchase for delivery. Users with an account can store their delivery information for re-use. All products within the Store are available to all users, and a number of products contain size variations.

- All users can edit and delete products from their account ahead of checking out by using the quantity selection buttons and the Update and Delete buttons in the cart page. At checkout, account holders can save their information for future orders by completing the form and ticking the box at the bottom. Anonymous users can still register at this point without clearing their cart, but any orders confirmed before they register will not show up in their account.

- The payments system for this project is [stripe](https://stripe.com/docs/api?lang=python/), no credit or debit card details are stored anywhere within the repository or hosting platforms of the project. Stripe's webhooks are used as a failsafe to ensure that any orders that do not reach the order database before the user closes the window or due to another error still show up within the database.

- All account registration, sign in/out and password retrieval processes are handled by the [django-allauth](https://pypi.org/project/django-allauth/) library. Delivery information is stored separately to this but the two tables are linked via a OneToOneField in the UserProfile table.

- Upon registering, users can see their order history and their saved delivery information in their profile (indicated by their username on the navbar). The orders are sorted in date descending order, and clicking the date will display the information that was e-mailed to the user at the time of purchase.

- Upon registering, account holders also gain access to member-only events in the Events page. Members can join these events by clicking the RSVP button within each Event's page, and can 'un-attend' these events by opening their profile and selecting the delete button underneath the My Events page. Deleting the attending from their profile subsequently releases their reserved place back to the available places for that event.

- Users can only get one ticket per event, a user who is already in the guestlist will not see the RSVP button, but instead a message that they already have a ticket. If an event is over 90% capacity, a 'Limited Availability' message will display at the top of that event's page. If an event is at 100% capacity, a 'Sold Out' message will replace it, and the RSVP button will not display.

- Account holders can also view all of their previous orders by navigating to their Profile page. This will give an overview of the date and products purchased, and the value of the order. Clicking the date will display more information about this order.

- Designated admin users have full CRUD functionality on all events and products. To add a new product or event, select the relevant button with the Admin page. All fields are mandatory on both the product and event forms apart the image fields. Product pricing and event capacity must be greater than zero, and the former can only be in increments of €0.10. The maximum event capacity is 150, and event dates must be in the format specified by the field placeholder. The loyalty field on the Product form is currently unused, please see the 'Features to Implement' section below for more information.

- Admin users can edit or delete any event or product by going to that event's page and selecting the edit or delete buttons. The Edit button will display a page identical to the 'Add Product' and 'Add Event' pages, but will be pre-filled with information from the required item's page. To delete an item, simply click the Delete button on the product page, and a confirmation prompt will display.

- Admins can also see a list of all orders that are displayed in date descending order by clicking the View All Orders link in the Admin page. Clicking the date on any 

- A Frequently Asked Questions page gives some background into the history of the business, as well as some details about how to make a complaint, the security of each customer's payment information and the benefits of signing up for an account.

### Features to Implement

- A number of features came up during the course of the project that would be required to run this as a viable e-commerce business in a real-life situation. The first of these would be a VAT calculator, which would actually be quite simple to implement by adding a VAT field to the Product model, then calculating the total alongside the subtotal and delivery totals at checkout.
- The second feature that I feel would be a requirement for any same-day food delivery business is a time selector. I experimented with using one of these but I couldn't get sufficient control over the date and time formatting being created to push it into a database in a usable format.
- One interesting idea I saw recently was Pret A Manger's unlimited coffee offer for a set monthly fee. I wanted to re-create this using Stripe's subscription payments system. The [setup process](https://stripe.com/docs/billing/subscriptions/overview) itself doesn't seem overly complex, but for the sake of creating an additional user level, as well as splitting orders based on whether the user was a subscriber or not, entailed a lot of work in the timeframe I had.
- Lockdown is not going to last forever and people will eventually be spending less time at home, so the logical next point for this business would be to set up a selection box in the checkout that indicates whether the user wishes to collect their order, removing the cost of delivery.
- One of my original ideas was to build a loyalty model, so customers could redeem points after repeated purchases. I got as far as calculating the points based on product eligibility, but I couldn't get points to carry through during the checkout process. I'm determined to implement this feature as part of my ongoing development after this project is submitted, so I've left the field in the Product and Order models for now. This item will show up in the admin-only Add Product form, but I have cleared any sign of this from any non-admin features. 


## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML is the language used to display and structure information on any website.

- [CSS3](https://en.wikipedia.org/wiki/CSS3)
    - Cascading Style Sheets is the language used to style HTML content.

- [Bootstrap](https://www.getbootstrap.com/)
    - Bootstrap's grid framework helped me bring my initial wireframe ideas to life.

- [Javascript](https://www.javascript.com/)
    - The language that makes the web interactive.

- [jQuery](https://jquery.com/)
    - An open-source Javascript library that simplifies interactive web design.

- [Font Awesome](https://fontawesome.com/)
    - Font Awesome's free package provides a comprehensive icon suite that is fully customisable in CSS.
    
- [Google Fonts](https://fonts.google.com/)
    - Google's free service provided countless fonts to help your project stand out.

- [Gitpod](https://www.gitpod.io/)
    - A software development editor perfect for personal or collaborative use. Gitpod changed their default IDE from Theia to Microsoft's VSCode mid-project, and this change was pretty seamless for myself.

- [GitHub](https://www.github.com/)
    - The world's leading code-hosting platform, and the location of the core code that the project is built upon.

- [Heroku](https://www.heroku.com/)
    - A cloud platform for hosting scaleable apps in a variety of programming languages.

- [Amazon Web Services](https://aws.amazon.com/)
    - A non-relational database in which all data submitted by users is stored, and also where the skeleton of the project's data structure was first mapped out.

- [Django](https://www.djangoproject.com/)
    - Django is an open-source Python framework that is designed for quick launches.

- [Stripe](https://www.stripe.com/)
    - One of the world's foremost payment-processing businesses, they offer lots of services designed for quick setup.

- [Balsamiq](https://www.balsamiq.com/)
    - An intuitive drafting tool that enables visual planning during a project's infancy.

- [Pixlr](https://www.pixlr.com/)
    - Pixlr is a great free software package that enabled me to quickly edit images and create logos. Pixlr has both free and premium versions of the software, but I've never had a task that the free version couldn't handle, and it is really easy to learn.

- [Color Hex](https://www.color-hex.com/)
    - This was a fantastic tool which takes an existing colour and recommends complementary colours. Another piece of software that I wish I had discovered a long time ago.

- [Favicon.io](https://favicon.io/)
    - A quick and easy tool to create favicons for display in the address bar.

- [DBDiagram](https://dbdiagram.io/)
    - This tool really helped me visualise my initial idea as a structure to build. I made a couple of changes but it allowed me to plan a route towards project completion.


## Testing

I have included a [testing log](planning/testing/TESTING.md) within the repository.

I tested this project primarily on Firefox but also Chrome and Edge, taking advantage of the screen size options to test using iPad, Samsung Galaxy and Kindle Fire. I also tested the site on my own Huawei device, as well as passing the initial site on to some friends for UI feedback and some rudimentary data entry testing.


## Deployment

I used [GitHub](https://www.github.com/) as the code host for this project, and [GitPod](https://www.gitpod.io/) to write it, using just a single branch. The project is deployed using [Heroku](https://www.heroku.com/), and all static and media files are hosted using Amazon's [Simple Storage Service](https://aws.amazon.com/s3/). A full guide to cloning and deploying this project can be found in the [setup](planning/testing/SETUP.md) document.


## Database Architecture

<img src="media/db-schema.png">

## Credits

### Content

- [Time and date welcome message](https://tecadmin.net/get-current-date-time-python/)
- The excellent [Noise and Gradient](https://www.noiseandgradient.com/) helped me get some nice colour gradients really quickly for logo backgrounds, and ultimately helped confirm the colour selection for the whole site.
- This very short [RIP Tutorial](https://riptutorial.com/django/example/32472/use-of----extends---------include----and----blocks---) lesson was very valuable as it showed me how to define variables inside Django template tags, I subsequently came to rely in equal parts on this site and the Django documentation (see below) in learning Django's core concepts.
- [This thread](https://stackoverflow.com/questions/9038522/regular-expression-for-any-number-greater-than-0) on Stack Overflow provided a regular expression for use in the event addition forms and checkout forms, while Django's [RegexValidator](https://docs.djangoproject.com/en/3.2/ref/validators/#regexvalidator) class helped implement this pattern on the event form itself. Another useful tool for experiment with regex was [regexr](https://regexr.com/).

### Documentation

- Some of the authentication requirements were copied directly from the django-allauth [documentation](https://django-allauth.readthedocs.io/en/latest/installation.html);
- The [Django documentation](https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.HttpRequest.get_full_path) was invaluable as I learnt how to use the framework, this link in particular showed me a method of retrieving the current URL so I could customise messages based on it;
- Sometimes it is useful to get a second explanation of a Django process and for this I found the guides at [Tutorials Point](https://www.tutorialspoint.com/django/django_models.htm) very comprehensive;
- The [Stripe documentation](https://stripe.com/docs/payments/accept-a-payment) became helpful when I had some problems with my webhooks.
- [Bootstrap's documentation](https://getbootstrap.com/docs/5.0/utilities/spacing/) is fairly comprehensive and I leant particularly on their guides for spacing shortcuts as I wanted to write as little basic CSS as possible as that is where I've gotten bogged down on previous projects.
- As always, W3Schools was invaluable, particularly [this link](https://www.w3schools.com/python/python_dictionaries.asp) on building dictionaries, which helped me build the event list and guest list CRUD functionality.

### Tutorials

- [Code Institute](https://www.codeinstitute.net/)'s [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) project gave me a good structure to work from, as well as the foundations for using Django. Indeed the core of logic for the home, profiles, checkout, cart and product apps is customised from the standard in the Boutique Ado project.
- Setting up favicons was slightly different in Django then just sticking them in the project root, luckily [this](https://learndjango.com/tutorials/django-favicon-tutorial) made this another painless transition.

### Media

- The image used in the index page header is taken from [Tourism Europe](https://www.tourlane.com/europe/ireland/limerick/). The [original](https://images.ctfassets.net/bth3mlrehms2/2CKgqB27vGnVOVRbDEtkll/b1d0d5183538f02650dea4450e08fbbd/Limerick__Ireland.jpg) is used as that page's background element; I styled this significantly using [Pixlr](https://www.pixlr.com/) to match the colour scheme of the project. A cropped version of this is used as a placeholder for events without an image.

- The image for the error pages is from [Townsquare Media](https://townsquare.media/site/158/files/2017/01/spilled-coffee.jpg), a website which doesn't look to be working at the moment but it's content is still showing up in Google searches.

- For brevity, I have created a spreadsheet

### Acknowledgements

- Thanks to [Igor Basuga](https://github.com/bravoalpha79) for spotting an error in my settings.py file that was causing my allauth template inheritance to fail.
- Thanks to Michael Park at Code Institute for spotting an error in how I was trying to unpack querysets when building the feature that allows users to delete their own attendance from an event;
- Thanks again to Michael and also to [Chris Zielinski](https://github.com/ckz8780) who helped me go through some of the code in relation to bugfix 11. I'm proud of myself for picking the error out but Michael and Chris kept me from going down some errant paths that would have wasted a lot of project time.
- Thanks to my brother for doing some purchasing testing on this, he sent me a ton of screenshots of each of his purchases and event 
subscriptions, and in the process accidentally uncovered a recurrence of bug 11 in my deployed site, a pretty important one!
- Thanks to Aine O Neill and Ben Kavanagh, two Code Institute students who responded when I submitted my initial project draft on the CI Slack channel, and both suggesting some helpful CSS shortcuts.
- My partner for letting me eternally bounce ideas of myself and my mentor Precious for helping me structure and prioritise my project work.