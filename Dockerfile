FROM python

RUN pip install torch
RUN pip install transformers
RUN pip install sty
RUN pip install accelerate

COPY main.py ./

ENTRYPOINT python main.py
