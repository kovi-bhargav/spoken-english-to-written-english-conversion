# spoken-english-to-written-english-conversion
spoken english to written english conversion 
This is the extension to the below git hub implementation  
https://github.com/vishaldhiman28/Spoken-To-Written-English/blob/master/spoken2written/sp2wr.py  As an entension, the current repository has the demonistration for extending to any future rule ( phrase deconstruction has been implemented here)

The following things will be taken care:

1) "two dollars" will be converted to $2. Abbreviations spoken as "C M" or "Triple A" will be written as "CM" and "AAA" respectively. 
2) Deconstruction of the phrases "won't" to "will not" etc.,

Example of the input and output to the model 

[IN]
Hi! This is Hero I acted in 7 movies and i start my day at 5 A M. my remuneration is hundred dollars per day .My contact number contains double 5, quadruple 8, single 9 and triple 4 and I won't take alcohol.

[OUT]:
  
  Hi! This is Hero I acted in 7 movies and i start my day at 5 A M. my remuneration is $100 per day. My contact number contains 55, 8888, 9 and 444 and I will not take alcohol.
  
  The System has the facility to incorporate any future rules easily, with out having the dependecy on the entire system.
