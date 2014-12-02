### CREATING LOCAL RUNNABLE DATA ###
touch NEW_FILE_NAME.txt
python create_local_data ORIGINAL.txt NEW_FILE_NAME.txt SIZE_OF_LOCAL_DATA


### JOINING INSTANCES AND DETAILS ON FEATURE_ID AS KEY ###

cat training.txt FEATURE.txt > COMBINED_FILE.txt
cat COMBINED_FILE | python join_FEATURE_mapper.py | sort -k1 > inter_FEATURE.txt
cat iter_FEATURE.txt | python join_FEATURE_reducer.py > final_FEATURE.txt
