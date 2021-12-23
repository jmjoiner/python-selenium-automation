# Created by jerma at 12/9/2021
Feature:
  Amazon Help Cancel Order

  Scenario: User can cancel an order on Amazon
    Given Open Amazon customer help page
    When Look for cancel order in help search
    Then Verify Cancel order
