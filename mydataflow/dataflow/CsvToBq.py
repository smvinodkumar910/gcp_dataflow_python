#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""A word-counting workflow."""

# pytype: skip-file

import argparse
import logging
import re
from typing import Dict

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.io import WriteToBigQuery
from apache_beam.io.gcp.bigquery import BigQueryDisposition
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

from mydataflow.configuration.SchemaLoad import SchemaLoad as sl
import mydataflow.Utilities.StringOperations as so

import os

filename = 'ANNUAL_ENTERPRISE_SURVEY.json'

class CsvToJsonDoFn(beam.DoFn):
  """Parse each line of input text into Json"""
  def process(self, element:str):
    """Returns an iterator over the words of this element.

    The element is a line of text.  If the line is blank, note that, too.

    Args:
      element: the element being processed

    Returns:
      The processed element.
    """
    colval=[]
    if '"' in element:
      colval=so.splitIntoVal(element,',','"')
    else:
      colval=element.split(',')
      
    fieldList = sl.getFieldList(filename)
    rowAsDict = dict(zip(fieldList, colval))
    return [rowAsDict]


def run(argv=None, save_main_session=True):
  

  """Main entry point; defines and runs the wordcount pipeline."""
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--input',
      dest='input',
      default='gs://mynewdevenv-bucket/SourceFiles/annual-enterprise-survey-2020.csv',
      help='Input file to process.')
  
  known_args, pipeline_args = parser.parse_known_args(argv)

  # We use the save_main_session option because one or more DoFn's in this
  # workflow rely on global context (e.g., a module imported at module level).
  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
  
  # The pipeline will be run on exiting the with block.
  with beam.Pipeline(options=pipeline_options) as p:

    # Read the text file[pattern] into a PCollection.
    lines = p | 'Read' >> ReadFromText(known_args.input, skip_header_lines =1)
    dicts = lines | 'Convert to Dicts' >> (beam.ParDo(CsvToJsonDoFn()))
    dicts | 'write to bigquery' >> beam.io.WriteToBigQuery( table='mynewdevenv:DATAFLOW_LOAD.ANNUAL_ENTERPRISE_SURVEY' ,
    schema= sl.getSchema(filename), create_disposition=BigQueryDisposition.CREATE_IF_NEEDED,
    write_disposition=BigQueryDisposition.WRITE_APPEND)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()
