# Machine Learning Nodes

## ML Feature Selection
- **Data Drift** `08-Machine-Learning/01-ML-Feature-Selection/data_drift.json` — This node calculates the Population Stability Index (PSI) for a set of features by comparing a reference dataset to a test dataset.
- **Feature Selection** `08-Machine-Learning/01-ML-Feature-Selection/feature-importance-python.json` — Compute per-feature importance for classification, regression, or clustering.
- **Feature Selection With Importance** `08-Machine-Learning/01-ML-Feature-Selection/feature-importance.json` — Produces Pass the input DataFrame to output and in table format feature importance is displayed.
- **Feature Selection With Correlation** `08-Machine-Learning/01-ML-Feature-Selection/feature-selection-with-correlation.json` — Produces Pass the input DataFrame to output and in table format correlation value between target and feature columns displayed.
- **Group By RFM Features** `08-Machine-Learning/01-ML-Feature-Selection/feature_eng_group_by_rfm.json` — This node computes feature engineering tasks such as group by, frequency, recency, average days between purchases, total value of purchases, and customer age.
- **Moving Average Features** `08-Machine-Learning/01-ML-Feature-Selection/feature_eng_moving_avg_feature.json` — This node computes various global moving average features from a DataFrame containing transactional data.
- **Time Series Features** `08-Machine-Learning/01-ML-Feature-Selection/feature_eng_time_Series.json` — This node computes various time-series related features from a DataFrame containing transactional data.

## FeatureScaler
- **Min Max Scaler** `08-Machine-Learning/02-ML-SparkML/02-FeatureScaler/MinMaxScaler.json` — MinMaxScaler transforms a dataset of Vector rows, rescaling each feature to a specific range (often [0, 1]).
- **Min Max Scaler Transform** `08-Machine-Learning/02-ML-SparkML/02-FeatureScaler/MinMaxScalerTransform.json` — MinMaxScaler transforms a dataset of Vector rows, rescaling each feature to a specific range (often [0, 1]).
- **Min Max Scaler Transform** `08-Machine-Learning/02-ML-SparkML/02-FeatureScaler/MinMaxScalerTransform_python.json` — MinMaxScaler transforms a dataset of Vector rows, rescaling each feature to a specific range (often [0, 1]).
- **Min Max Scaler** `08-Machine-Learning/02-ML-SparkML/02-FeatureScaler/MinMaxScaler_python.json` — MinMaxScaler transforms a dataset of Vector rows, rescaling each feature to a specific range (often [0, 1]).
- **Standard Scaler** `08-Machine-Learning/02-ML-SparkML/02-FeatureScaler/standardscaler.json` — StandardScaler transforms a dataset of Vector rows, normalizing each feature to have unit standard deviation and/or zero mean.
- **Standard Scaler Transform** `08-Machine-Learning/02-ML-SparkML/02-FeatureScaler/standardscaler_transform.json` — StandardScaler transforms a dataset of Vector rows, normalizing each feature to have unit standard deviation and/or zero mean.

## FeatureExtraction
- **Count Vectorizer** `08-Machine-Learning/02-ML-SparkML/03-FeatureExtraction/countvectorizer.json` — Extracts the vocabulary from a given collection of documents and generates a vector of token counts for each document.
- **Hashing TF** `08-Machine-Learning/02-ML-SparkML/03-FeatureExtraction/hashingtf.json` — Maps a sequence of terms to term frequencies using the hashing trick.
- **Markov Chain** `08-Machine-Learning/02-ML-SparkML/03-FeatureExtraction/markov_chain.json` — Executes the Markov Chain operation.
- **Word2 Vec** `08-Machine-Learning/02-ML-SparkML/03-FeatureExtraction/word2vec.json` — Transforms vectors of words into vectors of numeric codes for the purpose of further processing by NLP or machine learning algorithms.

