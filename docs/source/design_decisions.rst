.. _designdecisions:

Design decisions
================

This section covers any design decisions that were consciously made.

enlp.processing
---------------
For the functions contained within the processing module, in general the output, i.e., processed text, is returned as
a string. This is to allow for the output to be directly passed into another function, allowing the stringing
together of functions to build a processing pipeline.