AMS Short Course on Open Source Radar Software
=============================

Render this document as pdf by ``rst2pdf course_outline.rst``

**09:00 - 09:30** `Introduction`_::

   Taking seats, booting notebooks...

   Introduction of tutors and course outline, brief participant survey.


**09:30 - 10:15** `Sustainable software practices`_::

    Version Control including Git.

    Open community coding including GitHub.

**10:15 - 11:00** `Python, and Scientific Python`_::

   Python will be the key to use the presented radar software tools.

   Learn how to use Python for writing scripts and for interactive data analysis.

   Scipy, Numpy and Matplotlib

   What is IPython and the IPython notebook? 

**11:00 - 11:30** Coffee break

**11:30 - 13:00** `Practical Py-ART 1`_::

   The Py-ART data model, how is radar represented in Python using Py-ART

   Plotting in Py-ART

**13:00 - 14:00** Lunch break


**14:00 - 15:00** `Practical Py-ART 2`_::

   The Gatefilter and how to use it.

   Processing: Texture and dealiasing.

   Gridding: Gridding one or more radars. 

**15:00 - 15:30** Coffee break

**15:30 - 16:30**  `Python Tools`_::

    TBD, This is for ART-View and Py-TDMA etc.. 

**16:30 - 17:00** `Wrapup`_::

   Questions and comments.

   Feedback.


.. raw:: pdf

      PageBreak


Introduction
------------

Time to settle in and say hello. Course tutors will open the course and introduce themselves and their projects, as well as the general structure and concept of the short course.

With a brief `online survey TBD <TBD>`_, we will get an overview of the participants' background and motivations.


Sustainable software practices
------------------------------

We will provide a "real-time" demonstration of collaborative development based on a Distributed Version Control System.

The Virtual Machine (VM) already comes with hg and git clients so everyone will be set. Course tutors will demonstrate the following steps::

   User 1

    Submit a pull request against this course outline

   User 2

Course participants can create their own accounts at http://githubcom or http://bitbucket.org where they
can host the code they wrote during the course.


Python, and Scientific Python
-----------------------------

The Python quick start will cover e.g.::

   - Installing Python, Python distributions / scientific stacks, most important dependencies

   - Starting Python from the shell and "hello world"

   - Executing a Python script

   - General guidelines on programming style and syntax in Python

   - Control flow

   - Array operations in Numpy

   - Plotting with matplotlib



Practical Py-ART 1
------------------

Session outline can be found at: https://github.com/EVS-ATMOS/pyart_short_course

These notebooks and associate data will automagically be loaded onto the Virtual machine for use in the course.. For static notebooks:

Lesson 1: Introduction to the Py-ART data model
          http://nbviewer.ipython.org/github/EVS-ATMOS/pyart_short_course/blob/master/1%20Investigating%20the%20Py-ART%20Radar%20Object.ipynb

Lesson 2: Simple Py-ART usage, a lesson from Miami
          http://nbviewer.ipython.org/github/EVS-ATMOS/pyart_short_course/blob/master/2%20Simple%20Py-ART%20Usage%20plotting%20PPI%20data%20on%20a%20map%20and%20add%20a%20new%20field.ipynb

Lesson 3: Example Py-ART processing module, LP based phase proccessing
          http://nbviewer.ipython.org/github/EVS-ATMOS/pyart_short_course/blob/master/3%20Using%20LP%20to%20retrieve%20propigation%20phase%20from%20polarmetric%20phase%20shift.ipynb

Lesson 4: Mapping multiple radars onto a grid and visualizing
          http://nbviewer.ipython.org/github/EVS-ATMOS/pyart_short_course/blob/master/4%20Gridding%20multiple%20NEXRAD%20to%20a%20mesh.ipynb

Bonus 1: CHILL RHIs of Co Supercell
         http://nbviewer.ipython.org/github/EVS-ATMOS/pyart_short_course/blob/master/Bonus%201%2C%20CHILL%20RHI.ipynb


Practical Py-ART 2
------------------

TBD


Python Tools
------------

Overview::

    - Brief history and background

    - Development paradigm

    - Package structure and modules

    - ODIM_H5: the OPERA Data Information Model for use with the HDF5 file format

    - How to contribute

Examples::

    - Read polar data and see how they're represented

    - Quality controls and the quality management infrastructure

    - Processing a lot of data at once

    - Generating composites/mosaics

Wrapup
------

In this final exercise, we will demonstrate pairwise interaction between the presented OSS tools.

We will show how BALRAD and Py_ART can directly eschange data in a Python environment::

   @Scott, Daniel and Jonathan: Please outline the Py-ART + BALTRAD interaction.


We will show how BALTRAD and wradlib can exchange data via ODIM_H5 files::

   - a polar volume from Suergavere (Estland) will be processed using BALTRAD's odx_toolbox

   - the result will be read, georeferenced and presented by wradlib

   - processing alternatives might be tested using wradlib's own processing capabilities



Feedback round
--------------

We will discuss, together with the participants, the perspectives for using OSS software in different institutional environments.
Participants are invited to feedback on their impression of the presented OSS tools and whether these tools are an option
for their future activities.

