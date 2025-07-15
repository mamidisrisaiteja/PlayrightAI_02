@inventory
Feature: Inventory Module
  As a user, I want to view the product listing on the inventory page

  @TC_INV_01
  Scenario: Verify product listing
    Given the user is logged in
    When the user is on the inventory page
    Then the product grid should be displayed
