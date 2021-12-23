# Created by jerma at 12/22/2021
Feature: Amazon Cart
  Verifying test steps to view empty Amazon cart

Scenario: User can verify Amazon is empty
    Given Open Amazon page
    When Clicks on the cart icon
    Then Verifies that Your Amazon Cart is empty