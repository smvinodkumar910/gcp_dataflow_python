FROM gcr.io/dataflow-templates-base/python3-template-launcher-base 

ARG WORKDIR=/dataflow/template
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

COPY mydataflow .
COPY setup.py .
COPY ApiToBq.py .
COPY configuration .

ENV FLEX_TEMPLATE_PYTHON_SETUP_FILE="${WORKDIR}/setup.py"
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/ApiToBq.py"

RUN pip install apache-beam[gcp]