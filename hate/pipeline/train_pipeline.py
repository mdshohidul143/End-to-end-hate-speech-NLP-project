import sys
from hate.components.data_ingestion import DataIngestion
from hate.configuration.s3_operation import S3Operation

from hate.entity.config_entity import DataIngestionConfig

from hate.entity.artifact_entity import DataIngestionArtifacts

from hate.logger import logging
from hate.exception import CustomException


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.s3_operation = S3Operation()



    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from AWS S3 bucket")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
                )

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the imblanced data and raw data from AWS S3 bucket")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e


    def run_pipeline(self) -> None:
        logging.info("Entered the run_pipeline method of TrainPipeline class")

        try:
            data_ingestion_artifacts = self.start_data_ingestion()

            logging.info("Exited the run_pipeline method of TrainPipeline class")
        except Exception as e:
            raise CustomException(e, sys)