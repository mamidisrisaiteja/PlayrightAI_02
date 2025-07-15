@smoke @auth
Feature: Authentication Module
  As a user, I want to log in to the SauceDemo app so that I can access the inventory page

  @TC_AUTH_01
  Scenario: Login with valid credentials
    Given the user is on the login page
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the user should be redirected to the inventory page
    And the inventory items should be visible

  @TC_AUTH_02
  Scenario: Login with invalid credentials
    Given the user is on the login page
    When the user logs in with username "invalid_user" and password "invalid_pass"
    Then an error message should be displayed
