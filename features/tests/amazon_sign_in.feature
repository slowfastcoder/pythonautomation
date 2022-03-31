# Created by An Tran at 3/27/2022
Feature: Amazon Sign in

  Scenario: Sign in page can be opened from SignIn popup
    Given Open Amazon
    When Click on button from SignIn popup
    Then Verify Sign In page is opened

  Scenario: User can see sign in Page
    Given Open Amazon
    When Click Amazon Orders link
    Then Verify Sign In page is opened