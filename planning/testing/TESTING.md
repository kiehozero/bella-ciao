<img src="#">

TESTING

## Bugs

1. Highlight filtered category on selection: highlighting the sort options was pretty simple because the items are not added to
a query. On the other hand, the category names are added to a QuerySet. For this portion of the project I was following a template
from the Boutique Ado project so was wary of untangling something and breaking the whole operation, so after some painful attempts
at extracting the items from the QuerySet I realised that I could capture them before they were added. These are created as lists
so affixing [0] to the list name and setting as a new variable cat_list provided the solution seen in the 
[View Product](products/templates/view_product.html) page, namely '{% if 'snacks' == cat_list %}' in the category anchor tags.