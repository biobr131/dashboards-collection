FROM python:3.12

WORKDIR /usr/src

ARG REQ_DIR
COPY ${REQ_DIR} ./${REQ_DIR}/
ARG REQ_TXT
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r ${REQ_DIR}/${REQ_TXT}

RUN useradd --create-home --shell /bin/bash streamlit
USER streamlit

EXPOSE 8501

CMD ["/bin/bash"]
