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

**PURPOSE(mapper3)**

This mapper function serves to process the input data , specifically structured to handle information related to the articles and aggregates the counts associated with each article id . This Aggregation is essential for understanding the frequency of specific terms within the articles. Additionally it also can be utilized in the context of calculating the idf(inverse document frequency) or Df(Document Frequency).

**DESCRIPTION**

_1.INITIALIZATION:_

Here too as in the previous mapper first two variables are initialized one named **'current_atricle'** which tracks the current article id being processed and **'current_counts'** which is a dictionary that is used to store the counts associated with the current article.

_2.INPUT_PROCESSING:_

The mapper iterating over each line of the input systematically processes each line to extract the information.

_3.DETECTING_ARTICLE_BOUNDARIES:_

Each line is evaluated to determine if it represents the start pf a new article block . This detection is based on whether the line contains only digits which indicates an article id. On the other hand if a line represents a new article then the mapper prints the counts of the previous article (if any) and prepares to process the new article.

_4.PROCESSING_ARTICLE_COUNTS:_

The lines that are not article_ids are interpreted as tuples representing (code,count) pairs. The pairs represent the occurance of a particular code word or feature within the article. Then the lines are parsed by the mapper extracting the code and the count values from each tuple. The extracted counts are then accumulated in the **'current_counts'** dictionary, associating each code with its respective count for the current article.

**OUTPUT**

When the processing of the count has been completed for each article then the mapper function prints the aggregated counts for the article. The format of the output contains the article id with the associated counts formatted as strings of code-count pairs within the curly brackets.

**CALCULATING_IDF/DF**

In addition to aggregating the term frequencies , the mapper function plays a crucial role in the calculation of the IDF or DF values for terms in a collection of documements. IDF/DF values provide insights into the importance of the terms within a document collection . It is calculated as the logrithmically scaled inverse fraction of the number of documents in the collection.

This calculation of IDF/DF values is essential in document classification and information retrieval.

**USAGE**

The mapper function expects the input data in a specifix format tailored to the requirements where each line represents either an article Id or a code-count pair. The users can execute the mapper function as the part of the data processing pipeline to aggregate counts associated with each article Id. The aggregated data can then be utilized for various analytical tasks including the calculation of the IDF/DF values for the terms in a document collection.

**PURPOSE(reducer3)**

This reducer function aims to calculate the IDF/DF for each code in the collection of the articles. It helps to identify the terms that are rare or unique across the documents.

**DESCRIPTION**

_1.INITIALIZATION:_

Two main data structures are initiallized **'article_data'** a default dictionary to store the counts of each term (code) within the article . the outer dictionary is indexed by the article id and the inner dictionary stores the term counts the **'df-counts'** is also a default dict that stores the document frequency counts for each term , the keys represent terms (codes) , and the values represent the number of documents in which each term occurs .

_2.READING_INPUTS_

The reducer reads the input from the standard input stream which are generated by the mapper in the timeline. Each line represents the article id along with the count terms associated with the articles. The splitting of each line is also done to separate the article count form its associated counts.

_3.PARSING_COUNTS:_

The counts associated with each article are extracted and parsed . The counts are then represented as pairs of term codes and their corresponding frequencies. Each pair is split and the term code and the frequency are extracted and converted to integers.

These term frequencies are stored in the **'article_data'** which is a dictionary under the corresponding article_id. The DF counts for each of the term are updated in the **'df_counts'** dictionary.

_4.CALCULATING_IDF/DF:_

After the processing of all articles is done the reducer than claculates tge normalized counts for each term within the article . The normalization is performed by dividing the term frequency by the document frequency of the term across all the documents 

The normalized counts are calculated by the reducer using the formula : 

**normalized_count = term_frequency / document_frequency**

These normalized counts are then stored in a new dictionary **'normalized_counts'**

**OUTPUT(reducer3)**

Reducer prints the normalized counts for each article to the standard output stream . Each line of the output includes the article_id followed by the normalized counts of the terms associated with the article , formatted as pairs of term codes and their corresponding normalized_counts. 

**USAGE**

The reducer function is a crucial component in the data processing pipeline designed to calculate IDF/DF for terms in a corpus of articles . Users can execute the reducer function after the mapper phase to aggregate the term counts across articles and calculate the normalized counts required for IDF/DF computation.

# MAPPER AND REDUCER 4 (Storing Df_counts)

**PURPOSE(mapper4)**

This mapper function is designed to process input data and emit the key-value pairs as intermediate outputs , specifically geared towards storing document frequency counts for each term(code ) within a corpus of articles . the DF counts are essential for calculating the inverse Document Frequency (IDF) used in various text analysis and information retrieval tasks.