## FeatureTransformers
- **Polynominal Expansion** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/PolynominalExpansion.json` — Perform feature expansion in a polynomial space.
- **Quantile Discretizer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/QuantileDiscretizer.json` — QuantileDiscretizer takes a column with continuous features and outputs a column with binned categorical features.
- **Quantile Discretizer Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/QuantileDiscretizer_transform.json` — QuantileDiscretizer takes a column with continuous features and outputs a column with binned categorical features.
- **Word To Score Mapping** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/WordToScoreMapping.json` — It maps the original word of hashValue to score.
- **Binarizer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/binarizer.json` — Binarize a column of continuous features given a threshold.
- **Bucketizer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/bucketizer_python.json` — The Bucketizer transformer in PySpark is used to discretize continuous features into categorical ones by creating a fixed number of buckets.
- **Bucketizer Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/bucketizer_transform_python.json` — Bucketizer Transform.
- **Cosine Similarity** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/cosine_similarity.json` — Computes cosine similarity between NEW and OLD entities using encoded and scaled feature vectors.
- **IDF** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/idf.json` — Compute the Inverse Document Frequency (IDF) given a collection of documents.
- **Imputer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/imputer.json` — Imputation estimator for completing missing values.
- **Imputer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/imputer_python.json` — Imputation estimator for completing missing values.
- **Imputer Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/imputer_python_transform.json` — Imputation estimator for completing missing values.
- **Imputer Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/imputer_transform.json` — Imputation estimator for completing missing values.
- **Index To String** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/index_to_string_python.json` — Maps a column of indices back to a new column of corresponding string values.
- **Index To String Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/index_to_string_transform.json` — Maps a column of indices back to a new column of corresponding string values.
- **Index String** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/indexstring.json` — Maps a column of indices back to a new column of corresponding string values.
- **Interaction** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/interactions_python.json` — This transformer takes in Double and Vector type columns and outputs a flattened vector of their feature interactions.
- **Interaction Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/interactions_transform_python.json` — This transformer takes in Double and Vector type columns and outputs a flattened vector of their feature interactions.
- **MaxAbs Scaler** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/maxabs_scaler.json` — Rescale each feature individually to range [-1, 1] by dividing through the largest maximum absolute value in each feature.
- **MaxAbs Scaler** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/maxabs_scaler_python.json` — Rescale each feature individually to range [-1, 1] by dividing through the largest maximum absolute value in each feature.
- **MaxAbs Scaler Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/maxabs_scaler_transform.json` — Rescale each feature individually to range [-1, 1] by dividing through the largest maximum absolute value in each feature.
- **MaxAbs Scaler Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/maxabs_scaler_transform_python.json` — Rescale each feature individually to range [-1, 1] by dividing through the largest maximum absolute value in each feature.
- **N Gram Transformer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/ngram.json` — Converts the input array of strings into an array of n-grams.
- **Normalizer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/normalizer.json` — Normalizer is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm.
- **Normalizer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/normalizer_python.json` — Normalizer is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm.
- **Normalizer Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/normalizer_transform_python.json` — Normalizer is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm.
- **One Hot Encoder** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/onehotencoder.json` — Maps a column of label indices to a column of binary vectors, with at most a single one-value.
- **One Hot Encoder Advanced** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/onehotencoder_advanced.json` — Maps a column of label indices to a column of binary vectors, with at most a single one-value.
- **One Hot Encoder Advanced Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/onehotencoder_advanced_transform.json` — Maps a column of label indices to a column of binary vectors, with at most a single one-value.
- **One Hot Encoder** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/onehotencoder_python.json` — Maps a column of label indices to a column of binary vectors, with at most a single one-value.
- **One Hot Encoder Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/onehotencoder_transform_python.json` — Maps a column of label indices to a column of binary vectors, with at most a single one-value.
- **Robust Scaler** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/robust_scaler.json` — RobustScaler removes the median and scales the data according to the quantile range.
- **Robust Scaler** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/robust_scaler_python.json` — RobustScaler removes the median and scales the data according to the quantile range.
- **Robust Scaler Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/robust_scaler_transform.json` — RobustScaler removes the median and scales the data according to the quantile range.
- **Robust Scaler Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/robust_scaler_transform_python.json` — RobustScaler removes the median and scales the data according to the quantile range.
- **Signal Processing** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/signal_processing.json` — Expects a signal as column input and performs transformations.
- **SMOTE** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/smote.json` — Implementation of SMOTE - Synthetic Minority Over-sampling Technique.
- **SQL Transformer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/sqltransformer.json` — This node runs the given SQL on the incoming DataFrame using Spark ML SQLTransformer.
- **Stop Words Remover** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/stopwordsremover.json` — Filters out stop words from input.
- **String Indexer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/stringindexer.json` — StringIndexer encodes a string column of labels to a column of label indices.
- **String Indexer Advanced Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/stringindexerTransform.json` — StringIndexer encodes a string column of labels to a column of label indices.
- **String Indexer Advanced** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/stringindexer_advanced.json` — StringIndexer encodes a string column of labels to a column of label indices.
- **String Indexer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/stringindexer_python.json` — StringIndexer encodes a string column of labels to a column of label indices.
- **String Indexer Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/stringindexer_transform_python.json` — StringIndexer encodes a string column of labels to a column of label indices.
- **Tokenizer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/tokenizer.json` — A tokenizer that converts the input string to lowercase and then splits it by white spaces.
- **Vector Assembler** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/vectorassembler.json` — Merges multiple columns into a vector column.
- **Vector Functions** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/vectorfunctions.json` — Vector Functions for transforming Vectors.
- **Vector Indexer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/vectorindexer.json` — Vector Indexer indexes categorical features inside of a Vector.
- **Vector Indexer** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/vectorindexer_java.json` — Vector Indexer indexes categorical features inside of a Vector.
- **Vector Indexer Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/vectorindexer_transform.json` — Vector Indexer indexes categorical features inside of a Vector.
- **Vector Indexer Transform** `08-Machine-Learning/02-ML-SparkML/04-FeatureTransformers/vectorindexer_transform_java.json` — Vector Indexer indexes categorical features inside of a Vector.

