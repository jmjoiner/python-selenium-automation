# Created by jerma at 12/22/2021
Feature: Test for amazon cufflinks search
  Search for cufflinks on Amazon

  Scenario: User can search for cufflinks on Amazon
    Given Open Amazon page
    When Search for cufflinks
    And Click search icon
    And Click on the first product
    And Click on Add to cart button
    Then Verify cart has 1 item(s)
