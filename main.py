from networksecurity.components.data_ingestion import DataIngestion

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import os
import sys

if __name__=="__main__":
    try:
        dataIngestionconfig = DataIngestionConfig
        data_ingestion = DataIngestion(data_ingestion_config=dataIngestionconfig)
        
        logging.info("Enter try block")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)