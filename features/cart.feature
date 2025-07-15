@cart
Feature: Cart Module
  As a user, I want to view the cart contents

  @TC_CART_01
  Scenario: View cart contents
    Given the user is logged in
    When the user clicks the cart icon
    Then the cart page should display selected items
