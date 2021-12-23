# Created by jerma at 12/9/2021
Feature: Sign in test
  # Enter feature description here

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened
