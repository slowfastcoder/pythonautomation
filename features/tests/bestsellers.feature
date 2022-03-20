# Created by An T at 2/26/2022
Feature:  Verify that user can navigate to Amazon Best Sellers
   User can navigate to amazon best sellers page and there should be 5 links there

  Scenario: User navigates to Amazon Best Seller
    Given User goes to amazon best seller
    Then There should be 5 links present

  Scenario: User can add an item to the cart
    Given User goes to amazon best seller
    When User clicks 1 product to view
    And Adds that product to the cart
    When User navigates to view the cart page
    Then There should be 1 item in the cart

  Scenario: User navigates to Amazon Best Seller v2
    Given User goes to amazon best seller
    Then User can click through top links and verify correct page opens
    Then Verify there are 5 links
