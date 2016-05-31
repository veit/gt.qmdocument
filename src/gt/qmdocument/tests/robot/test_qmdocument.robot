# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gt.qmdocument -t test_qmdocument.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gt.qmdocument.testing.GT_QMDOCUMENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_qmdocument.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a QMDocument
  Given a logged-in site administrator
    and an add qmdocument form
   When I type 'My QMDocument' into the title field
    and I submit the form
   Then a qmdocument with the title 'My QMDocument' has been created

Scenario: As a site administrator I can view a QMDocument
  Given a logged-in site administrator
    and a qmdocument 'My QMDocument'
   When I go to the qmdocument view
   Then I can see the qmdocument title 'My QMDocument'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add qmdocument form
  Go To  ${PLONE_URL}/++add++QMDocument

a qmdocument 'My QMDocument'
  Create content  type=QMDocument  id=my-qmdocument  title=My QMDocument


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the qmdocument view
  Go To  ${PLONE_URL}/my-qmdocument
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a qmdocument with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the qmdocument title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