## DimensionalityReduction
- **PCA** `08-Machine-Learning/02-ML-SparkML/05-DimensionalityReduction/pca.json` — Trains a model to project vectors to a low-dimensional space using PCA.
- **SVD** `08-Machine-Learning/02-ML-SparkML/05-DimensionalityReduction/svd.json` — Executes the SVD operation.

## FeatureSelection
- **ChiSq Selector** `08-Machine-Learning/02-ML-SparkML/06-FeatureSelection/ChiSqSelector.json` — Chi-Squared feature selection, which selects categorical features to use for predicting a categorical label.
- **Vector Slicer** `08-Machine-Learning/02-ML-SparkML/06-FeatureSelection/vectorslicer.json` — VectorSlicer feature selection, which takes a feature vector and outputs a new feature vector with a sub-array of the original features.

## SplitDataset
- **Split** `08-Machine-Learning/02-ML-SparkML/07-SplitDataset/split.json` — This node splits the incoming DataFrame into 2.
- **Split Probability Column** `08-Machine-Learning/02-ML-SparkML/07-SplitDataset/splitprobabilitycol.json` — Executes the Split Probability Column operation.
- **Split With Stratified Sampling** `08-Machine-Learning/02-ML-SparkML/07-SplitDataset/stratified_sampling.json` — This node splits the incoming DataFrame into 2.

## Clustering
- **Gaussian Mixture** `08-Machine-Learning/02-ML-SparkML/08-Clustering/gmm.json` — Gaussian Mixture Model (GMM) performs probabilistic clustering using multiple Gaussian distributions, allowing each data point to belong to clusters with varying probabilities.
- **K-Means** `08-Machine-Learning/02-ML-SparkML/08-Clustering/kmeans.json` — K-Means is an unsupervised clustering algorithm that groups data points into a predefined number of clusters by minimizing intra-cluster distance.
- **LDA** `08-Machine-Learning/02-ML-SparkML/08-Clustering/lda.json` — Latent Dirichlet Allocation (LDA) is a topic modeling algorithm that discovers latent topics in a corpus of documents represented as term-frequency vectors.

## Regression
- **AFT Survival Regression** `08-Machine-Learning/02-ML-SparkML/09-Regression/AFTSurvivalRegression.json` — AFT Survival Regression is a parametric survival analysis model used to estimate time-to-event outcomes when data may be censored.
- **Decision Tree Regression** `08-Machine-Learning/02-ML-SparkML/09-Regression/DecisionTreeRegression.json` — Decision Tree Regression builds a tree-based model to predict continuous numerical values using rule-based splits on input features.
- **GBT Regression** `08-Machine-Learning/02-ML-SparkML/09-Regression/GBTRegression.json` — Gradient-Boosted Tree Regression builds an ensemble of decision trees to predict continuous numerical values by minimizing a specified loss function.
- **Random Forest Regression** `08-Machine-Learning/02-ML-SparkML/09-Regression/RandomForestRegression.json` — Random Forest Regression builds an ensemble of decision trees to predict continuous numeric outcomes using both continuous and categorical features.
- **XGBoost Regressor** `08-Machine-Learning/02-ML-SparkML/09-Regression/XGBoostRegression.json` — XGBoost Regressor is a high-performance gradient boosting algorithm designed for predicting continuous numeric values with strong accuracy and scalability.
- **Linear Regression** `08-Machine-Learning/02-ML-SparkML/09-Regression/linearregression.json` — Linear Regression models the relationship between a continuous target variable and one or more input features by fitting a linear equation.

