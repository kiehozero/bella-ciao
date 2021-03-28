<img src="#">

TESTING

## Bugs

1. Highlight filtered category on selection: highlighting the sort options was pretty simple because the items are not added to
a query. On the other hand, the category names are added to a QuerySet. For this portion of the project I was following a template
from the Boutique Ado project so was wary of untangling something and breaking the whole operation, so after some painful attempts
at extracting the items from the QuerySet I realised that I could capture them before they were added. These are created as lists
so affixing [0] to the list name and setting as a new variable cat_list provided the solution seen in the 
[View Product](products/templates/view_product.html) page, namely '{% if 'snacks' == cat_list %}' in the category anchor tags.

2. Following on from bug #1, I noticed that the sorting buttons were not functioning as expected when items were already filtered by
category. In the Code Institute 
[Boutique Ado tutorial](https://github.com/ckz8780/boutique_ado_v1/blob/656166307e469630d09e0eb17a0d17daa440e208/products/templates/products/products.html) 
I was following, the tutor used jQuery to isolate and amend the value attribute in a number of select items that were inside a 
drop-down menu. I had instead decided to use standalone buttons that would sit alongside the search bar and category buttons I
had already added. Initially, a quick search on Stack Overflow and W3C told me that I couldn't add a value attribute to an anchor
tag, but I could use a data-* attribute that was introduced with HTML5. A tutorial by 
[John Resig](https://johnresig.com/blog/html-5-data-attributes/) hinting that assigning a custom value would allow me to use the 
jQuery from the Boutique Ado project above. However, I then realised that in bug #1 I had set the cat_list variable to capture the
category name, so I could probably write some simple Django logic to use a link dependent cat_list. I've yet to work out whether
this is a 'better' or scalable solution than using the jQuery (it probably isn't), but I opted to use it purely because I came up
with it just by thinking through the problem logically and really understanding the code I had already fixed.