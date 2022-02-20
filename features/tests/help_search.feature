# Created by An Tran at 2/20/2022
Feature: Test Scenarios for Help Search Functionality
  This is for the amazon web page

  Scenario: User can search for help
    Given Open Amazon Help Page
    When Input Cancel Order into help search field
    And Press Enter on Search Field
    Then Cancel results for Cancel Items are shown

