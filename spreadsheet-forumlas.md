# Spreadsheet formulas 

## December 2018

For analysis of text and content inside a spreadsheet, and the requirements of the text 
analysis project don't allow any outside tools, there are formulas that can help to
analyse content:

	- ``IF`` formulas to determine if a item is greater or less than a value 
	- ``ISNUMBER``, and ``SEARCH`` formulas to check if information inside a cell contains a keyword or items 
	- ``SUMPRODUCT`` formulas to identify if a cell contains multiple keywords or items

I made use of these formulas to analyse a block of survey feedback for a list of keywords that 
indicate a positive or negative response.

Comparing a number response (similar to a net promoter score) with a semantic, verbal response with 
the ``TTEST`` formula. 

The ``IF`` formula with the greater than function returns a 1 or 0 value if the
score out of 10 was greater than or equal to 8, or less than 8 respectively..

Resources:
[Excel Jet article 1](https://exceljet.net/formula/categorize-text-with-keywords)
[Excel Jet article 2](https://exceljet.net/formula/cell-contains-one-of-many-things)
[Excel Jet article 3](https://exceljet.net/formula/count-keywords-cell-contains)
[Excel Jet article 4](https://exceljet.net/formula/if-cell-is-greater-than)
[TTest](https://support.google.com/docs/answer/6055837)
[Solving the #DIV/0! error](https://support.office.com/en-us/article/how-to-correct-a-div-0-error-3a5a18a9-8d80-4ebb-a908-39e759a009a5)