## Classification
- **Decision Tree Classifier** `08-Machine-Learning/02-ML-SparkML/10-Classification/DecisionTreeClassifier.json` — It supports both binary and multiclass labels, as well as both continuous and categorical features.
- **Decision Tree Classifier** `08-Machine-Learning/02-ML-SparkML/10-Classification/DecisionTreeClassifierPython.json` — It supports both binary and multiclass labels, as well as both continuous and categorical features.
- **GBT Classifier** `08-Machine-Learning/02-ML-SparkML/10-Classification/GBTClassifier.json` — Gradient-Boosted Trees (GBTs) is an ensemble-based classification algorithm that builds models sequentially to improve prediction accuracy.
- **GBT Classifier** `08-Machine-Learning/02-ML-SparkML/10-Classification/GBTClassifierPython.json` — Gradient-Boosted Trees (GBTs) is an ensemble-based classification algorithm that incrementally builds decision trees to improve prediction accuracy.
- **MultiLayer Perceptron** `08-Machine-Learning/02-ML-SparkML/10-Classification/MultiLayerPerceptron.json` — The Multilayer Perceptron node enables training of fully connected neural networks for classification tasks using feedforward artificial neural networks.
- **Naive Bayes** `08-Machine-Learning/02-ML-SparkML/10-Classification/NaiveBayes.json` — Naive Bayes is a probabilistic classification algorithm based on Bayes’ theorem.
- **Random Forest Classifier** `08-Machine-Learning/02-ML-SparkML/10-Classification/RandomForestClassifier.json` — Random Forest is an ensemble-based classification algorithm that combines multiple decision trees to improve prediction accuracy, robustness, and generalization across both binary and multiclass problems.
- **Random Forest Classifier** `08-Machine-Learning/02-ML-SparkML/10-Classification/RandomForestClassifierPython.json` — Random Forest is an ensemble-based classification algorithm that builds multiple decision trees and combines their outputs to improve prediction accuracy and stability across both binary and multiclass problems.
- **XGBoost Classifier** `08-Machine-Learning/02-ML-SparkML/10-Classification/XGBoostClassifier.json` — XGBoost is a high-performance gradient boosting algorithm designed for scalable and efficient classification tasks, supporting both binary and multi-class problems.
- **Logistic Regression** `08-Machine-Learning/02-ML-SparkML/10-Classification/logisticregression.json` — Logistic Regression is a statistical classification algorithm used to predict binary outcomes by estimating probabilities.
- **Logistic Regression** `08-Machine-Learning/02-ML-SparkML/10-Classification/logisticregressionPython.json` — Logistic Regression is a probability-based classification algorithm used to predict binary outcomes in a clear and interpretable manner.

## CollaborativeFiltering
- **ALS** `08-Machine-Learning/02-ML-SparkML/11-CollaborativeFiltering/als.json` — Alternating Least Squares (ALS) matrix factorization.

## FreqPatternMining
- **FP Growth** `08-Machine-Learning/02-ML-SparkML/12-FreqPatternMining/fpgrowth.json` — Does Pattern Mining using FPGrowth Algorithm.

## Modeling
- **Binary Classification Evaluator** `08-Machine-Learning/02-ML-SparkML/13-Modeling/binary-classification-evaluator-python.json` — Evaluator for binary classification, which expects two input columns: rawPrediction and label.
- **Binary Classification Evaluator** `08-Machine-Learning/02-ML-SparkML/13-Modeling/binary-classification-evaluator.json` — Evaluator for binary classification, which expects two input columns: rawPrediction and label.
- **Clustering Evaluator** `08-Machine-Learning/02-ML-SparkML/13-Modeling/clustering-evaluator.json` — Evaluator for Clustering, which expects two input columns: features and prediction.
- **Cross Validator** `08-Machine-Learning/02-ML-SparkML/13-Modeling/crossvalidator.json` — This node represents Cross Validator from Spark ML.
- **Load MLeap** `08-Machine-Learning/02-ML-SparkML/13-Modeling/load_mleap.json` — Executes the Load MLeap operation.
- **Spark ML Model Load** `08-Machine-Learning/02-ML-SparkML/13-Modeling/mlmodelload.json` — Executes the Spark ML Model Load operation.
- **Spark ML Model Load** `08-Machine-Learning/02-ML-SparkML/13-Modeling/mlmodelload_python.json` — Executes the Spark ML Model Load operation.
- **Spark ML Model Save** `08-Machine-Learning/02-ML-SparkML/13-Modeling/mlmodelsave.json` — This node saves the ML model generated at the specified path.
- **Multiclass Classification Evaluator** `08-Machine-Learning/02-ML-SparkML/13-Modeling/multiclass-classification-evaluator-python.json` — Evaluator for multiclass classification, which expects two input columns: score and label.
- **Multiclass Classification Evaluator** `08-Machine-Learning/02-ML-SparkML/13-Modeling/multiclass-classification-evaluator.json` — Evaluator for multiclass classification, which expects two input columns: score and label.
- **Spark Pipeline** `08-Machine-Learning/02-ML-SparkML/13-Modeling/pipeline.json` — This node represents Pipeline from Spark ML.
- **Spark Predict** `08-Machine-Learning/02-ML-SparkML/13-Modeling/predict.json` — Predict node takes in a DataFrame and Model and makes predictions.
- **Regression Evaluator** `08-Machine-Learning/02-ML-SparkML/13-Modeling/regression-evaluator.json` — Evaluator for regression, which expects two input columns: prediction and label.
- **Spark ML ROC** `08-Machine-Learning/02-ML-SparkML/13-Modeling/roc.json` — It produces the ROC curve based on the probability and label.
- **Save MLeap** `08-Machine-Learning/02-ML-SparkML/13-Modeling/save_mleap.json` — Executes the Save MLeap operation.
- **Train Validation Split** `08-Machine-Learning/02-ML-SparkML/13-Modeling/trainvalidationsplit.json` — This node represents Train Validation Split from Spark ML.

