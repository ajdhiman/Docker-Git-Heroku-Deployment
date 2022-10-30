from housing.config.configuration import Configuration
from housing.exception import HousingException
from housing.logger import logging
import os
import sys
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.component.data_ingestion import DataIngestion


class Pipeline:
    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e, sys) from e

    def Start_Data_Ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Start_Data_Ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            logging.info("data_ingestion found")
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e

    def run_pipeline(self):
        try:
            logging.info("run_pipeline")
            data_ingestion_artifact = self.Start_Data_Ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e
