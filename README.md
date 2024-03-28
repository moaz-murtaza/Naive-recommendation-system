# NAIVE-RECOMMENDATION-SYSTEM

This repository contains the Naive recommendation system which is a search engine based on the MapReduce Technology. Based on the data obtained from the portion of english wikipedia dump of 5 million wikipedia articles provided by wikimedia.The MapReducers are being used for the task of preprocessing , one for determining the word count , one for assigning a unique count for each word, one for the normalization of the words across the documents (ensures that words are represented consistently across documents, regardless of their frequency.), and one for the Query processing which uses the output from the previous mapreducers as an input.

**DEPENDENCIES**

The **sys** and **string** are the modules of python standard libaray and donot require additional installations.

 # MAPPER AND REDUCER 1 EPLAINATION (Generating keys for each word)

The first mapper reducer are for the preprocessing of the text to be used for the text analysis task.

 **PURPOSE(MAPPER)**
	
The first mapper function is a part of the data preprocessing phase in the naive recommendation system it processes the imput data, extracts relevant information , and outputs the key-value pairs to be futhur processed by the reducer.

**DESCRIPTION**

This mapper function reads the input data from the standard input line by line as each line represents a record or entry in the dataset seperated by commas. For a line containing less than four columns it is considered invalid and is skipped. The valid lines of the dataset the function extracts the text from the third index converts it into lowercase , removes the punctuation using the 'string.translate' method and splits them into induvidual words which are then emitted as key-value pairs where the word serves as the key and the value is set to '1' to denote the occurance

**OUTPUT(Mapper)**

The output for this mapper would be a series of lines , each containing a word followed by the tab character and the number indicating the word count of the occurrances.

For Example : 

Hello	1 

Book	1

Hello	1

Stamp	1

Each line represents the word and the number of times it is repeated in the input data .

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

**OUTPUT(reducer)**

1.The reducer initializes the variables while keeping in track of the current word being processed and its respective count by iterating over each line from the standard input.

2.For each line it splits the word and the count .

3.If the current word is same as the previous one the count is incremented 

4. If a certain new word is added it updates the vocabulary with the word and its count

5. The end output is the printing of the vocabulary with each word and its corresponding index .

The output for this reducer essentially provides each unique word and its coressponding index in the vocabulary.


# MAPPER AND REDUCER 2 EXPLAINATION (Generating tuples (Word(number), count)) : 

**PURPOSE(mapper2)**

This mapper function is tailored to transform raw text data into structured feature vectors , facilitating the downstream tasks like document analysis or classification .It processes the input data by mapping the words to their respective corressponding numerical codes based on a predefined codebook.

**DESCRIPTION**

_LOAD_CODES_FUNCTION:_ 

This function loads the codebook file containing the word-code mappings each line basically consists of a numerical code followed by its corressponfing word seperated by a delimiter (tab). It parses each line in the file to extract the word-code pairs and stores them in a dictionary.

_MAPPER_FUNCTION:_

This function also begins with the loading of the codebook using the load_codes function then by iterating over each line of data it process each line to extarct the words from the fourth column , lowercase them , removes the punctuation and splits them into induvidual words. Then a dictionary is initialized which represents the articles feature vectors , with the keys as numerical codes form the codebook and the values are initialized to 0.

For each word in the processed line the function retrieves the numerical code responding to the word from the codebook. If the word exists in the codebook then it increments the count for the corresponding code in the article's feature vector.

The outputs include the key-value pairs where the key is the article id (which is extracted from the first column of the input), and the value is the articles feature vector represented as the dictionary.

**USAGE**

The input data is usually provided in a structured format such as a csv or a json file with each line representing a distinct record (e.g article). 

The users need to ensure that the input data adheres to the expected format and that the codebook file contains appropriate mapping for efficient word encoding.

**OUTPUT(mapper2)**

The output for the mapper consists of the key-va;ue pairs where each key represents the article-id and value reprents the feature vector associated with the article . Feature vector represents the frequency of each word in the article.


**PURPOSE(reducer2)**

This reducer aims to consolidate the counts associated with the each article id and prints the aggregated counts for each article.

**DESCRIPTION**

_1.INITIALIZATION:_

There are two main variables **currrent article ** which stores the id of the current article being processed and the **current_counts** which is a dictionary that holds the counts associated with the current article.

_2.INPUT_PROCESSING :_

The reducer iterates over each line of the input as each line represents the article id followed by its associated counts , delimited by a curly bracket '{'. This reducer script splits each line to extract the article id and its corressponding counts.

_3.COUNT_AGGREGATION:_

For every line of input, the script constructs a dictionary named 'counts' to store the counts associated with the current article. It parses the counts string to extract the induvidual code-count pairs , delimited by commas and spaces. Each pair is then split into similar code and count components , both converted to integers . Then the script updates the **"current_counts"** dictionary with the counts extracted for thr current article. If the **current article id** matches the previous one , then the counts are aggregated by updation of the corresponding counts in the **current_counts** dictionary . Similarly if the current article id is different from the the previous one then it prints the aggregated counts for the previous articles and the updates the **current_article** and the **current_counts** with the new article ids and counts repspectively.


**OUTPUT**

After the processing of the input data , the reducer prints the aggregated counts for the last article . Then it calls the print_tuples function to print the article id followed by the non-zero count pairs in the format **(code. count)**.

**USAGE**

This reducer expects the input data in the format generated by mapper functions , where each line represents an article id followed by its associated counts. The users can run the reducer after the mapper phase to aggregate the counts and generate output for furthur analysis.


# MAPPER AND REDUCER 3 EXPLAINATION (Calculating Idf/Df): 









