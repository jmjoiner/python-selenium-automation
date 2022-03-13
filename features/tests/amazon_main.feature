# Created by jerma at 1/3/2022
Feature: Test for Amazon main page
  # Enter feature description here

  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu is present

  Scenario: User can see 39 footer links
    Given Open Amazon page
    Then Verify 39 links present

  Scenario: Sign In page can be opened from Sign In popup
    Given Open Amazon page
    When CLick Sign In from popup
    Then Verify Sign in page opened

  Scenario: User sees SignIn pop up for a few seconds
    Given Open Amazon page
    Then Verify that SignIn popup shown
    Then Verify that SignIn btn is clickable
    When Wait for 6 sec
    Then Verify that SignIn popup disappears

  Scenario: User can click on Best Seller Links
    Given Open Amazon page
    When Click on Best Sellers Link
    Then Verify that user is on the Best Sellers Page
    Then Verify user can click through Best Seller Links