## ML H2O
- **Extract Probabilities** `08-Machine-Learning/03-ML-H2O/extract_probabilities.json` — Executes the Extract Probabilities operation.
- **H2O Auto ML** `08-Machine-Learning/03-ML-H2O/h2o_auto_ml.json` — H2O AutoML.
- **H2O Auto ML** `08-Machine-Learning/03-ML-H2O/h2o_auto_ml_python.json` — H2O AutoML.
- ** H2O Clustering Evaluator** `08-Machine-Learning/03-ML-H2O/h2o_clustering_evaluator.json` — Evaluator for Clustering.
- ** H2O Clustering Evaluator** `08-Machine-Learning/03-ML-H2O/h2o_clustering_evaluator_scala.json` — Evaluator for Clustering, which expects two input columns: features and prediction.
- **H2O Distributed Random Forest** `08-Machine-Learning/03-ML-H2O/h2o_drf.json` — Distributed Random Forest (DRF) is a powerful classification and regression tool.
- **H2O Distributed Random Forest** `08-Machine-Learning/03-ML-H2O/h2o_drf_python.json` — Distributed Random Forest (DRF) is a powerful classification and regression tool.
- **H2O Gradient Boosting Machine** `08-Machine-Learning/03-ML-H2O/h2o_gbm.json` — Gradient Boosting Machine (for Regression and Classification) is a forward learning ensemble method.
- **H2O Gradient Boosting Machine** `08-Machine-Learning/03-ML-H2O/h2o_gbm_python.json` — Gradient Boosting Machine (for Regression and Classification) is a forward learning ensemble method that builds regression trees sequentially.
- **H2O Generalized Linear Models** `08-Machine-Learning/03-ML-H2O/h2o_glm.json` — Generalized Linear Models (GLM) estimate regression models for outcomes following exponential distributions.
- **H2O Generalized Linear Models** `08-Machine-Learning/03-ML-H2O/h2o_glm_python.json` — Generalized Linear Models (GLM) estimate regression models for outcomes following exponential distributions.
- **H2O Generalized Low Rank Models** `08-Machine-Learning/03-ML-H2O/h2o_glrm.json` — Generalized Low Rank Models (GLRM) is an algorithm for dimensionality reduction of a dataset.
- **H2O Generalized Low Rank Models** `08-Machine-Learning/03-ML-H2O/h2o_glrm_python.json` — Generalized Low Rank Models (GLRM) is an algorithm for dimensionality reduction of a dataset, capable of handling mixed data types and missing values.
- **H2O Isolation Forest** `08-Machine-Learning/03-ML-H2O/h2o_isolation_forest.json` — Isolation Forest is an unsupervised learning algorithm that identifies anomalies or outliers by isolating observations in a forest of decision trees.
- **H2O Isolation Forest** `08-Machine-Learning/03-ML-H2O/h2o_isolation_forest_python.json` — Isolation Forest is an unsupervised learning algorithm for anomaly detection that isolates observations by randomly selecting a feature and then randomly selecting a split value.
- **H2O K-Means** `08-Machine-Learning/03-ML-H2O/h2o_kmeans.json` — K-Means falls in the general category of clustering algorithms.
- **H2O K-Means** `08-Machine-Learning/03-ML-H2O/h2o_kmeans_python.json` — K-Means is an unsupervised clustering algorithm that groups data points into K clusters based on feature similarity.
- **H2O ML Model Load** `08-Machine-Learning/03-ML-H2O/h2o_mojo_load.json` — Loads an H2O MOJO ML model.
- **H2O ML Model Load** `08-Machine-Learning/03-ML-H2O/h2o_mojo_load_python.json` — Loads an H2O MOJO ML model.
- **H2O ML Model Save** `08-Machine-Learning/03-ML-H2O/h2o_mojo_save.json` — Saves an H2O MOJO ML model at the specified path.
- **H2O ML Model Save** `08-Machine-Learning/03-ML-H2O/h2o_mojo_save_python.json` — Saves an H2O MOJO ML model at the specified path.
- **H2O Neural Network** `08-Machine-Learning/03-ML-H2O/h2o_neural_network.json` — H2O Deep Learning is based on a multi-layer feedforward artificial neural network that is trained with stochastic gradient descent using back-propagation.
- **H2O PCA** `08-Machine-Learning/03-ML-H2O/h2o_pca.json` — Principal Component Analysis (PCA) is used for dimensionality reduction and identifying the primary patterns in high-dimensional data by transforming features into a set of uncorrelated components.
- **H2O PCA** `08-Machine-Learning/03-ML-H2O/h2o_pca_python.json` — Principal Component Analysis (PCA) is used for dimensionality reduction and identifying the primary patterns in high-dimensional data by transforming features into a set of uncorrelated components.
- **H2O Score** `08-Machine-Learning/03-ML-H2O/h2o_score.json` — Executes the H2O Score operation.
- **H2O Score** `08-Machine-Learning/03-ML-H2O/h2o_score_python.json` — Scores the data using the H2O model.
- **H2O Word to Vec** `08-Machine-Learning/03-ML-H2O/h2o_word2vec.json` — The Word2vec algorithm takes a text corpus as an input and produces the word vectors as output.
- **H2O Word to Vec** `08-Machine-Learning/03-ML-H2O/h2o_word2vec_python.json` — The Word2vec algorithm takes a text corpus as an input and produces the word vectors as output.
- **H2O XGBoost** `08-Machine-Learning/03-ML-H2O/h2o_xgboost.json` — XGBoost is a supervised learning algorithm that implements a process called boosting to yield accurate models.
- **H2O XGBoost** `08-Machine-Learning/03-ML-H2O/h2o_xgboost_python.json` — XGBoost is a supervised learning algorithm that implements a process called boosting to yield accurate models.

