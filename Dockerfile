FROM python:3-onbuild
COPY requirements.txt /tmp/requirements.txt
RUN mkdir /github_tool
COPY . /github_tool/
ENTRYPOINT ["python","/github_tool/github_hacking.py"]
