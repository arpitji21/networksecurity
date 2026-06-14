from networksecurity.entity.config_entity import DataValidationConfig

from networksecurity.entity.artifact_entity import DataValidationArtifact
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from scipy.stats import ks_2samp
import pandas as pd
import os
import sys

