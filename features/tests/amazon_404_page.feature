# Created by jerma at 3/10/2022
Feature: Test for Amazon 404 page
  # Enter feature description here

  Scenario: User is able to navigate to Amazon blog from 404 page
    Given Open Amazon product 887N$MGQ11111111 page
    And Store original window
    When CLick on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window
