# Created by jerma at 12/22/2021
Feature: Test for amazon cufflinks search
  Search for cufflinks on Amazon

  Scenario: User can search for cufflinks on Amazon
    Given Open Amazon page
    When Search for cufflinks
    And Click search icon
    Then Search result have "cufflinks"
