FROM gcr.io/dataflow-templates-base/python3-template-launcher-base 

ARG WORKDIR=/dataflow/template
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

#COPY mydataflow .
ADD ./mydataflow /dataflow/template/mydataflow/

ENV FLEX_TEMPLATE_PYTHON_SETUP_FILE="${WORKDIR}/mydataflow/setup.py"
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/mydataflow/ApiToBq.py"

RUN pip install apache-beam[gcp]