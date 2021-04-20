# Simpler Discourse
*A Python library for simplifying discourse tasks by Sean Steinle, Nolan Weinlader, and Brandon Kowalecki*

### What is Simpler Discourse?

Simpler Discourse is our term project for CS1699: AI Ethics. For our project, we wanted to simplify how
discourse data is used and visualized. To this end, we've begun this library to represent discourse relations
more elegantly in code.

### How It Works

As of now, our project is only two main classes, a test method, and a tutorial notebook. These classes
*DiscourseLoader.py* and *DiscourseUnit.py* load the PDTB3 corpus and represent its objects respectively.
Each DiscourseUnit corresponds to one line of PDTB labels, but it can access other relevant data such as
wider context to its relation.

### Current Status and Future Development

As of now, we only support the PDTB3 corpus. We chose to prioritize this corpus over others because there has been
no data engineering development for this corpus. In the future, we hope to develop more tools for the PDTB3 as well as to
expand to older corpora like the PDTB2 and other types of discourse corpora that use RST.

Our top priority right now is getting PDTB3 onto PyPI so that more people can access it. After that, we'll look to add more fields
of data from the raw PDTB3 files, and then we'll look to improve visualization outlets.

### How to Run

To run this library, simply clone this directory and import the two class files into your Python script or Jupyter Notebook.
In the future, you will be able to run *pip install Simpler-Discourse*.

### Acknowledgements

We'd like to thank our TA Kate Atwell, Mert Inan, and our professor Malihe Alikhani for helping to guide our development.