## ML DeepLearning
- **Dense Layer** `08-Machine-Learning/05-ML-DeepLearning/dl_layer_dense.json` — Executes the Dense Layer operation.
- **Keras Preprocessor** `08-Machine-Learning/05-ML-DeepLearning/dl_node_keras_preprocessor.json` — Executes the Keras Preprocessor operation.
- **Keras Model Compile** `08-Machine-Learning/05-ML-DeepLearning/dl_nodemodelcompile.json` — Executes the Keras Model Compile operation.
- **Keras Model Fit** `08-Machine-Learning/05-ML-DeepLearning/dl_nodemodelfit.json` — Executes the Keras Model Fit operation.
- **Keras Model Sequential** `08-Machine-Learning/05-ML-DeepLearning/dl_nodemodelsequential.json` — Executes the Keras Model Sequential operation.
- **Keras Predict** `08-Machine-Learning/05-ML-DeepLearning/dl_nodepredict.json` — Executes the Keras Predict operation.

## Classification
- **Sklearn Gradient Boosting Classifier** `08-Machine-Learning/06-ML-Sklearn/Classification/gradient-boosting-classifier.json` — Gradient Boosting Classifier builds an ensemble of decision trees in a stage-wise manner, optimizing a differentiable loss function for classification tasks including binary and multiclass problems.
- **Sklearn Logistic Regression** `08-Machine-Learning/06-ML-Sklearn/Classification/logistic-regression.json` — Logistic Regression is a linear classification algorithm that supports binary, One-vs-Rest, and multinomial classification with L1, L2, or Elastic-Net regularization.
- **Sklearn Random Forest Classifier** `08-Machine-Learning/06-ML-Sklearn/Classification/random-forest-classifier.json` — Random Forest Classifier is an ensemble-based supervised learning algorithm that builds multiple decision trees on different bootstrapped subsets of the training data and aggregates their predictions using majority voting.
- **Sklearn XGBoost Classifier** `08-Machine-Learning/06-ML-Sklearn/Classification/xgboost-classifier.json` — XGBoost Classifier is an optimized gradient boosting algorithm that uses ensemble of decision trees.

## Clustering
- **Sklearn K-Means** `08-Machine-Learning/06-ML-Sklearn/Clustering/kmeans.json` — K-Means clustering algorithm using scikit-learn.

## Data
- **Sklearn Polynomial** `08-Machine-Learning/06-ML-Sklearn/Data/polynomial.json` — Polynomial regression is a special case of linear regression, which generates a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree.