**DESCRIPTION**

_1.INITIALIZATION:_

The mapper initailizes the variables to keep the track of the current article being processed and a dictionaryto store the counts of each term within the current article.

_2.READING_INPUTS :_

The mapper also reads the input data from the standard input stream , ususally provided by a data source .

_3. PARSING_AND_AGGREGATING_COUNTS :_

Each line of input is stripped of leading / trailing whotespaces if the line consits of digits only , it signifies the start of a new article and the mapper at this point emits the counts of the previous articles  (if any) and initializes the current_article variable with the new article_id. On the other hand the mapper interprets each line as a tuple (code , count) where the code represents a term (code) identifier and 'count' represents its occurance count within the article. The counts are then aggregated in the 'current_counts' dictionary, with terms as keys and their respective counts as values . 

_4.EMITTING_INTERMEDIATE_OUTPUTS :_

After all the lines of the article habe been processed the mapper emits the article id along with the counts of the terms associated with the article . This emitted data is then formatted in the form of pairs of term codes with their coresponding counts , enclosed with in the curly brackets seperated with commas.

**USAGE**

This mapper serves as the cruicial step in the data processing pipeline for the calculation of the DF counts. User can use this mapper to process the input articles and generate intermediate outputs cotaining term counts , which are then aggregated to compute the DF counts in subsequent phases .

**OUTPUT**

The output of the mapper consists of intermediate key-value pairs representing the counts of terms (codes) within each article. Each line of output includes an article ID followed by the counts of terms associated with that article.

For example, an output line may look like this: article_id{code1:count1, code2:count2, ...}. 

Here, article_id denotes the unique identifier of the article, while code1, code2, etc., represent term codes found within the article along with their respective frequencies (count1, count2, etc.). This output format facilitates downstream processes, such as reducers, to aggregate and analyze term counts across articles for various text mining and information retrieval tasks.

**PURPOSE(reducer 4)**

This reducer function is responsible for aggregating term counts across articles emitted by the mapper and calculating the document frequency (DF) for each term (code) within the corpus of articles.


**DESCRIPTION**

_1.INITIALIZATION :_

Three main data structures have been initialized by the reducer here which include article_data which is a default dictionary with nested dictionaries to store term counts within each article , df_counts which is also a  default dictionary used to store the document frequency counts for each term ,  and  dictionary which stores the final document frequency counts for each term.

_2.READING_INPUTS :_

The reducer reads the input lines provided by the output of the mapper phase.Each line represents an article ID along with the counts of terms associated with that article .

_3. AGGREGATING_COUNTS_AND_CALCULATING_DOCUMENT_FREQUENCIES :_

The reducer iterates over each line of input and splits the article ID from its associated term counts.Term counts are extracted from each line and split into pairs of term codes and their corresponding frequencies.

For each pair, the reducer updates the article_data dictionary to store term counts within each article and increments the df_counts dictionary to calculate the document frequency for each term across all articles.

_4. Computing Final Document Frequencies :_

After the processing of all the articles, reducer iterates over the article_data dictionary to aggregate the document frequency counts for each term across all articles.These final document frequency counts are stored in the dictionary.

**OUTPUT**

The reducer prints the final document frequency counts for each term to the standard output stream. Each line of output contains a term code followed by its document frequency count, separated by a tab.

**USAGE**

This reducer function is a vital component in the data processing pipeline for calculating document frequency counts. Users can execute this reducer after the mapper phase to aggregate term counts across articles.

# MAPPER AND REDUCER 5 (Running Queries) 

**PURPOSE (mapper)**

This mapper function is designed to process input text data and convert it into a format suitable for query processing. It maps words in the input text to their corresponding codes, calculates their normalized counts based on Inverse Document Frequency (IDF), and emits intermediate key-value pairs for further processing.

**DESCRIPTION**

_1. LOADING_CODES_AND_IDF_VALUES :_

The mapper loads two important dictionaries  a **codes** dictionary mapping words to their corresponding codes. This is loaded from the output of a previous step, typically a dictionary generated during indexing  and **idf**  dictionary containing Inverse Document Frequency (IDF) values for each code. This is loaded from the output of another previous step, such as calculating IDF/DF counts.

_2. TOKENIZING_AND_MAPPING_WORDS :_

The mapper reads input text lines from the standard input stream .Each line is stripped of leading/trailing whitespace and converted to lowercase. Punctuation is removed from each line using string.punctuation.The line is split into individual words using split().

For each word, its corresponding code is retrieved from the codes dictionary.
If a code is found for the word, it is added to the article_dict along with a count of its occurrences within the text.

_3. CALCULAITNG_NORMALIZED_COUNTS :_

