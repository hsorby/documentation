.. Contribution documentation for OpenCMISS

============
Contributing
============

This document covers the process to follow for getting your changes into the :term:`prime repository`.  While there are many types of contribution, this section focuses on contributions made through GitHub and Git, or in other words assets that are managed using the version control system.  It is assumed that :doc:`Setup <dev_setup>` and the OpenCMISS build instructions have already been read and followed.

.. contents::

Overview
========

For any body of work intended for the :term:`prime repository` start with a GitHub issue.  The issue can be used to discuss the topic and clarify any problems related to it.  Once progress has been made towards addressing the issue a pull request is created that references the issue.

Reviewers provide feedback on the changes by adding comments to the pull request or associated commits. The Jenkin's build/test procedure will run each time changes are pushed to the pull request's branch, and the results are displayed in the pull request view.

Once all the changes and reviews are complete, one of the :term:`prime repository` owners will merge the pull request into the prime repository, onto the develop branch.

Note that a bug is just a type of issue, and that resolving the bug should have both the implementation to fix the bug and a test that triggers the bug.

:numref:`Figure %s <OpenCMISS-development-process>` gives a graphical overview of the developer contribution process.  For more detail see the text below.

.. _OpenCMISS-development-process:
.. figure:: images/OpenCMISSProcesses-DevelopmentProcess.png
   :align: center
   :alt: Developer contribution process

   Developer contribution process

GitHub Issue
============

Github issues is the place to discuss the particulars related to an issue, discussions on determining the scope of the issue or clarification of any points that are unclear.

If an issue does not exist for the required work (e.g. implementation of a feature, fixing of a bug), then create a new one.  Create the new issue in the issue list for the respective OpenCMISS component repository that it relates to. If the issue relates to multiple components then create an issue in each repository and add a comment to link to the other e.g. OpenCMISS/zinc#60 (see `this github-secrets blog post <https://github.com/blog/967-github-secrets/>`_ for more information).

Labels
------

A GitHub Issue may be assigned labels by the project administrators to help identify its status at a glance. General labels currently used for OpenCMISS are:

* **Bug**: The issue identifies a malfunction in the current codebase.
* **Feature**: The issue constitutes a request or plan for a new feature.
* **Needs tests**: The issue requires test(s) to be complete. This may refer to a bug report, contributed code, comments, etc. in the issue.
* **Needs documentation**: The issue requires documentation to be complete. This may refer to a bug report, contributed code, comments, etc. in the issue.
* **Needs reviewing**: The issue requires further review from project participants to be complete. This may refer to a bug report, contributed code, comments, etc. in the issue.

In addition, a **Platform** label may be used to identify the issue as specific to a given platform (Windows/Linux/OS X). **Milestone** labels may be used to project when a feature is expected to be complete and/or indicate the priority of a given issue. Higher priority issues will take precedence and therefore be assigned a more immediate (lower) milestone number.

Feature Branch
==============

A feature branch is a branch that is local to you (and anyone you collaborate with), it is a branch that will not be available from the :term:`prime repository`.  All development work should be carried out on a feature branch, for example any major feature that you work on or minor bug fix. Before creating a local feature branch, pull the latest changes from the :term:`prime repository` develop branch into your develop branch.

.. _OpenCMISS-branching:
.. figure:: images/OpenCMISSProcesses-GitBranching.png
   :align: center
   :alt: Git branching illustration

   Git branching illustration

Following this process will make it easier to have multiple feature branches at once and keep them in-sync with the :term:`prime repository` develop branch.  Which will in turn make it easier to manage multiple pull requests.

The following Git command line commands show an example of how to create a
feature branch for fixing a (hypothetical) bug described in `issue #46`::

   git fetch prime develop
   git checkout develop # Not required if already on develop branch
   git merge prime/develop
   git checkout -b 46_hypothetical_bug

We recommend users name their branches by starting with the issue number they are working on followed by a word or words to succinctly describe it. Some examples include: 56_refactor_fe or 36_derivatives.

Test Driven Development
=======================

Test driven development entails writing a test that covers the intended functionality (this may require a suite of tests to be written) and no more.  The tests will require some skeleton implementation so that the test(s) can compile but by definition not pass, at least not pass all the tests. The purpose of this is two-fold: 1. writing the test(s) first sets out the intended design which can be shared through a pull request; and  2. the skeleton implementation will include the documentation clearly describing the intended purpose.  Following this contribution process allows others to comment and make corrections before time is spent on the functional code.

It may be necessary to refactor the current design to enable the easiest possible way to add the new feature.  This is a good thing as the quality of the design improves this makes it easier to work with in the future.  Refactoring means improving the code without adding features, and the tests provide validation that the refactored code performs as well as before.

For simple or obvious bugs which have fallen through the testing gaps just the implementation is fine.

Committing changes to your feature branch
=========================================

Once some changes have been made and local commits committed push your changes to your GitHub OpenCMISS repository (refer to :numref:`Figure %s <OpenCMISS-branching>`).

The following Git command line commands show an example of how to add all files, commit the changes and push them to a GitHub repository for the first time::

   git add .
   git commit -m "Appropiately descriptive message about the changes made."
   git push -u origin 46_hypothetical_bug

The ``git add`` command will stage the changes you have selected. You can use this command multiple times to add all the necessary files that you intend to commit. The ``git commit`` command will commit these changes with the commit message indicated by the ``-m`` argument. The ``git push`` command will push the changes (and also create the branch if it does not already exist) to your origin repository. Your origin repository represents the OpenCMISS repository you have forked on GitHub.

GitHub Pull Request
===================

From there create a pull request from your feature branch to the :term:`prime repository` develop branch. When creating the pull request make sure to add in the comment ``addresses issue #46`` (replace the number 46 with the actual number of the issue you are addressing), or something to that effect. This will create a link between the issue and the pull request enabling other people to see that you are working on this issue and comment on your work.

To create a pull request from one GitHub repository to another follow the instructions `here <https://help.github.com/articles/creating-a-pull-request/>`_.

Satisfy Comments
================

It is important to respond to all feedback appropriately, the review process will check to make sure that all comments have been dealt with. Feel free to respond to comments as appropriate, e.g. through code changes, posting a direct reply etc.

Review
======

It may happen that submitted work is not reviewed immediately or the work is finished before any comments have been made.  If this is the case add a comment to the pull request asking for the submission to be reviewed.  An email will be sent out to the repository owners who will respond and review the submission, please remember that everyone is busy and it may not happen right away.

Completion
==========

To complete the process it is required to have two owners of the :term:`prime repository` comment on the pull request that they are satisfied that the work on the issue is complete and also that the feedback has been addressed, in essence that they are "happy" to merge the submission.  For small submissions it is sufficient for the second owner to show satisfaction by performing the merge.  For larger submissions one of the owners will post a comment on the issue notifying subscribers that they intend to merge the pull request.  If no further objections are raised the pull request will be merged and closed.

A little reminder for the repository owners to check that the :doc:`Review Process <dev_review_process>` has been followed/(is going to be followed) when merging the pull request.

