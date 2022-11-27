FROM gcr.io/dataflow-templates-base/python3-template-launcher-base 

ARG WORKDIR=/dataflow/template
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

COPY requirements.txt .
COPY setup.py .
COPY mydataflow .

ENV FLEX_TEMPLATE_PYTHON_SETUP_FILE="${WORKDIR}/setup.py"
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/ApiToBq.py"

RUN pip install apache-beam[gcp]