# NAIVE-RECOMMENDATION-SYSTEM

This repository contains the Naive recommendation system which is a search engine based on the MapReduce Technology. Based on the data obtained from the portion of english wikipedia dump of 5 million wikipedia articles provided by wikimedia.The MapReducers are being used for the task of preprocessing , one for determining the word count , one for assigning a unique count for each word, one for the normalization of the words across the documents (ensures that words are represented consistently across documents, regardless of their frequency.), and one for the Query processing which uses the output from the previous mapreducers as an input.

**DEPENDENCIES**

The **sys** and **string** are the modules of python standard libaray and donot require additional installations.

**MAPPER AND REDUCER 1 EPLAINATION**

The first mapper reducer are for the preprocessing of the text to be used for the text analysis task.

#PURPOSE(MAPPER)
The first mapper function is a part of the data preprocessing phase in the naive recommendation system it processes the imput data, extracts relevant information , and outputs the key-value pairs to be futhur processed by the reducer.

#DESCRIPTION 
This mapper function reads the input data from the standard input line by line as each line represents a record or entry in the dataset seperated by commas. For a line containing less than four columns it is considered invalid and is skipped. The valid lines of the dataset the function extracts the text fron the third inde converts it into lowercase , removes the punctuation using the 'string.translate' method and splits them into induvidual words which are then emitted as key-value pairs where the word serves as the key and the value is set to '1' to denote the occurance


