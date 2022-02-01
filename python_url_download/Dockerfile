FROM python:3.9-alpine
RUN pip install --user requests
#FROM python:3.9-slim
WORKDIR /home/test
#COPY --from=builder /root/.local/* /root/.local/
COPY ./req_download.py /src/
CMD python /src/req_download.py ${url}
