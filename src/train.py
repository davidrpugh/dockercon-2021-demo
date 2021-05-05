import pathlib

import joblib
import numpy as np
from sklearn import datasets, decomposition, ensemble, metrics
from sklearn import model_selection, pipeline, preprocessing


DATA_DIR = pathlib.Path("data/")
DATASET_NAME = "CIFAR_10"
DATASET_FILENAME = DATA_DIR / f"{DATASET_NAME}.joblib"
N_COMPONENTS = 0.95
OUTPUT_DIR = pathlib.Path("results/example-training-job/")
OUTPUT_FILENAME = OUTPUT_DIR / "model.joblib"
SEED = 42
TEST_SIZE = 0.1
TRAIN_N_JOBS = -1
VERBOSITY = 10


# download the dataset (if necessary!)
if not DATASET_FILENAME.exists():
    print("Started downloading the dataset...")
    bunch = datasets.fetch_openml(name=DATASET_NAME, as_frame=True)
    joblib.dump(bunch, DATASET_FILENAME)
    print("...finished downloading the dataset!")
else:
    bunch = joblib.load(DATASET_FILENAME)

# split the dataset into training and testing data
_random_state = (np.random
                   .RandomState(SEED))
train_df, test_df, train_target, test_target = model_selection.train_test_split(
    bunch["data"],
    bunch["target"],
    stratify=bunch["target"],
    test_size=TEST_SIZE,
    random_state=_random_state
)

# create a pipeline
ml_pipeline = pipeline.make_pipeline(
    preprocessing.MinMaxScaler(),
    decomposition.PCA(n_components=N_COMPONENTS, random_state=_random_state),
    ensemble.RandomForestClassifier(n_jobs=TRAIN_N_JOBS,
                                    random_state=_random_state,
                                    verbose=VERBOSITY),
    verbose=True,
)

# fit the pipeline and save the trained model to disk
print("Started training the pipeline...")
_ = ml_pipeline.fit(train_df, train_target)
joblib.dump(ml_pipeline, OUTPUT_FILENAME)
print("...finished training the pipeline!")

# make predictions
predictions = ml_pipeline.predict(test_df)

# generate a classification report
classification_report = metrics.classification_report(
    test_target,
    predictions,
)
print(classification_report)






