@smoke @auth
Feature: Login functionality
  As a user, I want to log in to the SauceDemo app so that I can access the inventory page

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the user should be redirected to the inventory page
    And the inventory items should be visible
