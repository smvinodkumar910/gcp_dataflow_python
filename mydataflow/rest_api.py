import apache_beam as beam
import re
import requests


inputs_pattern = 'data/*'
outputs_prefix = 'outputs/part'


def get_data():
  url = "https://imdb-top-100-movies.p.rapidapi.com/"
  headers = {
	"X-RapidAPI-Key": "11e969206dmsh2dc567692521a17p1aff25jsnf8d1e65d23f9",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"}

  response = requests.request("GET", url, headers=headers)
  return list(response.json())


class json_to_txt(beam.DoFn):
  def __init__(self):
    pass

  def process(self, movie_json):
    values_list = list(movie_json.values())
    list_output = list(map(str, values_list))
    movie_str = '|'.join(list_output)
    yield movie_str


# Running locally in the DirectRunner.
with beam.Pipeline() as pipeline:
  ( 
      pipeline 
      | 'Read Data From API' >> beam.Create(get_data())
      | 'Convert json to CSV' >> beam.ParDo(json_to_txt())
      | 'Write results' >> beam.io.WriteToText(outputs_prefix)
  )
