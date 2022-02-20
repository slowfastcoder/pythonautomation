# Created by Android007 at 2/20/2022
Feature: Verify that the user's cart is empty
  Test cases for when the user has no item in their cart

  Scenario: User has an empty cart
    Given Open Amazon Main Page
    When User clicks on cart icon
    Then An Empty Cart result should be shown