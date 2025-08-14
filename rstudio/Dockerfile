FROM bioconductor/bioconductor_docker:latest

RUN apt-get update && \
    apt-get install -y \
        libcurl4-openssl-dev \
        libpq-dev \
        libssl-dev \
        postgresql-client \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY install_packages.R /tmp/
RUN Rscript /tmp/install_packages.R && \
    rm /tmp/install_packages.R

COPY rserver.conf /etc/rstudio/rserver.conf

CMD ["/usr/lib/rstudio-server/bin/rserver", "--server-daemonize=0"]
