Files

aggregate_reducer.py

create_local_data.py
    ### CREATING LOCAL RUNNABLE DATA ###
    touch NEW_FILE_NAME.txt
    python create_local_data ORIGINAL.txt NEW_FILE_NAME.txt SIZE_OF_LOCAL_DATA

join_title_mapper.py
    prepends instance lines with titleid key

join_title_reducer.py
    reduces lines to instance lines with title tokens appended

join_user_mapper.py
    prepends instance lines with userid key

join_title_reducer.py
    reduces lines to instance lines with user gender and age appended

merge_title_mapper.py
    creates input for join_title_mapper.py

merge_user_mapper.py
    creates input for join_user_mapper.py

merge_reducer.py
    trivial reducer

sklearn_quant.py
    quantitative models

sklearn_qual.py
    qualitative models

token_test.py
    eileen stuff

### JOINING INSTANCES AND DETAILS ON FEATURE_ID AS KEY ###

cat training.txt FEATURE.txt > COMBINED_FILE.txt
cat COMBINED_FILE | python join_FEATURE_mapper.py | sort -k1 > inter_FEATURE.txt
cat iter_FEATURE.txt | python join_FEATURE_reducer.py > final_FEATURE.txt
