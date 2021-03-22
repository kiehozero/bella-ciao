<img src="#">

Welcome to my full-stack development milestone project. For this project I chose to create 
[Bella Ciao](#), an online store for a fictional coffee chain based at various locations in Limerick, Ireland.


## User Experience

### Styling

- A [Balsamiq](https://www.balsamiq.com/) wireframe for this project is included in the repository, with 
[desktop/tablet](planning/wireframes/desktop.pdf) and [mobile](planning/wireframes/mobile.pdf) versions.

I used the following hex colours, selected using [Pixlr](https://www.pixlr.com/)

- 
- 
- 

### Fonts and Icons

- Fonts

The icons I used within this project are all sources from [Font Awesome](https://fontawesome.com/)'s free package.


### Responsiveness

<<< In terms of look and feel, the site is similar across all browsers. The tablet and desktop views are almost identical
but for a few alignment changes, while mobile devices always drop into col-12 formatting. For mobile devices, I have 
included Materialize's default sidenav bar, which was much easier to set up than Bootstrap's mobile menu options. I have 
also tended to use jQuery to change descriptive buttons it icon-based buttons for smaller devices. A full responsiveness
testing procedure can be found within the [testing log](planning/testing/TESTING.md). >>>

### User Stories

Testing for each of the below user stories is included within the [testing log](planning/testing/TESTING.md).

As a user I want to...

  1. order an item for collection;
  2. order an item for pick-up;
  3. start a subscription.
  4. cancel a subscription;
  5. edit my profile information;
  6. see my loyalty points;
  7. ... .

As an admin, I want to
  1. add a new product;
  2. delete a product;
  3. ... ;
  4. ... .


## Features

### Existing Features



### Features to Implement




## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML is the language used to display and structure information on any website.

- [CSS3](https://en.wikipedia.org/wiki/CSS3)
    - Cascading Style Sheets is the language used to style HTML content.

- [Materialize](https://materializecss.com/)
    - Materialize's grid framework helped me bring my initial wireframe ideas to life.

- [Javascript](https://www.javascript.com/)
    - The language that makes the web interactive.

- [jQuery](https://jquery.com/)
    - An open-source Javascript library that simplifies interactive web design. In this case it is the key to utilising
    some of Materialize's key features.

- [Font Awesome](https://fontawesome.com/)
    - Font Awesome's free package provides a comprehensive icon suite that is fully customisable in CSS.
    
- [Google Fonts](https://fonts.google.com/)
    - Google's free service provided countless fonts to help your project stand out.

- [Gitpod](https://www.gitpod.io/)
    - A software development editor perfect for personal or collaborative use.

- [GitHub](https://www.github.com/)
    - The world's leading code-hosting platform, and the location of the core code that the project is built upon.

- [Heroku](https://www.heroku.com/)
    - A cloud platform for hosting scaleable apps in a variety of programming languages.

- [Balsamiq](https://www.balsamiq.com/)
    - An intuitive drafting tool that enables visual planning during a project's infancy.

- [Pixlr](https://www.pixlr.com/)
    - Pixlr is a great free software package that enabled me to quickly pick out hex colors and edit images. I have been
    using this for all sorts of things for about five years and it is somehow still free-to-use.

- [Favicon.io](https://favicon.io/)
    - A quick and easy tool to create favicons for display in the address bar.

- [Amazon Web Services](#)
    - A non-relational database in which all data submitted by users is stored, and also where the skeleton of the project's
    data structure was first mapped out.

- [Django](https://www.djangoproject.com/)
    - Django is an open-source Python framework that  is designed for quick launches.

- [DBDiagram](https://dbdiagram.io/)
    - >>>


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


## Database Architecture




## Credits

### Content

- Some of the authentication requirements were copied directly from the django-allauth 
[documentation](https://django-allauth.readthedocs.io/en/latest/installation.html)

### Tutorials

- [Code Institute](https://www.codeinstitute.net/)'s [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) project 
gave me a good structure to work from, as well as the foundations for using Django;
- Setting up favicons was slightly different in Django then just sticking them in the project root, luckily 
[this](https://learndjango.com/tutorials/django-favicon-tutorial) made this another painless transition.


### Media



### Acknowledgements

- My partner for letting me eternally bounce ideas of myself and my mentor Precious for helping me structure and prioritise
my project work.