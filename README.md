# spoken-english-to-written-english-conversion

This package facilitates the conversion of raw spoken english text to written english text. This package fulfills few cases. However, lot many cases still need to be included.

# Implemented cases:
1) This package will preprocess the text to decontract any "n't" suffix to "not" and "'re" suffix to "are" and "'s" suffix to "is" etc.,
2) This package will preprocess the text to remove any extra spaces or tabs or new line characters
3) This package will convert the words in the form of 'Triple A' to AAA etc.,
4) This package will replace the currecy names with symbols ( we can extend the currency dictionary )
5) This package can replace the abbrevations with their corresponding expansions as maintained in the abbrevations dictionary.

# Installation :
Please ensure that you have updated pip3 to the latest version before installing spoken2written.

You can install the module using Python Package Index using the below command.
```
>>python3 setup.py install
```

# Usage :

```
>>python3
 >>from spoken2written import sp2wr
 >>sp2wr.sp_to_wr()
 >>
 Enter Your paragraph of spoken english:
 
 The w h o wrote letter to P M O , to alert about the new vaccinne '     Triple H ' which isn't working as expected . 
 
Input:  The w h o wrote letter to P M O , to alert about the new vaccinne '     Triple H ' which isn't working as expected .
Output:  The World Health Organisation wrote letter to Prime Minister's Office , to alert about the new vaccinne ' Triple H ' which is not working as expected .
```
  
# Future Implemetations can be :

1) If the paragraph contains a money figure e.g. two million three thousand nine hundred and eighty-four then we may convert it to numbers as 2003984.

2) Handling of both American number system and Indian number system e.g. million, lakhs.

3) Handling of Dates e.g. Today's Date is twenty-eight October two thousand twenty as Today's Date is 28-10-2020/2020-10-28.

# Note :
It is pretty simple to extend this package. We just have to mention the function in the class as a method and call it in the driver. 
