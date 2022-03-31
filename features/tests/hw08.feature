# Created by An Tran at 3/29/2022
Feature: HW 8 1. Make another test scenario using a dropdown and search
  for an item in a different Amazon department.

  Scenario: Search for an item in a different amazon department
    Given Open Amazon
    When Select Dropdown
    And Search for 5g
    Then Verify Mobile department is selected

  Scenario: Hoover over New Arrivals and see the deals
    Given Open Random Amazon Page
    When Hoover New Arrivals
    Then Verify Deals Appear