## Modeling
- **Custom Metrics** `08-Machine-Learning/06-ML-Sklearn/Modeling/custom-metrics.json` — Custom Metrics to check on aggregated field, which expects prediction, label, aggregate column and metrics.
- **Sklearn Classification Evaluator** `08-Machine-Learning/06-ML-Sklearn/Modeling/sklearn-classification-evaluator.json` — Evaluator for classification, which expects two input columns: prediction and label.
- **Sklearn Clustering Evaluator** `08-Machine-Learning/06-ML-Sklearn/Modeling/sklearn-clustering-evalutor.json` — Evaluator for clustering models using Inertia and Silhouette Score.
- **Sklearn Model Load From S3** `08-Machine-Learning/06-ML-Sklearn/Modeling/sklearn-load-from-s3.json` — Load the Sklearn model stored in the pickel format in S3.
- **Sklearn Model Load** `08-Machine-Learning/06-ML-Sklearn/Modeling/sklearn-load.json` — Load the Sklearn model stored in the pickel file.
- **Sklearn Predict** `08-Machine-Learning/06-ML-Sklearn/Modeling/sklearn-predict.json` — Predict node takes in a dataframe and model and makes predictions.
- **Sklearn Regression Evaluator** `08-Machine-Learning/06-ML-Sklearn/Modeling/sklearn-regression-evaluator.json` — Evaluator for regression, which expects two input columns: prediction and label.
- **Sklearn Model Save To S3** `08-Machine-Learning/06-ML-Sklearn/Modeling/sklearn-save-to-s3.json` — Saves the Sklearn model generated at the specified path in S3 in pickle format.
- **Sklearn Model Save** `08-Machine-Learning/06-ML-Sklearn/Modeling/sklearn-save.json` — Saves the Sklearn model generated at the specified path in pickle file.

## Optimization
- **Optimization** `08-Machine-Learning/06-ML-Sklearn/Optimization/optimization.json` — Executes the Optimization operation.
- **Optimization Model Load And Score** `08-Machine-Learning/06-ML-Sklearn/Optimization/optimization_model_load_and_score.json` — Executes the Optimization Model Load And Score operation.

## PreProcessing
- **Sklearn Binarizer** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/binarizer.json` — Binarize data (set feature values to 0 or 1) according to a threshold.
- **Sklearn Binarizer Transform** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/binarizer_transform.json` — Binarize data (set feature values to 0 or 1) according to a threshold.
- **Sklearn Label Encoder** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/label_encoder.json` — Encode labels with value between 0 and n_classes-1.
- **Sklearn MinMaxScaler** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/min_max_scaler.json` — Transforms features by scaling each feature to a given range.
- **Sklearn MinMax Scaler Transform** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/min_max_scaler_transform.json` — Transforms DataFrame.
- **MinMax Scaler Inverse Transform** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/minmaxscaler_inverse_transform.json` — The inverse transform node is used to transform the scaled data back to its original form.
- **Sklearn Normalizer** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/normalizer.json` — Normalizes samples individually to unit norm.
- **Sklearn Normalizer Transform** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/normalizer_transform.json` — Normalizes samples individually to unit norm.
- **Sklearn OneHotEncoder** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/one_hot_encoder.json` — Encode categorical integer features as a one-hot numeric array.
- **Sklearn Quantile Fit Transform** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/quantile_transformer.json` — Transforms features using quantiles information.
- **Sklearn Quantile Transform** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/quantile_transformer_transform.json` — Transform features using quantiles information.
- **Sklearn StandardScalar** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/standard_scalar.json` — Standardizing a dataset involves rescaling the distribution of values so that the mean of observed values is 0 and the standard deviation is 1.
- **Sklearn StandardScalar Transform** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/standard_scalar_transform.json` — Standardizing a dataset involves rescaling the distribution of values so that the mean of observed values is 0 and the standard deviation is 1.
- **Standard Scaler Inverse Transform** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/standardscaler_inverse_transform.json` — The inverse transform node is used to transform the scaled data back to its original form.
- **Sklearn TF-IDF Vectorizer** `08-Machine-Learning/06-ML-Sklearn/PreProcessing/tfidf.json` — Applies scikit-learn's TfidfVectorizer to a text column.

