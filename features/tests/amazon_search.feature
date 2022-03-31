# Created by AN at 2/13/2022
Feature: # Amazon Search
  #
  Scenario: User can search for a product
    Given Open Amazon
    When Search for coffee
    Then Verify search results are shown for coffee

  Scenario: User can search for a product2
    Given Open Amazon
    When Search for table
    Then Verify search results are shown for table


  Scenario: User can select a specific color
    Given Navigate to Product Page
    When Sort through Color
    Then Verify color selected

  Scenario: User can view language
    Given Open Amazon
    When Hover over language options
    Then Verify Spanish option present


  Scenario: User can select and search in a department
    Given Open Amazon
    When Select books department
    And Search for Faust
    And Click on search icon
    Then Verify books department is selected

