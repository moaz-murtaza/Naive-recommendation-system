
**Moaz_Murtaza 22I-1902**

**Bilal_Bashir 22I-1901**

**Alizeh_Qamar 21I-1775**



# NAIVE-RECOMMENDATION-SYSTEM

This repository contains the Naive recommendation system which is a search engine based on the MapReduce Technology. Based on the data obtained from the portion of english wikipedia dump of 5 million wikipedia articles provided by wikimedia.The MapReducers are being used for the task of preprocessing , one for determining the word count , one for assigning a unique count for each word, one for the normalization of the words across the documents (ensures that words are represented consistently across documents, regardless of their frequency.), and one for the Query processing which uses the output from the previous mapreducers as an input.

**DEPENDENCIES**

The **sys** and **string** are the modules of python standard libaray and donot require additional installations.


# MAPPER AND REDUCER 1 EXPLAINATION (Generating tuples (Word(number), count)) : 

**PURPOSE(mapper1)**

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

**OUTPUT(mapper1)**

The output for the mapper consists of the key-va;ue pairs where each key represents the article-id and value reprents the feature vector associated with the article . Feature vector represents the frequency of each word in the article.


**PURPOSE(reducer1)**

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

**Sample Output**
0	
(28055, 1)	
(201876, 2)	
(389676, 1)	
(44918, 1)	
(58532, 1)	
(459954, 1)	
(780879, 3)	
(168983, 1)	
(894543, 1)	
(408607, 1)	
(476114, 1)	
(607508, 1)	
(347684, 1)	
(597446, 1)	
(40408, 1)	
(400688, 1)	
(847989, 1)	
(352983, 1)	
(611740, 1)	
(959039, 1)	
(626577, 1)	
(629233, 1)	
(28598, 1)	
(519358, 1)	
(937712, 1)	
(133187, 1)	
(139972, 1)	
(489355, 1)	
(551812, 1)	
(971355, 1)	
(367027, 1)	

**USAGE**

This reducer expects the input data in the format generated by mapper functions , where each line represents an article id followed by its associated counts. The users can run the reducer after the mapper phase to aggregate the counts and generate output for furthur analysis.


# MAPPER AND REDUCER 2 EXPLAINATION (Calculating Idf/Df): 

**PURPOSE(mapper2)**

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

**PURPOSE(reducer2)**

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

**OUTPUT(reducer2)**

Reducer prints the normalized counts for each article to the standard output stream . Each line of the output includes the article_id followed by the normalized counts of the terms associated with the article , formatted as pairs of term codes and their corresponding normalized_counts. 

**Final Output Sample:**

**10000**	(182163:0.000888494002665482), (47759:0.0017730496453900709), (402034:0.023255813953488372), (273206:0.004555808656036446), (293909:0.011235955056179775), (941196:0.02040816326530612), (334466:0.014925373134328358), (455196:0.0006140620202640467), (384896:0.04), (912442:0.02702702702702703), (82678:0.0006374840628984276), (76706:0.3333333333333333), (42055:0.5), (248222:0.041666666666666664), (427704:0.3333333333333333), (691500:0.017241379310344827), (3095:0.08333333333333333), (160695:0.010309278350515464), (221560:0.006060606060606061), (556513:0.0010604453870625664), (99912:0.2), (495372:0.001049097775912715), (140169:0.0136986301369863), (705838:0.001876172607879925), (234870:0.0007577192650123129), (428269:0.10526315789473684), (260779:0.043478260869565216), (300844:0.02631578947368421), (873628:2.0), (962980:5.0), (613394:0.14285714285714285), (377697:0.001903311762466692), (646365:0.0016313213703099511), (628106:0.005376344086021506), (67629:0.004901960784313725), (439461:0.045454545454545456), (853798:0.00423728813559322), (125451:0.0031847133757961785), (489373:0.0008227067050596463), (685975:0.5), (143185:0.0003621876131836291), (238145:0.0625), (415959:0.004694835680751174), (946865:0.008), (644474:0.009433962264150943), (36558:0.0025), (657013:0.25), (561757:0.00089126559714795), (88057:0.006896551724137931), (281984:0.00030665440049064706), (525710:0.3333333333333333), (384375:0.038461538461538464), (630709:0.021739130434782608), (499076:0.010526315789473684), (16379:1.0), (583745:0.02040816326530612), (870536:0.0002937720329024677), (769854:0.003861003861003861), (129353:0.0196078431372549), (119105:0.005813953488372093), (729844:0.006711409395973154), (141016:0.005376344086021506), (201777:0.023809523809523808), (900580:0.04), (218678:0.0047169811320754715), (712206:0.14285714285714285), (405248:0.009615384615384616), (257365:0.0003795066413662239), (470319:0.017241379310344827), (313528:0.16666666666666666), (210559:0.015873015873015872), (928499:0.5), (541417:0.14285714285714285), (512061:0.3333333333333333), (373278:0.00558659217877095), (613773:0.03571428571428571), (426920:0.09090909090909091), (763521:0.0004950495049504951), (616054:0.1), (197684:0.00980392156862745), (460583:0.03225806451612903), (898858:0.05555555555555555), (750196:0.1), (813959:0.1111111111111111), (745850:0.0003401360544217687), (63622:0.01639344262295082), (760505:0.0003248862897985705), (180238:0.03125), (293470:0.00023894862604540023), (520730:0.0625), (473273:0.0625), (255518:0.00641025641025641), (713850:0.0009216589861751152), (146187:0.003134796238244514), (785460:0.14285714285714285), (197773:0.0004476275738585497), (51610:0.0072992700729927005)
**10001**	(218850:0.007633587786259542), (788245:0.06666666666666667), (45234:0.25), (455196:0.00030703101013202335), (676361:0.25), (818203:0.25), (342841:0.5), (50853:0.009174311926605505), (103117:0.019230769230769232), (257365:0.0007590132827324478), (735793:0.04), (120558:0.011904761904761904), (281984:0.0006133088009812941), (47759:0.0017730496453900709), (191964:0.037037037037037035), (234870:0.00018942981625307822), (50097:0.02702702702702703), (822835:0.037037037037037035), (929044:0.011764705882352941), (622030:0.0037593984962406013), (556513:0.0007069635913750442), (888796:0.125), (867204:0.3333333333333333), (495372:0.000209819555182543), (783668:0.25), (129229:0.005434782608695652), (197773:0.0004476275738585497), (817482:0.007692307692307693), (471944:0.01818181818181818)

