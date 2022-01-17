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
from apache_beam.options.pipeline_options import GoogleCloudOptions, PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.transforms.core import Create

from mydataflow.configuration.SchemaLoad import SchemaLoad as sl
from mydataflow.configuration.AppProperties import AppProperties as app
import requests
import datetime


filename = 'API_DATA.json'

def httpRequest(url:str):
    res = requests.get(url)
    response = dict(res.json()).get('data')
    return list(response)

def run(argv=None, save_main_session=True):
  

  """Main entry point; defines and runs the wordcount pipeline."""
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--jobparams',
      dest='jobparams',
      default='apidataload',
      help='application properties file setment value to identify job parameters')
  
  known_args, pipeline_args = parser.parse_known_args(argv)
  

  timenow = (datetime.datetime.now())
  jobname = 'apitobq-'+timenow.strftime('%Y-%m-%d-%H%M%S')
  pipeline_args.append("--job_name={0}".format(jobname))
  
  gcpdtl = app.getProperty('gcp')
  loaddtl = app.getProperty(known_args.jobparams)

  projectid = gcpdtl.get('projectid')
  datasetid = gcpdtl.get('datasetid')

  tableid = loaddtl.get('tableid')
  templocation = loaddtl.get('tempLocationPath')
  apiurl = loaddtl.get('URL')

  filename = '{0}.json'.format(tableid)
  tableref = '{0}:{1}.{2}'.format(projectid,datasetid,tableid)

  # We use the save_main_session option because one or more DoFn's in this
  # workflow rely on global context (e.g., a module imported at module level).
  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(GoogleCloudOptions) #.save_main_session = save_main_session
  
  # The pipeline will be run on exiting the with block.
  with beam.Pipeline(options=pipeline_options) as p:

    # Read the text file[pattern] into a PCollection.
    lines = p | 'Read' >> Create(httpRequest(apiurl))
    #dicts = lines | 'Convert to Dicts' >> (beam.ParDo(CsvToJsonDoFn()))
    lines | 'write to bigquery' >> beam.io.WriteToBigQuery( table=tableref ,
    schema= sl.getSchema(filename), create_disposition=BigQueryDisposition.CREATE_IF_NEEDED,
    write_disposition=BigQueryDisposition.WRITE_APPEND)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()
