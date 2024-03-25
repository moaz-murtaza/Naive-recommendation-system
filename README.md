# NAIVE-RECOMMENDATION-SYSTEM

This repository contains the Naive recommendation system which is a search engine based on the MapReduce Technology. Based on the data obtained from the portion of english wikipedia dump of 5 million wikipedia articles provided by wikimedia.The MapReducers are being used for the task of preprocessing , one for determining the word count , one for assigning a unique count for each word, one for the normalization of the words across the documents (ensures that words are represented consistently across documents, regardless of their frequency.), and one for the Query processing which uses the output from the previous mapreducers as an input.

**DEPENDENCIES**

The **sys** and **string** are the modules of python standard libaray and donot require additional installations.

 # MAPPER AND REDUCER 1 EPLAINATION (INDEXER -SEO(search engine optimization))

The first mapper reducer are for the preprocessing of the text to be used for the text analysis task.

 **PURPOSE(MAPPER)**
	
The first mapper function is a part of the data preprocessing phase in the naive recommendation system it processes the imput data, extracts relevant information , and outputs the key-value pairs to be futhur processed by the reducer.

**DESCRIPTION**

This mapper function reads the input data from the standard input line by line as each line represents a record or entry in the dataset seperated by commas. For a line containing less than four columns it is considered invalid and is skipped. The valid lines of the dataset the function extracts the text fron the third inde converts it into lowercase , removes the punctuation using the 'string.translate' method and splits them into induvidual words which are then emitted as key-value pairs where the word serves as the key and the value is set to '1' to denote the occurance

**PURPOSE(REDUCER)**

The reducer for the above mapper aggregates the key-value pairs emitted by the mapper function and performs intermediate data processing and generates the final output. 

**DESCRIPTION**

Reducer function reads the key-value pairs and aggregated the occurrences of the same word and assigns a unique index to each word encountered creating a voacbulary. Which then outputs the index word pairs for which the index serves as the identifier. 

**KEY-COMPONENTS**

_1.Current-word and word-count:_
   Current word stores the word being processed and the word count stores the cumulative count of the occurances for the current word.
			
_2.Vocabulary Dictionary:_
   stores the unique words encountered along with their coressponding indices and the index is incrementally assigned as the word are encountered.
		
_3.Input Processing:_
   The word and the count are extracted from the tab seperated key-value pairs. The count is also converted to an integer for the numerical operations.

_4.Aggregation and Vocabulary-creation:_
   If the current word matches the previous word the count is added to the cumulative count for that word. as a new word is encountered it becomes the comulative count and is added to the vocabulary dictionary with a unique index.

**USAGE**
  This reducer function is designed to be used in conjunction with a mapper function in the mapreduce which is suitable for the tasks related to vocabulary creation and feature extraction as an indexer for the search engine optimization.



