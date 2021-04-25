<img src="#">

## Bugs

1. Highlight filtered category on selection: highlighting the sort options was pretty simple because the items are not added to
a query. On the other hand, the category names are added to a QuerySet. For this portion of the project I was following a template
from the Boutique Ado project so was wary of untangling something and breaking the whole operation, so after some painful attempts
at extracting the items from the QuerySet I realised that I could capture them before they were added. These are created as lists
so affixing [0] to the list name and setting as a new variable cat_list provided the solution seen in the 
[View Product](products/templates/view_product.html) page, namely '{% if 'snacks' == cat_list %}' in the category anchor tags.

2. Following on from bug #1, I noticed that the sorting buttons were not functioning as expected when items were already filtered by
category. In the Code Institute 
[Boutique Ado tutorial](https://github.com/ckz8780/boutique_ado_v1/blob/656166307e469630d09e0eb17a0d17daa440e208/products/templates/products/products.html) I was following, the tutor used jQuery to isolate and amend the value attribute in a number of select items 
that were inside a drop-down menu. I had instead decided to use standalone buttons that would sit alongside the search bar and 
category buttons I had already added. Initially, a quick search on Stack Overflow and W3C told me that I couldn't add a value 
attribute to an anchor tag, but I could use a data-* attribute that was introduced with HTML5. A tutorial by 
[John Resig](https://johnresig.com/blog/html-5-data-attributes/) hinted that assigning a custom value would allow me to use the 
jQuery from the Boutique Ado project above. However, I then realised that in bug #1 I had set the cat_list variable to capture the
category name, so I could probably write some simple Django logic to use a link dependent on cat_list, instead of add values to each
link. I've yet to work out whether this is a 'better' or scalable solution than using the jQuery (it probably isn't), but I opted 
to use it purely because I came up with it just by thinking through the problem logically and really understanding the code I had 
already fixed.

3. As mentioned above, I followed the Boutique Ado project to get any core apps up and running during the 
[Minimum Viable Concept](https://www.agilealliance.org/glossary/mvp/) phase of my project, and consciously trying to make to stand 
apart as development progressed. In the tutorial the buttons were placed directly underneath the quantity form, but I moved the 
buttons to the right-most part of each item row. This cause the form submission to fail as the .prev jQuery function could no longer locate the  form. Javascript is definitely not my strong point so I needed the [jQuery documentation](https://api.jquery.com/siblings/) and the [W3 jQuery tutorials](https://www.w3schools.com/JQuery/jquery_traversing.asp) to refresh my memory. A chain of the parent, 
siblings and children methods provided the solution I needed after console-logging each step to ensure the correct element displayed.

4. I initially wrote this project with Materialize in mind as I had become familiar with the classes and components, but when I
came to set up the checkout form I realised that crispy-forms doesn't offer native support for Materialize. My choices were either
to write my own forms and logic or make the switch to Bootstrap while I still only had four apps to deal with. It was a couple of
hours work to do this but it allowed me to follow a tutorial for a part of the project that links the front and back ends, namely
the crispy forms and Stripe payments, without potentially creating a mountain of work for myself. I had previously preferred using
Materialize to Bootstrap but switching over a ton of classes and removing the overwrites I'd done in my own CSS files gave me a new
appreciate for Bootstrap.

5. I suspected that there was always likely to be some Materialize 'ghosts' floating around my codebase after converting to 
Bootstrap, and one that I found was in the shopping cart, where I discovered that the remove item. This was a pretty easy fix as I 
had left an onclick event containing Materialize's toast feature inside this button's attributes, and has omitted a class to tie 
it to the JS at the bottom of the page.

6. When it came to testing the cart I found that if it contained a product with no image, the cart was returning an error. This was
due to the placement of an if loop inside an anchor, displayed an image if available and a placeholder otherwise. However, the anchor
element href contained a link to this image, so I just needed to put the anchor element inside the loop to fix this.

7. I initially could not get my allauth templates to inherit from templates/base.html, but a quick call to Code Institute tutoring
found the error, which was a missing comma in my settings.py file. Thanks to [Igor Basuga](https://github.com/bravoalpha79) for
spotting that one.

8. I initially created the event_attendees database of something of a data dump for event and user ids to be added to the same row.
As I did some [reading](https://riptutorial.com/django/example/30649/foreignkey), I realised that this could cause database problems
if I deleted a user or event. I tested this and it seems to work fine, i.e. deleting an event and then re-opening a user's profile
would see that event disappear, but something didn't sit right with leaving tons of user-event rows in the event_attendee database
once they were no longer needed, and using foreign keys to ensure cascading deletion seemed to be the best-practice option. Once I
got my head around the exact order of deleting old test attendee entries, updating models and migrating them, this was a relatively
simple process.

9. My initial message display was overlapping headers on smaller screens when the message was too long. I tried restricting the
maximum length of messages but this defeated the whole purpose of having one. I eventually found that the problem was actually 
caused by a vh height being set on the message-row tag. I then moved this above the page-header tagged elements and this provided
a much improved user experience.

10. During testing I noticed that a couple of the dummy accounts I had set up could see the guestlist on events. This was intended 
to be an admin feature so quickly wrapping the entire row in the request.user.is_superuser statement was a simple fix.

11. Probably the error I'm happiest to have fixed was one where upon submitting an order, the webhook would then duplicate the order,
at what seemed like random points. Obviously the likelihood of this occurrence actually being random was pretty low, so I had to start
combing through my code. The cause was eventually identified as a rounding issue I had added into the cart/contexts.py file. Because 
the delivery threshold is a percentage, it means that any items that were sold in decimal values (e.g. €2.30, €2.70, etc.) created a 
grand total that was then being rounded up to the nearest ten. Once I removed the rounding function the problem was resolved.

12. During responsiveness testing I found that things were generally working as planned but the iPad vertical view (width 768px) had significant whitespace at the top of the screen. I knew that in adding the mobile navbar I had added some margin in so it wouldn't 
overlap any content by default, but this was still showing up with my vertical navbar for large screens. The problem arises in a 
conflict between Bootstrap's default breakpoints and how I had defined my media queries. The medium breakpoint is equal to or 
greater than 768px, and I set my media query for that extra margin to sit behind the mobile navbar as 768px, instead of 767px, 
which was a simple fix at the bottom of the base.css document.

13. Admin page testing - could add event with no date and an order with no Eircode


## Outstanding Issues

1. Search bar results can't be sorted by sort buttons
2. Cart quantity will sometimes allow a user to submit a quantity outside of the parameters, seems to only occur when there are 
two versions of an item (i.e., one regular and one large) in the basket, and it only affects the second item - suspect this is to
do with how quantitySelect.js moves up and down the DOM to return the first item with a given item ID
3. Loyalty stamps don't seem to add up on certain drinks (noticed this first on the espresso added using the product form)
4. Cart quantity buttons on smaller devices
5. Sites database
6. Event form Description field styling, Date/Time widget UX (date format)
7. Rounding issue on products that aren't in pricing multiples of ten (Seabrook's at 1.35)
8. Sometimes issues rendering tables on ultra-narrow devices like Galaxy Fold


## Rendering

>>> User Lighthouse in Chrome here
>>> Am I Responsive 