## Regression
- **Sklearn Bayesian Ridge Regression** `08-Machine-Learning/06-ML-Sklearn/Regression/bayesian-ridge-regression.json` — Bayesian Ridge Regression implements a probabilistic linear regression model where model coefficients are treated as random variables with prior distributions.
- **Sklearn Gradient Boosting Regression** `08-Machine-Learning/06-ML-Sklearn/Regression/gradient-boosting-regression.json` — Gradient Boosting Regression builds a strong predictive model by combining multiple weak regression trees in a forward stage-wise manner.
- **SkLearn Lasso Regression** `08-Machine-Learning/06-ML-Sklearn/Regression/lasso-regression.json` — Lasso Regression is a linear regression technique that applies L1 regularization to shrink coefficients and perform feature selection by driving some coefficients exactly to zero.
- **Sklearn Random Forest Regression** `08-Machine-Learning/06-ML-Sklearn/Regression/random-forest-regression.json` — Random Forest Regression builds an ensemble of decision trees using bootstrap sampling and feature randomness, and averages their predictions to improve predictive accuracy, robustness, and control overfitting for continuous target variables.
- **Sklearn Ridge Regression** `08-Machine-Learning/06-ML-Sklearn/Regression/ridge-regression.json` — Ridge Regression solves a linear regression problem by minimizing the least squares loss while applying L2 regularization to the model coefficients.
- **Sklearn XGBoost Regressor** `08-Machine-Learning/06-ML-Sklearn/Regression/xgboost-regression.json` — XGBoost Regressor implements gradient boosted decision trees for regression problems.

## ML Pycaret
- **PyCaret AutoML Classification** `08-Machine-Learning/07-ML-Pycaret/pycaretauto_ml_classification.json` — Executes the PyCaret AutoML Classification operation.
- **PyCaret AutoML Regression** `08-Machine-Learning/07-ML-Pycaret/pycaretauto_ml_regression.json` — Executes the PyCaret AutoML Regression operation.

## ML TimeSeries
- **Arima** `08-Machine-Learning/08-ML-TimeSeries/arima.json` — AutoARIMA.
- **Arima Forecast** `08-Machine-Learning/08-ML-TimeSeries/arima_forecast.json` — Forecast by calling the forecast() or the predict() functions on the Arima object returned from calling fit.
- **Arima Model Load** `08-Machine-Learning/08-ML-TimeSeries/arima_load.json` — This node load the Arima model stored in the pickle file.
- **Arima Model Save** `08-Machine-Learning/08-ML-TimeSeries/arima_save.json` — This node saves the Arima model generated at the specified path in pickle file.
- **LSTM** `08-Machine-Learning/08-ML-TimeSeries/lstm.json` — Executes the LSTM operation.
- **Prophet** `08-Machine-Learning/08-ML-TimeSeries/prophet.json` — Executes the Prophet operation.
- **Prophet Cross Validator** `08-Machine-Learning/08-ML-TimeSeries/prophet_cross_validation.json` — Executes the Prophet Cross Validator operation.
- **Prophet Model Load** `08-Machine-Learning/08-ML-TimeSeries/prophet_load.json` — This node load the Prophet model stored in the pickel file.
- **Prophet Make Future Dataframe** `08-Machine-Learning/08-ML-TimeSeries/prophet_make_future_dataframe.json` — Executes the Prophet Make Future Dataframe operation.
- **Prophet Predict** `08-Machine-Learning/08-ML-TimeSeries/prophet_predict.json` — Executes the Prophet Predict operation.
- **Prophet Model Save** `08-Machine-Learning/08-ML-TimeSeries/prophet_save.json` — This node saves the Prophet model generated at the specified path in pickle file.
- **Sarimax** `08-Machine-Learning/08-ML-TimeSeries/sarimax.json` — Seasonal Autoregressive Integrated Moving Average, SARIMA or Seasonal ARIMA, is an extension of ARIMA that explicitly supports univariate time series data with a seasonal component.
- **Sarimax Forecast** `08-Machine-Learning/08-ML-TimeSeries/sarimax_forecast.json` — Forecast by calling the forecast() or the predict() functions on the SARIMAXResults object returned from calling fit.
- **Sarimax Model Load** `08-Machine-Learning/08-ML-TimeSeries/sarimax_load.json` — This node load the Sarimax model stored in the pickle file.
- **Sarimax Model Save** `08-Machine-Learning/08-ML-TimeSeries/sarimax_save.json` — This node saves the Sarimax model generated at the specified path in pickle file.
- **TS Decompose** `08-Machine-Learning/08-ML-TimeSeries/ts_decompose.json` — Reads A Dataframe consists of times series.
- **VAR** `08-Machine-Learning/08-ML-TimeSeries/var.json` — Executes the VAR operation.
- **VarForecast** `08-Machine-Learning/08-ML-TimeSeries/var_forecast.json` — Executes the VarForecast operation.
- **VAR Model Load** `08-Machine-Learning/08-ML-TimeSeries/var_load.json` — This node load the VAR model stored in the pickle file.
- **VAR Model Save** `08-Machine-Learning/08-ML-TimeSeries/var_save.json` — This node saves the VAR model generated at the specified path in pickle file.