**USAGE**

The reducer function is a crucial component in the data processing pipeline designed to calculate IDF/DF for terms in a corpus of articles . Users can execute the reducer function after the mapper phase to aggregate the term counts across articles and calculate the normalized counts required for IDF/DF computation.

# MAPPER AND REDUCER 3 (Storing Df_counts)

**PURPOSE(mapper3)**

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

**PURPOSE(reducer 3)**

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

**Final Output Sample**

182163	4502
47759	564
402034	86
273206	439
293909	89
941196	49
334466	67
455196	3257
384896	25
912442	37
82678	4706
76706	3
42055	2
248222	24
427704	3
691500	116
3095	12
160695	97
221560	165
556513	2829
99912	5
495372	4766
140169	73
705838	533
234870	5279
428269	19
260779	23
300844	38
873628	1
962980	1
613394	7
377697	2627
646365	613
628106	186
67629	204

# MAPPER AND REDUCER 4 (Running Queries) 

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

**A SMALL FINAL OUTPUT AFTER RUNNING THE QUERIES**

Article : 10082	 Relevance : 0.0002227667631989307
Article : 10198	 Relevance : 0.04000000000000001
Article : 10226	 Relevance : 0.0004455335263978614
Article : 10312	 Relevance : 0.0002227667631989307
Article : 10359	 Relevance : 0.0002227667631989307
Article : 10415	 Relevance : 0.25
Article : 10420	 Relevance : 0.0002227667631989307
Article : 10761	 Relevance : 0.0002227667631989307
Article : 10830	 Relevance : 5.0
Article : 10863	 Relevance : 0.012345679012345678
Article : 10979	 Relevance : 0.0004455335263978614
Article : 11011	 Relevance : 0.0002227667631989307
Article : 11018	 Relevance : 0.0002227667631989307
Article : 1129	  Relevance : 0.015625
Article : 11348	 Relevance : 0.0002227667631989307
Article : 11371	 Relevance : 0.0004455335263978614
Article : 11379	 Relevance : 0.0002227667631989307
Article : 1154	  Relevance : 0.04081632653061224
Article : 11572	 Relevance : 0.04000000000000001
Article : 11583	 Relevance : 0.012345679012345678

**Output-Explaination**

Each line in the output corresponds to an article and its associated relevance score.The relevance score indicates how relevant each article is for a recommendation.The article numbers (e.g., Article 10830, Article 10415) likely correspond to unique identifiers for different articles.The relevance scores are floating-point numbers, suggesting some form of calculation or ranking. Higher relevance scores indicate greater suitability for recommendation.

Based on these relevance scores, the recommendation system could:

-Recommend Article 10830 as a top choice.

-Consider Article 11415 as a secondary recommendation.

-Likely exclude Article 11348, Article 10420, and Article 11379 etc due to their low relevance.



# CONTRIBUTORS

This project was possible only because of the extraordinary people who contributed to it : 

>[ moaz-murtaza](https://github.com/moaz-murtaza) (i221902@nu.edu.pk)
 
>[ bilalbashir08](https://github.com/bilalbashir08) (i221901@nu.edu.pk)

>[Alizeh21](https://github.com/Alizeh21) (i211775@nu.edu.pk)
