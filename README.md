<img src="media/banner-text.png">

Welcome to my full-stack development milestone project. For this project I chose to create 
[Bella Ciao](https://cafe-bella-ciao.herokuapp.com/), an online store for a coffee chain based in Limerick, Ireland.
The owners are a commercial kitchen facility that specialises in corporate event catering, but during lockdown decided
that they wanted to diversify their business towards delivery orders. The business contains a number of highly-trained
staff who wished to display their own skills beyond the corporate catering environment, so the owners and employees
collectively decided to convert a vacant storehouse within their premises into an area where they can host a range of
exclusive events for repeat customers and corporate team-building events once public health restrictions are eased.


## User Experience

### Styling

- A [Balsamiq](https://www.balsamiq.com/) wireframe for this project is included in the repository, with 
[desktop/tablet](planning/wireframes/desktop.pdf) and [mobile](planning/wireframes/mobile.pdf) versions.

In colour selection I wanted to portray that the staff at the store have an authentic connection to both Italy, where many
of the staff trained, and Ireland. To achieve this I used the following hex colours, selected using 
[Pixlr](https://www.pixlr.com/), and all colour selections are stored in their own [CSS file](static/css/palette.css).

- #008763 - The natural place to start was the colour green, present on both national flags. Officially called 
[Golf Green](https://www.pantone.com/color-finder/18-5642-TCX), this green was used on the 
[flag of Italy](https://en.wikipedia.org/wiki/Flag_of_Italy#Description) before a constitutional change in 2006. 
This is the first shade used in the background of the navigation element on larger devices, and the only
shade used on smaller device navigation elements;
- #f0eee9 - officially called [Cloud Dancer](https://www.pantone.com/color-finder/11-4201-TCX), before 2006 this was
the official colour of the central band of the Italian flag. The [new colour](https://www.pantone.com/color-finder/11-0601-TCX) 
is much brighter and tended to stand out too much when used as a background, so I defaulted to the older version;
- #3b0022 - Rather than use the official red, I used Color Hex to identify a red shade that best complemented the greens already selected. This red jumped out as providing a dark contrast against items with a white background, or vice versa;
- #e64757 - For a red that needs to indicate danger or warning, I used a tint close to the default Bootstrap colour for such
elements (including their default 'danger' buttons), but made it slightly paler;
- #ceca03 - This is a gold that is slightly paler again than Bootstrap's default caution colour, and overrides the btn-warning
elements accordingly. It is also used to highlight the cart total once an item is placed there;
- #100f10 - Lastly this is the default colour of any text on the site that is not within a header element or a button tag.

### Fonts and Icons

- [Arvo](https://fonts.google.com/specimen/Arvo) - I wanted a blocky font that would not look out of place on a screen-printed
or stamped design, and Arvo fulfils that requirement, especially in upper case.
- [Montserrat](https://fonts.google.com/specimen/Montserrat) - luckily Google Fonts contains a handy tool which shows 
commonly-selected fonts against each other, so once I had selected Arvo I decided to pick out Montserrat as a lightweight 
font to display non-header elements or larger blocks of text.

The icons I used within this project are all sourced from [Font Awesome](https://fontawesome.com/)'s free package.

### Responsiveness

<<< In terms of look and feel, the site is similar across all browsers. The tablet and desktop views are almost identical
but for a few alignment changes, while mobile devices always drop into col-12 formatting. For mobile devices, >>>. I have 
also tended to use jQuery to change descriptive buttons it icon-based buttons for smaller devices. A full responsiveness
testing procedure can be found within the [testing log](planning/testing/TESTING.md). >>>

### User Stories

Testing for each of the below user stories is included within the [testing log](planning/testing/TESTING.md).

As a user I want to...

  1. order an item from the store;
  3. modify the size, quantity or variety of product I order;
  4. read more information about a product;
  5. filter or sort products by category or a search term of my choice;
  6. create an account;
  9. edit my profile information;
  10. see my loyalty points;
  11. sign up to an in-store event;
  12. view events I have signed up to;
  13. remove an event from my events list;
  13. view my current shopping cart;
  14. view my order history;
  15. save my address for future use;

As an admin, I want to
  1. add a new product;
  2. update a product;
  3. delete a product;
  6. view all orders;
  9. add an event;
  10. edit an event;
  11. delete an event;
  12. delete a user from an event;


## Features

### Existing Features

- Purchase items
- View order history
- Events for logged in users
- Admin panel for products and events

### Features to Implement

- Subscription requires separate payment method from Stripe, ran out of time
- VAT options
- Delivery/collection for when lockdown ends and the business might want to expand to a retail outlet

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
    - A software development editor perfect for personal or collaborative use. Gitpod changed their default IDE from Theia
    to Microsoft's VSCode mid-project, and this change was pretty seamless for myself.

- [GitHub](https://www.github.com/)
    - The world's leading code-hosting platform, and the location of the core code that the project is built upon.

- [Heroku](https://www.heroku.com/)
    - A cloud platform for hosting scaleable apps in a variety of programming languages.

- [Amazon Web Services](https://aws.amazon.com/)
    - A non-relational database in which all data submitted by users is stored, and also where the skeleton of the project's
    data structure was first mapped out.

- [Django](https://www.djangoproject.com/)
    - Django is an open-source Python framework that is designed for quick launches.

- [Stripe](https://www.stripe.com/)
    - One of the world's foremost payment-processing businesses, they offer lots of services designed for quick setup.

- [Balsamiq](https://www.balsamiq.com/)
    - An intuitive drafting tool that enables visual planning during a project's infancy.

- [Pixlr](https://www.pixlr.com/)
    - Pixlr is a great free software package that enabled me to quickly edit images and create logos. Pixlr has both free and
    premium versions of the software, but I've never had a task that the free version couldn't handle, and it is really easy
    to learn.

- [Color Hex](https://www.color-hex.com/)
    - This was a fantastic tool which takes an existing colour and recommends complementary colours. Another piece
    of software that I wish I had discovered a long time ago.

- [Favicon.io](https://favicon.io/)
    - A quick and easy tool to create favicons for display in the address bar.

- [DBDiagram](https://dbdiagram.io/)
    - This tool really helped me visualise my initial idea as a structure to build. I made a couple of changes but it allowed
    me to plan a route towards project completion.


## Testing

I have included a [testing log](planning/testing/TESTING.md) within the repository.

I tested this project primarily on Firefox but also Chrome and Edge, taking advantage of the screen size options to test 
using iPad, Samsung Galaxy and Kindle Fire. I also tested the site on my own Huawei device, as well as passing the initial 
site on to some friends for UI feedback and some rudimentary data entry testing.


## Deployment

I used [GitHub](https://www.github.com/) as the code host for this project, and [GitPod](https://www.gitpod.io/) to write 
it, using just a single branch. stuff about [Heroku](https://www.heroku.com/). The actual data is stored within 
a [MongoDB](https://www.mongodb.com/) cluster, and four sub-collections (see the Data Architecture section below).

### Cloning the GitHub repository

Assuming you already have Git [installed](https://git-scm.com/download/), anybody can clone this repository by following 
these steps:

1. Open the command prompt/terminal on your machine;
2. Type the command 'cd' followed by the directory you wish to store the repository in;
3. Go to the top of the [GitHub repository](https://github.com/kiehozero/pintbaby/) and click the green 'Code' drop-down 
button;
4. Copy the [link provided](https://github.com/kiehozero/pintbaby.git);
5. Return to the Command Prompt and type 'git clone' followed by the copied address.

For an in-depth guide to cloning repositories, click 
[here](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/), from which the steps above were taken.

### Django
>>> Installation information, creation of databases, runserver, makemigrations, etc.

### Heroku

I deployed this project to Heroku using the following method:

1. After setting up a [Heroku](https://www.heroku.com/) account and creating a new app, head back to your terminal
and set up a requirements.txt file that automatically updates when you import a library. Instead of using the 
regular 'touch' command, enter 'pip3 freeze -- local > requirements.txt' into the terminal and press enter;
2. Run the 'python app.py > Procfile' command to create a file that Heroku will use to run your app automatically, 
as opposed to you using the python3 app.py command each time you open Gitpod;
3. Push both the Procfile and requirements.txt to your repository;
4. In the Heroku app settings, click the Connect to GitHub button and select the repository you wish for Heroku to
connect to. Click the Config Variables button and select the Reveal option, and enter the items that were added to
your env.py file line-by-line. Since you added it to .gitignore, Heroku will not be able to see it in the GitHub
repository.
5. Once the connection is confirmed, scroll down to the bottom and click the Enable Automatic Deployment button.
6. After a couple of minutes select the Open App button, and you will now have a hosted URL for the project. Unlike
Gitpod or any other IDE, this app will only update when you push changes to your repository.

### Amazon Web Services

>>> S3, IAM

### Python Libraries

This project is built on the [Django](https://www.djangoproject.com/) framework. A number of libraries were installed
to complete this project:

- [django-allauth](https://pypi.org/project/django-allauth/) is an authentication and account management library;
>>> dj_database_url, gunicorn, stripe, django-crispy-forms

## Database Architecture




## Credits

### Content

- [Time and date welcome message](https://tecadmin.net/get-current-date-time-python/)
- The excellent [Noise and Gradient](https://www.noiseandgradient.com/) helped me get some nice colour gradients really quickly
for logo backgrounds, and ultimately helped confirm the colour selection for the whole site.
- This very short [RIP Tutorial](https://riptutorial.com/django/example/32472/use-of----extends---------include----and----blocks---)
lesson was very valuable as it showed me how to define variables inside Django template tags, I subsequently came to rely in equal
parts on this site and the Django documentation (see below) in learning Django's core concepts.

### Documentation

- Some of the authentication requirements were copied directly from the django-allauth 
[documentation](https://django-allauth.readthedocs.io/en/latest/installation.html);
- The [Django documentation](https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.HttpRequest.get_full_path)
was invaluable as I learnt how to use the framework, this link in particular showed me a method of retrieving the current
URL so I could customise messages based on it;
- Sometimes it is useful to get a second explanation of a Django process and for this I found the guides at
[Tutorials Point](https://www.tutorialspoint.com/django/django_models.htm) very comprehensive;
- [Stripe docs](https://stripe.com/docs/payments/accept-a-payment)
- As always, W3Schools was invaluable, particularly [this link](https://www.w3schools.com/python/python_dictionaries.asp) 
on building dictionaries, which helped me build the event list and guest list CRUD functionality.

### Tutorials

- [Code Institute](https://www.codeinstitute.net/)'s [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) project 
gave me a good structure to work from, as well as the foundations for using Django;
- Setting up favicons was slightly different in Django then just sticking them in the project root, luckily 
[this](https://learndjango.com/tutorials/django-favicon-tutorial) made this another painless transition.
- Thanks to [Igor Basuga](https://github.com/bravoalpha79) for spotting an error in my settings.py file that was causing
my allauth template inheritance to fail.
- Thanks to Michael Park at Code Institute for spotting an error in how I was trying to unpack querysets when building
the feature that allows users to delete their own attendance from an event;
- [Bootstrap's documentation](https://getbootstrap.com/docs/5.0/utilities/spacing/) is fairly comprehensive and I leant
particularly on their guides for spacing shortcuts as I wanted to write as little CSS as possible as that is where I've
gotten bogged down on previous Bootstrap projects.

### Media

- The image used in the index page header is taken from [Tourism Europe](https://www.tourlane.com/europe/ireland/limerick/).
The [original](https://images.ctfassets.net/bth3mlrehms2/2CKgqB27vGnVOVRbDEtkll/b1d0d5183538f02650dea4450e08fbbd/Limerick__Ireland.jpg)
is used as that page's background element; I styled this significantly using [Pixlr](https://www.pixlr.com/) to match the 
colour scheme of the project. A cropped version of this is used as a placeholder for events without an image.

### Acknowledgements

- My partner for letting me eternally bounce ideas of myself and my mentor Precious for helping me structure and prioritise
my project work.