# Created by jerma at 1/3/2022
Feature: Test for Amazon Bestsellers Page
  # Enter feature description here

  Scenario: User can see Bestsellers Results
    Given Open Amazon Bestsellers Page
    Then User sees 5 subheader links