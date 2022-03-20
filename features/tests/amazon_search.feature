# Created by jerma at 12/2/2021
Feature: Test for amazon search
  # Enter feature description here

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Search for coffee
    And Click search icon
    Then Search results have "coffee"

  Scenario Outline: User can search for a product on Amazon2
   Given Open Amazon page
   When Search for <product>
   And Click search icon
   Then Search results have <expected_result>
   Examples:
   |product  |expected_result    |
   |coffee   |"coffee"    |
   |table    |"table"    |


