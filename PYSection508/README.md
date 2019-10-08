# PYSection508
Scripts to Make PDF files Section 508 Compliant

The goal of this project is to use Python tools to make PDF files Section 508 Compliant. 
This is a work in progress.

## Dependencies
* Python 3
* pdfrw

## Objectives

### Audit files
PDFAudit.py displays current info about all documents in the folder 'files'.
PDFAuditFix.py displays current info about all documents in the folder 'files' and offers to fix issues. 

#### ToDo: 
1. In PDFAuditFix, need to be able to fix title or lang if it is not none. 

### Individual Fixes
Referance scripts to solve individual Section 508 Compliant issues. 

#### Add a title the the document
PDFfixtitle.py modifys all documents in the folder 'files' to the same title.
* Note: Need to edit the variable 'title' before you run.

#### Add a lang tag to the document
PDFfixlang.py adds the 'en-US' to the Lang tag. 
* Note: If the language is not english, then edit the script before you run.

#### Add tagging
PDFfixMark.py adds 'Marked = true' this a possable soltion to the issue of PDFs not tagged. 

This does not change anything in the document except the meta data. After using this method for PDF docs, are the documents 508 compliant for tagging or is this just a loop hole to trick the scanner?

http://www.w3.org/TR/WCAG20/#content-structure-separation-programmatic

#### Add Alt Tags to images
ToDo: 
Need a script that will add alt tags images in a PDF document. No soltion yet. 
