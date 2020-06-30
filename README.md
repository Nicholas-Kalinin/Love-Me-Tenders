# Love-Me-Tenders
A chicken tender review blog/capstone project for PDX Code Guild.

## Project Overview
Love Me Tenders is a review blog solely dedicated to the appreciation of an underappreciated and often times misunderstood food item: chicken tenders.  Initial development will begin as a blog containing my own user reviews,photos and data, but I would ideally like it to be a Yelp Clone that gathers crowd-sourced reviews.  

## Functionality
* [ ] Index view containing main page with individual review titles and images.
  * [ ] User system for submitting reviews.(flex)
  * [ ] Button at to create new review.
  * [ ] Search field to search for specific reviews.
* [ ] Detail view to see individual reviews.
 * [ ] Delete review button.
 * [ ] Button to return to index.
 * [ ] Like/Comment box to provide feedback on review.
  
  ## Data Models
  * TenderReview
    * image(ImageField)
    * restaurant(CharField)
    * location(CharField)
    * date (DateField)
    * sides(CharField)
    * sauces(CharField)
    * description(TextField)
    * rating(IntegerField)
    * recommend?(BooleanField)
    
## Schedule
   * Week 1:
      * Sketch out page format.
      * Establish Django models, views, template rendering, database.
      * Establish HTML search fields, load sample data into SQLite3 DB. 
      * Create user system.
      
   * Week 2:
      * Get data fields formatted on detail pages(HTML,CSS).
      * Lockdown basic page layout(Flexbox?).
      * Integrate search feature with JS.
      * Allow for crowd sourced reviews.
      * Troubleshoot functionality.
      
   * Week3: 
      * Fonts/Button Effects.
      * Upload detailed reviews.
      * Finalize styling.
      * Test functionality.
      

     
      * Troubleshoot functionality.