After processing all words in the input text, the mapper iterates over the article_dict.
For each code, it retrieves the corresponding IDF value from the idf dictionary.
If an IDF value is found and it's not equal to zero, the count of occurrences for that code is normalized by dividing it by the IDF value.
If no IDF value is found or if it's zero, the count remains unchanged.
The mapper emits intermediate key-value pairs in the format code\tnormalized_count for further processing.

**OUTPUT**

The output of this mapper consists of intermediate key-value pairs representing the normalized counts of terms (codes) within the input text data. Each line of output contains a term code followed by its corresponding normalized count. For example, a line of output may appear as follows: code1:normalized_count1, code2:normalized_count2, .... Here, code1, code2, etc., denote the unique identifiers (codes) associated with terms found in the input text, while normalized_count1, normalized_count2, etc., represent the normalized counts of occurrences for each term. These normalized counts are calculated based on the Inverse Document Frequency (IDF) values, adjusting for the significance of terms across the corpus of documents.

**USAGE**

This mapper function plays a crucial role in query processing tasks, where input text data needs to be converted into a format suitable for querying against an indexed corpus.
Users can execute this mapper as part of a query processing pipeline, where the output of this mapper serves as input for subsequent processing steps such as ranking or retrieval.


**PURPOSE(reducer)**

This reducer function is designed to calculate the relevance of each article to a given query based on pre-computed weights for each term (code) in the articles and the query. It performs a weighted sum of the weights of matching terms between the query and each article, thereby determining the relevance of each article to the query.


**DESCRIPTION**

_1. Loading Pre-computed Weights :_

The reducer first loads pre-computed weights for terms (codes) in the articles from an external file. These weights are typically computed during indexing or feature extraction and represent the significance of each term within each article.

The load_weights() function reads the weights from the specified file and stores them in a nested dictionary structure, where the outer dictionary maps article IDs to inner dictionaries containing term-weight pairs.

_2. Processing Input Query :_

The reducer reads input lines from the standard input stream, which typically contain term-weight pairs representing the query.
Each line is stripped of leading/trailing whitespace and split into a term code and its corresponding weight.
The term code and weight are stored in a query_dict defaultdict, which is used to represent the query.

_3. Calculating Relevance :_

After loading the weights for articles and processing the input query, the reducer iterates over each article's weights.

For each article, it calculates the relevance to the query by performing a weighted sum of the weights of matching terms between the query and the article.
The relevance is computed by multiplying the weight of each matching term in the query by the corresponding weight of the term in the article and summing up these products.

The resulting relevance score is printed for each article along with its ID, formatted as : 

**Article : article_id\t Relevance : relevance_score.**

**OUTPUT**

The output of this reducer function provides a comprehensive assessment of the relevance of each article to a given query in a search or recommendation system. Each line of output includes the unique identifier (ID) of an article along with its corresponding relevance score, which is calculated based on the weighted sum of matching terms between the query and the article. The relevance score quantifies the extent to which an article addresses the query's context and relevance. A higher relevance score indicates a stronger alignment between the article's content and the query, making it more likely to be relevant to the user's information needs. This output format enables users to evaluate and prioritize articles based on their relevance to the query, facilitating efficient information retrieval and decision-making processes. Additionally, users can seamlessly integrate this reducer function into their query processing pipelines to obtain relevance scores for articles dynamically, enhancing the overall effectiveness and usability of their search or recommendation systems.

**USAGE**

This reducer function plays a crucial role in determining the relevance of articles to a given query in a search or recommendation system.
Users can execute this reducer as part of a query processing pipeline, where the output of this reducer provides relevance scores for each article based on the input query.

**FINAL OUTPUT AFTER RUNNING THE QUERIES**

![Mapreduce 5](https://github.com/moaz-murtaza/Naive-recommendation-system/assets/157779652/ece4ee0c-256b-4802-b224-865d42550298)

**Output-Explaination**

Each line in the output corresponds to an article and its associated relevance score.The relevance score indicates how relevant each article is for a recommendation.The article numbers (e.g., Article 10, Article 11) likely correspond to unique identifiers for different articles.The relevance scores are floating-point numbers, suggesting some form of calculation or ranking.Higher relevance scores indicate greater suitability for recommendation.

Based on these relevance scores, the recommendation system could:

-Recommend Article 10 as a top choice.

-Consider Article 11 as a secondary recommendation.

-Likely exclude Article 12, Article 13, and Article 14 due to their low relevance.



# CONTRIBUTORs

This project was possible only because of the extraordinary people who contributed to it : 

> Moaz Murtaza(i221902@nu.edu.pk)

>Bilal Bashir (i221901@nu.edu.pk)








