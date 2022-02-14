# Created by AN at 2/13/2022
Feature: # Amazon Search
  #
  Scenario: User can search for a product
    Given Open Amazon
    When Search for "coffee"
    Then Verify search results are shown for coffee

  Scenario: User can search for a product2
    Given Open Amazon
    When Search for "table"
    Then Verify search results are shown for table
