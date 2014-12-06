Team-2
======

## KDD Cup 2012 Track 2
This repo contains code for creating models to solve the KDD Cup 2012 Track 2 competition. The competition page can be found [here](https://www.kddcup2012.org/c/kddcup2012-track2).

The full report can be found at Team-2/report/final_report.pdf.

## Local data preparation
1. create_local_data.py ARG0 ARG1 ARG2
  * Randomly samples ARG2 lines from file ARG0 and places them in fle ARG1

## Preparing data on Hadoop Elastic Map Reduce, training model, predicting

1. Join instances and query tokens on queryID

  * Mapper: join query mapper.py

  * Reducer:join query reducer.py

  * Input: training.txt, queryid tokensid.txt 
  
  * Output: join query out/

  * Output format: clicks impressions ... query tokens 

  * EMR:
  -files s3://stat157-uq85def/home/kevinshieh/code/join_query_mapper.py,
  s3://stat157-uq85def/home/kevinshieh/code/join_query_reducer.py
  -mapper join_query_mapper.py -reducer join_query_reducer.py
  -input s3://stat157-uq85def/shared/track2/training.txt,
  s3://stat157-uq85def/shared/track2/queryid_tokensid.txt
  -output s3://stat157-uq85def/home/kevinshieh/join_query_out
  
2. Join query-joined instances and title tokens on titleID 

  * Mapper: join title mapper.py

  * Reducer:join title reducer.py

  * Input: titleid tokensid.txt, join query out/ 
  
  * Output: join query title out/

  * Output format: clicks impressions ... query tokens title tokens 

  * EMR:
  -files s3://stat157-uq85def/home/kevinshieh/code/join_feature_mapper.py,
  s3://stat157-uq85def/home/kevinshieh/code/join_feature_reducer.py
  -mapper join_feature_mapper.py -reducer join_feature_reducer.py
  -input s3://stat157-uq85def/shared/track2/titleid_tokensid.txt,
  s3://stat157-uq85def/home/kevinshieh/join_query_out/part*
  -output s3://stat157-uq85def/home/kevinshieh/join_query_title_out/
  
3. Calculate similarity ratio

  * Mapper: similarity mapper.py

  * Reducer:similarity reducer.py

  * Input: join query title out/

  * Output: similarity title out/

  * Output format: clicks impressions similarity ratio 

  * EMR:
  -files s3://stat157-uq85def/home/kevinshieh/code/similarity_mapper.py,
  s3://stat157-uq85def/home/kevinshieh/code/similarity_reducer.py
  -mapper similarity_mapper.py -reducer similarity_reducer.py
  -input s3://stat157-uq85def/home/kevinshieh/join_query_title_out/part*
  -output s3://stat157-uq85def/home/kevinshieh/similarity_title_out/
  
4. Label instances to split into train, validation, and test sets 

  * Mapper: label data mapper.py

  * Reducer:label data reducer.py

  * Input: similarity title out/

  * Output: similarity title labeled out/

  * Output format: train clicks impressions similarity ratio 

  * EMR:
  -files s3://stat157-uq85def/home/kevinshieh/code/label_data_mapper.py,
  s3://stat157-uq85def/home/kevinshieh/code/label_data_reducer.py
  -mapper label_data_mapper.py -reducer label_data_reducer.py
  -input s3://stat157-uq85def/home/kevinshieh/similarity_title_out/part*
  -output s3://stat157-uq85def/home/kevinshieh/similarity_title_labeled_out/
  
5. Separate instances into train, validation, and test directories 

  * Mapper: separate train mapper.py 
  
  * Reducer:label data reducer.py

  * Input: similarity title labeled out/

  * Output: title train

  * Output format: train clicks impressions similarity ratio 

  * EMR:
  -files s3://stat157-uq85def/home/kevinshieh/code/separate_train_mapper.py,
  s3://stat157-uq85def/home/kevinshieh/code/label_data_reducer.py
  -mapper separate_train_mapper.py -reducer label_data_reducer.py
  -input s3://stat157-uq85def/home/kevinshieh/similarity_title_labeled_out/par
  -output s3://stat157-uq85def/home/kevinshieh/title_train/
  
6. Group instances on similarity ratio into 0.1 width buckets 

  * Mapper: group by rate mapper.py 

  * Reducer:group by rate reducer.py

  * Input: title train

  * Output: groupby title

  * Output format: similarity ratio clicks impressions 

  * EMR:
  -files s3://stat157-uq85def/home/kevinshieh/code/group_by_rate_mapper.py,
  s3://stat157-uq85def/home/kevinshieh/code/group_by_rate_reducer.py
  -mapper group_by_rate_mapper.py -reducer group_by_rate_reducer.py
  -input s3://stat157-uq85def/home/kevinshieh/title_train/part*
  -output s3://stat157-uq85def/home/kevinshieh/groupby_title/
  
7. simple combine.py

  * Input: groupby title

  * Output: final title.txt

  * Because the output in groupby title was split into multiple files, I needed to simply merge them into a single file.

8. simple model.py

  * Input: title train.txt, title test.txt

  * This is where I train the Naive Bayes model using title train.txt and test the model classifica- tion by feeding in some validation or test data. Here, I modeled my Bernoulli Naive Bayes by using the equations mentioned above in the ”Models” section. I test the test set here and calculate the AUC here.
