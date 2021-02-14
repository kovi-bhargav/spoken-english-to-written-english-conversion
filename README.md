# spoken-english-to-written-english-conversion
spoken english to written english conversion 
This is the extension to the below git hub implementation  
https://github.com/vishaldhiman28/Spoken-To-Written-English/blob/master/spoken2written/sp2wr.py  As an entension, the current repository has the demonistration for extending to any future rule (  'preprocess_text' function can be extended to apply any future rule on the complete sentence, ex : phrase deconstruction and removing the tabs and new line characters has been implemented here)

# The following things will be taken care:

1) "two dollars" will be converted to $2. Abbreviations spoken as "C M" or "Triple A" will be written as "CM" and "AAA" respectively. 
2) Removing the tabs and new lines and deconstruction of the phrases "won't" to "will not" etc., has been implemented. Similarly any rule can be easily added to 'preprocess_text' function and if we thouroughly test 'preprocess_text' function it will be enough.

Example of the input and output to the model 
  

[IN]:Enter Your paragraph of spoken english:

"Hi! This is Hero I acted in 7 movies and i start my day at 5 A M. my remuneration is hundred dollars per day .My contact number contains double 5, quadruple 8, single 9 and triple 4 and I won't             take alcohol. "

[OUT]:The input Spoken English Paragraph: 

The input Spoken English Paragraph: 

"Hi! This is Hero I acted in 7 movies and i start my day at 5 A M. my remuneration is hundred dollars per day .My contact number contains double 5, quadruple 8, single 9 and triple 4 and I won't             take alcohol. "

Converted Written English Paragraph: 
  
  Hi! This is Hero I acted in 7 movies and i start my day at 5 A M. my remuneration is $100 per day. My contact number contains 55, 8888, 9 and 444 and I will not take alcohol.
  
# Future Implemetations can be :

1) If the paragraph contains a money figure e.g. two million three thousand nine hundred and eighty-four then we may convert it to numbers as 2003984.

2) Handling of both American number system and Indian number system e.g. million, lakhs.

3) Handling of Dates e.g. Today's Date is twenty-eight October two thousand twenty as Today's Date is 28-10-2020/2020-10-28.
