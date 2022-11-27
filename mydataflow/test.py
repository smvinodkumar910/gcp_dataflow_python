import configuration.AppProperties as app


jsonoutput =  app.AppProperties.getProperty(propertyName='gcp')

print(jsonoutput)